#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insert a number into a sorted listint_t
 * @head: the head of the list
 * @n: the number to be inserted
 * Return: a pointer to the inserted node, or NULL if the insertion failed
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new_node, *node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	node = *head;
	new_node->n = n;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	if ((*head)->n > n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (1)
	{
		if ((node->n <= n) && ((node->next == NULL) || ((node->next)->n > n)))
		{
			new_node->next = node->next;
			node->next = new_node;
			return (new_node);
		}
		node = node->next;
	}
}
