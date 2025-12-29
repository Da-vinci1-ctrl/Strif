# STRIF v0.1 — Intent-Based Runtime Simulator
# Host language: Python (temporary execution vessel)

import re

class Intent:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.manifested = False

class Flow:
    def __init__(self, subject, action, target):
        self.subject = subject
        self.action = action
        self.target = target

class Observation:
    def __init__(self, text):
        self.text = text

class StrifScripture:
    def __init__(self, name):
        self.name = name
        self.intents = {}
        self.flows = []
        self.observations = []

class StrifEngine:

    def run(self, file):
        scripture = self.parse(file)
        print(f"\n🜂 Executing STRIF Scripture: {scripture.name}\n")

        self.manifest_intents(scripture)
        self.resolve_flows(scripture)
        self.observe(scripture)

    def parse(self, file):
        with open(file) as f:
            lines = [l.strip() for l in f if l.strip()]

        scripture = None
        mode = None

        for line in lines:
            if line.startswith("scripture"):
                name = line.split()[1]
                scripture = StrifScripture(name)

            elif line in ("intent", "flow", "observe"):
                mode = line

            elif line == "end":
                break

            else:
                if mode == "intent":
                    self.parse_intent(scripture, line)
                elif mode == "flow":
                    self.parse_flow(scripture, line)
                elif mode == "observe":
                    scripture.observations.append(Observation(line))

        return scripture

    def parse_intent(self, scripture, line):
        match = re.match(r"(\w+) exists(?: as \"(.*)\")?", line)
        if match:
            name, value = match.groups()
            scripture.intents[name] = Intent(name, value)

    def parse_flow(self, scripture, line):
        parts = line.split()
        if len(parts) == 3:
            subject, action, target = parts
            scripture.flows.append(Flow(subject, action, target))

    def manifest_intents(self, scripture):
        print("🌱 Manifesting Intents:")
        for intent in scripture.intents.values():
            intent.manifested = True
            if intent.value:
                print(f"  • {intent.name} exists as '{intent.value}'")
            else:
                print(f"  • {intent.name} exists")

    def resolve_flows(self, scripture):
        print("\n🌊 Resolving Flows:")
        for flow in scripture.flows:
            s = scripture.intents.get(flow.subject)
            t = scripture.intents.get(flow.target)

            if s and t:
                print(f"  • {flow.subject} {flow.action} {flow.target}")
                if flow.action == "reaches" and s.value:
                    t.value = s.value

    def observe(self, scripture):
        print("\n👁 Observations:")
        for obs in scripture.observations:
            print(f"  • {obs.text}")

        print("\n✨ STRIF Reality Manifested ✨\n")


if __name__ == "__main__":
    engine = StrifEngine()
    engine.run("hello.strf")
