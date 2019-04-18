import time
start_time = time.time()
def func(n):
    c=0
    for i in range(1,n+1):
       c+=i**i
    ad=str(c)
    print(ad[-10:])
print("--- %s seconds ---" % (time.time() - start_time))