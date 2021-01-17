import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the biggerIsGreater function below.
    static String biggerIsGreater(String w) {
        for(int i=w.length()-2;i>=0;i--)
        {
            for(int j=w.length()-1;j>i;j--)
            {
               if(w.charAt(j)>w.charAt(i))
               {
                       
                            String w1=w.substring(0,i)+w.charAt(j);
                            String w2=w.substring(i+1,j)+w.charAt(i)+w.substring(j+1);
                            StringBuilder s=new StringBuilder(w2);
                            s.reverse();
                       return w1+s;
                
               }
            }
        }
        return "no answer";


    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int T = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int TItr = 0; TItr < T; TItr++) {
            String w = scanner.nextLine();

            String result = biggerIsGreater(w);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
