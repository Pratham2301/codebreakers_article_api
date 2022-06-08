#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
    int pid;
    pid = fork();
    if (pid == 0)
    {
        printf("Process ID of child is %d\n", getpid());
    }
    else
    {
        printf("Process ID of Parent is %d\n", getppid());
    }
    return 0;
}