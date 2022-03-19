#include <stdio.h>
struct TIME
{
    int seconds;
    int minutes;
    int hours;
};
void differenceBetweenTimePeriod(struct TIME t1, struct TIME t2, struct TIME *diff);