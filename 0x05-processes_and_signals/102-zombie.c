#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - a function that runs forever
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - the entry to a program that creats 5 zombie process
 * Return: 0
*/
int main(void)
{
	pid_t pid;
	int processes_count = 0;

	while (processes_count < 5)
	{
		pid = fork();

		if (!pid)
			break;

		printf("Zombie process created, PID: %i\n", (int)pid);
		processes_count++;
	}

	if (pid != 0)
		infinite_while();

	return (0);
}
