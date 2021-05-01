import time
a="Akash"
initial=time.time()


for i in range(50):
    print(f"This is {a}")
    time.sleep(1)#we use time.sleep function to play the loop is given time delays
print("for loop run in",time.time()-initial)
k=0
intial=time.time()


while(k<50):
    print(f"this is not {a}")
    k=k+1
print("while loop ran in",time.time()-intial)