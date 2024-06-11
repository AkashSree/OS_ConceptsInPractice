# Function to sort processes by burst time
def sort_processes(processes):
    return sorted(processes, key=lambda x: x[1])

# Function to calculate average waiting and turnaround time
def calculate_avg_times(processes, n):
    total_wt = 0
    total_tat = 0
    wt = [0] * n  # waiting time
    tat = [0] * n  # turnaround time
    
    # Calculate waiting time for each process
    for i in range(1, n):
        wt[i] = wt[i - 1] + processes[i - 1][1]
        total_wt += wt[i]
    
    # Calculate turnaround time for each process
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]
        total_tat += tat[i]
    
    avg_wt = total_wt / n
    avg_tat = total_tat / n

    # Print the process details
    print("PId  Burst Time  Waiting Time  Turnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}    {processes[i][1]}          {wt[i]}             {tat[i]}")
    
    print(f"Average Waiting Time = {avg_wt:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")

def main():
    # Input number of processes
    n = int(input("Enter number of processes: "))
    
    # Input burst time for each process
    processes = []
    for i in range(n):
        bt = int(input(f"P{i + 1} Burst Time: "))
        processes.append((i + 1, bt))
    
    # Sort processes by burst time
    processes = sort_processes(processes)
    
    # Calculate and print average times
    calculate_avg_times(processes, n)

if __name__ == "__main__":
    main()
