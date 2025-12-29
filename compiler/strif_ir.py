# compiler/strif_ir.py
# Strif Intermediate Representation (IR)

class IRInstruction:
    def __init__(self, op, args=None):
        self.op = op
        self.args = args or []

    def __repr__(self):
        return f"{self.op} {' '.join(map(str, self.args))}"


class StrifIR:
    def __init__(self):
        self.instructions = []

    def emit(self, op, *args):
        self.instructions.append(IRInstruction(op, args))

    def dump(self):
        return "\n".join(str(i) for i in self.instructions)
