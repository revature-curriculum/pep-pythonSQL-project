# Project: Python SQL API with File I/O

## Background 

There are two halves in a full-stack application: the front end, responsible for user interaction and display, and the backend, which handles data storage and processing. In this project, we'll work on the backend, creating an application to manage data in a hypothetical call center. Our application will handle user accounts and calls, and provide analytics and data ordering functionality.

The primary technologies you will leverage in this project are Python, SQL, and File I/O with .csv files. The project will be written in Python. Data will be loaded into an in-memory SQLite database from existing .csv files, and analytic data will be saved into new .csv files. 

## Database Tables 

The following tables will be initialized in your project's built-in database upon startup.

### users
```
userId INTEGER PRIMARY KEY,
firstName TEXT
lastName TEXT
```

### callLogs
```
callId INTEGER PRIMARY KEY,
phoneNumber TEXT,
startTimeEpoch INTEGER,
endTimeEpoch INTEGER,
callDirection TEXT,
userId INTEGER,
FOREIGN KEY (userId) REFERENCES users(userId)
```

Note - by specifying IDs as primary keys, the id value should auto-increment for each new record.

# Technical Requirements

### SQLite

- The app will already be a Python project with SQLite tables created at runtime. 
- You will be responsible for cleaning and inserting data into the database, as well as selecting and modifying that data for analysis.  

### CSV

- The callLogs.csv and users.csv files will be included in the resources folder for loading into the DB tables.
- You will be responsible for loading the data from these existing files into the database, as well as writing analytic data to new files.

# User Stories

(in progress, needs detail)

### Load user data into users table
- read users.csv
- clean the data
- insert into DB

### Load call data into callLogs table
- read callLogs.csv
- clean the data
- insert into DB

### Save user analytic data into userAnalytics.csv
- save analytic data for users into csv files. The file must be named userAnalytics.csv
- {details about the following bullet}
- records must include userId, avgDuration, numCalls
- HINT:

### Save ordered call logs into orderedCallLogs.csv
- Save call logs into csv files, ordered by userId, then start time. The file must be named orderedCallLogs.csv
- HINT: order by



