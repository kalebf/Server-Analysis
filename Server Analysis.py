def read_log_file():
    while True:
        file_name = input("Enter the name of the log file: ")
        try:
            with open(file_name, 'r') as file:
                log_entries = file.readlines()
                return log_entries
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")

def process_log_entries(log_entries):
    processed_entries = []

    for entry in log_entries:
        # Split the log entry into its components
        components = entry.split()

        # Extract relevant information from the log entry
        date = components[0]
        time = components[1]
        ip_address = components[2]
        status_code = int(components[3])

        # Process only entries with a status code of 200 (OK)
        if status_code == 200:
            processed_entries.append((date, time, ip_address, status_code))

    return processed_entries

def write_processed_data_to_file(processed_data):
    with open("processed_log.txt", "w") as output_file:
        for entry in processed_data:
            # Convert the tuple to a string and write it to the file
            output_file.write(' '.join(map(str, entry)) + ' OK\n')


if __name__ == "__main__":
    log_entries = read_log_file()
    processed_entries = process_log_entries(log_entries)
    processed_data = [('Date:',entry[0], 'Timestamp:', entry[1], 'IP Address:', entry[2], 'Status Code:', entry[3]) for entry in processed_entries]
    write_processed_data_to_file(processed_data)
    print("Processed data has been successfully written to 'processed_log.txt'.")

