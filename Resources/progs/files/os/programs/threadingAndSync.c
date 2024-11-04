#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdint.h>

void *myThreadFun(void *vargp) {
    int thread_id = (int)(intptr_t)vargp;
    printf("Thread %d is processing\n", thread_id);
    for (volatile long i = 0; i < 100000000; i++);
    printf("Thread %d is completed\n", thread_id);
    pthread_exit(NULL);
}

int main() {
    int i;
    pthread_t a[5];

    printf("Before Thread\n");
    for (i = 0; i < 5; i++) {
        if (pthread_create(&a[i], NULL, myThreadFun, (void *)(intptr_t)i) != 0) {
            printf("Thread not created\n");
        }
    }

    for (i = 0; i < 5; i++) {
        pthread_join(a[i], NULL);
    }

    printf("All threads completed.\n");
    return 0;
}