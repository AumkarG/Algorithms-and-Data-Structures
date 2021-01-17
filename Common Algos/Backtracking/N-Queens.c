#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void check(int [],int,int);
void main()
{
	int n;
	printf("ENTER SIZE OF CHESSBOARD\n");
	scanf("%d",&n);
	int arr[n+1];
	for(int i=0;i<n;i++)
   	arr[i]=-1;
	arr[n]=0;
	int row=0;
	check(arr,row,n);
	printf("\n No. of solutions is : %d",arr[n]);
}
void print(int arr[],int n)
{
	for(int k=0;k<n;k++)
	{
    	for(int j=0;j<n;j++)
    	{
        	if(arr[k]==j)
           	printf("Q\t");
        	else
           	printf("_\t");
    	}
    	printf("\n");
	}
	printf("\n\n");
}
void check(int arr[],int row,int n)
{
  	for(int i=0;i<n;i++)
  	{
      	int flag=0;
      	for(int j=0;j<row;j++)
      	{
          	if(arr[j]==i || abs(arr[j]-i)==abs(j-row))
          	{
              	flag=1;
              	break;
          	}
      	}
      	if(flag==0)
      	{
          	arr[row]=i;
          	if(row==n-1)
          	{
              	print(arr,n);
              	arr[n]+=1;
          	}
          	else
             	check(arr,row+1,n);
      	}
      	arr[row]=-1;
  	}
}
