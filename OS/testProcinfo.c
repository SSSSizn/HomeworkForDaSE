#include "types.h"
#include "user.h"
#include "pstat.h"

int main(void)
{
    struct pstat st;
    if (getpinfo(&st) != 0)
    {
        printf(1,"Error retrieving process information\n");
        exit();
    }
    printf(1, "PID\tTickets\tln use\n");
    for(int i = 0; i < NPROC; i++)
    {
        if (st.inuse[i])
        {
            printf(1,"%d\t%d\t%d\n", st.pid[i], st.ticket[i], st.inuse[i]);
        }
    }
    exit();
}