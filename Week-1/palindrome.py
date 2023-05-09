def palindrome(x):
    l = ""
    for i in range(len(x)):
        l += x[len(x)-i-1]
    if(l == x):
        return 1
    else:
        return 0

x = input()
print(palindrome(x))