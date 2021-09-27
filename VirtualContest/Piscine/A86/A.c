#include<stdio.h>
#include<unistd.h>
#include<string.h>



int main(void)
{
	int a;
	int b;
	scanf("%d", &a);
	scanf("%d", &b);

	if (a<10 && b<10){
		int ans = a*b;
		printf("%d",ans);
	}else{
		printf("-1");
	}
}	
