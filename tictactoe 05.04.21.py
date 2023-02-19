import random

o = False


def board():
    print("---------")
    print("|", cells[:5], "|")
    print("|", cells[6:11], "|")
    print("|", cells[12:17], "|")
    print("---------")


def draw_or_not_finished():
    global a
    global c
    empty_cells = 0
    for _p in range(0, 17, 2):
        if cells[_p] == ' ':
            empty_cells += 1
    if empty_cells == 0 and check_rws_diag() is False and check_rws_dwn() is False and check_rws_l_to_r() is False:
        print("Draw")
        a = False
        c = False
        exit()
    if empty_cells == 0:
        print("Game not finished")
        a = False
        c = False
        exit()


occupied = False
placement = ""


def ai_is_occupied(x, y):
    global occupied, placement
    if x == 1:
        if y == 1:
            placement = cells[0]
        if y == 2:
            placement = cells[2]
        if y == 3:
            placement = cells[4]
    if x == 2:
        if y == 1:
            placement = cells[6]
        if y == 2:
            placement = cells[8]
        if y == 3:
            placement = cells[10]
    if x == 3:
        if y == 1:
            placement = cells[12]
        if y == 2:
            placement = cells[14]
        if y == 3:
            placement = cells[16]
    if 'X' in placement or 'O' in placement:
        occupied = True
        return True
    if ' ' in placement:
        occupied = False
        return False


def is_occupied(x, y):
    global occupied, placement
    ai_is_occupied(x, y)
    if 'X' in placement or 'O' in placement:
        print("This cell is occupied! Choose another one!")
        occupied = True
    if ' ' in placement:
        occupied = False


# Loop that checks rows from left to right
def check_rws_l_to_r():
    for x in range(0, 13, 6):
        if cells[x] == 'X' and cells[x + 2] == 'X' and cells[x + 4] == 'X':
            print("X wins")
            exit()
        elif cells[x] == 'O' and cells[x + 2] == 'O' and cells[x + 4] == 'O':
            print("O wins")
            exit()


# Loop that checks rows downwards
def check_rws_dwn():
    for x in range(0, 5, 2):
        if cells[x] == 'X' and cells[x + 6] == 'X' and cells[x + 12] == 'X':
            print("X wins")
            break
        elif cells[x] == 'O' and cells[x + 6] == 'O' and cells[x + 12] == 'O':
            print("O wins")
            exit()


# Function that checks rows diagonally
def check_rws_diag():
    for x in range(0, 5, 4):
        if cells[x] == 'X' and cells[8] == 'X' and cells[16 - x] == 'X':
            print("X wins")
            exit()
        if cells[x] == 'O' and cells[8] == 'O' and cells[16 - x] == 'O':
            print("O wins")
            exit()


result = ''
cells = "_________"
for ch in cells:
    result = result + ch + ' '
for _i in cells:
    cells = result.replace("_", " ")
# Game menu
global a
global b
global c
global whofirst
global mode
global ii
global user
global ai
while True:
    whofirst = ""
    answer = input("")
    if answer == "start easy easy":
        a = True
        b = True
        c = True
        whofirst = "easy_ai"
        mode = "easy-ai"
        ai = "both_ai"
        board()
        break
    if answer == "start easy user":
        a = True
        b = True
        c = False
        whofirst = "easy_ai"
        mode = "easy-ai"
        ai = "p1"
        user = "p2"
        ii = 0
        board()
        break
    if answer == "start user easy":
        a = True
        b = True
        c = False
        mode = "easy-ai"
        user = "p1"
        ai = "p2"
        ii = 1
        board()
        break
    if answer == "start user medium":
        a = True
        b = True
        c = False
        mode = "medium-ai"
        user = "p1"
        ai = "p2"
        ii = 1
        board()
        break
    if answer == "start medium user":
        a = True
        b = True
        c = False
        whofirst = "medium_ai"
        mode = "medium-ai"
        ai = "p1"
        user = "p2"
        ii = 0
        board()
        break
    if answer == "start user hard":
        a = True
        b = True
        c = False
        mode = "hard-ai"
        user = "p1"
        ai = "p2"
        ii = 1
        board()
        break
    if answer == "start hard user":
        a = True
        b = True
        c = False
        whofirst = "hard_ai"
        mode = "hard-ai"
        ai = "p1"
        user = "p2"
        ii = 0
        board()
        break
    if answer == "start user user":
        a = True
        b = False
        c = False
        user = "both_usrs"
        board()
        break
    if answer == "start hard hard":
        b = False
        c = True
        ii = -1
        whofirst = "hard_ai"
        ai = "both_ai"
        mode = "hard"
        board()
        break
    if answer == "exit" or answer == "quit":
        exit()
    else:
        print("Bad parameters!")
        continue


