#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    
    char *myflag = malloc(0x30);
    int fd = open("flag.txt", O_RDONLY);
    read(fd, myflag, 0x30);
    close(fd);

    char fmt[0x10] = {0};
    while (1) {
        read(0, fmt, 0x10);
        printf(fmt);
    }

    return 0;
}