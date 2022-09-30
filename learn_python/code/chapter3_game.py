# A suggested solution to escape exercise in Python learning tutorial
# https://mojtaba-komeili.github.io/learn_python/chapter2.html
import random

class GameBoard():
    def __init__(self, hero, deamon) -> None:
        self.hero = hero
        self.deamon = deamon
    
    def render(self):
        # First create an empty series of dots and the exit
        board = ['.', '.','.','.','.', '.', '.','.','.','E']

        # Replace the empty space dot with the symbols for here or the deamon
        board[self.hero.get_position() - 1] = self.hero.get_symbol()
        board[self.deamon.get_position() - 1] = self.deamon.get_symbol()

        print('-'*40)
        for c in board:
            print(c, end=' ')
        print()
        print('-'*40)
        print()


class Character():
    def __init__(self, initial_position) -> None:
        self.position = initial_position

    def set_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position


class Hero(Character):
    def get_symbol(self):
        return 'H'


class Deamon(Character):
    def get_symbol(self):
        return 'D'


if __name__ == '__main__':
    print('Starting the game.')
    game_ended = False
    hero_turn = True

    hero = Hero(2)
    deamon = Deamon(8)
    game_board = GameBoard(hero, deamon)

    while not game_ended:
        game_board.render()
        if hero_turn:
            print('It is Hero\'s turn.')
        else:
            print('It is Deamon\'s turn.')

        # Asking for players' action
        response = 'No response'
        move_steps = random.randint(1, 3)
        while (response != 'r') and (response != 'l'):
            print('Next move is ' + str(move_steps) + ' moves.')
            response = input('Push "r" for moving right "l" for left. ')
        
       


        if hero_turn:
            # Figuring out the move
            if response == 'l':
                new_pos = hero.get_position() - move_steps
            else:
                # if it was 'l' then it must be 'r', we already made sure it is 'r' or 'l'
                new_pos = hero.get_position() + move_steps

            # Hero can go out of the room, so we only check for going out from left side.
            if new_pos > 0:
                hero.set_position(new_pos)
                hero_turn = False
            else:
                print('This is not a valid move. Try again.')
                continue
        else:
            # Figuring out the move
            if response == 'l':
                new_pos = deamon.get_position() - move_steps
            else:
                # if it was 'l' then it must be 'r', we already made sure it is 'r' or 'l'
                new_pos = deamon.get_position() + move_steps

            # Deamon stays in the room. So, we check from left and right.
            if new_pos > 0 and new_pos < 11:
                deamon.set_position(new_pos)
                hero_turn = True
            else:
                print('This is not a valid move. Try again.')
                continue

        # Checking if anyone has won the game yet.
        if hero.get_position() >= 10:
            print('Hero has won!')
            game_ended = True
        if deamon.get_position() == hero.get_position():
            print('Deamon has won the game!') 
            game_ended = True
