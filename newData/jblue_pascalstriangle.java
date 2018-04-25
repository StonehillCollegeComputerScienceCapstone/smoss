package combinatorics;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class PascalsTriangle {

    public static void main(String[] args) {
        System.out.println(new PascalsTriangle().pascals(5));
        System.out.println(new PascalsTriangle().nthPascal(3));
    }

    List<List<Integer>> pascals(int n) {
        List<List<Integer>> ret = new ArrayList<>(n);
        ret.add(Arrays.asList(1));
        for(int i = 1; i < n; ++i) {
            List<Integer> row = new ArrayList<>(Collections.nCopies(i + 1, 0));
            row.set(0, 1);
            row.set(i, 1);
            System.out.println(row)
            List<Integer> prev = ret.get(i - 1);
            int j=1;
            while(j<i){
                row.set(j ,prev.get(j) + prev.get(j - 1));
                j++;
        	}
            ret.add(row);
        }
        return ret;
    }
    
    	
	private String getPower(String a, int pow) {
		if (pow == 1) {
			
		} else {
			a += "^" + Integer.toString(pow);
		}
		return a;
	}

    List<Integer> nthPascal(int n) {
        if(n == 1)
            return Arrays.asList(1);
        List<Integer> res = new ArrayList<>(Collections.nCopies(n, 0));
        res.set(0, 1);
        res.set(1, 1);
        System.out.println(res)
        for(int i = 1; i < n ; ++i) {
            res.set(i, 1);
            int cur = 1;
            int next = res.get(1);
            int j=1; 
            while(j<i){
                cur = next;
                res.set(j, cur + next);
                next = res.get(j + 1);
                j++;
            }
        }
        return res;
    }
}