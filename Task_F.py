def print_list(lst):
    for x in lst:
        print(x, end=' ')
    print()


def factorial(n):  # n!
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result





def next_permutation(p):
    i = len(p) - 1
    while i > 0 and p[i - 1] > p[i]:
        i -= 1

    if i == 0:
        p.reverse()
    else:

        pos = len(p) - 1
        while p[pos] < p[i - 1]:
            pos -= 1

        p[i - 1], p[pos] = p[pos], p[i - 1]  # меняем местами p[pos] и p[i - 1]

        p[i::] = reversed(p[i::])


def main():
    p = list(map(int, input().split()))
    n = len(p)

    for i in range(factorial(n)):
        print_list(p)
        next_permutation(p)


main()
