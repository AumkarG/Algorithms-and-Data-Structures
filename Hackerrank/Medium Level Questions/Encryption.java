import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the encryption function below.
    static String encryption(String s) {
        s=s.replace(" ","");
        int L=s.length();
        double t=Math.sqrt(L);
        double f=Math.floor(t);
        double c=Math.ceil(t);
        double r,col;
        if(f*c>=L)
        r=f;
        else
        r=f+1;
        col=c;
        String s1="";
        for(int i=0;i<col;i++)
        {
            for(int j=0;j<r;j++)
            {
                if(i+col*j>=L)
                    break;
                s1+=s.charAt((int)(i+col*j));
            }
            s1+=" ";               
        }
        return s1;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        String result = encryption(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
