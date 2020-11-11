import java.lang.Math;

public class Functions {
    static int[] base = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9};
    public static boolean validBoard(int[][] board) {
        int cont = 0;
        for(int i = 0; i < board.length; i++){
            if (board[i].length != Functions.base.length) return false;
            if (i == Functions.base.length) cont++;
        }
        if (cont > 0) return false;

        return true;
    }

    public static boolean validNum(int row, int col, int num, int[][] board){
        for(int i = 0; i < Functions.base.length; i++){
            if(board[row][i] == num) return false;
            if(board[i][col] == num) return false;
        }

        int box_x = (int) Math.floor(row/3);
        int box_y = (int) Math.floor(col/3);

        int cur_box_x = 3*box_x;
        int cur_box_y = 3*box_y;
        for(int i = cur_box_x; i < cur_box_x+3; i++){
            for(int j = cur_box_y; j < cur_box_y+3; j++){
                if(board[i][j] == num) return false;
            }
        }
        
        return true;
    }


    public static void printBoard(int[][] board){
        int i = 0, j = 0;
        for(int[] row : board){
            if(i % 3 == 0 && i != 0){
                System.out.print("---------------------------------\n");
            }
            for(int val : row){
                if(j % 3 == 0 && j != 0){
                    System.out.print(" | ");
                }
                System.out.printf(" %d ",val);
                j++;
            }
            System.out.println();
            j = 0;
            i++;
        }
    }


}