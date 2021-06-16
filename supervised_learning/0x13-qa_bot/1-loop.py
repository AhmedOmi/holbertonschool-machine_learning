#!/usr/bin/env python3
"""
script that takes in input from the user
"""
while True:
    txt = input("Q: ")
    if txt in ["exit", "quit", "goodbye", "bye"]:
        print("A: Goodbye")
        break
    print("A:")
