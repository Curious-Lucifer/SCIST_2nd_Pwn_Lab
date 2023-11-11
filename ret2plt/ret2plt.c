#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);

    if (puts("never call system") >= 0)
        system("echo never_call");

    unsigned long addr;
    printf("addr: ");
    scanf("%lu", &addr);
    read(0, (char *)addr, 8);

    char name[0x10];
    printf("What's your name: ");
    scanf("%s", name);
    puts(name);

    return 0;
}