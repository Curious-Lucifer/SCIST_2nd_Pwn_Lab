#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    
    char fmt[0x10] = {0};
    int gogo = 1;

    while (gogo)
    {
        memset(fmt, 0, 0x10);
        read(0, fmt, 0x10);
        printf(fmt);
    }

    return 0;
}
