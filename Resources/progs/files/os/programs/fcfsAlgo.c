#include <stdio.h>

int main() {
    int pid[15];
    int bt[15];
    int n;

    printf("Enter the number of processes: ");
    scanf("%d", &n);

    printf("Enter process ID of all the processes:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &pid[i]);
    }

    printf("Enter burst time of all the processes:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &bt[i]);
    }

    int wt[n];
    wt[0] = 0;

    for (int i = 1; i < n; i++) {
        wt[i] = bt[i - 1] + wt[i - 1];
    }

    printf("\nProcess ID\tBurst Time\tWaiting Time\tTurnaround Time\n");
    float total_wt = 0.0;
    float total_tat = 0.0;

    for (int i = 0; i < n; i++) {
        printf("%d\t\t%d\t\t%d\t\t\t%d\n", pid[i], bt[i], wt[i], bt[i] + wt[i]);

        total_wt += wt[i];
        total_tat += (wt[i] + bt[i]);
    }

    float avg_wt = total_wt / n;
    float avg_tat = total_tat / n;

    printf("\nAvg. waiting time = %f\n", avg_wt);
    printf("Avg. turnaround time = %f\n", avg_tat);

    return 0;
}