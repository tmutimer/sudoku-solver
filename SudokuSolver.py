import numpy as np;
#input grid
grid_in = np.array([[3, 0, 6, 0, 0, 8, 4, 0, 0],[0, 8, 0, 0, 1, 0, 7, 2, 0],[2, 0, 0, 0, 4, 0, 0, 0, 9],[5, 0, 7, 0, 0, 9, 0, 1, 0],[0, 0, 0, 0, 3, 0, 0, 9, 0],[0, 3, 0, 0, 5, 0, 2, 0, 7],[1, 0, 8, 0, 0, 4, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 4, 8],[9, 2, 0, 1, 0, 7, 3, 0, 0]]);
ans_grid = grid_in
#the rules
# 1. each 3x3 square has 1-9 exactly
# 2. each row has 1-9 exactly
# 3. each column has 1-9 exactly

#==========================
#== Function Definitions ==
#==========================

#eval_square function will find what possible answers there are for a given square in a sudoku grid
def eval_square(ans_grid, coord):
    validation_values = [];
    for b in ans_grid[coord[0],:]:
        if b < 10:
            validation_values.append(b)
    for c in ans_grid[:,coord[1]]:
        if c < 10:
            validation_values.append(c)
    for d in ans_grid[3*int(coord[0]/3):3*int(coord[0]/3)+3,3*int(coord[1]/3):3*int(coord[1]/3)+3].flat:
        if d < 10:
            validation_values.append(d)
    possibilities = np.setdiff1d(range(1,10),validation_values);
    return possibilities;

#compute_all_workings finds all the possible answers and 'writes' them in each box
def compute_all_workings(ans_grid):
    for i in range(9):
        for j in range(9):
            if ans_grid[i,j] > 9 or ans_grid[i,j] == 0:
                poss_concat = '';
                possibilities = eval_square(ans_grid, [i,j]);
                for k in possibilities:
                    poss_concat += str(k)
                ans_grid[i,j] = poss_concat;
    return ans_grid;

#crunch attempts to solve each position by checking if any number is the only possibility for the row, column or square
def crunch(ans_grid):

    for i in range(9):
        for j in range(9):
            validation_values_row = [];
            validation_values_col = [];
            validation_values_squ = [];
            if ans_grid[i,j] > 9:
                str_workings = str(ans_grid[i,j]);
                expanded_workings = [];
                for k in str_workings:
                    expanded_workings.append(k);
                for b in ans_grid[i,:][:]:
                    str_validation = str(b);
                    for x in str_validation:
                        validation_values_row.append(x);
                for c in ans_grid[:,j][:]:
                    str_validation = str(c);
                    for x in str_validation:
                        validation_values_col.append(x);
                for d in ans_grid[3*int(i/3):3*int(i/3)+3,3*int(j/3):3*int(j/3)+3].flat[:]:
                    str_validation = str(d);
                    for x in str_validation:
                        validation_values_squ.append(x);
                for y in expanded_workings:
                    validation_values_squ.remove(y);
                    validation_values_col.remove(y);
                    validation_values_row.remove(y);
                row_crunch = np.setdiff1d(expanded_workings,validation_values_row);
                col_crunch = np.setdiff1d(expanded_workings,validation_values_col);
                squ_crunch = np.setdiff1d(expanded_workings,validation_values_squ);
                if len(row_crunch) == 1:
                    ans_grid[i,j] = row_crunch;
                elif len(col_crunch) == 1:
                    ans_grid[i,j] = col_crunch;
                elif len(squ_crunch) == 1:
                    ans_grid[i,j] = squ_crunch;
    return ans_grid;

def process_input(in_str):
    num_list = np.empty(0, int)
    for x in in_str:
        num_list = np.append(num_list, [int(x)]);
    grid = np.reshape(num_list,[9,9]);
    return grid;

#======================
#==     Program      ==
#======================

