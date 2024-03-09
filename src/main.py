import csv
import sqlite3

# Connect to the SQLite in-memory database
conn = sqlite3.connect(':memory:')

# A cursor object to execute SQL commands
cursor = conn.cursor()


def main():

    # users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        userId INTEGER PRIMARY KEY,
                        firstName TEXT,
                        lastName TEXT
                      )'''
                   )

    # callLogs table (with FK to users table)
    cursor.execute('''CREATE TABLE IF NOT EXISTS callLogs (
        callId INTEGER PRIMARY KEY,
        phoneNumber TEXT,
        startTime INTEGER,
        endTime INTEGER,
        direction TEXT,
        userId INTEGER,
        FOREIGN KEY (userId) REFERENCES users(id)
    )''')

    # You will implement these methods below. They just print TO-DO messages for now.
    load_and_clean_users()
    load_and_clean_call_logs()
    write_user_analytics()
    write_ordered_calls()

    # Helper method that prints the contents of the users and callLogs tables
    select_from_users_and_call_logs()

    # Close the cursor and connection. main function ends here.
    cursor.close()
    conn.close()


# TODO: Implement the following functions. The functions must pass the unit tests to complete the project.


# This function will load the users.csv file into the users table, discarding any records with incomplete data
def load_and_clean_users():
    print("TODO: load_users")

    # print out the contents of users.csv from the resources directory
    file_path = '../resources/users.csv'

    # Open the file and read its contents
    with open(file_path, 'r') as file:

        # Skip the first line
        next(file)

        # Read the contents of the file line by line
        for line in file:

            # Split the line into individual fields
            fields = line.strip().split(',')

            # Assure that there are only 2 fields in the record
            if len(fields) == 2:

                # If any of the fields are empty, skip the record
                if fields[0] == '' or fields[1] == '':
                    continue

                # Insert the fields into the users table
                cursor.execute('''INSERT INTO users (firstName, lastName)
                                  VALUES (?, ?)''', fields)


# This function will load the callLogs.csv file into the callLogs table, discarding any records with incomplete data
def load_and_clean_call_logs():

    print("TODO: load_call_logs")

    # print out the contents of callLogs.csv from the resources directory
    file_path = '../resources/callLogs.csv'

    # Open the file and read its contents
    with open(file_path, 'r') as file:

        # Skip the first line
        next(file)

        # Read the contents of the file line by line
        for line in file:
            # Split the line into individual fields
            fields = line.strip().split(',')

            # Assure that there are only 5 fields in the record
            if len(fields) == 5:

                # If any of the fields are empty, skip the record
                if fields[0] == '' or fields[1] == '' or fields[2] == '' or fields[3] == '' or fields[4] == '':
                    continue

                # Insert the fields into the callLogs table
                cursor.execute('''INSERT INTO callLogs (phoneNumber, startTime, endTime, direction, userId)
                                  VALUES (?, ?, ?, ?, ?)''', fields)


# This function will write analytics data to userAnalytics.csv - average call time, and number of calls per user.
# You must save records consisting of each userId, avgDuration, and numCalls
def write_user_analytics():
    print("TODO: write_user_analytics")

    # Get all callLogs from the callLogs table
    cursor.execute('''SELECT * FROM callLogs''')
    call_logs = cursor.fetchall()

    # Create dictionaries to store total call duration and number of calls for each user ID
    total_duration = {}
    num_calls = {}

    # Calculate total call duration and number of calls for each user ID
    for log in call_logs:
        user_id = log[5]  # Assuming the user ID is at index 4
        duration = log[3] - log[2]  # Assuming index 2 and 3 represent start and end times
        if user_id not in total_duration:
            total_duration[user_id] = 0
            num_calls[user_id] = 0
        total_duration[user_id] += duration
        num_calls[user_id] += 1

    # Calculate average call duration for each user ID
    average_times = []
    for user_id in total_duration:
        average_duration = total_duration[user_id] / num_calls[user_id]
        average_times.append((user_id, average_duration, num_calls[user_id]))

    # Define the file path
    csv_file_path = '../resources/userAnalytics.csv'

    # Write the results to a CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['userId', 'avgDuration', 'numCalls']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user_id, avg_duration, num_calls in average_times:
            writer.writerow({'userId': user_id, 'avgDuration': avg_duration, 'numCalls': num_calls})


# This function will write the callLogs ordered by userId, then start time.
# Then, write the ordered callLogs to orderedCalls.csv
def write_ordered_calls():

    print("TODO: write_ordered_calls")

    # Get all callLogs from the callLogs table, ordered by userId, then start time
    cursor.execute('''SELECT * FROM callLogs ORDER BY userId, startTime''')
    call_logs = cursor.fetchall()

    # Define the file path
    csv_file_path = '../resources/orderedCalls.csv'

    # Write the results to a CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['callId', 'phoneNumber', 'startTime', 'endTime', 'direction', 'userId']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for log in call_logs:
            writer.writerow({'callId': log[0], 'phoneNumber': log[1], 'startTime': log[2],
                             'endTime': log[3], 'direction': log[4], 'userId': log[5]})


# This function is for debugs/validation - uncomment the function invocation in main() to see the data in the database.
def select_from_users_and_call_logs():

    print()
    print("PRINTING DATA FROM USERS")
    print("-------------------------")

    # Select and print users data
    cursor.execute('''SELECT * FROM users''')
    for row in cursor:
        print(row)

    # new line
    print()
    print("PRINTING DATA FROM CALLLOGS")
    print("-------------------------")

    # Select and print callLogs data
    cursor.execute('''SELECT * FROM callLogs''')
    for row in cursor:
        print(row)


if __name__ == '__main__':
    main()
