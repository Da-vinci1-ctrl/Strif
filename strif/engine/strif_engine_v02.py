import time
import re

class Intent:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.manifested = False

class Flow:
    def __init__(self, subject, action, target, delay=None):
        self.subject = subject
        self.action = action
        self.target = target
        self.delay = delay

class Observation:
    def __init__(self, text, condition=None):
        self.text = text
        self.condition = condition

class StrifEngineV02:

    def run(self, file):
        self.intents = {}
        self.flows = []
        self.observations = []

        self.parse(file)
        print("\n🜂 STRIF v0.2 EXECUTION\n")

        self.manifest_intents()
        self.resolve_flows()
        self.observe()

    def parse(self, file):
        with open(file) as f:
            lines = [l.strip() for l in f if l.strip()]

        mode = None
        for line in lines:
            if line in ("intent", "flow", "observe"):
                mode = line
                continue
            if line == "end" or line.startswith("scripture"):
                continue

            if mode == "intent":
                m = re.match(r"(\w+) exists(?: as \"(.*)\")?", line)
                if m:
                    self.intents[m.group(1)] = Intent(m.group(1), m.group(2))

            elif mode == "flow":
                delay = None
                if "after" in line:
                    parts = line.split("after")
                    line = parts[0].strip()
                    delay = int(parts[1].strip())

                s, a, t = line.split()
                self.flows.append(Flow(s, a, t, delay))

            elif mode == "observe":
                if "only if" in line:
                    text, cond = line.split("only if")
                    self.observations.append(Observation(text.strip(), cond.strip()))
                else:
                    self.observations.append(Observation(line))

    def manifest_intents(self):
        print("🌱 Intents:")
        for i in self.intents.values():
            i.manifested = True
            print(f" • {i.name} exists")

    def resolve_flows(self):
        print("\n🌊 Flows:")
        for f in self.flows:
            if f.delay:
                print(f" • waiting {f.delay}s")
                time.sleep(f.delay)
            print(f" • {f.subject} {f.action} {f.target}")
            if f.subject in self.intents and f.target in self.intents:
                self.intents[f.target].value = self.intents[f.subject].value

    def observe(self):
        print("\n👁 Observations:")
        for o in self.observations:
            if o.condition:
                if o.condition in self.intents:
                    print(f" • {o.text}")
            else:
                print(f" • {o.text}")
