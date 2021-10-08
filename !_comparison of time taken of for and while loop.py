import time
#while loop
start1=time.time()
k=0
while(k<4500):
    k+=1
    print("I am a Superman")
c=time.time()-start1
#for loop
start=time.time()
for i in range(4500):
    print("I am a Superman")
d=time.time()-start
print(f"Time taken in while loop is {c} seconds and time take in for loop is {d} seconds")