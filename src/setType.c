/*

FILENAME : setType.c

Responsible for handling log type setting
and user confirmation

*/

#include <stdio.h>
#include <stdbool.h>


/* +--- CONSTANTS---+ */
typedef enum {
    TAG_ANECDOTE,
    TAG_ECCLESIASTICAL,
    TAG_CODING
} Tags;

typedef enum {
    NO,
    YES
} ConfirmVals;

const char *tagNames[] = {
    "ANECDOTE",
    "ECCLESIASTICAL",
    "CODING"
};


/* +--- FUNCTION DECLARARION ---+ */
char *setType();
char confirmType(Tags inptIndx);


int main(void)
{
    *setType();
    return 0;
}

char *setType()
{
    int  inptIndx;      // input index
    int runflg = true;  // run flag
    char confrmFlg;     // confirmation flag

    while (runflg) {

        printf("Set tag:\n");
        printf("\t[0]\tfor %s (general slice-of-life)\n", tagNames[TAG_ANECDOTE]);
        printf("\t[1]\tfor %s\n", tagNames[TAG_ECCLESIASTICAL]);
        printf("\t[2]\tfor %s\n", tagNames[TAG_CODING]);
        printf("\tDo not include brackets in input. '0' only, not '[0]'.\n");
        printf("\tEnter here >>> ");
    
        scanf("%d", &inptIndx);

        
    
        confrmFlg = confirmType(inptIndx) ? 1 : 0;

    }

}

char confirmType(Tags inptIndx)
{
    ConfirmVals confrmFlg;

    printf("\tConfirm chosen tag type: %s?\n", tagNames[inptIndx]);
    printf("\t[0]\tfor CANCEL\t\t[1]\tfor CONFIRM\n");
    printf("\tEnter here >>> ");

    scanf("%d", &confrmFlg);

    if (confrmFlg == (int)NO)  { return 0; }
    if (confrmFlg == (int)YES) { return 1; }
    else return 1;
}