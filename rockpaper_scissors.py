import random


def play():
    player = input("'r' for rock,'s' for scissors,'p' for paper:")
    computer = random.choice(['r', 'p', 's'])
    condition = is_win(player, computer)
    return condition


def is_win(player, computer):
    # return False when the player win
    # winning conditions - r > s , s > p , p > r
    if (player == computer):
        print("It is a tie!")
        return True
    elif (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or \
            (player == 'p' and computer == 'r'):
        print("The player wins")
        return False
    elif (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or \
            (computer == 'p' and player == 'r'):
        print("The computer wins!")
        return True
    else:
        print('Something went wrong!')
        return True


while True:
    play()
    if (play() == False):
        break
print("Thank for playing!")
