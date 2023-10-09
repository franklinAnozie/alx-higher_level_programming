#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: points to the head of the linked list
 * Return: 1 if it is a palindrome, 0 if it isn't
 */

int is_palindrome(listint_t **head)
{
	listint_t *last = *head, *chaser = *head;
	listint_t *second_half = NULL;
	listint_t *next_node = NULL, *first_half = NULL;
	int i = 1;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (i);
	}
	while (last != NULL && last->next != NULL)
	{
		chaser = chaser->next;
		last = last->next->next;
	}
	if (last != NULL)
	{
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
	return (i);
}
