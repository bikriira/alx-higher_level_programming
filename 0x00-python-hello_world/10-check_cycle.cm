#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: The head of the list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *helper;
	int first = 1;

	while (list != NULL)
	{
		if (first == 1)
		{
			helper = list;
			first++;
		}
		if (list->next == helper)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}
