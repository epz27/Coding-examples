# -*- coding: utf-8 -*-


def sudokHelp(board,pos,regions,region_assign,rows,cols,op):
    '''
    Solves Sudoku board using backtracking, by trying each possible number that is not already
    in the current row, column, or region


    '''
    if pos==len(op):
        return board
    
    pt=op[pos]
    (reg1,reg2)=region_assign[pt]
    for num in "123456789":
        if num not in regions[reg1][reg2] and num not in rows[pt[0]] and num not in cols[pt[1]]:
            board[pt[0]][pt[1]]=num
            regions[reg1][reg2].add(num)
            rows[pt[0]].add(num)
            cols[pt[1]].add(num)
            ans=sudokHelp(board,pos+1,regions,region_assign,rows,cols,op)
            if ans!=None:
                return ans
            board[pt[0]][pt[1]]="."
            regions[reg1][reg2].remove(num)
            rows[pt[0]].remove(num)
            cols[pt[1]].remove(num)
            
    return None


def sudoku(board):
    '''
    

    Parameters
    ----------
    board : 9 x 9 valid Sudoku board, to be solved

    Returns
    -------
    solved 9 x 9 board.

    '''
    regions=[]
    region_assign={}
    rows=[]
    cols=[]
    op=[]
    for i in range(3):
        regions.append([])
        for j in range(3):
            regions[i].append(set())    
    for i in range(len(board)):
        rows.append(set())
        for j in range(len(board)):
            if len(cols)<j+1:
                cols.append(set())
            if board[i][j]==".":
                op.append((i,j))
                # open position that needs to be filled
            else:
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
            if 0<=i<=2:
                reg1=0
            elif 3<=i<=5:
                reg1=1
            else:
                reg1=2
            if 0<=j<=2:
                reg2=0
            elif 3<=j<=5:
                reg2=1
            else:
                reg2=2
            region_assign[(i,j)]=(reg1,reg2)
            # a way to determine which of 9 regions a pair (i,j) is in
            if board[i][j]!=".":
                regions[reg1][reg2].add(board[i][j])
                #the number board[i][j] can't be used for any other pair in 
                #region_assign[(i,j)]
    return sudokHelp(board,0,regions,region_assign,rows,cols,op)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(sudoku(board))

                
