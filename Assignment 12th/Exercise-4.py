num=int(input("what is your number?"))
def is_even(integer):
    if integer %2 == 0:
        return True
    else:
        return False
    
print(is_even(num))