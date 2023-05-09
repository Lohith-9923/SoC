def reverse_string(x):
    l = ""
    for i in range(len(x)):
        l += x[len(x)-i-1]
    return l
x = input()
print(reverse_string(x))

