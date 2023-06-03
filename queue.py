q = []
f = None
r = None

def isEmpty(que):
    if(que==[]):
        return True
    else:
        return False

def enqueue(que,item):
    que.append(item)
    if(len(que)==1):
        f=r=0
    else:
        r = len(que)-1

def dequeue(que):
    if(isEmpty(que)):
        return('underflow')
    else:
        i = que.pop(0)
        if(len(que)==0):
            f=r= None
        return i

def peek(que):
    if (isEmpty(que)):
        return ('underflow')
    else:
        f = 0
        return que[f]

def display(que):
    if (isEmpty(que)):
        print ('Underflow! Queue is Empty.')
    elif(len(que)==1):
        print(que[0], "<--Front <---Rear")
    else:
        f = 0
        r = len(que)-1
        print(que[f],"<---Front")
        for x in range(1,r):
            print(que[x])
        print(que[r],"<---Rear")

for i in range(6):
    x = int(input("Enter element: "))
    enqueue(q,x)

display(q)

for i in range(3):
    item=dequeue(q)
    if(item=="underflow"):
        print("queue is empty")
    else:
        print("%d is dequeued"%item)