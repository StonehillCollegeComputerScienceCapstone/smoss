// credit: https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/d2nbgrl/

public class MagicSquare
{
static int[][] test = {{1,2,3},{4,5,6},{7,8,9}};

static int[][] test1 = {{8,1,6},{3,5,7},{4,9,2}};
static int[][] test2 = {{2,7,6},{9,5,1},{4,3,8}};
static int[][] test3 = {{3,5,7},{8,1,6},{4,9,2}};


public static boolean verifyMagicSquare(int[][] m_square){
    for (int i = 0; i <3;i++){
        if(!check3(m_square[i][0],m_square[i][1],m_square[i][2],15))
            return false;
    }
    for (int i =0;i<3; i++){
        if(!check3(m_square[0][i],m_square[1][i],m_square[2][i],15))
            return false;
    }
    if(!check3(m_square[0][0],m_square[1][1],m_square[2][2],15)) return false;
    if(!check3(m_square[0][2],m_square[1][1],m_square[2][0],15)) return false;

return true;

}
public static boolean check3(int i, int j, int k,int l){
    return i + j + k == l;
}

public static void main(String args[]){
    System.out.println(verifyMagicSquare(test));
    System.out.println(verifyMagicSquare(test1));
    System.out.println(verifyMagicSquare(test2));
    System.out.println(verifyMagicSquare(test3));
}
}