
public class PascalsTriangle {
	private int rows;
	private long[] finalRow;


	public PascalsTriangle(int rows) {
		this.rows = rows;

		long[] r = {1};
		long[] preR;
		for (int x=1; x<=rows; x++) {
			preR = r;
			// calc size of new r=x;
			r = new long[x];
			int y=0;
			while (y<x) {
				r[y] = calcValue(preR, y);
				y++;
			}
			public static writeToFile(){
		BufferedWriter bw = null;
		FileWriter fw = null;


		} catch (IOException e) {
		}
		finalRow = r;
	}

	public long[] getPascalsTriangle() {

		return finalRow;
	}
public static writeToFile(){
		BufferedWriter bw = null;
		FileWriter fw = null;

		try {

			String content = "This is the content to write into file\n";

			fw = new FileWriter(FILENAME);
			bw = new BufferedWriter(fw);
			bw.write(content);

			System.out.println("Done");

		} catch (IOException e) {
	public String toString() {
		long[] r = {1};
		long[] preR;
		String retStr = "Pascal Triangle size " + Integer.toString(rows);
		retStr += "\n";
		for (int x=1; x<=rows; x++) {
			preR = r;
			// calc size of new r=x;
			r = new long[x];
			int y=0;
			while (y<x) {
				r[y] = calcValue(preR, y);
				retStr += Long.toString(r[y]);
				retStr += " ";
				y++;
			}
			retStr += "\n";
		}

		return retStr;
	}
	private long calcValue(long[] r, int y) {
		long ret = getValue(y-1,r) + getValue(y,r);
		return ret;
	}

	private long getValue(int y, long[] r) {
		if (y<0) {
			return 0;
		} else if (y>=r.length) {
				return 0;
		} else {
				return r[y];
		}
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int rows = Integer.parseInt(args[0]);
		PascalsTriangle t = new PascalsTriangle(rows);

		System.out.println(t);

		String s = t.getPoly();
		System.out.println("poly = " + s);
	}

	private String getPoly() {
		long[] r = {1};
		System.out.println("r0 is " + r[0]);
		long[] preR;
		String retStr = "Pascal Polynomial size " + Integer.toString(rows);
		retStr += "\n";
		for (int x=1; x<=rows; x++) {
			preR = r;
			// calc size of new r=x;
			r = new long[x];
			int y=0;
			while (y<x) {
				r[y] = calcValue(preR, y);
				y++;
			}

		}
		int maxLen = r.length-1;
		retStr += "x^" + Integer.toString(maxLen) + " + ";
		for (int x=1; x<maxLen; x++){
			retStr += Long.toString(r[x]) + getPower("x",maxLen-x) + getPower("y",x) + " + ";
		}
		retStr += "y^" + Integer.toString(maxLen) + " ";
		return retStr;
	}

}