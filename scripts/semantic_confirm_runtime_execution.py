import asyncio
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import Request, urlopen

RUNTIME_COMMIT = "1632318bf8d1e5a26b379f206fe3ab49d5740371"
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
        raise SystemExit("SEMANTIC-CONFIRM-03 FAILED: " + message)


class RecordingSink:
    def __init__(self):
        self.events = []

    def emit(self, event):
        self.events.append(event)
        return f"audit://{event.request_id or 'invalid-request'}/{len(self.events)}"


class FastExecutor:
    async def execute(self, action):
        return None


def main():
    runtime = load_runtime(fetch(RUNTIME_URL))
    sink = RecordingSink()

    valid = asyncio.run(runtime.execute(
        runtime.ExecutionRequest("semantic-301", "probe", 1000), sink, FastExecutor()
    ))
    require(valid.success is True, "valid request did not succeed")
    require(valid.request_id == "semantic-301", "request_id was not preserved")
    require(bool(valid.evidence_reference), "accepted audit event has no reference")
    require(len(sink.events) == 1, "valid request did not emit exactly one event")
    require(sink.events[0].success is True, "audit event outcome is incorrect")

    invalid_action = asyncio.run(runtime.execute(
        runtime.ExecutionRequest("semantic-302", "", 1000), sink, FastExecutor()
    ))
    require(not invalid_action.success, "invalid action was accepted")
    require(invalid_action.error_code == "INVALID_ACTION",
            "invalid action did not produce deterministic error")
    require(sink.events[-1].error_code == "INVALID_ACTION",
            "invalid action was not represented in audit event")

    invalid_timeout = asyncio.run(runtime.execute(
        runtime.ExecutionRequest("semantic-303", "probe", 0), sink, FastExecutor()
    ))
    require(not invalid_timeout.success, "non-positive timeout was accepted")
    require(invalid_timeout.error_code == "INVALID_TIMEOUT",
            "non-positive timeout did not produce deterministic error")
    require(sink.events[-1].error_code == "INVALID_TIMEOUT",
            "invalid timeout was not represented in audit event")

    class SlowExecutor:
        async def execute(self, action):
            await asyncio.sleep(1)

    timed_out = asyncio.run(runtime.execute(
        runtime.ExecutionRequest("semantic-304", "slow", 10), sink, SlowExecutor()
    ))
    require(not timed_out.success, "long-running action succeeded after deadline")
    require(timed_out.error_code == "EXECUTION_TIMEOUT",
            "cooperatively cancelled action did not produce EXECUTION_TIMEOUT")
    require(sink.events[-1].error_code == "EXECUTION_TIMEOUT",
            "timeout was not represented in audit event")

    class CancellationSuppressingExecutor:
        async def execute(self, action):
            try:
                await asyncio.sleep(1)
            except asyncio.CancelledError:
                return

    uncertain = asyncio.run(runtime.execute(
        runtime.ExecutionRequest("semantic-305", "slow", 10),
        sink, CancellationSuppressingExecutor()
    ))
    require(not uncertain.success, "uncertain completion was reported as success")
    require(uncertain.error_code == "EXECUTION_STATE_UNKNOWN",
            "uncertain completion was not distinguished from confirmed cancellation")

    class BrokenSink:
        def emit(self, event):
            raise OSError("sink unavailable")

    audit_failure = asyncio.run(runtime.execute(
        runtime.ExecutionRequest("semantic-306", "probe", 1000), BrokenSink(), FastExecutor()
    ))
    require(not audit_failure.success, "request succeeded despite audit sink failure")
    require(audit_failure.error_code == "AUDIT_SINK_FAILURE",
            "audit sink failure was not deterministic")

    print("SEMANTIC-CONFIRM-03: PASS")
    print(f"runtime commit: {RUNTIME_COMMIT}")
    print("valid request, audit evidence, deterministic validation errors: pass")
    print("long-running cooperative action deadline and cancellation: pass")
    print("cancellation uncertainty distinguished from confirmed timeout: pass")
    print("audit sink failure is fail-closed: pass")
    print("adoption: unchanged")
    

if __name__ == "__main__":
    main()
