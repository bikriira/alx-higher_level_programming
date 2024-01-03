#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: The head of the list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *helper = list, *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		helper = helper->next;
		hare = hare->next->next;

		if (helper == hare)
		return (1);
	}

	return (0);
}

