#include "lists.h"
#include <stdlib.h>

/**
 * len_listint_t - get the length of a listint_t
 * @head: a pointer to the head of the linked list
 * Return: the number of elements in the list
 */
int len_listint_t(listint_t *head)
{
	int size = 0;

	if (head == NULL)
		return (0);
	while (head)
	{
		size++;
		head = head->next;
	}

	return (size);
}

/**
 * listint_to_arr - convert a listint_t to an array of integers
 * @head: pointer to the head of the linked list
 * @size: number of nodes in the linked list
 * Return: pointer to the first element of the newly created array
 */
int *listint_to_arr(listint_t *head, int size)
{
	int *arr, i = 0;

	if (head == NULL)
		return (NULL);

	arr = malloc(sizeof(int) * size);
	if (arr == NULL)
		return (NULL);

	while (head)
	{
		arr[i] = head->n;
		i++;
		head = head->next;
	}

	return (arr);
}

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: a double pointer to the head of the linked list
 * Return: 1 if the list is a palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	int size, i, stop, is_palindrome = 1;
	int *arr;

	if (head == NULL)  /* An empty list is a palindrome */
		return (1);

	size = len_listint_t(*head);
	if (size == 1)  /* A list with one element is a palindrome */
		return (1);

	arr = listint_to_arr(*head, size);
	stop = size / 2;

	for (i = 0; i < stop; i++)
	{
		if (arr[i] != arr[size - i - 1])
		{
			is_palindrome = 0;
			break;
		}
	}
	free(arr);

	return (is_palindrome);
}
