#include<stdlib.h>
#include<stdio.h>
#define max(a,b) (a>b?a:b)

int maxSubArray(int* nums,int numSize){
    int n = numSize;
    int **dp;
    // dp = (int *)malloc(n*n*sizeof(int)); 
    dp=(int**)malloc(sizeof(int*)*n);  
    for(int i=0;i<n;i++){
        dp[i]=(int*)malloc(sizeof(int)*n);
        for(int j=0;j<n;j++){
            dp[i][j] = 0;
        }
    };  
    int maxx =  0x80000000 ;
    for (int i=n-1;i>=0;i--){
        dp[i][i] = nums[i];
        maxx = max(maxx,dp[i][i]);
        for (int j=i+1;j!=n;j++){
            dp[i][j] = max(dp[i+1][j]+nums[i],dp[i][j-1]+nums[j]);
            maxx = max(dp[i][j],maxx);
        }
    }
    free(dp);
    return maxx;
}
int nums[9] = {-2,1,-3,4,-1,2,1,-5,4};
int main(){
    printf("%d",maxSubArray(nums,9));
}