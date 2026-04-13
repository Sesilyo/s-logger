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


// +--- CONSTANTS ---+ //
#define MAX_MESSAGE_LENGTH 256
#define LOG_FILE "../logs/logs.txt"



// +--- STRUCTURES BLOCK ---+ //
typedef struct LogEntry {
    char timestamp[32];
    char *message
} LogEntry;


// +--- MAIN ---+ //
int main(void)
{
    // SETH WAS HERE
    printf("Hello, World!\n");

    char *s = getDateTime();
    printf("%s\n", s);
    free(s);

    instantiateLog();

    return 0;
}





char *finalStringLine()
{

}