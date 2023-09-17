import random
import time
def instructions():
    # provinding instructions to the user
    x=('''    How to play?????     
                You have to select any choice (Stone,Paper,Scissor)  
                the computer will automatically select its choice and then the 
                competition begins.....

              Who will win???????
              
              1. If you choose Stone and computer choose Paper You lose
              2. If you choose Stone and computer choose Scissor You Wins
              3. If you choose Stone and computer choose Stone the Maths is tie
              4. If you choose Paper and computer choose Stone You lose
              5. If you choose Paper and computer choose Scissor You Wins
              6. If you choose Paper and computer choose Paper the Maths is tie
              7. If you choose Stone and computer choose Scissor You lose
              8. If you choose Stone and computer choose Paper You Wins
              9. If you choose Stone and computer choose Stone the Maths is tie
          ''')
    print(x)

# Symbols used
sym1=str(chr(3374))  # മ
sym2=str(chr(3424))  # ൠ
sym3=str(chr(1792))  # ܀
sym4=str(chr(1421))  # 


    
def play():
    choice='yes'
 
    
    while choice in ['y','Y','Yes','yes']:

        # Displaying the options to the user to select his weapon
        print('\t\t\t '+sym1*17+'')
        print('\t\t\t '+sym1+ '  Here is your Weapons!!!  '+sym1+ '')
        print('\t\t\t '+sym1+ '  1. Stone                          '+sym1+ '')
        print('\t\t\t '+sym1+ '  2. Paper                          '+sym1+ '')
        print('\t\t\t '+sym1+ '  3. Scissor                        '+sym1+ '')
        print('\t\t\t '+sym1*17+'')
        print()
        
        # Taking Weapon choice From the user
        user=int(input(sym2+' Enter Your Weapon choice '))

        print()
        
        if user==1:             # if user chooses Stone as its weapon
            comp=random.randint(1,3)
            if comp==1:       # computer chooses Stone         
                print('The game is tie')
            elif comp==2:    # computer chooses Paper
                print('You loose....')
            else:                 # computer chooses Scissor
                print('You Win ')

        elif user==2:          # if user chooses Paper as its weapon
            comp=random.randint(1,3)
            if comp==1:       # computer chooses Stone
                print('You Win... ')
            elif comp==2:    # computer chooses Paper
                print('The game is tie')
            else:                 # computer chooses Scissor
                print('You loose....')

        elif user==3:          # if user chooses Scissor as its weapon
            comp=random.randint(1,3)
            if comp==1:       # computer chooses Stone
                print('You loose....')
            elif comp==2:    # computer chooses Paper
                print('You Win ')
            else:                 # computer chooses Scissor
                print('The game is tie ')

        print()
        #Asking For user He/She want's to play more or not
        choice=input('Do you want to play more (y/n).... ')
        if choice in ['n','N','no','No']:
            print('Thanks for Playing ')
        else:
            continue

# ஃஃஃஃ Main Program ஃஃஃஃ
print('\t\t'+sym3*16+'')
print('\t\t'+sym3+' Stone '+sym3*9+'')
print('\t\t'+sym3*5+' Paper '+sym3*5+'')
print('\t\t'+sym3*8+'Scissor '+sym3+'')
print('\t\t'+sym3*16+'')
#choices for user
print()
print()
while True:
    print('\t\t\t'+sym4*9+'')
    print('\t\t\t'+sym4+ '1. instructions  '+sym4+'')
    print('\t\t\t'+sym4+ '2. play game    '+sym4+'')
    print('\t\t\t'+sym4+ '3. exit    '+sym4+'')
    print('\t\t\t'+sym4*9+'')
    ask=int(input('Enter your choice '))
    if ask==1:
        instructions()
        input('Press enter to continue')
    if ask==2:
        play()
    if ask==3:
        print(exit())
    if ask not in [1,2]:
        print()
        print('\t\tYou have given Wrong choice')
        print()
        x=input('Do you want to continue(y/n)')
        if x in ['y','Y','Yes','yes']:
            continue
        else:
            print(exit())
