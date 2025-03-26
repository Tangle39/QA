#!/bin/bash

# Set the output file name
FILE_NAME=${FILE_NAME:-result.txt}

# Write the current user and folder to the output file
{
    echo "Current user is $(whoami), current folder is $(pwd)"

    # Calculate the total size of Shell_Question directory
    if [ -d "Shell_Question" ]; then
        SIZE=$(du -sh Shell_Question | awk '{print $1}')
        echo "The total size of Shell_Question is $SIZE"
    else
        echo "The Shell_Question directory does not exist."
    fi

    # Query all the lines of 404 in access.log
    if [ -f "access.log" ]; then
        COUNT=$(grep -c "404" access.log)
        echo "The lines of code 404 are $COUNT"

        IP_LIST=$(grep "404" access.log | awk '{print $1}' | sort -u)
        echo "The IP list of code 404 are:"
        echo "$IP_LIST"

        # Check if 10.110.120.110 is in the IP list
        if echo "$IP_LIST" | grep -q "10.110.120.110"; then
            echo "10.110.120.110 is in the ip list"
        else
            echo "10.110.120.110 is not in the ip list"
        fi
    else
        echo "The access.log file does not exist."
    fi
} > "$FILE_NAME"

echo "Debug summary saved to $FILE_NAME"
