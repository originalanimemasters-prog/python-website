#!/usr/bin/env python
import subprocess
import sys
import os
import json

# Read input from stdin
code = sys.stdin.read()

# Write code to file
with open('solution.py', 'w') as f:
    f.write(code)

try:
    result = subprocess.run(
        ['python', 'solution.py'],
        capture_output=True,
        text=True,
        timeout=5
    )
    print(json.dumps({
        'stdout': result.stdout,
        'stderr': result.stderr,
        'exit_code': result.returncode
    }))
except subprocess.TimeoutExpired:
    print(json.dumps({
        'stdout': '',
        'stderr': 'Time limit exceeded',
        'exit_code': -1
    }))
except Exception as e:
    print(json.dumps({
        'stdout': '',
        'stderr': str(e),
        'exit_code': -1
    }))
