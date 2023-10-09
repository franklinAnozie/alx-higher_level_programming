#include "lists.h"

listint_t *reset_list(listint_t *reset, listint_t *mid);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: points to the head of the linked list
 * Return: 1 if it is a palindrome, 0 if it isn't
 */

int is_palindrome(listint_t **head)
{
	listint_t *last = *head, *chaser = *head;
	listint_t *mid = NULL, *reset = NULL, *second_half = NULL;
	listint_t *next_node = NULL, *first_half = NULL;
	int i = 1;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (i);
	}
	while (last != NULL && last->next != NULL)
	{
		reset = chaser;
		chaser = chaser->next;
		last = last->next->next;
	}
	if (last != NULL)
	{
		mid = chaser;
		chaser = chaser->next;
	}

	while (chaser != NULL)
	{
		next_node = chaser->next;
		chaser->next = second_half;
		second_half = chaser;
		chaser = next_node;
	}
	first_half = *head;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			i = 0;
			return (i);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	*head = reset_list(reset, mid);
	return (i);
}

/**
 * reset_list - resets list to its initail path
 * @reset: new head
 * @mid: continues list from middle
 * Return: the new head
 */

listint_t *reset_list(listint_t *reset, listint_t *mid)
{
	listint_t *next_node = NULL;

	reset->next = mid;
	while (mid != NULL)
	{
		next_node = mid->next;
		mid->next = reset;
		reset = mid;
		mid = next_node;
	}
	return (reset);
}
