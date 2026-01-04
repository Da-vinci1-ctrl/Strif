class StrifVM:
    def __init__(self):
        self.memory = {}

    def run(self, bytecode):
        for instr in bytecode:
            op = instr[0]

            if op == "AI_CALL":
                prompt = instr[1]
                print("[VM] AI CALL:", prompt)

            elif op == "SET":
                self.memory[instr[1]] = instr[2]

            elif op == "END":
                print("[VM] END")
