class Process:
    def __init__(self, at, bt, pt):
        self.AT = at  # Arrival Time
        self.BT = bt  # Burst Time
        self.PT = pt  # Priority
        self.WT = 0   # Waiting Time
        self.TAT = 0  # Turn Around Time

def main():
    processes = []
    
    # Input number of processes
    n = int(input("Enter the number of processes: "))
    
    # Input arrival time, burst time, and priority for each process
    print("Enter the arrival time, burst time, and priority of the process")
    print("AT BT PT")
    for i in range(n):
        at, bt, pt = map(int, input().split())
        processes.append(Process(at, bt, pt))
    
    temp_bt = [proc.BT for proc in processes]  # Copy burst times for future use
    
    total_wt = 0
    total_tat = 0
    count = 0
    t = 0
    short_p = None
    
    # Initialize a large value for comparison purposes
    max_priority = 10000
    
    while count != n:
        short_p = None
        
        # Find the process with the highest priority that has arrived and has remaining burst time
        for i in range(n):
            if (short_p is None or processes[i].PT < processes[short_p].PT) and processes[i].AT <= t and processes[i].BT > 0:
                short_p = i
        
        if short_p is not None:
            processes[short_p].BT -= 1  # Reduce burst time by 1
            
            # If process is completed
            if processes[short_p].BT == 0:
                count += 1
                completion_time = t + 1
                processes[short_p].WT = completion_time - processes[short_p].AT - temp_bt[short_p]
                processes[short_p].TAT = completion_time - processes[short_p].AT
                
                total_wt += processes[short_p].WT
                total_tat += processes[short_p].TAT
        
        t += 1
    
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    
    # Print results
    print("ID WT TAT")
    for i in range(n):
        print(f"{i+1} {processes[i].WT} {processes[i].TAT}")
    
    print(f"Avg waiting time of the process is {avg_wt:.2f}")
    print(f"Avg turn around time of the process is {avg_tat:.2f}")

if __name__ == "__main__":
    main()
