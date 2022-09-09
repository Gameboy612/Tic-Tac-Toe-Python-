grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def showgrid():
    print("     |     |     ")
    print("  " + str(grid[0]) +"  |  " + str(grid[1]) +"  |  " + str(grid[2]) +"    ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + str(grid[3]) +"  |  " + str(grid[4]) +"  |  " + str(grid[5]) +"    ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + str(grid[6]) +"  |  " + str(grid[7]) +"  |  " + str(grid[8]) +"    ")
    print("     |     |     ")


playerturn = ""
while not (playerturn == "O" or playerturn == "X"):
    playerturn = str(input("Who goes first, O or X?\n"))

while 1:
    showgrid()

    chosengrid = -1
    while not (1 <= chosengrid <= 9):
        chosengrid = input("Which grid do u want to choose?\n")
        try:
            chosengrid = int(chosengrid)
        except ValueError:
            chosengrid = -1


    if grid[chosengrid - 1] == " ":
        grid[chosengrid - 1] = playerturn
        


        # check if anyone had won:
        if (grid[0] == grid[1] == grid[2] != " ") or (grid[3] == grid[4] == grid[5] != " ") or (grid[6] == grid[7] == grid[8] != " ") or (grid[0] == grid[3] == grid[6] != " ") or (grid[1] == grid[4] == grid[7] != " ") or (grid[2] == grid[5] == grid[8] != " ") or (grid[0] == grid[4] == grid[8] != " ") or (grid[2] == grid[4] == grid[6] != " "):
            showgrid()
            print(str(playerturn) + " won!!!")
            break
        # detecting if there is a tie
        if " " not in grid:
            showgrid()
            print("tie")
            break
        
        if  playerturn == "O":
            playerturn = "X"
        elif playerturn == "X":
            playerturn = "O"