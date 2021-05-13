def hangman(word):
    win = False
    remaining = list(word)
    board = ["_"] * len(word)
    chance = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    wrong_guess = 0
    print("Welcome to hangman...Created by vinson")
    while wrong_guess < len(chance) - 1:
        print("\n")
        answer = input("enter the word to guess:  ")
        if answer in remaining:
            temp = remaining.index(answer)
            board[temp] = answer
            remaining[temp] = '$'
        else:
            wrong_guess = wrong_guess + 1
        range = wrong_guess + 1
        print(" ".join(board))
        print("\n")
        print("\n".join(chance[0: range]))
        if '_' not in board:
            print("you won the game...congrats!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("you lost the game...Better luck next time!")
        print(" ".join(board))
        print("\n".join(chance[0: wrong_guess]))
        print("The missed word is {}".format(word))


ques = input("Enter the word to make the question for player:  ")
hangman(ques)