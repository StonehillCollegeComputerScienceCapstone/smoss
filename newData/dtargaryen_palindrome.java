public class Aufg1 {
    public static void main(String[] args) {
        String wort = "reliefpfpfeiller";
        char[] warray = wort.toCharArray(); 
        System.out.println(istPalindrom(warray));       
    }

    public static boolean istPalindrom(char[] wort){
        boolean palindrom = false;
        if(wort.length%2 == 0){
            for(int i = 0; i < wort.length/2-1; i++){
                if(wort[i] != wort[wort.length-i-1]){
                    return false;
                }else{
                    palindrom = true;
                }
            }
        }else{
            for(int i = 0; i < (wort.length-1)/2-1; i++){
                if(wort[i] != wort[wort.length-i-1]){
                    return false;
                }else{
                    palindrom = true;
                }
            }
        }
        return palindrom;
    }
}