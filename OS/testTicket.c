#include "types.h"
#include "user.h"
#include "pstat.h"

int main(int argc, char *argv[])
{
    int tickets;
    if (argc != 2)
    {
        printf(1, "Usage:testticket tickets\n");
        exit();
    }
    tickets = atoi(argv[1]);
    if (tickets < 1)
    {
        printf(1, "testticket:tickets must be at least one\n");
        exit();
    }
    printf(1,"setting tickets to %d\n", tickets);
    if (settickets(tickets) < 0)
    {
        printf(1, "testticket:failed to set tickets\n");
    }
    for(int i = 0; i < 1000000; i++)
    {
        asm("nop");
    }
    exit();
}