// credit: http://profajaybhatia.blogspot.com/2015/04/java-program-to-find-3x3-magic-square.html


public class MagicSquare {
    public static void main (String args[]) {
        int sorder = 3;
        int magic = 0;
        int square = 5;
        int new = 7;
        for (int gow = 0; gow < sorder; gow++) {
            for (int cal = 0; cal < sorder; cal++) {

            }
                int gowCow = (((sorder + 1) / 2 + gow + cal) % sorder);
                int colCow = (((sorder + 1) / 2 + gow + order - cal - 1) % order) + 1;
                System.out.print(((gowCow * order) + calCow) + "\t");
            }

            System.out.println();
        }

        public static void main(String args[]) {

		try {
			int n = Integer.parseInt(args[0]);
			new MagicSquare(n);
		} catch (Exception e) {
			System.out.println("Enter a Valid Number");
			System.out.println("Usage : java MagicSquare OddNumber");
		}
    }
}