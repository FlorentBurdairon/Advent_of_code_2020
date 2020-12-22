# Solve day3 : find the number of trees you will encounter
# Remember : the slope is right 3, down 1
import numpy as np

def read_puzzle_input( myfilename ):
    input_list = list()
    with open(myfilename) as fp:
        filecontent = fp.readlines()
        for element in filecontent:
            input_list.append(element[:-1])
    return input_list

def forest_size( input_list ):
    Lx = len(input_list[0])
    Ly = len(input_list)
    return Lx, Ly

def convert_input_to_matrix( input_list ):
    Lx, Ly = forest_size( input_list )
    input_forest_matrix = np.zeros([Ly,Lx], dtype=np.int8)
    i=0
    for entry in input_list:
        j = 0
        for element in entry:
            if element == '.':
                input_forest_matrix[i,j] = 0
            elif element == '#':
                input_forest_matrix[i,j] = 1
            else:
                print(f"[Error] {element} is not a valid element")
                input_forest_matrix[i,j] = np.nan
            j += 1
        i += 1
    return input_forest_matrix

def repeat_forest( slope, input_forest_matrix ):
    Lx = input_forest_matrix.shape[1]
    Ly = input_forest_matrix.shape[0]
    dx = slope[0] ; dy = slope[1]
    delta_x = Lx-1 ; delta_y = Ly-1
    if dy/dx < delta_y/delta_x:
        delta_y_max = delta_y
        delta_x_max = delta_y_max* dx/dy
        x_mult = int(delta_x_max/Lx) +1
        print(f"The forest must be repeated {x_mult} times in the direction x")
        repeated_forest = np.tile( input_forest_matrix, x_mult )
    else:
        print("No need to repeat horizontally")
        repeated_forest = input_forest_matrix
    return repeated_forest

def get_path_into_forest( slope, repeated_forest ):
    path = np.array([], dtype=np.int8)
    x_pos = 0
    y_pos = 0
    while y_pos < repeated_forest.shape[0]:
        path = np.append(path, repeated_forest[y_pos, x_pos])
        x_pos += slope[0]
        y_pos += slope[1]
    nb_trees = sum(path)
    return nb_trees

def solve_part1( slope, input_list ):
    input_forest_matrix = convert_input_to_matrix( input_list )
    repeated_forest = repeat_forest( slope, input_forest_matrix )
    nb_encountered_trees = get_path_into_forest( slope, repeated_forest )
    return nb_encountered_trees

def solve_part2( list_of_slopes, input_list ):
    answer = 1
    for slope in list_of_slopes:
        print("-------------------------------------------------------")
        print(f"slope = ({slope[0]}, {slope[1]})")
        nb_of_trees = solve_part1( slope, input_list )
        answer = answer * nb_of_trees
    print("-------------------------------------------------------")
    print(f"Answer to part 2 is {answer}")


# Convention : x increasing from left to the right, y increasing from top to bottom, origin is top left
slope = np.array([3,1])
print(f"Remember : the slope is {slope[0]} horizontal, {slope[1]} vertical")
filename = "puzzle.input"
dirname = "./"
input_list = read_puzzle_input( dirname+filename )
Lx, Ly = forest_size( input_list )
print(f"The dimensions of the input are : {Lx} horizontal units, {Ly} vertical units")
print(f"Part 1 : number of trees encountered on the path = {solve_part1( slope, input_list )}")

list_of_slopes = np.array([[1,1], [3,1], [5,1], [7,1], [1,2]])
solve_part2( list_of_slopes, input_list )
