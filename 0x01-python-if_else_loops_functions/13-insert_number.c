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
listint_t *mover = *head;
listint_t *new = malloc(sizeof(listint_t));
if (!new)
{
return (NULL);
}
while (mover->next->n < number)
{
mover = mover->next;
}
new->next = mover->next;
new->n = number;
mover->next = new;
return (new);
}
