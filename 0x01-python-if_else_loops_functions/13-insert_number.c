#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - a function that inserts a node in a ordered way
 *
 * @head: pointer to the head of the function
 *
 * @number: number to add to the list
 *
 * Return: pointer to the new added node
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp = NULL;
listint_t *mover = *head;
listint_t *new = malloc(sizeof(listint_t));
if (!new)
{
return (NULL);
}
if (!*head)
{
*head = new;
new->n = number;
new->next = NULL;
return (new);
}
if ((*head)->n > number)
{
new->n = number;
new->next = *head;
*head = new;
return (new);
}
while (mover->n < number)
{
if (mover->next != NULL)
{
temp = mover;
mover = mover->next;
}
else
{
new->next = NULL;
new->n = number;
temp->next = new;
}
}
new->next = mover;
new->n = number;
temp->next = new;
return (new);
}
