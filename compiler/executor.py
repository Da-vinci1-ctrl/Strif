import time


class StrifMemory:
    def __init__(self):
        self.store = {}

    def set(self, key, value=True):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key, False)

    def dump(self):
        return self.store


class TimeRule:
    def __init__(self, mode, seconds):
        self.mode = mode
        self.seconds = seconds
        self.last_run = None


class ExplainTrace:
    def __init__(self):
        self.steps = []

    def log(self, message):
        timestamp = round(time.time(), 2)
        self.steps.append(f"[{timestamp}] {message}")

    def show(self):
        print("\n📘 STRIF EXPLANATION TRACE")
        for step in self.steps:
            print(step)


def evaluate_condition(condition, memory):
    if condition is None:
        return True
    return memory.get(condition)


def parse_time_rule(line):
    parts = line.split()
    return TimeRule(parts[0], int(parts[1].replace("s", "")))


def execute_strif_module(path):
    with open(path, "r") as f:
        lines = f.readlines()

    memory = StrifMemory()
    trace = ExplainTrace()

    module = {
        "scripture": None,
        "rules": [],    # (condition, time_rule, action)
        "goals": []
    }

    current_condition = None
    current_time = None
    in_flow = False

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("scripture"):
            module["scripture"] = line.split()[1]
            trace.log(f"Loaded scripture {module['scripture']}")

        elif line.startswith("intent"):
            var = line.replace("intent", "").strip()
            memory.set(var)
            trace.log(f"Intent declared: {var}")

        elif line.startswith("aim"):
            goal = line.replace("aim", "").strip()
            module["goals"].append(goal)
            trace.log(f"Goal set: {goal}")

        elif line.startswith("when"):
            current_condition = line.replace("when", "").strip()
            trace.log(f"Condition registered: {current_condition}")

        elif line.startswith("after") or line.startswith("every"):
            current_time = parse_time_rule(line)
            trace.log(f"Time rule added: {line}")

        elif line.startswith("flow"):
            in_flow = True

        elif line == "end":
            current_condition = None
            current_time = None
            in_flow = False

        else:
            if in_flow:
                module["rules"].append(
                    (current_condition, current_time, line)
                )
                trace.log(
                    f"Action '{line}' added under condition '{current_condition}'"
                )

    return module, memory, trace


def goals_satisfied(goals, memory):
    return all(memory.get(goal) for goal in goals)


def run_strif_engine(module, memory, trace, duration=15):
    start = time.time()
    trace.log("Execution started")

    while time.time() - start < duration:
        if goals_satisfied(module["goals"], memory):
            trace.log("All goals satisfied → stopping execution")
            break

        now = time.time()

        for condition, rule, action in module["rules"]:
            if not evaluate_condition(condition, memory):
                continue

            if rule is None:
                trace.log(f"Executed '{action}' (no time rule)")
                memory.set(action)

            elif rule.mode == "after":
                if rule.last_run is None and now - start >= rule.seconds:
                    trace.log(
                        f"Executed '{action}' after {rule.seconds}s because '{condition}' was true"
                    )
                    rule.last_run = now
                    memory.set(action)

            elif rule.mode == "every":
                if rule.last_run is None or now - rule.last_run >= rule.seconds:
                    trace.log(
                        f"Executed '{action}' every {rule.seconds}s while '{condition}' was true"
                    )
                    rule.last_run = now

        time.sleep(0.1)

    trace.log("Execution ended")
