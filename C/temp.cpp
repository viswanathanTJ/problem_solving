#include<bits/stdc++.h>
using namespace std;
int ans[10000000];
int dp[1000000];
int solve(int num)
 {
   if(num<0) return 0;
   if(dp[num]!=-1)
     {
     return dp[num];
    }
    else
    {
       long long int ret=0;
       int k=num;
       while(k!=0)
        {
           
           int v=k%10;
           if(v!=0)
    ret+=solve(num-v*v);
    k/=10;  
      }
      if(ret)
      dp[num]=1;
      else dp[num]=0;
      return dp[num];
    }
    return 0;
 }
int main()
 {
   int t;
   cin>>t;
   memset(dp,-1,sizeof dp);
  
  for(int i=0;i<10;i++)
   {
    int num=1;
     for(int j=1;j<=i;j++)
      {
       num*=i;
   }
   if(num<=1000000)
   {
    dp[num]=1;
   
   }
   
   }
  //  solve(10);
    for(int i=0;i<=1000000;i++)
     {
       int ty= solve(i);
       if(ty>=0) 
       {
         ans[i]=1; 
    }
  }
   while(t--)
   {
    
    int n;
       cin>>n;
       if(dp[n])
        {
         cout<<"Yes"<<endl;
     }
     else
     {
      cout<<"No"<<endl;
     }
   }
  
 }