from wasmtime import Store, Module, Instance

def ir_to_wasm(ir):
    wat = """
    (module
      (func $main
    """

    for instr in ir.instructions:
        if instr.op == "DECLARE":
            wat += f'  ;; declare {instr.args[0]}\n'
        elif instr.op == "FLOW":
            wat += f'  ;; flow {instr.args[0]}\n'
        elif instr.op == "OBSERVE":
            wat += f'  ;; observe {instr.args[0]}\n'

    wat += """
      )
      (start $main)
    )
    """

    return wat
