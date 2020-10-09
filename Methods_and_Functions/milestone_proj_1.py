import sys

tic_tac_dict = {
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': 'i'
}
players = [0, 1]


def reset_dict(tic_tac_dict):
    tic_tac_dict['a'] = 'a'
    tic_tac_dict['b'] = 'b'
    tic_tac_dict['c'] = 'c'
    tic_tac_dict['d'] = 'd'
    tic_tac_dict['e'] = 'e'
    tic_tac_dict['f'] = 'f'
    tic_tac_dict['g'] = 'g'
    tic_tac_dict['h'] = 'h'
    tic_tac_dict['i'] = 'i'


def menu_game():
    reset_dict(tic_tac_dict)
    print("Choose an option:\n\t1) New Game.\n\t2) Exit.\n")
    user_selection = int(input("Option: "))
    user_selection_validation(user_selection)


def user_selection_validation(user_selection):
    while True:
        if user_selection == 1:
            game_start()
        elif user_selection == 2:
            print("Exiting...\nBye!")
            sys.exit()
        else:
            user_selection = int(input("Not valid option. Please try again.\nOption: "))
            user_selection_validation(user_selection)


turn_number = 0


def game_start():
    player_turn(turn_number)


def player_turn(turn_number):
    while True:
        for player in players:
            turn_number = turn_number + 1
            player_tic_tac(player, turn_number)


def player_tic_tac(player, turn_number):
    print(f"Value of counter: {turn_number}")
    if player == 0:
        display_board()
        player_x = input("Player 1 turn: ")
        while True:
            if tic_tac_dict[player_x] != 'X' and tic_tac_dict[player_x] != 'O':
                tic_tac_dict[player_x] = 'X'
                break
            else:
                player_x = input("Try another cell. Player 1 turn: ")
        define_winner(player, turn_number)
    if player == 1:
        display_board()
        player_x = input("Player 2 turn: ")
        while True:
            if tic_tac_dict[player_x] != 'X' and tic_tac_dict[player_x] != 'O':
                tic_tac_dict[player_x] = 'O'
                break
            else:
                player_x = input("Try another cell. Player 2 turn: ")
        define_winner(player, turn_number)

def display_board():
    print(f" {tic_tac_dict['a']} | {tic_tac_dict['b']} | {tic_tac_dict['c']} \n"
          f"-----------\n"
          f" {tic_tac_dict['d']} | {tic_tac_dict['e']} | {tic_tac_dict['f']} \n"
          f"-----------\n"
          f" {tic_tac_dict['g']} | {tic_tac_dict['h']} | {tic_tac_dict['i']} \n")


def define_winner(player, turn_number):
    if turn_number >= 5:
        print(f"Buscando ganador con contador = {turn_number}")
        if turn_number == 9:
            print("DRAW!")
            display_board()
            menu_game()
        elif player == 0:
            if check_for_winner_p1():
                print("P1 WON!")
                display_board()
                menu_game()
        elif player == 1:
            if check_for_winner_p2():
                print("P2 WON!")
                display_board()
                menu_game()


def check_for_winner_p1():
    if tic_tac_dict['a'] == 'X' and tic_tac_dict['b'] == 'X' and tic_tac_dict['c'] == 'X':
        return True
    elif tic_tac_dict['d'] == 'X' and tic_tac_dict['e'] == 'X' and tic_tac_dict['f'] == 'X':
        return True
    elif tic_tac_dict['g'] == 'X' and tic_tac_dict['h'] == 'X' and tic_tac_dict['i'] == 'X':
        return True
    elif tic_tac_dict['a'] == 'X' and tic_tac_dict['d'] == 'X' and tic_tac_dict['g'] == 'X':
        return True
    elif tic_tac_dict['b'] == 'X' and tic_tac_dict['e'] == 'X' and tic_tac_dict['h'] == 'X':
        return True
    elif tic_tac_dict['c'] == 'X' and tic_tac_dict['f'] == 'X' and tic_tac_dict['i'] == 'X':
        return True
    elif tic_tac_dict['a'] == 'X' and tic_tac_dict['e'] == 'X' and tic_tac_dict['i'] == 'X':
        return True
    elif tic_tac_dict['g'] == 'X' and tic_tac_dict['e'] == 'X' and tic_tac_dict['c'] == 'X':
        return True


def check_for_winner_p2():
    if tic_tac_dict['a'] == 'O' and tic_tac_dict['b'] == 'O' and tic_tac_dict['c'] == 'O':
        return True
    elif tic_tac_dict['d'] == 'O' and tic_tac_dict['e'] == 'O' and tic_tac_dict['f'] == 'O':
        return True
    elif tic_tac_dict['g'] == 'O' and tic_tac_dict['h'] == 'O' and tic_tac_dict['i'] == 'O':
        return True
    elif tic_tac_dict['a'] == 'O' and tic_tac_dict['d'] == 'O' and tic_tac_dict['g'] == 'O':
        return True
    elif tic_tac_dict['b'] == 'O' and tic_tac_dict['e'] == 'O' and tic_tac_dict['h'] == 'O':
        return True
    elif tic_tac_dict['c'] == 'O' and tic_tac_dict['f'] == 'O' and tic_tac_dict['i'] == 'O':
        return True
    elif tic_tac_dict['a'] == 'O' and tic_tac_dict['e'] == 'O' and tic_tac_dict['i'] == 'O':
        return True
    elif tic_tac_dict['g'] == 'O' and tic_tac_dict['e'] == 'O' and tic_tac_dict['c'] == 'O':
        return True


menu_game()
