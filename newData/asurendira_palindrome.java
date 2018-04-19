// java program for palindrome
// taken from https://stackoverflow.com/questions/4138827/check-string-for-palindrome?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
// authors (stackoverflow usernames): Michael Myers, dcp

public static boolean istPalindrom(char[] word){
    int i1 = 0;
    int i2 = word.length - 1;
    while (i2 > i1) {
        if (word[i1] != word[i2]) {
            return false;
        }
        ++i1;
        --i2;
    }
    return true;
}