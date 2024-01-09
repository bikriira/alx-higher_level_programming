#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    for i in range(len(sentence)):
        if i == 0:
            first_char = sentence[i]
        continue
    return (i + 1, first_char)
