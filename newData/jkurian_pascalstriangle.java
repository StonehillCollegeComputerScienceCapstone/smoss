import java.util.Arrays;

/**
 * Created by sdargo on 22/07/16.
 */

public class PascalsTriangle {

  public static int[][] computeTriangle(int numberOfLevels) {
    if (numberOfLevels < 0) { throw  new IllegalArgumentException(); }
    int[][] pascalsTriangle = new int[numberOfLevels][];
    for (int level=1; level <= numberOfLevels; ++level) {
      pascalsTriangle[level-1] = new int[level];
      int numberToAdd;
      for (int numbersOnLevel=1; numbersOnLevel <= level; ++numbersOnLevel) {
        if (level <= 2 || numbersOnLevel == 1  || numbersOnLevel == level) {
          numberToAdd = 1;
        } else {
          numberToAdd = pascalsTriangle[level - 2][numbersOnLevel - 2] + pascalsTriangle[level - 2][numbersOnLevel - 1];
        }
        pascalsTriangle[level - 1][numbersOnLevel - 1] = numberToAdd;
      }
    }
    printTriangle(pascalsTriangle);
    return pascalsTriangle;
  }

  private static void printTriangle(int[][] triangle) {
    for (int level = 0; level < triangle.length; ++level)
    {
      System.out.println("Level " + level);
      for (int element = 0; element <= level; ++element) {
        System.out.println(triangle[level][element]);
      }
    }
  }

  public static boolean isTriangle(int[][] inputTriangle) {
    int numberOfLines = inputTriangle.length;
    return Arrays.deepEquals(inputTriangle, PascalsTriangle.computeTriangle(numberOfLines));
  }
}