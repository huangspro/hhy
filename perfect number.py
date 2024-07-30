from time import *
a=time()
p=1
for i in range(0,10000):
    m=0
    for i in range(1,p):
   	 if (p/i)%1==0:
  	     m=m+i
    if m==p:
       print(p)
    print(p)   
    p=p+1
b=time()
print(str(b-a)+"  s")

==============================================================

import java.util.*;

public class HelloWorld { 
    public static void main(String[] args) { 
    double k=System.currentTimeMillis();
    double y=0;
    double p=1;
    for(int hhh=0;hhh<=20000;hhh++){
    y=0;
    System.out.print(hhh);
    System.out.print('\n');
    for(double i=1;i<p;i++){
    if((p/i)==(int)(p/i)){
    y=y+i;}}
    if(y==p){System.out.print(p);System.out.print('\n');}
    p++;
    }
    double o=System.currentTimeMillis();
    System.out.print((o-k)/1000+"   s");
    }
}

==================================================================

#include<iostream>
#include <time.h>
using namespace std;

int main()
{
    double t=clock();
    
    int y=0;
    double p=1;
    for(int hhh=1;hhh<=20000;hhh++){
    
    y=0;
    for(double i=1;i<p;i++){
    if((p/i)==(int)(p/i)){
    y=y+i;}}
    if(y==p){cout<<p<<endl;}
    p++;
    }
    double h=clock();
    cout<<(h-t)/CLOCKS_PER_SEC<<"  s"<<endl;
    
    
}