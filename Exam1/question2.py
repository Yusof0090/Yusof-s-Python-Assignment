subject1=int(input('what is your first subject score?'))
subject2=int(input('what is your second subject score?'))
subject3=int(input('what is your third subject score?'))
def totalScore(sub1,sub2,sub3):
    total=sub1+sub2+sub3
    print('total score is ',total)
totalScore(subject1,subject2,subject3)


car=1200
your=int(input('how much money do you have?'))
def totalScore(carprice,yourmoney):
    total=yourmoney-carprice    
    print('your remaining money is ',total)
totalScore(car,your)



m1=int(input('what is front len of your house?'))
m2=int(input('what is side len of your house?'))
def area(meter1,meter2):
    total=meter1*meter2
    print('area of your house is ',total)
area(m1,m2)

per=int(input('how much person?'))
your=int(input('type the money do you want to share?'))
def moneysharing(yourmoney,persons):
    total=yourmoney/persons
    print('you can give ',total,"for each one!")
moneysharing(your,per)