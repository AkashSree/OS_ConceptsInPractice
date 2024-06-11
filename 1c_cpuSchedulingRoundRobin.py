def main():
    # Initialize the variables
    sum_time = 0  # Total time
    count = 0
    wt = 0  # Waiting time
    tat = 0  # Turn around time

    # Input the total number of processes
    NOP = int(input("Total number of processes in the system: "))
    y = NOP  # Assign the number of processes to variable y

    # Initialize arrays for arrival time, burst time, and temporary burst time
    at = [0] * NOP
    bt = [0] * NOP
    temp = [0] * NOP

    # Use a loop to enter the details of the processes
    for i in range(NOP):
        at[i] = int(input(f"\nEnter the Arrival time of Process[{i + 1}]: "))
        bt[i] = int(input(f"Enter the Burst time of Process[{i + 1}]: "))
        temp[i] = bt[i]  # Store the burst time in temp array

    # Accept the time quantum
    quant = int(input("Enter the Time Quantum for the process: "))

    # Display the process No, burst time, Turn Around Time, and waiting time
    print("\nProcess No\tBurst Time\tTAT\t\tWaiting Time")

    i = 0  # Initialize the index for processes
    while y != 0:
        if temp[i] <= quant and temp[i] > 0:  # If remaining burst time is less than or equal to quantum
            sum_time += temp[i]
            temp[i] = 0
            count = 1
        elif temp[i] > 0:  # If burst time is greater than quantum
            temp[i] -= quant
            sum_time += quant
        
        if temp[i] == 0 and count == 1:
            y -= 1  # Decrement the process count
            tat += sum_time - at[i]  # Calculate turn around time
            wt += sum_time - at[i] - bt[i]  # Calculate waiting time
            print(f"Process No[{i + 1}]\t{bt[i]}\t\t{sum_time - at[i]}\t\t{sum_time - at[i] - bt[i]}")
            count = 0
        
        # Move to the next process
        found = False
        for j in range(1, NOP + 1):
            if at[(i + j) % NOP] <= sum_time and temp[(i + j) % NOP] > 0:
                i = (i + j) % NOP
                found = True
                break
        if not found:
            sum_time += 1  # If no process has arrived yet, increment the total time

    # Calculate and print average waiting time and turn around time
    avg_wt = wt / NOP
    avg_tat = tat / NOP
    print(f"\nAverage Turn Around Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
