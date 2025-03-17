import random 

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors:\n")
    

    if error(user):
        return "Error: wrong letter. Try again!"
    
    computer = random.choice(['r','p','s'])
    print("Computer chose", computer)
 
    
# r > s, s > p, p > r

    if user == computer:
       return "Draw"
    
    if is_win(user, computer):
        return "You won!"
    return "You lost. Try again!"



def is_win(player, opponent): #return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
def error(letter): #return error if wrong letter
    if (letter != 'r') and (letter != 'p') and (letter != 's') :
        return True

    
print(play())
