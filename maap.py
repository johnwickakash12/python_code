lst=["23","321","3","56",]
lst=list(map(int,lst))
print(type(lst))
def sq(a):
    return a*a
def cube(a):
    return a*a*a
numbr=[sq,cube]
for i in range(5):
    val=list(map(lambda x:x(i),numbr))
    print(val)