import chess
import random


def get_random_move(fen):
    board = chess.Board(fen)
    legal_moves = list(board.legal_moves)
    if len(legal_moves) > 0:
        random_move = str(random.choice(legal_moves))
    else:
        random_move = ""
    print(random_move)
    return random_move


class State():
    def __init__(self):
        pass


if __name__ == '__main__':
    fen = 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1'
    get_random_move(fen)