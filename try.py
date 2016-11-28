import turtle as t
def initT():
    t.shape("circle")
    t.speed(0)
    t.penup()
    t.goto(-100, -200)
    t.pendown()
    t.right(90)

def createCode(n, code = ["1"]):
    if n == 1:
        return code
    else:
        code.append("1")
        code+=universe(code[0:-1])
        return createCode(n-1,code)
def universe(s):
    ret = []
    for c in s:
        if c == '0':
            ret.append('1')
        else:
            ret.append("0")
    return ret[::-1]
def make1(l):
    t.left(90)
    t.forward(l)
def make0(l):
    t.right(90)
    t.forward(l)
def draw(L, N):
    code = createCode(N)
    for c in code:
        if c == "0":
            make0(L)
        else:
            make1(L)
    t.done()

initT()
N=10
L=200/N
draw(L,N)