#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        return "not valid number"
    fib  = [0, 1]
    if length <= 2:
        return fib[:length]
    for i in range(2, length):
        fib.append(fib[i-1] + fib[i - 2])
    return fib

