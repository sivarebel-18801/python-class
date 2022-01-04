a1=input("1st player name:")
a2=input("2nd player name:")
b=int(input("no.of turns you want to play:"))
user_points=0
system_points=0
TIE_points=0
for i in range(1,b+1):
    print(i,"turn")
    user=input("enter 1st player choice:rock,paper,scissor:")
    l1=['rock','paper','scissor']
    import random
    system=random.choice(l1)
    print(user)
    print(system)
    if user==system:
        print("TIE")
        TIE_points=TIE_points+1
        print(TIE_points)
    elif user=="rock":
        if system=="scissor":
            print("user wins",user)
            user_points=user_points+1
            print(user_points)
        else:
            print("system wins")
            system_points=system_points+1
            print(system_points)
    elif user=="paper":
        if system=="scissor":
            print("system wins",system)
            system_points=system_points+1
            print(system_points)
        else:
            print("user wins")
            user_points=user_points+1
            print(user_points)
    elif user=="rock":
        if system=="paper":
            print("system wins",system)
            system_points=system_points+1
            print(system_points)
        else:
            print("user wins")
            user_points=user_points+1
            print(user_points)
    elif user=="scissor":
        if system=="paper":
            print("user wins",user)
            user_points=user_points+1
            print(user_points)
        else:
            print("system wins")
            system_points=system_points+1
            print(system_points)
    elif user=="rock":
        if system=="paper":
            print("system wins",system)
            system_points=system_points+1
            print(system_points)
        else:
            print("user wins")
            user_points=user_points+1
            print(user_points)
    else:
        print('invalid')
print('Total turns:'b)
print('user wins:',user_points)
print('system wins:',system_points)
print('TIE:',TIE_points)




            
        
    
