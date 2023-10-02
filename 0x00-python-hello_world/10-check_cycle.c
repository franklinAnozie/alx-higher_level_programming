#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *first = list;
    listint_t *next = list;

    if (list == NULL)
    {
        return (0);
    }

    while(next->next != NULL)
    {
        first = first->next;
        next = next->next->next;
        if (first == next)
        {
            return (1);
        }
    }
    return(0);
}
