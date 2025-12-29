import json
import sys

def compile_strif(file):
    ir = {"intents": [], "flows": [], "observe": []}
    mode = None

    with open(file) as f:
        for line in f:
            line = line.strip()
            if line in ("intent", "flow", "observe"):
                mode = line
                continue
            if not line or line.startswith("scripture") or line == "end":
                continue

            if mode == "intent":
                ir["intents"].append(line)
            elif mode == "flow":
                ir["flows"].append(line)
            elif mode == "observe":
                ir["observe"].append(line)

    out = file.replace(".strf", ".sbc")  # Strif Bytecode
    with open(out, "w") as f:
        json.dump(ir, f, indent=2)

    print(f"Compiled → {out}")

if __name__ == "__main__":
    compile_strif(sys.argv[1])
