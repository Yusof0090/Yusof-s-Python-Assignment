input_value=input("how much you want to print?")

####### while loop #########
def print_message(message,repeat_count=1):
    x=1
    while x <= repeat_count:
        print(message)
        x+=1

print_message("hello world",input_value)

####### for loop ##########

def print_msg(msg,count=1):
    for x in range(0,count):
        if x <= count:
            print(msg)
        x+=1

print_msg('hello',input_value)


