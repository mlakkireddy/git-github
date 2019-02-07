import time
l2=[]
l3=[]

def decorator(func):
    def inner(*args):
            start=time.time()
            result=func(*args)
            end=time.time()
            print(f"time to execute is:{(end-start)*1000}")
            return result

    return  inner

@decorator
#sqr=decorator(sqr)
def sqr(l1):
    #start=time.time()
    for i in l1:
        l2.append(i*i)
    #end=time.time()
    #print(f"sqr takes:{(end-start)*1000} ms to execute")
    return l2
@decorator
#thrice=decorator(thrice)
def thrice(l1):
    #start=time.time()
    for i in l1:
        l2.append(i*i)
    #end=time.time()
    #print(f"sqr takes:{(end-start)*1000} ms to execute")
    return l2


l1=range(1,100)


print(sqr(l1))

print(thrice(l1))