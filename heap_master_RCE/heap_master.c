#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

struct slot_t {
    char *str;
};
struct slot_t *slot[0x10] = {0};

void add()
{
    int idx;
    printf("idx:\n> ");
    scanf("%d", &idx);

    slot[idx] = malloc(sizeof(struct slot_t));
    slot[idx]->str = "heap_master";
}

void del()
{
    int idx;
    printf("idx:\n> ");
    scanf("%d", &idx);
    
    if (slot[idx])
        free(slot[idx]);
}

void show()
{
    int idx;
    printf("idx:\n> ");
    scanf("%d", &idx);
    
    if (slot[idx] && slot[idx]->str)
        printf("%s\n", slot[idx]->str);
}

void edit()
{
    int idx;
    printf("idx:\n> ");
    scanf("%d", &idx);
    
    if (slot[idx]) {
        int size;
        printf("size:\n> ");
        scanf("%d", &size);

        slot[idx]->str = malloc(size);
        size = size < 0x100 ? 0x100 : 0x100;
        read(0, slot[idx]->str, size);
    }
}

int main()
{
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);

    void *gift = malloc(0x10);
    printf("GIFT: %p\n", gift);
    strcpy(gift, "FLAG{TEST}");

    char buf[0x8];

    while (1)
    {
        printf("1. add\n"
               "2. del\n"
               "3. show\n"
               "4. edit\n"
               "5. bye\n"
               "> ");
        read(0, buf, 2);
        switch (buf[0]) {
        case '1': add();  break;
        case '2': del();  break;
        case '3': show(); break;
        case '4': edit(); break;
        case '5': goto _main_bye;
        }
    }

_main_bye:
    return 0;
}
