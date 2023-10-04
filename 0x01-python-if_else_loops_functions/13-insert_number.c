#include "lists.h"

/**
 * insert_node - singly linked list
 * @number: integer
 * @head: points to the head node
 * Return: Pointer to new node
 * Description: singly linked list node structure
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp_node, *prev_node;

	new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	temp_node = *head;

	if (head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;

		return (new_node);
	}
	else if (temp_node->n > number)
	{
		new_node->next = temp_node;
		*head = new_node;

		return (new_node);
	}
	else
	{
		while (temp_node->next != NULL && temp_node->n <= number)
		{
			prev_node = temp_node;
			temp_node = temp_node->next;
		}
		prev_node->next = new_node;
		new_node->next = temp_node;
	}
	return (new_node);
}
