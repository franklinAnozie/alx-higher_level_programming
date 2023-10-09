#include "lists.h"

int check_palindrome(int *array_n, int count);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: points to the head of the linked list
 * Return: 1 if it is a palindrome, 0 if it isn't
 */

int is_palindrome(listint_t **head)
{
	listint_t *iter;
	int *array_n;
	int count = 0, i = 0;

	if (head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	iter = *head;
	while (iter != NULL)
	{
		count++;
		iter = iter->next;
	}
	array_n = malloc(sizeof(int) * count);
	if (array_n == NULL)
	{
		return (0);
	}
	iter = *head;
	while (i < count)
	{
		array_n[i] = iter->n;
		iter = iter->next;
		i++;
	}
	i = check_palindrome(array_n, count);
	free(array_n);

	return (i);
}

/**
 * check_palindrome - checks an arrayof ints is a palindrome
 * @array_n: array to be checked
 * @count: number of elements in the array
 * Return: 1 if it is a palindrome, 0 if it isn't
 */

int check_palindrome(int *array_n, int count)
{
	int i = 0, j = count - 1;

	while (i < j)
	{
		if (array_n[i] != array_n[j])
		{
			return (0);
		}
		i++;
		j--;
	}
	return (1);
}
