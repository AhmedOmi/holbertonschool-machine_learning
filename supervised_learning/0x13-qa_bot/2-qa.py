#!/usr/bin/env python3
"""
answer_loop
"""


def answer_loop(reference):
    """
    reference is the reference text
    """
    while True:
        txt = input("Q: ")
        if txt in ["exit", "quit", "goodbye", "bye"]:
            print("A: Goodbye")
            break
        a = question_answer(txt, reference)
        if a is None:
            return "Sorry, I do not understand your question."
        print("A: ",a)
