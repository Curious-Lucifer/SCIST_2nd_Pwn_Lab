#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);

    char name[0x10];
    read(0, name, 0x100);

    return 0;
}