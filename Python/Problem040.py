from time import time

def make(s):
    i=0
    k=''
    p=''
    while(i<len(s)):
        p=str(s[i])
        k+=p
        i+=1
    return k

dx
def con(n):
    s=[]
    t=[]
    i=0
    while(i<=n):
        s.append(i)
        i+=1
    return s

def d(n,i):
    s=make(con(n))
    return s[i]

answer = d(1000,1)*d(1000,10)*d(1000,100)*d(1000*1000)*(1000*10000)

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(answer))
    print("Time Taken:{}".format(time() - start))
