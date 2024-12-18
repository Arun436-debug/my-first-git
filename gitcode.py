def upper(f):
    def inner(x):
        if x.lower() == True:
            return x.upper()
        else:
            return 'Konni Capital letters vunnai Bhai'
    return inner
@upper
def fun(s):
    return s

s = input()
res = fun(s)
print(res)