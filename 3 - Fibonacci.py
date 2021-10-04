print("Enter the length of the Fibonacci Series to print: ", end="")
n = int(input())
a = 0
b = 1

print(f"{a}, {b}", end="")
for i in range(2, n):
    c = a + b
    print(", ", end="")
    print(c, end="")
    a = b
    b = c
