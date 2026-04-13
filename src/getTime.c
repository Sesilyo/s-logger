/*
    FILENAME : getTime.c

*/

#include <stdio.h>
#include <time.h>

#define BASE_YEAR 1900

char *getDateTime();


int main(void)
{

    return 0;
}

char *getDateTime()
{
    time_t t = time(NULL);

    // get local time structure
    struct tm date = *localtime(&t);

    // allocate memort for the string
    char *buffer = malloc(32 * sizeof(char));
    if (buffer == NULL) return NULL; // check if memory allocation failed

    sprintf(buffer, "%02d-%d-%02d",
                date.tm_mon + 1,
                date.tm_mday,
                date.tm_year + BASE_YEAR
            );

    return buffer;
}
