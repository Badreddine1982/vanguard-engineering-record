from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import Request, urlopen

RUNTIME_COMMIT = "fa4365571612ce9e583af27174ca3322aad0b740"
RUNTIME_URL = (
    "https://raw.githubusercontent.com/Badreddine1982/"
    f"vanguard-runtime/{RUNTIME_COMMIT}/src/execution.py"
)


def fetch(url):
    req = Request(url, headers={"User-Agent": "vanguard-semantic-confirmation"})
    with urlopen(req, timeout=15) as response:
        return response.read().decode("utf-8")


def load_runtime(source):
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "execution.py"
        path.write_text(source, encoding="utf-8")
        spec = spec_from_file_location("vanguard_runtime_execution", path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module


def require(condition, message):
    if not condition:
        raise SystemExit("SEMANTIC-CONFIRM-02 FAILED: " + message)


class RecordingSink:
    def __init__(self):
        self.events = []

    def emit(self, event):
        self.events.append(event)
        return f"audit://{event.request_id or 'invalid-request'}/{len(self.events)}"


def main():
    runtime = load_runtime(fetch(RUNTIME_URL))
    sink = RecordingSink()

    valid = runtime.execute(
        runtime.ExecutionRequest("semantic-201", "probe", 1000), sink
    )
    require(valid.success is True, "valid request did not succeed")
    require(valid.request_id == "semantic-201", "request_id was not preserved")
    require(bool(valid.evidence_reference), "accepted audit event has no reference")
    require(len(sink.events) == 1, "valid request did not emit exactly one event")
    require(sink.events[0].success is True, "audit event outcome is incorrect")

    invalid_action = runtime.execute(
        runtime.ExecutionRequest("semantic-202", "", 1000), sink
    )
    require(not invalid_action.success, "invalid action was accepted")
    require(invalid_action.error_code == "INVALID_ACTION",
            "invalid action did not produce deterministic error")
    require(sink.events[-1].error_code == "INVALID_ACTION",
            "invalid action was not represented in audit event")

    invalid_timeout = runtime.execute(
        runtime.ExecutionRequest("semantic-203", "probe", 0), sink
    )
    require(not invalid_timeout.success, "non-positive timeout was accepted")
    require(invalid_timeout.error_code == "INVALID_TIMEOUT",
            "non-positive timeout did not produce deterministic error")
    require(sink.events[-1].error_code == "INVALID_TIMEOUT",
            "invalid timeout was not represented in audit event")

    class BrokenSink:
        def emit(self, event):
            raise OSError("sink unavailable")

    audit_failure = runtime.execute(
        runtime.ExecutionRequest("semantic-204", "probe", 1000), BrokenSink()
    )
    require(not audit_failure.success, "request succeeded despite audit sink failure")
    require(audit_failure.error_code == "AUDIT_SINK_FAILURE",
            "audit sink failure was not deterministic")

    print("SEMANTIC-CONFIRM-02: PASS")
    print(f"runtime commit: {RUNTIME_COMMIT}")
    print("valid request and audit event: pass")
    print("deterministic validation errors and audit events: pass")
    print("audit sink failure is fail-closed: pass")
    print("timeout enforcement: NOT TESTED; only non-positive timeout validation tested")
    print("adoption: unchanged")


if __name__ == "__main__":
    main()
