# def execute1(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a=execute1(1)
# # print(a)
# def execut(func):
#     func("this")
#
#
# execut(print)
def execut(func):
    def nowsee():
        print("before ")
        func()
        print("after")
    return nowsee

@execut
def Akash():
    print("Akash ia a good boy")

# Akash = execut(Akash)



Akash()

