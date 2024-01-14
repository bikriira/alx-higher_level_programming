#include "lists.h"
#include <stdio.h>


int is_palindrome(listint_t **head)
{
	listint_t *curr, *slow, *fast, *prev, *second_head;
	int checked = 1;

	curr = *head;
	slow = *head;
	fast = *head;
	if (*head == NULL)
		return (1);

	prev = NULL;
	while (curr != NULL)
	{
		if (fast->next == NULL)
		{
			printf("Middle %d\n", slow->n);
			make_new_list(&slow, &fast, &prev, &checked);
			printf("Done reversing\n");
			break;
		}
		else if (fast->next->next == NULL)
		{
			make_new_list(&slow, &fast, &prev, &checked);
			break;
		}
		else
		{
			printf("Not yet slow at middle, slow: %d\n", slow->n);
			slow = slow->next;
			fast = fast->next->next;
		}
		curr = curr->next;
	}
	second_head = slow;
	if (slow == NULL)
		printf("HHHHH\n");
	printf("The value at second head is %d\n", slow->n);
	printf("Asign second_harf to slow, new list head\n");

	curr = *head;
	while (curr != NULL)
	{
		printf("Start checking elem curr: %d, 2curr: %d\n", curr->n, second_head->n);
		if (curr->n != second_head->n)
			return (0);
		printf("Cheking elem\n");
		curr = curr->next;
		second_head = second_head->next;
	}
	printf("\nend...\n");

	return (1);
}

void make_new_list(listint_t **slow, listint_t **fast, listint_t **prev, int *checked)
{
	while (*slow != NULL)
	{
		listint_t *next = (*slow)->next;
    	(*slow)->next = *prev;
    	*prev = *slow;
    	*slow = next;
    	printf("Slow is %d\n", (*prev)->n);

		if ((*fast)->next != NULL && *checked == 1)
		{
			if ((*fast)->next->next == NULL)
			{
				*prev = NULL;
				*checked = 0;
				printf("The list is even making its last-second part point to null\n");
			}
		}
	}
	*slow = *prev;
}
