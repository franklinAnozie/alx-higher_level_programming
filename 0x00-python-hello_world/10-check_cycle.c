#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *first_node = list;
    listint_t *next_node = list;

    if (list == NULL)
    {
        return (0);
    }

    while(next_node && next_node->next != NULL)
    {
        first_node = first_node->next;
        next_node = next_node->next->next;
        if (first_node == next_node)
        {
            return (1);
        }
    }
    return(0);
}
