public class PascalsTriangle {
    
    public void generatePascalsTriangle(int level) {
        int[][] pascalsTriangle = new int[level][];
        
        pascalsTriangle[0] = new int[2];
        pascalsTriangle[0][0] = 1;
        
        for (int currentLevel = 1; currentLevel<level; currentLevel++) {
            pascalsTriangle[currentLevel] = new int[currentLevel+2];
            for(int j = 0; j<currentLevel+1; j++) {
                if(j == 0)
                    pascalsTriangle[currentLevel][j] = 1;
                else
                    pascalsTriangle[currentLevel][j] = pascalsTriangle[currentLevel-1][j]+pascalsTriangle[currentLevel-1][j-1];
            }
        }
        
        for (int i = 0; i<level; i++) {
            for (int j = 0; j<i+1; j++) {
                System.out.print(" "+pascalsTriangle[i][j]);
            }
            System.out.println("");
        }
    }
    
    private static void generateFactorials(BigInteger[] factorialArray) {
		factorialArray[0] = BigInteger.valueOf(1);
		int i=1;
		while(i < factorialArray.length) {
			factorialArray[i] = factorialArray[i - 1].multiply(BigInteger.valueOf(i));
			i++;
		}
	}

	private static void printTriangle(List<List<Integer>> triangle) {
		for (List<Integer> row : triangle) {
			for (int i : row) {
				System.out.print(i + " ");
			}
			System.out.println("");
		}
	}

    
    public static void main(String[] args) {
        PascalsTriangle obj = new PascalsTriangle();
        obj.generatePascalsTriangle(6);
    }
}