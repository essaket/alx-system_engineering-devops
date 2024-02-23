#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop to make the program hang
 * Return: always 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates a 5 zombie processes
 * Return: always 0
 */
int main(void)
{
	int x;
	pid_t zombie;

	for (x = 0; x <= 4; x++)
	{
		zombie = fork();
		if (zombie > 0)
		{
			printf("Zombie process created, PID: %d\n", zombie);
			infinite_while();
		}
		else
			return (0);
	}
	infinite_while();
	return (0);
}
