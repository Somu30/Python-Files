print("Number to check if palindrome or not: ", end = "")
p = input()
l = len(p)
flag = True

for i in range(0, l):
    if p[i] != p[l-1-i]:
        flag = False
        break

if flag:
    print(f"{p} is a Palindrome.")
else:
    print(f"{p} is not a Palindrome.")
