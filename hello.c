#include <stdio.h>
#include <stdlib.h>

void display();
void create();
void ins_at_last();

typedef struct node {
  struct node *prev;
  int data;
  struct node *next;
} node;
node *start=NULL;

int main(void) {

  char *var_list = "Hello there!\n";

  printf(var_list);

  create();
  ins_at_last();
  ins_at_last();
  ins_at_last();
  display();
}

void display() {
  node *iter = start;
  while (iter != NULL) {
    printf("%i\t", iter->data);
    iter=iter->next;
  }
  printf("\n");
}

void create() {
  if (start != NULL) {
    start = NULL;
  } else {
    node *first = malloc(sizeof(node));
    start = first;
    printf("\nEnter the data for the first node: ");
    scanf("%i", &first->data);
  }
}

void ins_at_beg(){
  node* beg=malloc(sizeof(node));
  beg->next=start;
  start->prev=beg;
  printf("\nEnter the data for the node: ");
  scanf("%i", &beg->data);
}

void ins_at_last() {
  node *iter = start;
  while (iter->next != NULL) {
    iter = iter->next;
  }
  node *last = malloc(sizeof(node));
  iter->next = last;
  last->prev = iter;  
  printf("\nEnter the data for the last node: ");
  scanf("%i", &last->data);
}