msg=input('type your message!')
count=int(input("how much you want to print!"))
def print_message(message,repeat_count=1):
    i=1
    while i<=repeat_count:
        print(message)
        i+=1

print_message(msg,count)
