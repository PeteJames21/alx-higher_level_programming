#include "lists.h"

/**
 * check_cycle - check if a linked list has a cylce
 * @list: the head of the linked list
 * Return: 1 if the @list has a cycle, else 0
 */
int check_cycle(listint_t *list)
{
	int has_cycle = 0, i = 0, j = 0;
	listint_t *current, *head, *tmp;

	if (list == NULL)
		return (0);

	current = head = tmp = list;

	while (current != NULL)
	{
		for (j = 0; j < i; j++)
		{
			if (tmp == current->next)
			{
				return (1);  /* Cycle detected */
			}
			tmp = tmp->next;
		}
		current = current->next;
		tmp = head;
		i++;
	}

	return (0);
}
