import java.util.Scanner;
import java.lang.*;
public class B432G{
public static void main(String ar[]){
   Scanner sb=new Scanner(System.in);
   String s1=sb.nextLine();
    int n=Integer.parseInt(s1);
	int c=0;
	int a[]=new int[100000];
	int a1[]=new int[n];
	for(int i=0;i<n;i++)
	{
	  String s=sb.nextLine();
	  String s2[]=s.split(" ");
	  c=Integer.parseInt(s2[0]);
	  a[c-1]++;
	  a1[i]=Integer.parseInt(s2[1]);
	  }
	  	for(int i=0;i<n;i++){
		 System.out.println((n-1+a[a1[i]-1])+" "+(n-1-a[a1[i]-1]));
		 }
		 }}
	  