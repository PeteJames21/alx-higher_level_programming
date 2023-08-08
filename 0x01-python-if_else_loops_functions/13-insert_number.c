#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

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

	if ((node->next == NULL) && (node->n > n))
	{
		new_node->next = node;
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
