from compiler.strif_to_ir import compile_to_ir
from compiler.ir_to_wasm import ir_to_wasm

# temporary fake AST for testing
ast = [
    {"type": "intent", "name": "alarm"},
    {"type": "flow", "action": "wait_5"},
    {"type": "observe", "event": "ring"}
]

ir = compile_to_ir(ast)
wat = ir_to_wasm(ir)

with open("out/strif.wat", "w") as f:
    f.write(wat)

print("Strif → WASM generated (strif.wat)")
