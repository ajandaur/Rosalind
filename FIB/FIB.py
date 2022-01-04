'''
Problem 003
Rabbits and Recurrence Relations
Rosalind ID: FUB
'''

def fib(n, k):
    if n <= 1:
        return 1
    else:
        return fib(n-1, k) + fib(n-2, k) * k

def main():
    with open('/Users/anmoljandaur/Projects/ajandaur/Rosalind/FIB/rosalind_fib.txt', 'r') as file:
        n, k = [int(i) for i in file.read().strip().split(' ')]

        print(fib(n-1, k))

if __name__ == '__main__':
    main()