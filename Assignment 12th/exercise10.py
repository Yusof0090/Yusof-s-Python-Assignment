input_tr=int(input("how much rows?"))
def print_triangle(n):
    x=0
    while x <= n:
        print('y' * x)
        x=x+1
        
print_triangle(input_tr)