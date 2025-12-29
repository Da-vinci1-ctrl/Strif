# run_strif.py
# Temporary Strif runner (compiler pipeline demo)

from compiler.strif_ir import StrifIR
from compiler.ir_to_wasm import ir_to_wasm

# STEP 1: Create IR manually (temporary)
ir = StrifIR()
ir.emit("DECLARE", "alarm")
ir.emit("FLOW", "wait_5")
ir.emit("OBSERVE", "ring")

# STEP 2: Compile IR to WASM (WAT)
wat = ir_to_wasm(ir)

# STEP 3: Save output
with open("out.wat", "w") as f:
    f.write(wat)

print("Strif compiled successfully → out.wat")
