import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the larrysArray function below.
    static String larrysArray(int[] A) {
              int B[]=new int[A.length];
              for(int c=0;c<A.length;c++)
              {
                  B[c]=A[c];
              }
              System.out.println("HI");
              for(int k=0;k<B.length-1;k++)
              {
                  for(int s=0;s<B.length-k-1;s++)
                  {
                      if(B[s]>B[s+1])
                      {
                      int tm=B[s];
                      B[s]=B[s+1];
                      B[s+1]=tm;
                      }
                  }
              }
              for(int i=0;i<A.length-2;i++)
              {
                  int pos=-1;
                  for(int j=i;j<A.length;j++)
                  {  
                      if(A[j]==B[i])
                      {
                         pos=j;
                         break;
                      }
                  }
                      while(pos!=i)
                      {
                          if(pos!=A.length-1)
                          {
                          int temp;
                          temp=A[pos+1];
                          A[pos+1]=A[pos-1];
                          A[pos-1]=A[pos];
                          A[pos]=temp;
                        
                          }
                          else
                          {
                              int t=A[pos-1];
                              A[pos-1]=A[pos];
                              A[pos]=A[pos-2];
                              A[pos-2]=t;
                          }
                          pos--;
                      }           
              }
              if(A[A.length-2]==A.length-1)
                 {                    System.out.println("YES");

                     return "YES";
                 }
              else
              {
                  System.out.println("NO");
                 return "NO";
              }

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] A = new int[n];

            String[] AItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int AItem = Integer.parseInt(AItems[i]);
                A[i] = AItem;
            }

            String result = larrysArray(A);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
