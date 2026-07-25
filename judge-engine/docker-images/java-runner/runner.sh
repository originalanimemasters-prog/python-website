#!/bin/bash
# Java runner script
code=$(cat)
echo "$code" > Solution.java
javac Solution.java
timeout 5 java Solution
