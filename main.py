# main.py

from game.game import Game

if __name__ == "__main__":
    game = Game()
    game.run_game('moves.txt')
    game.save_final_state('final_state.json')
