#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_sequence = [0, 1]
        for i in range(2, length):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
            
        print(fib_sequence)

# Test the function
print_fibonacci(10)
