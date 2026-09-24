from pathlib import Path
from urllib.request import Request, urlopen

CONTRACT_URL = (
    "https://raw.githubusercontent.com/Badreddine1982/"
    "vanguard-contracts/775c9850d6a2231cc619b3d64570ca9f08429635/"
    "contracts/runtime/execution.v1.yaml"
)
RUNTIME_URL = (
    "https://raw.githubusercontent.com/Badreddine1982/"
    "vanguard-runtime/9ed82687afe24615ad41894934efa78baf07b89b/"
    "src/execution.py"
)

def fetch(url):
    req = Request(url, headers={"User-Agent": "vanguard-compatibility-confirmation"})
    with urlopen(req, timeout=15) as response:
        return response.read().decode("utf-8")

def require(text, fragments, label):
    missing = [item for item in fragments if item not in text]
    if missing:
        raise SystemExit(f"{label} verification failed: " + ", ".join(missing))

def main():
    contract = fetch(CONTRACT_URL)
    runtime = fetch(RUNTIME_URL)

    require(contract, [
        "id: runtime.execution",
        "version: 1.0.0",
        "input: ExecutionRequest",
        "output: ExecutionResult",
        "request_id_required: true",
        "deterministic_errors: true",
        "timeout_required: true",
        "success_required: true",
        "error_code_required_on_failure: true",
    ], "contract")

    require(runtime, [
        "class ExecutionRequest",
        "class ExecutionResult",
        "def execute",
        "INVALID_REQUEST",
        "INVALID_ACTION",
        "INVALID_TIMEOUT",
        "return ExecutionResult(request.request_id, True)",
    ], "runtime")

    print("COMPATIBILITY CONFIRMATION: PASS")
    print("source: vanguard-contracts@775c9850d6a2231cc619b3d64570ca9f08429635")
    print("target: vanguard-runtime@9ed82687afe24615ad41894934efa78baf07b89b")
    print("contract/runtime boundary: structurally compatible")
    print("adoption: unchanged")

if __name__ == "__main__":
    main()
