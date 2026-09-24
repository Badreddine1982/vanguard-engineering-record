from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import Request, urlopen

RUNTIME_URL = (
    "https://raw.githubusercontent.com/Badreddine1982/"
    "vanguard-runtime/9ed82687afe24615ad41894934efa78baf07b89b/"
    "src/execution.py"
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
        raise SystemExit("SEMANTIC-CONFIRM-01 FAILED: " + message)

def main():
    runtime = load_runtime(fetch(RUNTIME_URL))

    valid = runtime.execute(
        runtime.ExecutionRequest("semantic-001", "probe", 1000)
    )
    require(valid.success is True, "valid request did not succeed")
    require(valid.request_id == "semantic-001", "request_id was not preserved")

    invalid_action = runtime.execute(
        runtime.ExecutionRequest("semantic-002", "", 1000)
    )
    require(invalid_action.success is False, "invalid action was accepted")
    require(invalid_action.error_code == "INVALID_ACTION",
            "invalid action did not produce deterministic error")

    invalid_timeout = runtime.execute(
        runtime.ExecutionRequest("semantic-003", "probe", 0)
    )
    require(invalid_timeout.success is False, "invalid timeout was accepted")
    require(invalid_timeout.error_code == "INVALID_TIMEOUT",
            "invalid timeout did not produce deterministic error")

    # The pinned contract requires an observable audit event.
    # The current runtime result exposes no audit_event field.
    audit_fields = ("audit_event", "audit_event_reference", "audit")
    require(
        any(hasattr(valid, field) for field in audit_fields),
        "contract requires an observable audit event, but ExecutionResult exposes none",
    )

    print("SEMANTIC-CONFIRM-01: PASS")
    print("valid request: pass")
    print("deterministic errors: pass")
    print("timeout enforcement: pass")
    print("audit event: observable")
    print("adoption: unchanged")

if __name__ == "__main__":
    main()
