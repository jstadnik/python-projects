import sys

"""
An easy program that illustrates the recursive solution to a "Towers of Hanoi" 
problem for a specified number of rings on the first tower.
The internal representation of the towers is a list of length 3 -- 
Each element representing one tower. To represent a tower we use a list of ints,
where each element is one ring and its value the size of the ring. 
The first elemtent of the list is the bottom-most ring on the tower. 

***Currently the version is missing checks to ensure we don't place a bigger
ring on a smaller ring, which should not occur anyway using 
this non-naive implementation, but.***
"""


def make_stick(column_list):
    """
    Given a list of rings, generate a graphical representation of 
    each level of the tower, for one tower. 
    """
    stick = []
    for i in range(height):
        if i < len(column_list):
            stick.append('*'*column_list[i])
        else:
            stick.append('|')
    return stick


def draw_board(board):
    """Given the internal representation of the board, render a human-friendly view."""
    board_of_sticks = []
    for column in board:
        board_of_sticks.append(make_stick(column))
    board_zipped = list(zip(board_of_sticks[0], board_of_sticks[1], 
        board_of_sticks[2]))
    string = "";
    for i in range(height, 0, -1):
        string += "".join(x.ljust(12) for x in board_zipped[i-1])
        string += "\n"
    print(string)

def the_other(not_this, and_not_this):
    """Find the missing tower"""
    for i in range(3):
        if i != not_this and i != and_not_this:
            return i

def move(board, what, where):
    """
    Recursive method performing a specified move on the board.
    what -- tuple of the form (tower_to_take_rings_from, number_of_rings_to_move_counting_from_top)
    where -- tower to move the rings to
    """

    #The base case of the recursion -- if there's only one ring, just move it.
    if what[1] == 1:
        bad_boy = board[what[0]][-1]
        board[what[0]] = board[what[0]][:-1]
        board[where].append(bad_boy)
        return board

    #We have more rings to move.

    #First, move all BUT the biggest ring (of the rings to move) 
    #to the OTHER tower that is neither "from" tower nor "where" tower
    the_other_stick = the_other(what[0], where)
    board = move(board, [what[0], what[1]-1], the_other_stick)
    draw_board(board)
    
    #Identify the remaining biggest ring and move it to the destination
    bad_boy = board[what[0]][-1]
    board[what[0]] = board[what[0]][:-1]
    board[where].append(bad_boy)
    draw_board(board)
    
    #Move what we've put on the other tower to the destination
    board = move(board, [the_other_stick, what[1]-1], where)
    return board #return the monster we've created in this move


def run(board):
    """First step, kick off the game -- tell the program to move the stack 
    from the first tower to the last""" 
    draw_board(board)
    board = move(board, [0, len(board[0])], 2)
    draw_board(board)


if __name__ == "__main__":
    
    #This is just to make the "sticks" of the towers of hanoi an equal
    #height throught the running of the program -- visual purpose only
    global height
    height = 4
   
    if len(sys.argv) == 1:
        print ("You didn't provide the number of rings to start with, so I'll pick 5")
        no_of_rings = 5
    else: 
        no_of_rings = int(sys.argv[1])

    if no_of_rings > height:
        height = no_of_rings #if there are more than 4 rings, we need to make the towers higher
    run([list(range(no_of_rings, 0, -1)), [], []])
        
