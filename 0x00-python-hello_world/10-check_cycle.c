#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Checks for a cycle
  *
  * @list: the head of the list
  *
  * Return: 1 if cycle 0 if nothing
  */
int check_cycle(listint_t *list)
{
listint_t *f = list, *s = list;
int check = 0;
while ((f && s) && s->next)
{		
f = f->next;
if (s->next || s->next->next)
{	
s = s->next->next;
}
else
{
break;
}
if (f == s)
{
check = 1;
break;
}
}
return (check);
}