#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

char myflag[0x30];

int main()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    
    int fd = open("flag.txt", O_RDONLY);
    read(fd, myflag, 0x30);
    close(fd);
    
    char sc[0x100];
    printf("shellcode: ");
    read(0, sc, 0x100);
    void (*func_ptr)(void);
    func_ptr = sc;
    (*func_ptr)();
    return 0;
}