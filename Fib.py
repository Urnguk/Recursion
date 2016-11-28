def Fib(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    elif N < 0:
        return "error"
    else:
        return Fib(N-1) + Fib(N-2)
print(Fib(-3))