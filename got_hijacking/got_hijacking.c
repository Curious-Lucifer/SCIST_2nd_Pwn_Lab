#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void backdoor()
{
    system("/bin/sh");
}

int main()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);

    unsigned long addr;
    printf("addr: ");
    scanf("%lu", &addr);
    read(0, (char *)addr, 8);
    exit(1);
}