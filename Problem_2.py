'''
Problem statement:

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
import time
start_time = time.time()

#Naive solution:
def naive_solution():
    a = 1
    b = 1
    c = 0
    sum = 0
    while c <= 4*(10**6):
        if c % 2 == 0:
            sum += c
        c = a + b
        a = b
        b = c
    return sum


if __name__ == "__main__":
    print(naive_solution())
    print((time.time() - start_time))
#Seeing as the naive solution takes an amount of time that rounds to 0, I'll stick with it.