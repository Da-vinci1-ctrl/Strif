from .ai_bridge import call_ai
from .trace import ExplainTrace
from .bytecode import compile_to_bytecode
from vm.strif_vm import StrifVM

def execute_strif_module(path):
    """
    Reads a Strif file and prepares memory, trace, and bytecode.
    """
    with open(path, "r") as f:
        lines = f.readlines()

    memory = {}
    trace = ExplainTrace()

    # Compile to bytecode
    bytecode = compile_to_bytecode(lines)

    # Run VM
    vm = StrifVM()
    vm.run(bytecode)

    return lines, memory, trace

def run_strif_engine(module, memory, trace, duration=15):
    """
    Legacy support: trace the module execution (kept for compatibility)
    """
    trace.log("Execution started")
    for line in module:
        line = line.strip()
        if line.startswith("consult ai"):
            prompt = line.split('"')[1]
            trace.log("Consulting AI...")
            response = call_ai(prompt)
            trace.log("AI response: " + response)
        elif line.startswith("set"):
            parts = line.split()
            memory[parts[1]] = parts[2]
            trace.log(f"Set {parts[1]} = {parts[2]}")
        elif line == "end":
            trace.log("Block ended")
    trace.log("Execution finished")
