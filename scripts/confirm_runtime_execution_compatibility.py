from urllib.request import Request, urlopen

CONTRACT_SHA = "108b5b2cf52932d5807144b4b6ba00f4065e2498"
RUNTIME_SHA = "1632318bf8d1e5a26b379f206fe3ab49d5740371"
CONTRACT_URL = (
    "https://raw.githubusercontent.com/Badreddine1982/vanguard-contracts/"
    + CONTRACT_SHA + "/contracts/runtime/execution.v2.yaml"
)
RUNTIME_URL = (
    "https://raw.githubusercontent.com/Badreddine1982/vanguard-runtime/"
    + RUNTIME_SHA + "/src/execution.py"
)


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
        "id: runtime.execution", "version: 2.0.0",
        "input: ExecutionRequest", "output: ExecutionResult",
        "audit_sink: AuditSink", "action_executor: ActionExecutor",
        "audit_event_required: true", "timeout_required: true",
        "EXECUTION_TIMEOUT", "EXECUTION_STATE_UNKNOWN", "AUDIT_SINK_FAILURE",
    ], "contract")
    require(runtime, [
        "class ExecutionRequest", "class AuditEvent", "class AuditSink",
        "class ActionExecutor", "class ExecutionResult",
        "async def execute(", "asyncio.wait({task}, timeout=timeout_ms / 1000)",
        "EXECUTION_TIMEOUT", "EXECUTION_STATE_UNKNOWN", "AUDIT_SINK_FAILURE",
        "audit_sink.emit(event)", "evidence_reference=reference",
    ], "runtime")
    print("CANDIDATE COMPATIBILITY CHECK: PASS")
    print("contract v2 commit: " + CONTRACT_SHA)
    print("runtime commit: " + RUNTIME_SHA)
    print("scope: structural assertions only; semantic timeout evidence is separate")
    print("adoption: unchanged")


if __name__ == "__main__":
    main()
