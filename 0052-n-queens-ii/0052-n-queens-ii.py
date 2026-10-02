def safe(row,col,board,n):
    dupr=row
    dupc=col

    while(row>=0 and col>=0):
        if board[row][col]=='Q':
            return False
        row-=1
        col-=1
    row=dupr
    col=dupc
    while col>=0:
        if board[row][col]=='Q':
            return False
        col-=1
    row=dupr
    col=dupc
    while row<n and col>=0:
        if board[row][col]=='Q':
            return False
        row+=1
        col-=1
    return True

def queen(col,board,ans,n):
    if col==n:
        ans.append([''.join(row) for row in board])
        return  
    
    for row in range(n):
        if safe(row,col,board,n):
            board[row][col]='Q'
            queen(col+1,board,ans,n)
            board[row][col]='.'


class Solution:
    def totalNQueens(self, n: int) -> list[list[str]]:
        board=[['.']*n for _ in range(n)]
        ans=[]
        queen(0,board,ans,n)
        return len(ans)