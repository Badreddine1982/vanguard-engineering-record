from urllib.request import Request, urlopen

CONTRACT_SHA = "1237f443606d2b06c10778fbe1293257d048874e"
RUNTIME_SHA = "fa4365571612ce9e583af27174ca3322aad0b740"
CONTRACT_URL = "https://raw.githubusercontent.com/Badreddine1982/vanguard-contracts/" + CONTRACT_SHA + "/contracts/runtime/execution.v1.yaml"
RUNTIME_URL = "https://raw.githubusercontent.com/Badreddine1982/vanguard-runtime/" + RUNTIME_SHA + "/src/execution.py"


def fetch(url):
    request = Request(url, headers={"User-Agent": "vanguard-compatibility-confirmation"})
    with urlopen(request, timeout=15) as response:
        return response.read().decode("utf-8")


def require(source, fragments, label):
    missing = [item for item in fragments if item not in source]
    if missing:
        raise SystemExit(f"{label} check failed: " + ", ".join(missing))


def main():
    contract = fetch(CONTRACT_URL)
    runtime = fetch(RUNTIME_URL)
    require(contract, [
        "id: runtime.execution", "version: 1.0.0",
        "input: ExecutionRequest", "output: ExecutionResult",
        "audit_sink: AuditSink", "audit_event_required: true",
        "audit_event_emission_owner: runtime",
        "audit_event_sink_acceptance_required: true",
        "AUDIT_SINK_FAILURE", "evidence_reference",
    ], "contract")
    require(runtime, [
        "class ExecutionRequest", "class AuditEvent", "class AuditSink",
        "class ExecutionResult",
        "def execute(request: ExecutionRequest, audit_sink: AuditSink)",
        "INVALID_REQUEST", "INVALID_ACTION", "INVALID_TIMEOUT",
        "AUDIT_SINK_FAILURE", "audit_sink.emit(event)",
        "evidence_reference=reference",
    ], "runtime")
    print("CANDIDATE COMPATIBILITY CHECK: PASS")
    print("contract commit: " + CONTRACT_SHA)
    print("runtime commit: " + RUNTIME_SHA)
    print("scope: structural boundary only")
    print("adoption: unchanged")


if __name__ == "__main__":
    main()
