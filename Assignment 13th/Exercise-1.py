input_value=input("how much you want to print?")
def print_message(message,repeat_count=1):
    x=1
    while x <= repeat_count:
        print(message)
        x+=1

print_message("hello world",int(input_value))
