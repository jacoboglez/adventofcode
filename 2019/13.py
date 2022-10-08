'''
https://adventofcode.com/2019/day/13
'''
DAY = 13

from utils import *
from icc import intCodeComputer
from collections import defaultdict, deque
from time import sleep

# How to print:
# 0 is an empty tile. No game object appears in this tile.
# 1 is a wall tile. Walls are indestructible barriers.
# 2 is a block tile. Blocks can be broken by the ball.
# 3 is a horizontal paddle tile. The paddle is indestructible.
# 4 is a ball tile. The ball moves diagonally and bounces off objects.
# 
#        0    1    2    3    4
FILL = [' ', '█', '#', '―', 'o']
SHOW_GAME = False



def part1(program):
    software = intCodeComputer(program, id=1)
    software.compute()

    tile_ids = software.outputArray[2::3]

    return tile_ids.count(2)



def paint(output_array, show_output=True):
    tiles = {}
    output_array = deque(output_array)

    xmax = 0
    ymax = 0

    ball_pos = (-1, -1)
    paddle_pos = (-1, -1)

    while output_array:
        tile_x = output_array.popleft()
        tile_y = output_array.popleft()
        tile_id = output_array.popleft()

        tiles[(tile_x, tile_y)] = tile_id

        if tile_id == 4: # ball
            ball_pos = (tile_x, tile_y)
        elif tile_id == 3: # paddle
            paddle_pos = (tile_x, tile_y)

        if tile_x > xmax: xmax = tile_x
        if tile_y > ymax: ymax = tile_y


    score = tiles[(-1, 0)]

    if show_output:

        line = ''
        for y in range(ymax+1):
            for x in range(xmax+1):
                line += FILL[ tiles[(x, y)] ]
            line += '\n'

        print(line)

        print('')
        print(f'Score: {score}')
        sleep(0.2)

    return ball_pos, paddle_pos, score


 
def part2(program):
    software = intCodeComputer(program, id=2, verbose=False)

    # Add two quarters to play
    software.memory[0] = 2

    # Play the game
    movement_ant = 0
    ball_ant = (0, 0)

    software.compute()
    ball_pos, paddle_pos, score = paint(software.outputArray, show_output=SHOW_GAME)

    ball_1 = ball_pos

    x_pad = paddle_pos[0]
    y_pad = paddle_pos[1]

    movement = 0

    while not software.finished:

        software.inputArray = [ movement ]
        software.compute()
        ball_pos, paddle_pos, score = paint(software.outputArray, show_output=SHOW_GAME)

        ball_2 = ball_pos
        x_pad = paddle_pos[0]

        if (ball_2[1] - ball_1[1]) == 0:
            x_predicted = ball_2[0]
        else:
            x_predicted = (y_pad - ball_1[1]) / (ball_2[1] - ball_1[1]) * (ball_2[0] - ball_1[0]) + ball_1[0] -1

        if x_predicted < x_pad: # pad on the right
            movement = -1
        elif x_pad < x_predicted: # pad on the left
            movement = 1
        else: # pad on the spot
            movement = 0

        # If the ball is going up move with the ball
        if ball_2[1] < ball_1[1]:
            movement = ball_2[0] - ball_1[0]

        software.inputArray = [ movement ]
        # print(f'xpad: {x_pad} | xpred: {x_predicted} | mov: {movement}')
        ball_1 = ball_2

    # Show the final game
    a,b,c = paint(software.outputArray)
    print(f'FINAL SCORE: {score}')



def main():
    input = Input(DAY, 2019, line_parser = integers)
    program = list(input[0])

    # print(f'Part 1: {part1(program)}')
    # print('')
    print(f'Part 2:')# {part2(program)}')
    part2(program)


if __name__ == "__main__":
    main()