class MagicSquare
{

static void addUp(List<Integer> rowsColumnsList, List<Integer> square, int sideLength, boolean isPartial){
    int rows = 0;
    if(isPartial)
        rows = sideLength-1;
    else
        rows = sideLength;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < sideLength; j++){
            int rowValue = rowsColumnsList.get(i);
            rowValue += square.get(j);
            rowsColumnsList.set(i, rowValue);
            int colValue = rowsColumnsList.get(j+sideLength);
            colValue += square.get(i*sideLength+j);
            rowsColumnsList.set(j+sideLength, colValue);
        }
    }
}

static void createList(List<Integer> rowsColumnsList, int sideLength){
    for(int i = 0; i < 2 * sideLength; i++){
        rowsColumnsList.add(0);
    }
}

static int leftDiag(List<Integer> square, int sideLength, boolean isPartial){
    int leftDiag = 0;
    int rows = 0;
    if(isPartial)
        rows = sideLength-1;
    else
        rows = sideLength;
    for(int i = 0; i < rows; i++){
        if(i == 0){
            leftDiag += square.get(i);
        }
        else{
            leftDiag += square.get(sideLength * i + i);
        }
    }
    return leftDiag;
}

static int rightDiag(List<Integer> square, int sideLength, boolean isPartial){
    int rightDiag = 0;
    int rows = 0;
    if(isPartial)
        rows = sideLength-1;
    else
        rows = sideLength;
    for(int i = 0; i < rows; i++){
        if(i == 0){
            rightDiag += square.get(sideLength-1);
        }
        else{
            rightDiag += square.get(sideLength * (i + 1) - (i + 1));
        }
    }
    return rightDiag;
}

static boolean checkSquare(List<Integer> square, int sideLength){
    int leftDiag = 0, rightDiag = 0;
    List<Integer> rowsColumnsList = new ArrayList<Integer>();
    createList(rowsColumnsList, sideLength);
    addUp(rowsColumnsList, square, sideLength, false);
    leftDiag = leftDiag(square, sideLength, false);
    rightDiag = rightDiag(square, sideLength, false);
    boolean allSame = true;
    int magicNumber = rowsColumnsList.get(0);
    for(int i = 0; i < rowsColumnsList.size(); i++){
        if(rowsColumnsList.get(i) != magicNumber)
            allSame = false;
    }
    if(allSame && leftDiag == magicNumber && rightDiag == magicNumber)
        return true;
    else
        return false;
}

static List<Integer> findMissingNums(List<Integer> square, int sideLength){
    List<Integer> missingNums = new ArrayList<Integer>();
    List<Integer> squareList = new ArrayList<Integer>();
    for(int i = 0; i < square.size(); i++){
        squareList.add(square.get(i));
    }
    Collections.sort(squareList);
    for(int i = 0; i < sideLength; i++){
        squareList.add(0);
    }
    for(int i = 0; i < squareList.size(); i++){
        if(squareList.get(i-missingNums.size()) != i+1)
            missingNums.add(i+1);
    }
    return missingNums;
}

static void getSumsFinishSquare(List<Integer> rowsColumnsList, List<Integer> missingNums, List<Integer> list, List<Integer> square, int sideLength, int magicNumber){
    magicNumber = rowsColumnsList.get(0);
    for(int i = 0; i < rowsColumnsList.size(); i++){
        for(int j = 0; j < missingNums.size(); j++){
            if(missingNums.get(j) == magicNumber - rowsColumnsList.get(i)){
                int value = rowsColumnsList.get(i);
                value += missingNums.get(j);
                rowsColumnsList.set(i, value);
                list.add(missingNums.get(j));
                value = rowsColumnsList.get(sideLength-1);
                value += missingNums.get(j);
                rowsColumnsList.set(sideLength-1, value);
                square.add(missingNums.get(j));
                missingNums.remove(j);
                break;
            }
        }
    }
}

