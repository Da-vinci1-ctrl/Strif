def compile_to_bytecode(lines):
    """
    Convert Strif source code lines into VM bytecode instructions.
    """
    bytecode = []

    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("consult ai"):
            # Extract string inside quotes
            prompt = line.split('"')[1]
            bytecode.append(("AI_CALL", prompt))

        elif line.startswith("set"):
            parts = line.split()
            bytecode.append(("SET", parts[1], parts[2]))

        elif line == "end":
            bytecode.append(("END",))

    return bytecode
