f=open("map.txt")
try:
    f1=open("map.txt")
except Exception as e:
    print(e)
else:
    print("This will run only when try is running")
finally:
    print("This is important ")
