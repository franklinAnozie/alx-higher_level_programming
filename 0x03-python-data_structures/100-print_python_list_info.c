#include "Python.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @list: pointer to python list object list
 * Return: void
 */

void print_python_list_info(PyListObject *list)
{
	ssize_t i = 0, size, allocated;

	size = list->ob_base.ob_size;
	allocated = list->allocated;
	printf("[*] Size of the Python List: %ld\n", size);
	printf("[*] Allocated: %ld\n", allocated);
	while (i < size)
	{
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		i++;
	}
}
