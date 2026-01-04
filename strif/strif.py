#!/usr/bin/env python3
import sys
from strif.compiler.executor import execute_strif_module, run_strif_engine

def main():
    if len(sys.argv) < 2:
        print("Usage: strif <file.strf>")
        return

    path = sys.argv[1]
    module, memory, trace = execute_strif_module(path)
    run_strif_engine(module, memory, trace)

if __name__ == "__main__":
    main()
