import random
ROCK='r'
SCISSOR='s'
PAPER='p'
emoji={
    ROCK:"♦",
    SCISSOR:"✂",
    PAPER:"📃"
}
choices=tuple(emoji.keys())

def get_user_input():
    while True:
        user_choice=input("Rock,paper or scissor ?(r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("invalid choice..!")
            
def display_choices(user_choice,computer_choice):
    print(f"your choice is {emoji[user_choice]}")
    print(f"computer choice is {emoji[computer_choice]}")


def determinate_winner(user_choice,computer_choice):
        if user_choice == computer_choice:
            print("Tie")
        elif (
            (user_choice==ROCK and computer_choice==SCISSOR) or 
            (user_choice==SCISSOR and computer_choice==PAPER) 
            or (user_choice==PAPER and computer_choice==ROCK)):
            print("You Win!")
        else:
            print("You loss")

       
def play_game():
    while True:
        user_choice=get_user_input()
        computer_choice=random.choice(choices)
        display_choices(user_choice,computer_choice)
        determinate_winner(user_choice,computer_choice)
        should_contine=input("continue? (y/n): ").lower()
        if should_contine=="n":
            break

play_game()
    

