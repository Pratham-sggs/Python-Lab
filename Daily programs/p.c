#include <stdio.h>
int main(){
int a,b,c;
char operation;
printf("enter first number");
scanf("%d",&a);
printf("enter second number");
scanf("%d",&b);
printf("enter operation");
scanf(" %c",&operation);
if (operation=='+'){
    c=a+b;
}
else if (operation=='-'){
    c=a-b;

}
else if (operation=='*'){
    c=a*b;
    
}
else if (operation=='/'){
    c=a/b;
    
}
else 
printf ("error")

}