# a = general game loop
# b = ai_makes_a_move function control
# c = AI with AI game control
def easy_ai_makes_a_move(z):
    global cells
    global b
    figure = 'X'
    global i
    while b:
        if ai == "p1":
            figure = 'X'
        if ai == "p2":
            figure = 'O'
        if ai == "both_ai":
            if z % 2 == 0:
                figure = 'X'
            if z % 2 != 0:
                figure = 'O'
        coord1 = random.randint(1, 3)
        coord2 = random.randint(1, 3)
        str(coord1)
        str(coord2)
        ai_coords = f'{coord1} {coord2}'
        print(ai_coords)
        if '1' in ai_coords[0]:
            if '1' in ai_coords[2]:
                ai_is_occupied(1, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:0] + figure + cells[1:]
                    print('Making move level "easy"')
                    board()
                    break
            if '2' in ai_coords[2]:
                ai_is_occupied(1, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:2] + figure + cells[3:]
                    print('Making move level "easy"')
                    board()
                    break
            if '3' in ai_coords[2]:
                ai_is_occupied(1, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:4] + figure + cells[5:]
                    print('Making move level "easy"')
                    board()
                    break
        if '2' in ai_coords[0]:
            if '1' in ai_coords[2]:
                ai_is_occupied(2, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:6] + figure + cells[7:]
                    print('Making move level "easy"')
                    board()
                    break
            if '2' in ai_coords[2]:
                ai_is_occupied(2, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:8] + figure + cells[9:]
                    print('Making move level "easy"')
                    board()
                    break
            if '3' in ai_coords[2]:
                ai_is_occupied(2, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:10] + figure + cells[11:]
                    print('Making move level "easy"')
                    board()
                    break
        if '3' in ai_coords[0]:
            if '1' in ai_coords[2]:
                ai_is_occupied(3, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:12] + figure + cells[13:]
                    print('Making move level "easy"')
                    board()
                    break
            if '2' in ai_coords[2]:
                ai_is_occupied(3, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:14] + figure + cells[15:]
                    print('Making move level "easy"')
                    board()
                    break
            if '3' in ai_coords[2]:
                ai_is_occupied(3, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:16] + figure + cells[17:]
                    print('Making move level "easy"')
                    board()
                    break


