#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into a sorted singly
 * linked list.
 * @head: The address ot the first node.
 * @number: The number to be inserted in the list.
 *
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *helper = *head, *next_holder;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (helper == NULL)
	{
		new->next = helper;
		return (new);
	}
	while (helper != NULL)
	{
		if (helper->next->n >= number || helper->next == NULL)
		{
			next_holder = helper->next;
			helper->next = new;
			new->next = next_holder;
			break;
		}
		helper = helper->next;
	}

	return (new);
}
