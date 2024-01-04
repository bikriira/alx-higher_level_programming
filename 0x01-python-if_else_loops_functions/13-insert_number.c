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
	new->next = NULL;
	if (helper == NULL)
	{
		*head = new;
		return (new);
	}
	while (helper != NULL)
	{
		next_holder = helper->next;
		if (helper->next == NULL)
		{
			helper->next = new;
			break;
		}
		if (helper->n >= number)
		{
			*head = new;
			new->next = helper;
			break;
		}
		if (helper->next->n >= number)
		{
			helper->next = new;
			new->next = next_holder;
			break;
		}
		helper = helper->next;
	}

	return (new);
}
