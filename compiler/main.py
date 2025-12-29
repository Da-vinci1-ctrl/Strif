from executor import execute_strif_module, run_strif_engine

module, memory, trace = execute_strif_module(
    "agents/system_agent.strf"
)

print("INITIAL MEMORY:", memory.dump())
print("\n🤖 STRIF AGENT STARTED\n")

run_strif_engine(module, memory, trace, duration=10)

print("\nFINAL MEMORY:", memory.dump())
trace.show()
