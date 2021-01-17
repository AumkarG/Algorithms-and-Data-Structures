import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the organizingContainers function below.
    static String organizingContainers(int[][] container) {
        int n=container.length;
        int c[]=new int[n];
        int ballc[]=new int[n];
        for(int i=0;i<n;i++)
        {
            c[i]=0;
            ballc[i]=0;
        }
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<n;k++)
            {
                c[j]+=container[j][k];
                ballc[j]+=container[k][j];
            }
        }
        for(int m=0;m<n;m++)
        {
             for(int p=0;p<n-m-1;p++)
             {
                 int temp;
                 if(c[p]>c[p+1])
                 {
                     temp=c[p];
                     c[p]=c[p+1];
                     c[p+1]=temp;
                 }
                 if(ballc[p]>ballc[p+1])
                 {
                     temp=ballc[p];
                     ballc[p]=ballc[p+1];
                     ballc[p+1]=temp;
                 }
             }
        }
        for(int q=0;q<n;q++)
        {
            if(c[q]!=ballc[q])
              return "Impossible";
        }
        return "Possible";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[][] container = new int[n][n];

            for (int i = 0; i < n; i++) {
                String[] containerRowItems = scanner.nextLine().split(" ");
                scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

                for (int j = 0; j < n; j++) {
                    int containerItem = Integer.parseInt(containerRowItems[j]);
                    container[i][j] = containerItem;
                }
            }

            String result = organizingContainers(container);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