print('Hi, this is my first program and I am very proud of it.');
instruction = 'r'
while instruction == 'r':
    print('Input the grid as a series of numbers in one long line, typing a zero for the blank squares')
    input_grid = input();
    grid = process_input(input_grid);
    print('If this looks right, just hit enter, or if you want to redo, enter "r".')
    print (grid[0,0],grid[0,1],grid[0,2],'|',grid[0,3],grid[0,4],grid[0,5],'|',grid[0,6],grid[0,7],grid[0,8]);
    print (grid[1,0],grid[1,1],grid[1,2],'|',grid[1,3],grid[1,4],grid[1,5],'|',grid[1,6],grid[1,7],grid[1,8]);
    print (grid[2,0],grid[2,1],grid[2,2],'|',grid[2,3],grid[2,4],grid[2,5],'|',grid[2,6],grid[2,7],grid[2,8]);
    print('---------------------');
    print (grid[3,0],grid[3,1],grid[3,2],'|',grid[3,3],grid[3,4],grid[3,5],'|',grid[3,6],grid[3,7],grid[3,8]);
    print (grid[4,0],grid[4,1],grid[4,2],'|',grid[4,3],grid[4,4],grid[4,5],'|',grid[4,6],grid[4,7],grid[4,8]);
    print (grid[5,0],grid[5,1],grid[5,2],'|',grid[5,3],grid[5,4],grid[5,5],'|',grid[5,6],grid[5,7],grid[5,8]);
    print('---------------------');
    print (grid[6,0],grid[6,1],grid[6,2],'|',grid[6,3],grid[6,4],grid[6,5],'|',grid[6,6],grid[6,7],grid[6,8]);
    print (grid[7,0],grid[7,1],grid[7,2],'|',grid[7,3],grid[7,4],grid[7,5],'|',grid[7,6],grid[7,7],grid[7,8]);
    print (grid[8,0],grid[8,1],grid[8,2],'|',grid[8,3],grid[8,4],grid[8,5],'|',grid[8,6],grid[8,7],grid[8,8]);
    instruction = input();
loops = 0
solved = False
while not solved and loops < 81:
    grid = compute_all_workings(grid);
    grid = crunch(grid);
    loops += 1;
    if np.sum(grid) == (45*9):
        solved = True;
if solved:
    print("Here's the answer:");
    print (grid[0,0],grid[0,1],grid[0,2],'|',grid[0,3],grid[0,4],grid[0,5],'|',grid[0,6],grid[0,7],grid[0,8]);
    print (grid[1,0],grid[1,1],grid[1,2],'|',grid[1,3],grid[1,4],grid[1,5],'|',grid[1,6],grid[1,7],grid[1,8]);
    print (grid[2,0],grid[2,1],grid[2,2],'|',grid[2,3],grid[2,4],grid[2,5],'|',grid[2,6],grid[2,7],grid[2,8]);
    print('---------------------');
    print (grid[3,0],grid[3,1],grid[3,2],'|',grid[3,3],grid[3,4],grid[3,5],'|',grid[3,6],grid[3,7],grid[3,8]);
    print (grid[4,0],grid[4,1],grid[4,2],'|',grid[4,3],grid[4,4],grid[4,5],'|',grid[4,6],grid[4,7],grid[4,8]);
    print (grid[5,0],grid[5,1],grid[5,2],'|',grid[5,3],grid[5,4],grid[5,5],'|',grid[5,6],grid[5,7],grid[5,8]);
    print('---------------------');
    print (grid[6,0],grid[6,1],grid[6,2],'|',grid[6,3],grid[6,4],grid[6,5],'|',grid[6,6],grid[6,7],grid[6,8]);
    print (grid[7,0],grid[7,1],grid[7,2],'|',grid[7,3],grid[7,4],grid[7,5],'|',grid[7,6],grid[7,7],grid[7,8]);
    print (grid[8,0],grid[8,1],grid[8,2],'|',grid[8,3],grid[8,4],grid[8,5],'|',grid[8,6],grid[8,7],grid[8,8]);
    print("The puzzle grid was crunched {attempts} times to get the answer".format(attempts=loops));
elif not solved:
    print ('Here is the best I could do:');
    print(grid);


#NOTES
#the compute/crunch combo is not enough to solve it every time. Need a third thing.
#here is a stalemated board from compute/crunching
#[   17   167     4   169 16789    18     5     3     2]
#[    3    26     8  2456    56    24     1     9     7]
#[    5     9    27   123    17   123     6     8     4]
#[  279    27     1     8     4     6    29     5     3]
#[    6    23   239   129    19     5     4     7     8]
#[    4     8     5    29     3     7    29     1     6]
#[   89     4   369   356   568    38     7     2     1]
#[ 1278     5   237   134    18  1348    38     6     9]
#[   18   136    36     7     2     9    38     4     5]
