def compile_to_bytecode(lines):
    bytecode = []

    for line in lines:
        line = line.strip()

        if line.startswith("consult ai"):
            prompt = line.split('"')[1]
            bytecode.append(("AI_CALL", prompt))

        elif line.startswith("set"):
            parts = line.split()
            bytecode.append(("SET", parts[1], parts[2]))

        elif line == "end":
            bytecode.append(("END",))

    return bytecode
