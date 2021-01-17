import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the queensAttack function below.
    static int queensAttack(int n, int k, int r_q, int c_q, int[][] obstacles) {
        int n1,n2,n3,n4,n5,n6,n7,n8;
        n1=n-r_q;
        n2=Math.min(n-r_q,n-c_q);
        n3=n-c_q;
        n4=Math.min(n-c_q,r_q-1);
        n5=r_q-1;
        n6=Math.min(r_q-1,c_q-1);
        n7=c_q-1;
        n8=Math.min(n-r_q,c_q-1);
        
        for(int i=0;i<k;i++)
        {
            int r=obstacles[i][0];
            int c=obstacles[i][1];
            if(r==r_q)
            {
                if(c>c_q&&(c-c_q-1)<n3)
                    n3=c-c_q-1;
                else if(c<c_q&&(c_q-1-c)<n7)
                    n7=c_q-1-c;
                    
            }
            else if(c==c_q)
            {
                if(r>r_q&&(r-r_q-1)<n1)
                    n1=r-r_q-1;
                else if(r<r_q&&(r_q-1-r)<n5)
                    n5=r_q-1-r;
            }
            else if(Math.abs(r_q-r)==Math.abs(c_q-c))
               {
                if(r>r_q&&c>c_q)
                {
                     if(r-r_q-1<n2)
                       n2=r-r_q-1;
                }
                else if(c<c_q&&r<r_q)
                {
                   if(r_q-r-1<n6)
                       n6=r_q-r-1;
                }
                else if(c<c_q&&r>r_q)
               {
                if(r-r_q-1<n8)
                    n8=r-r_q-1;
               }
               else if(c>c_q&&r<r_q)
               {
                  if(r_q-r-1<n4)
                      n4=r_q-r-1;
               }
            }    
            
        }
        return n1+n2+n3+n4+n5+n6+n7+n8;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]);

        String[] r_qC_q = scanner.nextLine().split(" ");

        int r_q = Integer.parseInt(r_qC_q[0]);

        int c_q = Integer.parseInt(r_qC_q[1]);

        int[][] obstacles = new int[k][2];

        for (int i = 0; i < k; i++) {
            String[] obstaclesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 2; j++) {
                int obstaclesItem = Integer.parseInt(obstaclesRowItems[j]);
                obstacles[i][j] = obstaclesItem;
            }
        }

        int result = queensAttack(n, k, r_q, c_q, obstacles);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
