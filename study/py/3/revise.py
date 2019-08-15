# 19-8-15
#今天复习下快排
def qsort(l):
    if len(l)<= 1:
        return l
    else:
        return qsort([x for x in l[1:] if x <= l[0]])+[l[0]]+qsort([x for x in l[1:] if x >l[0]]) # 对list的理解  array slice
l=[5,4,3,2]
print(qsort(l))
my_string = 'sakupopo'
k = [print(i) for i in my_string if i not in "aeiou"]#print(i) is executed if the given character is not a vowel.
p = [print(i) for i in my_string if i not in "aeiou"]
print(k) #Explanation: print() returns None.
c = [1,4,7,6,-4]

#易理解版：
def qs2(l):
    b=[]
    d=[]
    if len(l)<= 1:
        return l

    for x in l[1:]:
        if x<=l[0]:
            b.append(x)
            print(b)

    for x in l[1:]:
        if x>l[0]:
            d.append(x)
            print(d)
    return qs2(b)+[l[0]]+qs2(d)

print(qs2(l))
#List Comprehension (LC)
b =[x for x in range(1,20) if x%2==0 ]
print(b)