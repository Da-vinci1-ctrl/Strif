# FUTURE: This logic will be replaced by Strif module:
# strif_compiler/ir_builder.strf
# compiler/strif_to_ir.py
from compiler.strif_ir import StrifIR

def compile_to_ir(ast):
    ir = StrifIR()

    for node in ast:
        if node["type"] == "intent":
            ir.emit("DECLARE", node["name"])
        elif node["type"] == "flow":
            ir.emit("FLOW", node["action"])
        elif node["type"] == "observe":
            ir.emit("OBSERVE", node["event"])

    return ir