def medium_ai_makes_a_move(k):
    global cells
    global b
    global figure
    global ii
    if k % 2 != 0:
        figure = 'X'
    else:
        figure = 'O'
    # check_rws_diag
    cell0 = cells[0]
    cell4 = cells[4]
    cell8 = cells[8]
    cell12 = cells[12]
    cell16 = cells[16]
    fields = (cell0, cell4, cell8, cell12, cell16)

    two_of_three = sum(1 for f in fields if f == 'X')
    if two_of_three == 2:

        if cell4 == 'X' and cell8 == 'X' and ai_is_occupied(3, 1) is False:
            cells = cells[:12] + figure + cells[13:]
            b = False
            print('Making move level "medium"')
            board()
        if cell12 == 'X' and cell8 == 'X' and ai_is_occupied(1, 3) is False:
            cells = cells[:4] + figure + cells[5:]
            b = False
            print('Making move level "medium"')
            board()
        if cell0 == 'X' and cell8 == 'X' and ai_is_occupied(3, 3) is False:
            cells = cells[:16] + figure + cells[17:]
            b = False
            print('Making move level "medium"')
            board()
        if cell16 == 'X' and cell8 == 'X' and ai_is_occupied(1, 1) is False:
            cells = cells[:0] + figure + cells[1:]
            b = False
            print('Making move level "medium"')
            board()

    two_of_three = sum(1 for f in fields if f == 'O')
    if two_of_three == 2:

        if cell4 == 'O' and cell8 == 'O' and ai_is_occupied(3, 1) is False:
            cells = cells[:12] + figure + cells[13:]
            b = False
            print('Making move level "medium"')
            board()
        if cell12 == 'O' and cell8 == 'O' and ai_is_occupied(1, 3) is False:
            cells = cells[:4] + figure + cells[5:]
            b = False
            print('Making move level "medium"')
            board()
        if cell0 == 'O' and cell8 == 'O' and ai_is_occupied(3, 3) is False:
            cells = cells[:16] + figure + cells[17:]
            b = False
            print('Making move level "medium"')
            board()
        if cell16 == 'O' and cell8 == 'O' and ai_is_occupied(1, 1) is False:
            cells = cells[:0] + figure + cells[1:]
            b = False
            print('Making move level "medium"')
            board()
    # check_rws_l_to_r_for_ai_mediums_sake
    cell2 = cells[2]
    cell6 = cells[6]
    cell10 = cells[10]
    cell14 = cells[14]
    fields_l_r = (cell2, cell4, cell6, cell8, cell10, cell12, cell14, cell16)
    two_of_three = sum(1 for f in fields_l_r if f == 'X')
    if two_of_three == 2:
        if cell0 == "X" and cell2 == "X" and ai_is_occupied(1, 3) is False:
            cells = cells[:4] + figure + cells[5:]
            b = False
            print('Making move level "medium"')
            board()
        if cell6 == "X" and cell4 == "X" and ai_is_occupied(1, 1) is False:
            cells = cells[:0] + figure + cells[1:]
            b = False
            print('Making move level "medium"')
            board()
        if cell0 == "X" and cell4 == "X" and ai_is_occupied(1, 2) is False:
            cells = cells[:2] + figure + cells[3:]
            b = False
            print('Making move level "medium"')
            board()
        if cell6 == "X" and cell8 == "X" and ai_is_occupied(2, 3) is False:
            cells = cells[:10] + figure + cells[11:]
            b = False
            print('Making move level "medium"')
            board()
        if cell10 == "X" and cell8 == "X" and ai_is_occupied(2, 1) is False:
            cells = cells[:6] + figure + cells[7:]
            b = False
            print('Making move level "medium"')
            board()
        if cell6 == "X" and cell10 == "X" and ai_is_occupied(2, 2) is False:
            cells = cells[:8] + figure + cells[9:]
            b = False
            print('Making move level "medium"')
            board()
        if cell12 == "X" and cell14 == "X" and ai_is_occupied(3, 3) is False:
            cells = cells[:16] + figure + cells[17:]
            b = False
            print('Making move level "medium"')
            board()
        if cell16 == "X" and cell14 == "X" and ai_is_occupied(3, 1) is False:
            cells = cells[:12] + figure + cells[13:]
            b = False
            print('Making move level "medium"')
            board()
        if cell12 == "X" and cell16 == "X" and ai_is_occupied(3, 2) is False:
            cells = cells[:14] + figure + cells[15:]
            b = False
            print('Making move level "medium"')
            board()

    two_of_three = sum(1 for f in fields_l_r if f == 'O')
    if two_of_three == 2:
        if cell0 == "O" and cell2 == "O" and ai_is_occupied(1, 3) is False:
            cells = cells[:4] + figure + cells[5:]
            b = False
            print('Making move level "medium"')
            board()
        if cell6 == "O" and cell4 == "O" and ai_is_occupied(1, 1) is False:
            cells = cells[:0] + figure + cells[1:]
            b = False
            print('Making move level "medium"')
            board()
        if cell0 == "O" and cell4 == "O" and ai_is_occupied(1, 2) is False:
            cells = cells[:2] + figure + cells[3:]
            b = False
            print('Making move level "medium"')
            board()
        if cell6 == "O" and cell8 == "O" and ai_is_occupied(2, 3) is False:
            cells = cells[:10] + figure + cells[11:]
            b = False
            print('Making move level "medium"')
            board()
        if cell10 == "O" and cell8 == "O" and ai_is_occupied(2, 1) is False:
            cells = cells[:6] + figure + cells[7:]
            b = False
            print('Making move level "medium"')
            board()
        if cell6 == "O" and cell10 == "O" and ai_is_occupied(2, 2) is False:
            cells = cells[:8] + figure + cells[9:]
            b = False
            print('Making move level "medium"')
            board()
        if cell12 == "O" and cell14 == "O" and ai_is_occupied(3, 3) is False:
            cells = cells[:16] + figure + cells[17:]
            b = False
            print('Making move level "medium"')
            board()
        if cell16 == "O" and cell14 == "O" and ai_is_occupied(3, 1) is False:
            cells = cells[:12] + figure + cells[13:]
            b = False
            print('Making move level "medium"')
            board()
        if cell12 == "O" and cell16 == "O" and ai_is_occupied(3, 2) is False:
            cells = cells[:14] + figure + cells[15:]
            b = False
            print('Making move level "medium"')
            board()

    # check_rws_up_to_dwn
    two_of_three = sum(1 for f in fields_l_r if f == 'X')
    if two_of_three == 2:
        if cell0 == 'X' and cell6 == 'X' and ai_is_occupied(3, 1) is False:
            cells = cells[:12] + figure + cells[13:]
            b = False
            print('Making move level "medium"')
            board()
        if cell12 == 'X' and cell6 == 'X' and ai_is_occupied(1, 1) is False:
            cells = cells[:0] + figure + cells[1:]
            b = False
            print('Making move level "medium"')
            board()
        if cell0 == 'X' and cell12 == 'X' and ai_is_occupied(2, 1) is False:
            cells = cells[:6] + figure + cells[7:]
            b = False
            print('Making move level "medium"')
            board()
        if cell2 == 'X' and cell8 == 'X' and ai_is_occupied(3, 2) is False:
            cells = cells[:14] + figure + cells[15:]
            b = False
            print('Making move level "medium"')
            board()
        if cell14 == 'X' and cell8 == 'X' and ai_is_occupied(1, 2) is False:
            cells = cells[:2] + figure + cells[3:]
            b = False
            print('Making move level "medium"')
            board()
        if cell2 == 'X' and cell14 == 'X' and ai_is_occupied(2, 2) is False:
            cells = cells[:8] + figure + cells[9:]
            b = False
            print('Making move level "medium"')
            board()
        if cell4 == 'X' and cell10 == 'X' and ai_is_occupied(3, 3) is False:
            cells = cells[:16] + figure + cells[17:]
            b = False
            print('Making move level "medium"')
            board()
        if cell16 == 'X' and cell10 == 'X' and ai_is_occupied(1, 3) is False:
            cells = cells[:4] + figure + cells[5:]
            b = False
            print('Making move level "medium"')
            board()
        if cell4 == 'X' and cell16 == 'X' and ai_is_occupied(2, 3) is False:
            cells = cells[:10] + figure + cells[11:]
            b = False
            print('Making move level "medium"')
            board()
        # Separator
    two_of_three = sum(1 for f in fields_l_r if f == 'O')
    if two_of_three == 2:
        if cell0 == 'O' and cell6 == 'O' and ai_is_occupied(3, 1) is False:
            cells = cells[:12] + figure + cells[13:]
            b = False
            print('Making move level "medium"')
            board()
        if cell12 == 'O' and cell6 == 'O' and ai_is_occupied(1, 1) is False:
            cells = cells[:0] + figure + cells[1:]
            b = False
            print('Making move level "medium"')
            board()
        if cell0 == 'O' and cell12 == 'O' and ai_is_occupied(2, 1) is False:
            cells = cells[:6] + figure + cells[7:]
            b = False
            print('Making move level "medium"')
            board()
        if cell2 == 'O' and cell8 == 'O' and ai_is_occupied(3, 2) is False:
            cells = cells[:14] + figure + cells[15:]
            b = False
            print('Making move level "medium"')
            board()
        if cell14 == 'O' and cell8 == 'O' and ai_is_occupied(1, 2) is False:
            cells = cells[:2] + figure + cells[3:]
            b = False
            print('Making move level "medium"')
            board()
        if cell2 == 'O' and cell14 == 'O' and ai_is_occupied(2, 2) is False:
            cells = cells[:8] + figure + cells[9:]
            b = False
            print('Making move level "medium"')
            board()
        if cell4 == 'O' and cell10 == 'O' and ai_is_occupied(3, 3) is False:
            cells = cells[:16] + figure + cells[17:]
            b = False
            print('Making move level "medium"')
            board()
        if cell16 == 'O' and cell10 == 'O' and ai_is_occupied(1, 3) is False:
            cells = cells[:4] + figure + cells[5:]
            b = False
            print('Making move level "medium"')
            board()
        if cell4 == 'O' and cell16 == 'O' and ai_is_occupied(2, 3) is False:
            cells = cells[:10] + figure + cells[11:]
            b = False
            print('Making move level "medium"')
            board()
    if mode == "hard":
        b = False
    while b:
        if ai == "p1":
            figure = 'X'
        if ai == "p2":
            figure = 'O'
        coord1 = random.randint(1, 3)
        coord2 = random.randint(1, 3)
        str(coord1)
        str(coord2)
        ai_coords = f'{coord1} {coord2}'
        if '1' in ai_coords[0]:
            if '1' in ai_coords[2]:
                ai_is_occupied(1, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:0] + figure + cells[1:]
                    board()
                    break
            if '2' in ai_coords[2]:
                ai_is_occupied(1, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:2] + figure + cells[3:]
                    board()
                    break
            if '3' in ai_coords[2]:
                ai_is_occupied(1, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:4] + figure + cells[5:]
                    board()
                    break
        if '2' in ai_coords[0]:
            if '1' in ai_coords[2]:
                ai_is_occupied(2, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:6] + figure + cells[7:]
                    board()
                    break
            if '2' in ai_coords[2]:
                ai_is_occupied(2, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:8] + figure + cells[9:]
                    board()
                    break
            if '3' in ai_coords[2]:
                ai_is_occupied(2, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:10] + figure + cells[11:]
                    board()
                    break
        if '3' in ai_coords[0]:
            if '1' in ai_coords[2]:
                ai_is_occupied(3, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:12] + figure + cells[13:]
                    board()
                    break
            if '2' in ai_coords[2]:
                ai_is_occupied(3, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:14] + figure + cells[15:]
                    board()
                    break
            if '3' in ai_coords[2]:
                ai_is_occupied(3, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:16] + figure + cells[17:]
                    board()
                    break
        print('Making move level "medium"')


