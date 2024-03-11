# Project: Python SQL API with File I/O

## Background 

There are two halves in a full-stack applications: the front end, responsible for user interaction and display, and the backend, handling data storage and processing.

In this project, we'll work on the backend, crafting an application to manage data in a hypothetical call center. Our application will handle user accounts and calls, providing analytics and data ordering functionality.


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
- You will be responsible for inserting and selecting data from the built-in SQLite database. 

### CSV

- The callLogs.csv and users.csv files will be included in the resources folder for loading into the DB tables.
- You will be responsible for loading the data from these existing files into the database, as well as writing data to new files.

# User Stories

(to be organized/fleshed out into actual subsections)

- LOAD csv data into DB tables, cleaning up any junk data (just delete it? or edit it).
- SAVE analytic data for users into csv files. userAnalytics.csv
- SAVE call logs into csv files, ordered by (name?... userId?), then start time, excluding any junk data. orderedCallLogs.csv



