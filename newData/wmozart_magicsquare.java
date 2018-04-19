// credit: https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/
public class DP_261 {

    public static void main(String[] args) {
        // TODO Auto-generated method stub

        ArrayList<int[]> inpArr = new ArrayList();
        inpArr.add(new int[] { 8, 1, 6, 3, 5, 7, 4, 9, 2 });
        inpArr.add(new int[] { 2, 7, 6, 9, 5, 1, 4, 3, 8 });
        inpArr.add(new int[] { 3, 5, 7, 8, 1, 6, 4, 9, 2 });
        inpArr.add(new int[] { 8, 1, 6, 7, 5, 3, 4, 9, 2 });

        for (int[] inp : inpArr) {
            System.out.println(Arrays.toString(inp) + " -> " + (isMagicSquare(inp) ? "true" : "false"));
        }

        ArrayList<int[]> inpArr_2 = new ArrayList();
        inpArr_2.add(new int[] { 8, 1, 6, 3, 5, 7 });
        inpArr_2.add(new int[] { 3, 5, 7, 8, 1, 6 });

        for (int[] inp : inpArr_2) {
            System.out.println(Arrays.toString(inp) + " -> " + (couldBeMagicSquare(inp) ? "true" : "false"));
        }
    }

    public static boolean isMagicSquare(int[] inp) {
        if (isPerfectSquare(inp.length)) {
            int sideLength = (int) Math.sqrt(inp.length);
            // horizontal
            int count = 0;
            for (int i = 0; i < sideLength; i++) {
                for (int j = 0; j < sideLength; j++) {
                    count += inp[sideLength * i + j];
                }
                if (count != 15) {
                    return false;
                }
                count = 0;
            }
            // vertiacal
            for (int i = 0; i < sideLength; i++) {
                for (int j = 0; j < sideLength; j++) {
                    count += inp[j * sideLength + i];
                }
                if (count != 15) {
                    return false;
                }
                count = 0;
            }
            // diagonal top left bottom right
            for (int i = 0; i < sideLength; i++) {
                count += inp[i * (sideLength + 1)];
            }
            if (count != 15) {
                return false;
            }
            count = 0;
            // diagonal top right bottom left
            count = 0;
            for (int i = 0; i < sideLength; i++) {
                count += inp[i * (sideLength - 1) + sideLength - 1];
            }
            if (count != 15) {
                return false;
            }
            return true;
        }
        return false; // NO SQUARE
    }

    public static boolean couldBeMagicSquare(int[] inp) {
        int sideLength = isPerfectSquareNoBottom(inp.length);
        int[] resArr = new int[sideLength];
        if (sideLength != 0) {
            // VERT
            int count = 0;
            for (int i = 0; i < sideLength; i++) {
                for (int j = 0; j < sideLength - 1; j++) {
                    count += inp[j * sideLength + i];
                }
                count = 15 - count;
                if (!(Arrays.asList(inp).contains(count) || Arrays.asList(resArr).contains(count) || count < 1
                        || count > 9)) {
                    resArr[i] = count;
                    count = 0;
                } else {
                    return false;
                }
            }
        }
        int[] array1and2 = new int[inp.length + resArr.length];
        System.arraycopy(inp, 0, array1and2, 0, inp.length);
        System.arraycopy(resArr, 0, array1and2, inp.length, resArr.length);
        return isMagicSquare(array1and2);
    }

    public static int isPerfectSquareNoBottom(int n) {
        int x = 2;
        while (true) {
            if (Math.pow(x, 2) > n) {
                if (Math.pow(x, 2) - n == x) {
                    return x;
                } else {
                    return 0;
                }
            }
            x++;
        }
    }

    // http://stackoverflow.com/questions/295579/fastest-way-to-determine-if-an-integers-square-root-is-an-integer
    public final static boolean isPerfectSquare(long n) {
        if (n < 0)
            return false;

        long tst = (long) (Math.sqrt(n) + 0.5);
        return tst * tst == n;
    }
}
