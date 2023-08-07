#include "lists.h"

/**
 * check_cycle - check if a linked list has a cylce
 * @list: the head of the linked list
 * Return: 1 if the @list has a cycle, else 0
 *
 * Description - this function uses the Floyd’s Cycle-Finding Algorithm
 */
int check_cycle(listint_t *list)
{
	listint_t *slowp, *fastp;

	if (list == NULL)
		return (0);

	slowp = fastp = list;

	while (slowp && fastp && fastp->next)
	{
		slowp = slowp->next;
		fastp = fastp->next->next;

		if (slowp == fastp)  /* Pointer comparison */
			return (1);
	}

	return (0);
}
