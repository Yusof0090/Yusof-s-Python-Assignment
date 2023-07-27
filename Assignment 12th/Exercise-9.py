input_n=int(input("what is your number?"))
input_f=int(input("what is your number?"))

def sum_multiples(n,f):
    a=range(n,100,n)
    b=range(f,100,f)
    g=list(a)
    h=list(b)
    c=sum(list(a))
    d=sum(list(b))
    print(g ,"=", c)
    print(h ,"=", d)
    print(c+d)
sum_multiples(input_n,input_f)