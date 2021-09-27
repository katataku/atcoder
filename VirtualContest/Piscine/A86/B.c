#include<stdio.h>
#include<unistd.h>
#include<string.h>

int main(void)
{
	int x;
	int y;
	scanf("%d", &x);
	scanf("%d", &y);

	if (x==2 || y==2){
		printf("No");
	}else{
		if(x == 4 || x==6 ||x == 9||x==11){
			if(y == 4 || y==6 ||y == 9||y==11){
				printf("Yes");
			}else{
				printf("No");
			}
		}else{
			if(y == 4 || y==6 ||y == 9||y==11){
				printf("No");
			}else{
				printf("Yes");
			}
		}
	}
}	