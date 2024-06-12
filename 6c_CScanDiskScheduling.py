def c_scan_disk_scheduling():
    # Initialize variables
    RQ = []  # Request Queue
    TotalHeadMovement = 0

    # Get the number of requests
    n = int(input("Enter the number of Requests: "))

    # Get the request sequence
    print("Enter the Requests sequence:")
    for _ in range(n):
        RQ.append(int(input()))

    # Get the initial head position, size of the disk, and initial direction of head movement
    initial = int(input("Enter initial head position: "))
    size = int(input("Enter the size of the disk: "))
    move = int(input("Enter the head movement direction (1 for high, 0 for low): "))

    # Sort the request queue
    RQ.sort()

    # Find the index of the first request greater than the initial position
    index = next((i for i, req in enumerate(RQ) if req > initial), n)

    if move == 1:  # if movement is towards high value
        # Process requests to the right of the initial position
        for i in range(index, n):
            TotalHeadMovement += abs(RQ[i] - initial)
            initial = RQ[i]

        # Move the head to the end of the disk and then to the beginning
        if index < n:  # Check if there were any requests to the right
            TotalHeadMovement += abs(size - initial - 1)
            TotalHeadMovement += size - 1
            initial = 0

        # Process the remaining requests from the beginning of the disk
        for i in range(index):
            TotalHeadMovement += abs(RQ[i] - initial)
            initial = RQ[i]

    else:  # if movement is towards low value
        # Process requests to the left of the initial position
        for i in range(index - 1, -1, -1):
            TotalHeadMovement += abs(RQ[i] - initial)
            initial = RQ[i]

        # Move the head to the beginning of the disk and then to the end
        if index > 0:  # Check if there were any requests to the left
            TotalHeadMovement += abs(initial)
            TotalHeadMovement += size - 1
            initial = size - 1

        # Process the remaining requests from the end of the disk
        for i in range(n - 1, index - 1, -1):
            TotalHeadMovement += abs(RQ[i] - initial)
            initial = RQ[i]

    print(f"Total head movement is {TotalHeadMovement}")

if __name__ == "__main__":
    c_scan_disk_scheduling()
