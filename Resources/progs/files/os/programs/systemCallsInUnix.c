#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int pid;
    char s[100];

    pid = fork();
    if (pid < 0) {
        perror("Fork error");
    } else if (pid > 0) {
        wait(NULL);
        printf("\nParent Process:\n");
        printf("\n\tParent Process ID: %d\n", getpid());
        execlp("cat", "cat", argv[1], (char *)0);
        perror("Can't execute cat");
    } else {
        printf("\nChild Process:");
        printf("\n\tChild Process Parent ID: %d", getppid());
        sprintf(s, "\n\tChild Process ID: %d", getpid());
        write(1, s, strlen(s));
        printf("\n");
        execvp(argv[2], &argv[2]);
        perror("Can't execute command");
    }

    return 0;
}