def hard_ai_makes_a_move():
    global cells
    global b
    global figure
    global ii
    global user
    global answer
    global turn
    if ai == "p1":
        figure = 'X'
        user = "p2"
    if ai == "p2":
        figure = 'O'
        user = "p1"
    if ai == "both_ai" and turn % 2 != 0:
        figure = 'X'
    if ai == "both_ai" and turn % 2 == 0:
        figure = 'O'
    # possibleMoves = []
    # for q in range(0, 17, 2):
    #    if cells[q] == " ":
    #       possibleMoves.append(f"cell{q}")
    #  else:
    #    continue
    if figure == 'X' and turn == 1 or turn == 2:
        randcell = random.choice([0, 4, 12, 16])
        if cells[randcell] == " ":
            cells = cells[:randcell] + figure + cells[randcell + 1:]
            print("Making move level 'hard'")
            board()
            print(turn)
    elif turn % 2 != 0 and turn >= 2:
        medium_ai_makes_a_move(turn)

    if figure == 'O':
        if not ai_is_occupied(2, 2):
            cells = cells[:8] + figure + cells[9:]
            print("Making move level 'hard'")
            board()
        elif turn % 2 == 0 and turn >= 3:
            medium_ai_makes_a_move(turn)
            # randcell = random.choice([0, 4, 12, 16])
            # if cells[randcell] == " ":
                # cells = cells[:randcell] + figure + cells[randcell + 1:]
            print("Making move level 'hard'")
            print(turn)
            board()


