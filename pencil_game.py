import random
class NumOfPencilsMustBePostive(Exception):
    pass


# Incorporate once game is in final stages possibly idk
class Player:
    def __init__(self, name):
        self.name = name

# Incorporate once game is in final stages possibly idk
class Pencil:
    def __init__(self, number):
        self.number = number

class PencilGame:
    def __init__(self):
        self.play_game = True
        self.player1 = ''
        self.player2 = ''
        self.bot = 0
        self.turn = ''
        self.initial_pencils = 0
        self.pencils = 0
        self.turn_index = 0

    def game_loop(self):
        while self.play_game:
            self.get_pencils()
            print('Who will be the first (John, Jack):')
            self.get_players()
            while self.pencils > 0:
                print('|' * self.pencils)
                if self.turn_index == 0:
                    if self.bot == 1:
                        print(f'{self.player1}\'s turn:')
                    else:
                        print(f'{self.player1}\'s turn!')
                else:
                    if self.bot == 2:
                        print(f'{self.player2}\'s turn:')
                    else:
                        print(f'{self.player2}\'s turn!')
                self.start_turn()
                # temp line of code to pass hyperskill check
                if self.pencils == 0:
                    self.play_game = False
                    if self.turn_index == 0:
                        print(f'{self.player1} won!')
                    else:
                        print(f'{self.player2} won!')
            self.restart_or_exit()
        print('Thanks for playing the game. Have a nice day!')

    def get_pencils(self):
        try:
            self.initial_pencils = int(input('How many pencils would you like to use:\n'))
            self.pencils = self.initial_pencils
            if self.pencils <= 0:
                raise NumOfPencilsMustBePostive
        except ValueError:
            print('The number of pencils should be numeric')
            self.get_pencils()
        except NumOfPencilsMustBePostive:
            print('The number of pencils should be positive')
            self.get_pencils()

    def get_players(self):
        self.player1 = input() # 'Who will be the first (John, Jack):\n'
        if self.player1 == 'John':
            self.turn = 'John'
            self.player2 = 'Jack'
            self.bot = 2
        elif self.player1 == 'Jack':
            self.turn = 'Jack'
            self.player2 = 'John'
            self.bot = 1
        else:
            print('Choose between \'John\' and \'Jack\'')
            self.get_players()


    def start_turn(self):
        '''
        print('|' * self.pencils)
        if self.turn_index == 0:
            print(f'{self.player1}\'s turn!')
        else:
            print(f'{self.player2}\'s turn!')
        #
        '''
        try:
            if self.turn == 'John':
                pencils = int(input())
                if pencils not in [1, 2, 3]:
                    print('Possible values: \'1\', \'2\' or \'3\'')
                    self.start_turn()
                elif pencils > self.pencils:
                    print('Too many pencils were taken')
                    self.start_turn()
                else:
                    self.pencils -= pencils
                    self.turn = 'Jack'
                    self.turn_index += 1
                    self.turn_index %= 2
            else:
                if self.pencils % 4 == 0:
                    print('3')
                    self.pencils -= 3
                elif self.pencils % 4 == 3:
                    print('2')
                    self.pencils -= 2
                else:
                    print('1')
                    self.pencils -= 1
                self.turn = 'John'
                self.turn_index += 1
                self.turn_index %= 2
        except ValueError:
            print('Possible values: \'1\', \'2\' or \'3\'')
            self.start_turn()





    def restart_or_exit(self):
        play_again = input('Would you like to play again? y/n\n')
        if play_again != 'y':
            if play_again == 'n':
                self.play_game = False
            else:
                print('Please type y or n')
                self.restart_or_exit()


PencilGame().game_loop()


'''
Remember that the person who picks up the last pencil loses
Ok so if there are 2, 3, or 4 pencils left, you automatically win. Because you can pick up 3, 2 or 1
pencils leaving only 1 left for the other player.
If you have 5 pencils on the table, you are going to lose for this same reason.

'''
