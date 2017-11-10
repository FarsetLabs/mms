# Member Management System - Server
The Member Management System server is a Django based server which provides an API to manage members via REST calls.

## Requirements
The member management system is targetted for Python 3, and a variety of python dependencies as laid out in the requirements directory. The requirements directory consists of a number of files based on the environment. The base.txt file contains the minimum number of requirements required to run the server.

## Getting Started
A Makefile is provided for users in a POSIX environment to ease common tasks. To understand the underlying commands pllease read that file.

```
# Run the dev server
make devserver

# Create new migrations following model changes
make migrations

# Run any new migrations on the configured database
make migrate

# Execute the tests
make test
```
