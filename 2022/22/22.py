from Board import Board
from Cube import Cube
from input import input1, input2
from utils import transitions, transitionsDemo
from re import findall


def main():
    [case_board, case_path] = input1.split('\n\n')
    [case_board, case_path] = case_board.split(
        '\n'), findall('(\d+|[RL]+)', case_path)
    board = Board(case_board)
    board.applyMovements(case_path)
    print(board.getAwnser())

    [case_board, case_path] = input2.split('\n\n')
    [case_board, case_path] = case_board.split(
        '\n'), findall('(\d+|[RL]+)', case_path)
    board = Board(case_board)
    board.applyMovements(case_path)
    print(board.getAwnser())

    [case_board, case_path] = input1.split('\n\n')
    [case_board, case_path] = case_board.split(
        '\n'), findall('(\d+|[RL]+)', case_path)
    cube = Cube(case_board, 4, transitionsDemo)
    cube.applyMovements(case_path)
    print(cube.getAwnser())

    [case_board, case_path] = input2.split('\n\n')
    [case_board, case_path] = case_board.split(
        '\n'), findall('(\d+|[RL]+)', case_path)
    cube = Cube(case_board, 50, transitions)
    cube.applyMovements(case_path)
    print(cube.getAwnser())


main()
