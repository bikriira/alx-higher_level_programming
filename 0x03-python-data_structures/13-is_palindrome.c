#include "lists.h"
#include <stdio.h>


/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: The head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr, *slow, *fast, *second_head;
	int first_round = 1, round_count = 0;

	curr = *head, slow = *head, fast = *head;
	if (*head == NULL)
		return (1);
	while (curr != NULL)
	{
		if (fast->next == NULL)
		{
			divide_list(&slow, &fast, &round_count);
			break;
		}
		else if (first_round == 0)
		{
			if (fast->next->next == NULL)
			{
				divide_list(&slow, &fast, &round_count);
				break;
			}
		}
		else
		{
			slow = slow->next;
			fast = fast->next->next;
			first_round = 0;
		}
		round_count++;
		curr = curr->next;
	}
	second_head = slow;
	curr = *head;
	while (curr != NULL)
	{
		if (curr->n != second_head->n)
			return (0);
		curr = curr->next;
		second_head = second_head->next;
	}
	return (1);
}


/**
 * divide_list - This chunks the list into two evenly lists
 * @slow: The address of the slow node
 * @fast: the address of the fast node
 * @round: Times the original list was iterated
 * To know if the list was iterated only once so that the condition in this
 * function won't be executed(Helps alot if the list contains only 3 nodes
 *
 * Return: Void
 */
void divide_list(listint_t **slow, listint_t **fast, int *round)
{
	int checked = 0;
	listint_t *prev = NULL;

	while (*slow != NULL)
	{
		listint_t *next = (*slow)->next;
		(*slow)->next = prev;
		prev = *slow;
		*slow = next;

		if ((*fast)->next != NULL && checked == 0 && *round > 1)
		{
			if ((*fast)->next->next == NULL)
			{
				prev = NULL;
				checked = 1;
			}
		}
	}
	*slow = prev;
}
