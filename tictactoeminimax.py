#import random
#import sys
from random import randint
import copy
#Index3x3=
# -------------
# | 0 | 1 | 2 |
# -------------
# | 3 | 4 | 5 |
# -------------
# | 6 | 7 | 8 |
# -------------

StartingState=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def BoardState(State): 
    print('------------')
    print('   |   |')
    print(' ' + State[0] + ' | ' + State[1] + ' | ' + State[2])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + State[3] + ' | ' + State[4] + ' | ' + State[5])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + State[6] + ' | ' + State[7] + ' | ' + State[8])
    print('   |   |')
    print('------------')

 

def PlayersLetterChoice():
    PlayerLetter = ''
    ComputerLetter=''
    while not (PlayerLetter == 'X' or PlayerLetter == 'O' or PlayerLetter == 'x' or PlayerLetter == 'o'):
        PlayerLetter = input('Do you want to be X or O?')
    if PlayerLetter == 'X' or PlayerLetter=='x':
        print('You have chosen X, I am O!')
        PlayerLetter='X'
        ComputerLetter='O'
    else:
        print('You have chosen O, I am X!')
        PlayerLetter='O'
        ComputerLetter='X'
    return PlayerLetter, ComputerLetter

def Winner(State, Letter):
    if ((State[0] == Letter and State[1] == Letter and State[2] == Letter) or 
        (State[3] == Letter and State[4] == Letter and State[5] == Letter) or 
        (State[6] == Letter and State[7] == Letter and State[8] == Letter) or 
        (State[0] == Letter and State[3] == Letter and State[6] == Letter) or 
        (State[1] == Letter and State[4] == Letter and State[7] == Letter) or 
        (State[2] == Letter and State[5] == Letter and State[8] == Letter) or 
        (State[0] == Letter and State[4] == Letter and State[8] == Letter) or
        (State[2] == Letter and State[4] == Letter and State[6] == Letter)):
        return True
        
def RandomFirstPlayer():
    print("Let's flip a coin and see who is playing first!")
    i=randint(0, 1)
    if i==0:
        print( 'I play first!')
    else:
        print( 'You are playing first!')
    return i


def InputPlayerMove(State,Letter):
    NextMove = ' '
    while NextMove not in ['0','1','2','3','4','5','6','7','8']:
        NextMove = input('What is your next move? (pick number from 0 to 8):')
    return int(NextMove)
        

def NewBoardState(State, Letter, NextMove):
    State[NextMove]=Letter
    return State
            
def FreeBlocks(State):
    Free=[]
    for i in range(0,9):
        if State[i] != 'X' and State[i] != 'O':
            Free.append(i)
    return Free


def Children(State, Letter):
    ChildrenStates=[]
    NewState=[]
    for i in range (0,9):
        NewState = copy.copy(State)
        if i in FreeBlocks(State):
            ChildrenStates.append(NewBoardState(NewState, Letter, i))
    return ChildrenStates


def Evaluation(State,ComputerL, PlayerL):
    if Winner(State, ComputerL):
        return 10
    elif Winner(State, PlayerL):
        return -10
    else:
        return 0
count=0
def Minimax(State, Depth, Maximizingplayer, ComputerL, PlayerL):

    Score= Evaluation(State, ComputerL, PlayerL)
    if Depth == 0 or Score == 10 or Score == -10:
        return Score, State

    if Maximizingplayer==True:
        Best = -10
        BestChild = None
        ChildrenM = Children(State, ComputerL)
        for Child in ChildrenM:
            global count
            count+=1
            Val, Move = Minimax(Child, Depth-1, False,ComputerL, PlayerL)
            if Val > Best:
                BestChild = Child
                Best = Val
        return Best, BestChild
    else:
        Best = 10
        BestChild = None
        ChildrenM = Children(State, PlayerL)
        for Child in ChildrenM:
            count+=1
            Val, Move = Minimax(Child, Depth-1, True, ComputerL, PlayerL)
            if Val <= Best:
                BestChild = Child
                Best = Val
        return Best, BestChild



def main():
    BoardState(StartingState)  
    PlayerL, ComputerL = PlayersLetterChoice()
    Player=RandomFirstPlayer()
    #Player=0
    #Player=1
    State=StartingState

    ItsOn=True
    while ItsOn:
        if Player==1:
            NewMove=InputPlayerMove(State, PlayerL)
            
            if NewMove in FreeBlocks(State):
                State=NewBoardState(State, PlayerL, NewMove)
                if Winner(State,PlayerL):
                    print('You Won... I lost...')
                    break
                if len(FreeBlocks(State))==0:
                    print("The game is a tie")
                    break
                else:
                    Player=0
                
# MINIMAX OPPONENT              
        else:
            Score, NewMove= Minimax(State, 2, True, ComputerL, PlayerL)
            print (count)
            State=NewMove
            print(BoardState(NewMove))
            if Winner(State,ComputerL):
                print('I won!!! You lose!!!')
                break
            if len(FreeBlocks(State))==0:
                print("The game is a tie")
                break
            else:
                Player=1
                
# RANDOM OPPONENT              
#        else:
#            PossibleMoves=FreeBlocks(State)
#            NewMove = random.choice(PossibleMoves)
#            State=NewBoardState(State, ComputerL, NewMove)
#            if Winner(State,ComputerL):
#                print('I won!!! You lose!!!')
#                break
#            if len(FreeBlocks(State))==0:
#                print("The game is a tie")
#                break
#            else:
#                Player=1
 
if __name__ == "__main__":
    main()