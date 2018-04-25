class EntryOfPascalsTriangle {
    public static void main(String[] args) {
        validateInput(args);

        int row = 0;
        row = parseInteger(args[0]);

        int column = 0;
        column = parseInteger(args[1]);

        // A Pascal’s triangle expands quadratic.
        // There are never entries at a position greater column length
        if (column > row) {
            handleError("There can't be entries in a column that doesn't exist in a Pascal's triangle.");
        }

        // We know already that the first and last entries in a row are always 1
        if (column == 0 || column == row) {
            System.out.println(1);
            System.exit(0);
        }

        int pascalsTriangle[][] = initPascalsTriangle(row);

        // initPascalsTriangle() takes care of the cases `0` and `1` already …
        if (row > 1) {
            // … so we can start to fill the rows starting from 2.
            pascalsTriangle = fillPascalRows(pascalsTriangle, 2);
        }

        System.out.println(pascalsTriangle[row][column]);
    }

    /**
     * Initializes a Pascal’s triangle with all cells filled with `0`
     * except for the first and last cell in a row which are `1`
     */
    private static int[][] initPascalsTriangle(int rows) {
        int[][] pascalsTriangle = new int[rows+1][];

        // Iterate over the columns of the rows of pascalsTriangle
        for (int cell = 0; cell < pascalsTriangle.length; cell++) {
            pascalsTriangle[cell] = new int[cell+1];

            // Fill the first cell of each row with `1`
            pascalsTriangle[cell][0] = 1;

            // Also fill the last cells with `1`
            pascalsTriangle[cell][cell] = 1;
        }

        return pascalsTriangle;
    }

    /**
     * Fills in the cells of Pascal’s triangle recursively
     */
    private static int[][] fillPascalRows(int[][] pascalsTriangle, int row) {
        for (int cell = 1; cell < pascalsTriangle[row].length-1; cell++) {
            pascalsTriangle[row][cell] = pascalsTriangle[row-1][cell-1] + pascalsTriangle[row-1][cell];
        }

        if (row < pascalsTriangle.length-1) {
            fillPascalRows(pascalsTriangle, row+1);
        }

        return pascalsTriangle;
    }

    /**
     * We need to make sure that two arguments are provided
     * and fail with a helpful message if they weren’t.
     */
    private static void validateInput(String[] args) {
        if (args.length < 2) {
            handleError("Not enough arguments.");
        }

        if (args.length > 2) {
            handleError("Too many arguments.");
        }
    }

    /**
     * Small wrapper to parse strings as integers.
     */
    private static int parseInteger(String arg) {
        int result = 0;

        try {
            result = Integer.parseInt(arg);
        } catch (NumberFormatException nfe) {
            handleError("'" + arg + "' was not an integer.");
        }

        return result;
    }

    /**
     * Small wrapper to produce error messages
     */
    private static void handleError(String errorMessage) {
        String basicUsage = "Please enter the column and the row of a Pascal's triangle.";
        System.out.println(errorMessage);
        System.out.println("\n" + basicUsage);
        System.exit(1);
    }
}