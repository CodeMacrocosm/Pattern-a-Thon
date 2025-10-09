public class ArrowPattern {
    public static void main(String[] args) {
        int n = 7;

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n-i; j++){
                System.out.print(" ");
            }
            for(int j = 1; j <= i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
        for(int i = n-1; i >= 1; i--){
            for(int j = 1; j <= n-i; j++){
                System.out.print(" ");
            }
            for(int j = 1; j <= i; j++){
                System.out.print("*");
            }
            System.out.println();
        }

        int stem_width = n / 2;
        int stem_height = n;
        for(int i = 1; i <= stem_height; i++){
            for(int j = 1; j <= n-1; j++){
                System.out.print(" ");
            }
            for(int j = 1; j <= stem_width; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
