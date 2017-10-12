import java.io.*;
import java.util.*;

public class Solution {
    
    static long inversion = 0;
    
    private static void mergeArray(int[] data, int[] buffer, int start, int mid, int end){
        int i = start, j = mid+1;
        int upBound_i = mid, upBound_j = end;
        int k = 0;
        while(i<=upBound_i && j<=upBound_j){
            if(data[i]<=data[j]){
                buffer[k++] = data[i++];
            }
            else{
                buffer[k++] = data[j++];
                inversion+=(mid-i+1);
            }
        }

        while(i<=upBound_i)
            buffer[k++] = data[i++];
        while(j<upBound_j)
            buffer[k++] = data[j++];
        for(int cur=0; cur<k; cur++)
            data[start+cur] = buffer[cur];
    }
    
    private static void mergeSort(int[] data, int[] buffer, int start, int end){
        if(start<end){
            int mid = (start+end)/2;
            mergeSort(data, buffer, start, mid);
            mergeSort(data, buffer, mid+1, end);
            mergeArray(data, buffer, start, mid, end);
        }
    }
    
    private static void calInversion(int[] data){
        int buffer[] = new int[data.length];
        mergeSort(data, buffer, 0, data.length-1);
    }
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int t=0; t<T; t++){
            int n = sc.nextInt();
            int data[] = new int[n];
            for(int i=0; i<n; i++)
                data[i] = sc.nextInt();
            calInversion(data);
            System.out.println(inversion);
            inversion = 0;
        }
        sc.close();
        
    }
}