import turtle
def code(n, b):
    if n==0:
        return b
    res = []
    k=0
    j=0

    for i in range(len(b)*2+1):
        if i%2==0:
            if k==0:
                res.append(k)
                k=1
            else:
                res.append(k)
                k=0
        else:
            res.append(b[j])
            j+=1
    return code(n-1, res)
def draw(l, n):
    x = l / n
    mass=[]
    Code=code(n,mass)
    turtle.forward(x)
    for i in range(len(Code)):
        if Code[i]==0:
            turtle.right(90)
        else:
            turtle.left(90)
        turtle.forward(x)
draw(10, 10)
turtle.done()