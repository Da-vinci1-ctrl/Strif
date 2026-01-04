class ExplainTrace:
    def __init__(self):
        self.logs = []

    def log(self, message):
        print(f"[TRACE] {message}")
        self.logs.append(message)
