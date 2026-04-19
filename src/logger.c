/*
    FILENAME: logger.c

    This is where the log input is received
    and parsed together with the current time
    to build the final string line to put
    in logs.txt
*/

#include <stdio.h>
#include <stdlib.h>


// +--- FUNCTION DECLARATION BLOCKS ---+ //


// +--- MACROS ---+ //
#ifndef GETTIME_H
#define GETTIME_H

char *getDateTime();

#endif

#define MAX_MESSAGE_LENGTH 256
#define LOG_FILE "../logs/logs.txt"



// +--- STRUCTURES BLOCK ---+ //
typedef struct LogEntry {
    char *logLine;
} LogEntry;


char *finalStringLine()
{

}