static List<Integer> checkPartialSquare(List<Integer> square, int sideLength){
    int leftDiag = 0, rightDiag = 0, magicNumber = 0;
    List<Integer> list = new ArrayList<Integer>();
    List<Integer> rowsColumnsList = new ArrayList<Integer>();
    createList(rowsColumnsList, sideLength);
    addUp(rowsColumnsList, square, sideLength, true);
    leftDiag = leftDiag(square, sideLength, true);
    rightDiag = rightDiag(square, sideLength, true);
    if(rowsColumnsList.get(sideLength) == rightDiag && rowsColumnsList.get(rowsColumnsList.size()-1) == leftDiag){
        List<Integer> missingNums = new ArrayList<Integer>();
        missingNums = findMissingNums(square, sideLength);
        getSumsFinishSquare(rowsColumnsList, missingNums, list, square, sideLength, magicNumber);
        if(checkSquare(square, sideLength))
            return list;
        else{
            System.out.println("Your square is not solvable without repeating number. Try to rework your square.");
        }
    }
    else{
        System.out.println("Your square is not solvable without repeating numbers. Try to rework your square.");
        return null;
    }
    return list;
}

@SuppressWarnings("resource")
public static void main(String[] args){
    System.out.print("Would you like to check a full(f) magic square or a partial(p) one with a missing bottom line?: ");
    Scanner fOrM = new Scanner(System.in);
    String reply = fOrM.next();

    reply.toLowerCase();

    if(reply.compareTo("p") != 0 && reply.compareTo("f") != 0){
        System.out.println("You didn't follow the rules. Now you get to restart the application.");
        System.exit(1);
    }

    System.out.print("What is the size of one side of your square?(i.e. 4 for a 4x4 square): ");
    Scanner grid = new Scanner(System.in);

    int square = grid.nextInt();
    List<Integer> square_num_list = new ArrayList<Integer>();

    if(reply.equals("p")){
        System.out.println("Enter the numbers for a " + square + "x" + square + " square minus the last line, separting numbers with spaces:");
        grid = new Scanner(System.in);
        for(int i = 0; i < square*square-square; i++){
            square_num_list.add(grid.nextInt());
        }
    }

    else if(reply.equals("f")){
        System.out.println("Enter the numbers for a " + square + "x" + square + " square, separting numbers with spaces:");
        grid = new Scanner(System.in);
        for(int i = 0; i < square*square; i++){
            square_num_list.add(grid.nextInt());
        }
    }

    fOrM.close();
    grid.close();

    System.out.print("\n[");

    if(reply.equals("f")){
        for(int i = 0; i < square_num_list.size(); i++){
            if(i == square_num_list.size()-1)
                System.out.print(square_num_list.get(i) + "]");
            else if((i+1)%square == 0)
                System.out.print(square_num_list.get(i) + ",\n ");
            else
                System.out.print(square_num_list.get(i) + ", ");
        }
        System.out.println(" => " + checkSquare(square_num_list, square));
    }

    else if(reply.equals("p")){
        for(int i = 0; i < square_num_list.size(); i++){
            if((i+1)%square == 0)
                System.out.print(square_num_list.get(i) + ",\n ");
            else
                System.out.print(square_num_list.get(i) + ", ");
        }
        System.out.println("\nThe final line should be:\n");
        List<Integer> lastLine = new ArrayList<Integer>();
        lastLine = checkPartialSquare(square_num_list, square);
        if(lastLine != null){
            for(int i = 0; i < lastLine.size(); i++){
                if((i+1) == lastLine.size())
                    System.out.println(lastLine.get(i) + "]\n");
                else
                    System.out.print(lastLine.get(i) + ", ");
            }
            System.out.print("[");
            for(int i = 0; i < square_num_list.size(); i++){
                if(i == square_num_list.size()-1)
                    System.out.println(square_num_list.get(i) + "]\n");
                else if((i+1)%square == 0)
                    System.out.print(square_num_list.get(i) + ",\n ");
                else
                    System.out.print(square_num_list.get(i) + ", ");
            }
            System.out.println("Verified by the full square check function!");
        }
    }
}
}