# User and AI game scenario
# This is where the actual game is executed
turn = 1
while b:
    if whofirst == "easy_ai" and ai == "p1" and ii == 0:
        easy_ai_makes_a_move(turn)
    if whofirst == "medium_ai" and ii == 0:
        medium_ai_makes_a_move()
    if whofirst == "hard_ai" and ii == 0:
        hard_ai_makes_a_move(turn)
    coordinates = input("Enter the coordinates: ")
    fix = coordinates.replace(" ", "")
    coordinates_lower = coordinates.lower()
    if coordinates_lower.islower():
        print("You should enter numbers!")
        continue
    if len(fix) != 2:
        print("You should enter numbers!")
        continue
    elif int(fix[0]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif int(fix[0]) < 1:
        print("Coordinates should be from 1 to 3!")
        continue
    elif int(fix[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif int(fix[1]) < 1:
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        if user == "p1":
            l = 'X'
        if user == "p2":
            l = 'O'
        if '1' in fix[0]:
            if '1' in fix[1]:
                is_occupied(1, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:0] + l + cells[1:]
                    board()
            if '2' in fix[1]:
                is_occupied(1, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:2] + l + cells[3:]
                    board()
            if '3' in fix[1]:
                is_occupied(1, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:4] + l + cells[5:]
                    board()
        if '2' in fix[0]:
            if '1' in fix[1]:
                is_occupied(2, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:6] + l + cells[7:]
                    board()
            if '2' in fix[1]:
                is_occupied(2, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:8] + l + cells[9:]
                    board()
            if '3' in fix[1]:
                is_occupied(2, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:10] + l + cells[11:]
                    board()
        if '3' in fix[0]:
            if '1' in fix[1]:
                is_occupied(3, 1)
                if occupied:
                    continue
                else:
                    cells = cells[:12] + l + cells[13:]
                    board()
            if '2' in fix[1]:
                is_occupied(3, 2)
                if occupied:
                    continue
                else:
                    cells = cells[:14] + l + cells[15:]
                    board()
            if '3' in fix[1]:
                is_occupied(3, 3)
                if occupied:
                    continue
                else:
                    cells = cells[:16] + l + cells[17:]
                    board()
    ii += 1
    if b == True and mode == "easy-ai" and ii != 0:
        easy_ai_makes_a_move(turn)
    if b == True and mode == "medium-ai" and ii != 0:
        medium_ai_makes_a_move()
    if b == True and mode == "hard" and ii != 0:
        hard_ai_makes_a_move(turn)
    turn += 1
    check_rws_l_to_r()
    check_rws_dwn()
    check_rws_diag()
    draw_or_not_finished()
while c:
    if mode == "easy-ai":
        easy_ai_makes_a_move(turn)
        draw_or_not_finished()
        turn += 1
        check_rws_l_to_r()
        check_rws_dwn()
        check_rws_diag()
        draw_or_not_finished()
    elif mode == "hard":
        hard_ai_makes_a_move()
        draw_or_not_finished()
        turn += 1
        check_rws_l_to_r()
        check_rws_dwn()
        check_rws_diag()
        draw_or_not_finished()
