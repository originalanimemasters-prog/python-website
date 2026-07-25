#!/bin/bash
# C++ runner script
code=$(cat)
echo "$code" > solution.cpp
g++ -O2 solution.cpp -o solution
timeout 5 ./solution
