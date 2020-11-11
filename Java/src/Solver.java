public class Solver{
    public static int[] findZero(int[][] board){
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                if (board[i][j] == 0) {;
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }

    public static boolean solverBacktracking(int[][] board){
        int[] empty = Solver.findZero(board);
        if(empty == null){
            return true;
        }
        int row = empty[0], col = empty[1];

        for(int i = 1; i <= 9; i++){
            if(Functions.validNum(row, col, i, board)){
                board[row][col] = i;

                if(Solver.solverBacktracking(board)){
                    return true;
                }
                board[row][col] = 0;
            }
        }
        return false;
    }

    public static void main(String[] args){
        final long start_time = System.currentTimeMillis();
        int[][] board = {{0, 6, 2, 0, 1, 7, 0, 5, 0},
                        {0, 0, 0, 0, 0, 0, 0, 2, 0},
                        {0, 5, 0, 0, 0, 0, 7, 0, 0},
                        {0, 0, 0, 2, 0, 0, 0, 6, 9},
                        {0, 4, 1, 0, 0, 0, 0, 0, 0},
                        {0, 0, 0, 8, 9, 0, 0, 0, 0},
                        {1, 0, 0, 0, 7, 4, 0, 0, 5},
                        {0, 0, 0, 0, 0, 0, 0, 0, 0},
                        {3, 0, 0, 0, 5, 0, 1, 0, 0}};
        Functions.printBoard(board);
        
        Solver.solverBacktracking(board);
        System.out.println();
        Functions.printBoard(board);
        final long elapsed_time = System.currentTimeMillis() - start_time;
        System.out.printf("Elapsed Time (in miliseconds): %f", (float)elapsed_time);

    }
}
