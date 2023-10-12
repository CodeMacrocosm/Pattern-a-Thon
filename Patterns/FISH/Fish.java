class Fish {
 
    // Function to print the pattern of a fish
    // over N rows
    public static void printFish(int N) {
 
        String spaces1 = "";
        String stars1 = "*", stars2 = "";
        for (int i = 0; i < N; ++i) {
            spaces1 += ' ';
        }
 
        for (int i = 0; i < 2 * N + 1; ++i)
        {
           
            // For upper part
            if (i < N) {
                System.out.print(spaces1 + stars1 + spaces1 + spaces1);
                System.out.println(stars2);
                spaces1 = spaces1.substring(0, spaces1.length() - 1);
                stars1 += "**";
                stars2 += "*";
            }
 
            // For middle part
            if (i == N) {
                System.out.print(spaces1 + stars1 + spaces1 + spaces1);
                System.out.println(stars2);
            }
 
            // For lower part
            if (i > N) {
                spaces1 += ' ';
                stars1 = stars1.substring(0, stars1.length() - 1);
                stars1 = stars1.substring(0, stars1.length() - 1);
                stars2 = stars2.substring(0, stars2.length() - 1);
                System.out.print(spaces1 + stars1 + spaces1 + spaces1);
                System.out.println(stars2);
            }
        }
    }
 
    // Driver Code
    public static void main(String args[]) {
        int N = 5;
        printFish(N);
    }
}
 