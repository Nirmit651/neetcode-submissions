class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const seenSquares = Array.from({ length: 9 }, () => new Set());

        for(let i = 0;i<board.length;i++) {
            const seenRow = new Set();
            const seenCol = new Set();
            for(let j = 0;j<board[i].length;j++) {
                //row
                if(board[i][j] == ".") {
                    
                }else if(seenRow.has(board[i][j])){
                    return false;
                } else {
                    seenRow.add(board[i][j])
                }

                //col
                if(board[j][i] == ".") {
                    
                }else if(seenCol.has(board[j][i])){
                    return false;
                } else {
                    seenCol.add(board[j][i])
                }

                //square
                if (board[i][j] !== ".") {
                    const squareIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);
                    if (seenSquares[squareIndex].has(board[i][j])) {
                        return false;
                    }
                    seenSquares[squareIndex].add(board[i][j]);
                }
                
            } // end of for loop
            seenRow.clear();
            seenCol.clear();
        } // end of outer for loop


        return true;

    }
}
