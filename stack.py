s = []
top = None

def isEmpty(stk):
    if(stk==[]):
        return True
    else:
        return False

def push(stk, item):
    stk.append(item)
    top = len(stk)-1

def peek(stk):
    if(isEmpty(stk)):
        return("underflow")
    else:
        top = len(stk)-1
        return stk[top]

def s_pop(stk):
    if (isEmpty(stk)):
        return ("underflow")
    else:
        i = stk.pop()
        if(len(stk)==0):
            top = None
        else:
            top = len(stk) - 1
    return i

def display(stk):
    if (isEmpty(stk)):
        return ("underflow")
    else:
        top = len(stk) - 1
        print(stk[top], "<--- Top")
        for i in range(top-1,-1,-1):
            print(stk[i])



