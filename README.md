# Server-Analysis
This project reads, processes, and filters log files based on the status code. It is designed to extract relevant log entries, specifically those with a status code of 200 (OK), and write the processed data into a new file for further analysis
The program ensures that users input a valid log file and performs the following steps:

Read Log File: Prompts the user to enter the name of the log file. If the file is not found, it asks for a valid file name until a correct file is provided.
Process Log Entries: Splits each log entry into components (date, time, IP address, and status code) and filters only those with a status code of 200.
Write Processed Data to File: The filtered entries are written to a new file named processed_log.txt, including the date, timestamp, IP address, and status code.
How to Run:

Run the Python script in a terminal or command line.
Enter the log file name when prompted.
The processed entries with a status code of 200 will be written to processed_log.txt.
