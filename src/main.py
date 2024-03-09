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

    # Helper method that prints the contents of the users and callLogs tables. Uncomment to see data.
    # select_from_users_and_call_logs()

    # Close the cursor and connection. main function ends here.
    cursor.close()
    conn.close()


# TODO: Implement the following functions. The functions must pass the unit tests to complete the project.


# This function will load the users.csv file into the users table, discarding any records with incomplete data
def load_and_clean_users():

    print("TODO: load_users")


# This function will load the callLogs.csv file into the callLogs table, discarding any records with incomplete data
def load_and_clean_call_logs():

    print("TODO: load_call_logs")


# This function will write analytics data to userAnalytics.csv - average call time, and number of calls per user.
# You must save records consisting of each userId, avgDuration, and numCalls
# example: 1,105.0,4 - where 1 is the userId, 105.0 is the avgDuration, and 4 is the numCalls.
def write_user_analytics():

    print("TODO: write_user_analytics")


# This function will write the callLogs ordered by userId, then start time.
# Then, write the ordered callLogs to orderedCalls.csv
def write_ordered_calls():

    print("TODO: write_ordered_calls")


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