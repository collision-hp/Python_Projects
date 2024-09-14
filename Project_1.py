import random

'''Snake Water Gun Game Rules

1 - Snake
2 - Water
3 - Gun

'''
comp=random.choice([1,2,3])
you=int(input('Enter your choice\n1 - Snake \n2 - Water \n3 - Gun \n'))
youDict={1:"Snake" , 2:"Water" , 3:"Gun"}
younum=youDict[you]
print(younum)
print(f"You chose {you} and computer chose {comp}")

if(comp==you):
    print("Tie")
else:
    if(comp==1 and you==2):
        print('You Lose')
    elif(comp==1 and you==3):
        print("You Win")
    elif(comp==2 and you==1):
        print("You Win")
    elif(comp==2 and you==3):
        print("You Lose")
    elif(comp==3 and you==2):
        print("You Win")
    elif(comp==3 and you==1):
        print("You Lose")
