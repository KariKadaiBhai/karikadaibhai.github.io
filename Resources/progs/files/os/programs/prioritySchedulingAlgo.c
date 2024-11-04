#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int n;
    printf("Enter Number of Processes: ");
    scanf("%d", &n);
    
    int b[n], p[n], index[n];
    
    for (int i = 0; i < n; i++) {
        printf("Enter Burst Time and Priority Value for Process %d: ", i + 1);
        scanf("%d %d", &b[i], &p[i]);
        index[i] = i + 1;
    }
    
    for (int i = 0; i < n; i++) {
        int highest_priority = p[i], pos = i;
        for (int j = i; j < n; j++) {
            if (p[j] > highest_priority) {
                highest_priority = p[j];
                pos = j;
            }
        }
        swap(&p[i], &p[pos]);
        swap(&b[i], &b[pos]);
        swap(&index[i], &index[pos]);
    }
    
    int t = 0;
    printf("\nOrder of process execution is:\n");
    for (int i = 0; i < n; i++) {
        printf("P%d is executed from %d to %d\n", index[i], t, t + b[i]);
        t += b[i];
    }
    
    printf("\n");
    printf("Process ID\tBurst Time\tWait Time\tTurnAround Time\n");
    
    int wait_time = 0;
    for (int i = 0; i < n; i++) {
        printf("P%d\t\t%d\t\t%d\t\t%d\n", index[i], b[i], wait_time, wait_time + b[i]);
        wait_time += b[i];
    }
    
    return 0;
}