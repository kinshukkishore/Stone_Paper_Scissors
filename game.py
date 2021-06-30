# Stone paper scissors
import random

def game(comp,you):
    if comp=='s':
        if you=='p':
            print('You win')
        elif you=='sc':
            print('Comp win')
        elif you=='s':
            print("Tie")
        else:
            print('Wrong input')
    if comp=='p':
        if you=='sc':
            print('You win')
        elif you=='s':
            print('Comp win')
        elif you=='p':
            print("Tie")
        else:
            print('Wrong input')
    if comp=='sc':
        if you=='s':
            print('You win')
        elif you=='p':
            print('Comp win')
        elif you=='sc':
            print("Tie")
        else:
            print('Wrong input')
            
if __name__=="__main__":        

    while(True):
        a=random.randint(1,3)
        if a==1:
            comp='s'
        elif a==2:
            comp='p'
        elif a==3:
            comp='sc'
        print("Computer's turn: Stone(s), Paper(p), Scissors(sc)")
        you=input('Your Turn: Stone(s), Paper(p), Scissors(sc): ')
        print("Computer Choose: ",comp ,"\nYou Choose: ",you)
        game(comp,you)
        e=input("Enter e to exit or any other key to continue: ")
        if e=='e':
            exit()
