def main():
    # Initialize variables
    RQ = []
    TotalHeadMovement = 0

    # Get the number of requests
    n = int(input("Enter the number of Requests: "))

    # Get the request sequence
    print("Enter the Requests sequence:")
    for _ in range(n):
        RQ.append(int(input()))

    # Get the initial head position
    initial = int(input("Enter initial head position: "))

    # Logic for FCFS disk scheduling
    for i in range(n):
        TotalHeadMovement += abs(RQ[i] - initial)
        initial = RQ[i]

    print(f"Total head movement is {TotalHeadMovement}")

if __name__ == "__main__":
    main()
