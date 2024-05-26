#!/usr/bin/env python3

def print_fibonacci(length):
    prev1 = 0
    prev2 = 0
    counting = 0
    fibonacci = list()
    while counting < length:
        sequence = prev1 +prev2
        fibonacci.append(sequence)
        #print(fibonacci, sequence)
        if(sequence == 0):
            prev1 += 1
            prev2 = prev2
        else:
            prev1 = fibonacci[len(fibonacci) -1]
            prev2 = fibonacci[len(fibonacci) -2]
        
        counting += 1
    print(fibonacci)
    return(fibonacci)
x = print_fibonacci(9)