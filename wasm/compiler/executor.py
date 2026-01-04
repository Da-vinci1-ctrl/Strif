class Memory:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def dump(self):
        return self.data


class Trace:
    def __init__(self):
        self.logs = []

    def log(self, msg):
        self.logs.append(msg)
        print("[TRACE]", msg)

    def show(self):
        print("\n--- TRACE LOG ---")
        for l in self.logs:
            print(l)


def execute_strif_module(path):
    memory = Memory()
    trace = Trace()

    with open(path) as f:
        lines = f.readlines()

    module = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        module.append(line)

    trace.log("Loaded Strif module")
    return module, memory, trace


def run_strif_engine(module, memory, trace, duration=5):
    trace.log("Strif engine started")

    for line in module:
        if line.startswith("intent"):
            _, key, value = line.split()
            memory.set(key, value)
            trace.log(f"Intent set: {key} = {value}")

        elif line.startswith("aim"):
            trace.log("Aim registered")

        elif line.startswith("observe"):
            trace.log("Observation made")

    trace.log("Strif engine finished")
