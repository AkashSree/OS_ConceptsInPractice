# Function to find the waiting time for all processes
def find_waiting_time(processes, n, bt, wt):
    wt[0] = 0  # waiting time for first process is 0
    for i in range(1, n):  # calculating waiting time
        wt[i] = bt[i - 1] + wt[i - 1]

# Function to calculate turn around time
def find_turnaround_time(processes, n, bt, wt, tat):
    for i in range(n):  # calculating turnaround time by adding bt[i] + wt[i]
        tat[i] = bt[i] + wt[i]

# Function to calculate average time
def find_avg_time(processes, n, bt):
    wt = [0] * n  # waiting time
    tat = [0] * n  # turnaround time
    total_wt = 0  # total waiting time
    total_tat = 0  # total turnaround time

    find_waiting_time(processes, n, bt, wt)  # Function to find wt of all processes
    find_turnaround_time(processes, n, bt, wt, tat)  # Function to find tat for all processes

    # Display processes along with all details
    print("Processes    Burst time    Waiting time    Turn around time")

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"   {processes[i]}           {bt[i]}              {wt[i]}                {tat[i]}")

    avg_wt = total_wt / n
    avg_tat = total_tat / n
    print(f"Average waiting time = {avg_wt}")
    print(f"Average turn around time = {avg_tat}")

# Main function
if __name__ == "__main__":
    processes = [1, 2, 3]  # Process IDs
    n = len(processes)  # Number of processes
    burst_time = [12, 4, 7]  # Burst time of all processes

    find_avg_time(processes, n, burst_time)
