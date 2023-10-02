import random

print("Let's play rock, paper and scissors!!!")
def play():
    user=input("Enter your choice - 'r' for rock, 's' for scissors or 'p' for papers : ")
    comp=random.choice(['p','r','s'])

    if user==comp :
        return 'It\'s a tie.'

    elif is_win(user,comp) :
        return 'You won.'

    else:
        return 'You lost.'

def is_win(player,opp):
    #p>r, r>s, s>p
    if (player=='r' and opp=='s') or (player=='p' and opp=='r') or (player=='s' and opp=='p') :
        return True

print(play())
        
