import json
import random
from collections import defaultdict
from settlers.settlers_layer import *


def lambda_handler(event, context):
    # TODO implement
    shuffle = False
    board = defaultdict(dict)

    if 'shuffle' in event:
        shuffle = event['shuffle']

    coords = [(0, 2, -2), (1, 1, -2), (2, 0, -2),  # Row 1
              (-1, 2, -1), (0, 1, -1), (1, 0, -1), (2, -1, -1),  # Row 2
              (-2, 2, 0), (-1, 1, 0), (0, 0, 0), (1, -1, 0), (2, -2, 0),  # Center row
              (-2, 1, 1), (-1, 0, 1), (0, -1, 1), (1, -2, 1),  # Row 4
              (-2, 0, 2), (-1, -1, 2), (0, -2, 2)]  # Row 5

    die_values = [11, 12, 9, 4, 6, 5, 10, None, 3, 11, 4, 8, 8, 10, 9, 3, 5, 2, 6]
    if shuffle:
        random.shuffle(die_values)

    for i, c in enumerate(coords):
        board[HexCube(*c)] = {"die_value": die_values[i]}

    d = edge_distance(HexCube(-3, 0, 3), HexCube(3, -3, 0))

    return json.dumps({'board': [{str(k): v} for k, v in board.items()]})
