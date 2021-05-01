number=int(input("enter the number of items you want to put in the list"))
lst=input("enter the item by leaving a space")
print("which type of comprehension you want to keep")
print("1 for list comprehension")
print("2 for set comprehension")
print("3 for dictionary comprehension")
choice=input()
if choice==1:
    ls=[i for i in lst]
    print(ls)
    print(type(ls))
elif choice ==2 :
    ls=(i for i in lst)
    print(ls)
    print(type(ls))
elif choice ==3:
    ls={i for i in lst}
    print(ls)
    print(type(ls))

