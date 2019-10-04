def fb(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    import sys
    n = sys.argv[1]
    n = int(n)
    print(fb(n))
