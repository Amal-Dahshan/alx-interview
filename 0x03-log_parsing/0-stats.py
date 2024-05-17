import sys

# Read input line by line
for line in sys.stdin:
    # Process each line
    print(line.strip())
    # Initialize variables
    total_size = 0
    status_counts = {}

    try:
        # Read input line by line
        for line_number, line in enumerate(sys.stdin, start=1):
            # Skip lines that don't match the expected format
            if not line.startswith('<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'):
                continue

            # Extract status code and file size from the line
            parts = line.split()
            status_code = parts[4]
            file_size = int(parts[5])

            # Update total file size
            total_size += file_size

            # Update status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            # Print statistics every 10 lines
            if line_number % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_counts):
                    print(f"{code}: {status_counts[code]}")

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print(f"Total file size: {total_size}")
        for code in sorted(status_counts):
            print(f"{code}: {status_counts[code]}")
    