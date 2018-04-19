// credit: https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/d21zwcw/
public class MagicSquare
{
public static boolean isMagicSquare(int[][] square) {
   int column, row, diag1, diag2, magicNum;
   magicNum = (int)(square.length*(Math.pow(square.length, 2)+1)/2);
   for (int counter = 0; counter < square.length; counter++) {
       column = 0;
       row = 0;
       for (int counter2 = 0; counter2 < square.length; counter2++) {
           row += square[counter][counter2];
           column += square[counter2][counter];
       }
       if (column != magicNum || row != magicNum) return false;
   }
   diag1 = 0;
   diag2 = 0;
   for (int diagCounter = 0; diagCounter < square.length; diagCounter++) {
       diag1 += square[diagCounter][square.length-diagCounter-1];
       diag2 += square[square.length-diagCounter-1][diagCounter];
   }
   if (diag1 != magicNum || diag2 != magicNum) return false;
   return true;
}
}