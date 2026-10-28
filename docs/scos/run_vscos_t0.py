#!/usr/bin/env python3
"""Self-contained, read-only T0 checks for the SCOS intake package.
The submitted AGI source is never imported or executed.
Paths are rooted at this script's directory; no legacy v0.2 package is required.
"""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import hashlib, json, re, sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'Epistemology_V9.0_Source.docx'
MANIFEST = ROOT / 'VANGUARD_SCOS_PACKAGE_SHA256_MANIFEST_v0.2.txt'
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
REQUIRED = [
    'Epistemology_V9.0_Source.docx',
    'Epistemology_V9_Static_Intake_Audit_v0.1.md',
    'VANGUARD_SCOS_Component_Intake_Register_v0.4.md',
    'VANGUARD_SCOS_Acceptance_Test_Execution_Ledger_v0.3.md',
    'VANGUARD_SCOS_Acceptance_Test_Plan_v0.1.md',
    'VANGUARD_SCOS_Transfer_Evidence_Ledger_v0.2.md',
]

def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def main():
    results = []
    def record(test, ok, detail):
        results.append({'test': test, 'status': 'PASS' if ok else 'FAIL', 'detail': detail})
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    record('T0-REQUIRED-PAYLOADS', not missing, json.dumps({'required': REQUIRED, 'missing': missing}, sort_keys=True))
    source_hash = sha256(SOURCE) if SOURCE.is_file() else None
    record('T0-SOURCE-SHA256', bool(source_hash and re.fullmatch(r'[0-9a-f]{64}', source_hash)), source_hash or 'missing')
    source_text = ''
    try:
        with ZipFile(SOURCE) as z:
            bad = z.testzip()
            xml = z.read('word/document.xml')
            root = ET.fromstring(xml)
            paragraphs = [''.join(t.text or '' for t in p.findall('.//w:t', NS)) for p in root.findall('.//w:p', NS)]
            source_text = '\n'.join(paragraphs)
            record('T0-DOCX-ZIP-AND-XML', bad is None and bool(paragraphs), f'zip_test={bad}; paragraphs={len(paragraphs)}; document_xml_parsed=true')
    except Exception as exc:
        record('T0-DOCX-ZIP-AND-XML', False, f'{type(exc).__name__}: {exc}')
    manifest_entries, errors = {}, []
    try:
        for line in MANIFEST.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('VANGUARD-') or line.startswith('Generated:') or line.startswith('Algorithm:') or line.startswith('Rule:'):
                continue
            parts = line.split(None, 1)
            if len(parts) != 2 or not re.fullmatch(r'[0-9a-f]{64}', parts[0]):
                errors.append('malformed manifest line: ' + line)
                continue
            manifest_entries[parts[1].strip()] = parts[0]
        for name, digest in manifest_entries.items():
            path = ROOT / name
            if not path.is_file():
                errors.append('missing manifest payload: ' + name)
            elif sha256(path) != digest:
                errors.append('hash mismatch: ' + name)
        if not manifest_entries:
            errors.append('manifest has no payload records')
        record('T0-MANIFEST-HASHES', not errors, json.dumps({'entries': len(manifest_entries), 'errors': errors}, sort_keys=True))
    except Exception as exc:
        record('T0-MANIFEST-HASHES', False, f'{type(exc).__name__}: {exc}')
    markers = {
        'synthetic_random_metric_present': 'random.uniform' in source_text,
        'DGM_external_dependency_reference_present': 'CodeMutator()' in source_text,
        'QMARL_external_dependency_reference_present': 'QMARLModel()' in source_text,
        'A2A_class_present': 'class A2ACommunication' in source_text,
        'main_entrypoint_present': 'if __name__ == "__main__"' in source_text,
    }
    record('T0-SMOKE-SOURCE-MARKERS', all(markers.values()), json.dumps(markers, sort_keys=True))
    legacy = (ROOT / 'VANGUARD_SCOS_Intake_Completion_Package_v0.2.zip').exists()
    record('T0-NO-LEGACY-PACKAGE-DEPENDENCY', True, json.dumps({'legacy_v0_2_present': legacy, 'script_requires_legacy_v0_2': False}, sort_keys=True))
    overall = 'PASS' if all(x['status'] == 'PASS' for x in results) else 'FAIL'
    report = {
        'record_id': 'VSC-T0-2026-10-28-002',
        'scope': 'source identity, DOCX container integrity, manifest hashes, and deterministic static markers only',
        'execution_boundary': 'submitted AGI source was NOT imported or executed',
        'package_version': 'v0.3.1',
        'script_root': '.',
        'source_file': SOURCE.name,
        'source_bytes': SOURCE.stat().st_size if SOURCE.exists() else None,
        'source_sha256': source_hash,
        'manifest_file': MANIFEST.name,
        'manifest_entries': len(manifest_entries),
        'tests': results,
        'overall': overall,
        'limitations': ['T0 is not an AGI runtime test.', 'No performance, security, quantum execution, or adoption claim is made.', 'T1-T12 remain NOT RUN.']
    }
    (ROOT / 'VSC_T0_Smoke_Test_Results_v0.2.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if overall == 'PASS' else 1

if __name__ == '__main__':
    sys.exit(main())
