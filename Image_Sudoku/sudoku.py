#====================================================#
#       Printing Board in real-time board format     #
#====================================================#
def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")

        for j in range(len(b)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")

                
#====================================================#        
#        Lookup for empty/zero value in Board        #
#====================================================#
                
def lookup_empty(b):
    for row in range(len(b)):
        for col in range(len(b)):            
            # return postion (x,y) if missing box found in board
            if b[row][col] == 0:
                return (row, col)
    return None


#====================================================#
#  Validating board if new number is enter in empty  # 
#====================================================#
def valid_n(b, n, pos):
    
    #checking in row
    for col in range(len(b)):
        if col != pos[1] and b[pos[0]][col] == n:
            return False
        
    #checking in column
    for row in range(len(b)):
        if row != pos[0] and b[row][pos[1]] == n:
            return False
       
    
    #checking in sub-board (3x3) in which we are validating that number
    sb_x = pos[1]//3     #let say for 7 at (2,7),  pos[1] is 7 and so sb_x = 7//3 == 2 
    sb_y = pos[0]//3     #let say for 7 at (2,7),  pos[0] is 2 and so sb_y = 2//3 == 0
    #so here 2 along x axis and 0 along y axis
    
    for row in range( sb_y * 3, sb_y * 3 + 3):         #for above example it will loop from 0 to 3
        for col in range(sb_x * 3, sb_x * 3 + 3):       #for above example it will loop from 6 to 9
            if (row,col) != pos and b[row][col] == n:   # so like (0,6) to (3,9)
                return False
    
    return True

#====================================================#
#                    Sudoku solver                   # 
#====================================================#
def solver(b):
    get_pos = lookup_empty(b)
    
    if not get_pos:
        return True
    else: 
        row,col = get_pos
        
    for i in range(1,10):
        if valid_n(b, i, (row, col)):
            b[row][col] = i
            
            if solver(b):
                return True
            
            b[row][col] = 0
            
    return False


#====================================================#
#               Validating solved board              # 
#====================================================#
def validation(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if not valid_n(b, b[i][j], (i,j)):
                return False
    return True