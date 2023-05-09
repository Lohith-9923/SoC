def leader(l):
    lead = []
    for i in range(len(l)):
        a = l[i]
        l1 = l[i:]
        count = 0
        for j in l1:
            if(a >= j):
                count += 1
            else:
                break
        if(count == len(l1)):
            lead.append(a)
    return lead
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(leader(l))
