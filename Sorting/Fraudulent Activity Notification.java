import java.io.*;
import java.util.*;

class DS{
    public double data;
    public int index;
    DS(double d,int i){
        data=d;index=i;
    }
    public String toString(){
        return "{"+data+" "+index+"}";
    }
}

public class Solution {
    public static void removeAndBalance(TreeSet<DS> starting,TreeSet<DS> ending,int index,double element){
        if(starting.contains(new DS(element,index)))
            starting.remove(new DS(element,index));
        else{
            ending.remove(new DS(element,index));
            ending.add(starting.pollLast());
        }
    }
    public static void addIn(TreeSet<DS> starting,TreeSet<DS> ending,int index,double element){
        if(element>ending.first().data){
            ending.add(new DS(element,index));
            starting.add(ending.pollFirst());
        }
        else{
            starting.add(new DS(element,index));
        }
    }
    public static void main(String[] args) throws Exception{
//        Scanner in=new Scanner(new File("C://Users//Saransh Jain//Desktop//input01.txt"));
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();int m=in.nextInt();
        double[] arr=new double[n];
        for(int i=0;i<n;i++)
            arr[i]=in.nextDouble();
        TreeSet<DS> starting=new TreeSet<>(new Comparator<DS>(){
        	public int compare(DS a,DS b){
                if(a.data<b.data)
                    return -1;
                if(a.data>b.data)
                    return 1;
                if(a.index<b.index)
                    return -1;
                if(a.index>b.index)
                    return 1;
                return 0;
        	}
        });

        TreeSet<DS> ending=new TreeSet<>(new Comparator<DS>(){
        	public int compare(DS a,DS b){
                if(a.data<b.data)
                    return -1;
                if(a.data>b.data)
                    return 1;
                if(a.index<b.index)
                    return -1;
                if(a.index>b.index)
                    return 1;
                return 0;
        	}
        });
        for(int i=0;i<m;i++)
            starting.add(new DS(arr[i],i));
//        System.out.println(starting.last());
        for(int i=0;i<m/2;i++)
            ending.add(starting.pollLast());
        double median;int notif=0;
        for(int i=m;i<n;i++){
            if(m%2==0)
                median=(starting.last().data+ending.first().data)/2;
            else
                median=starting.last().data;
//            System.out.println(median+" "+arr[i]);
//            System.out.println(starting+" "+ending);
            if(arr[i]>=2*median)
                notif++;
            removeAndBalance(starting,ending,i-m,arr[i-m]);
            addIn(starting,ending,i,arr[i]);
        }
        System.out.println(notif);
    }
}