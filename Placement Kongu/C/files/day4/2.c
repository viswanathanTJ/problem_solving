#include <stdio.h>
struct TIME
{
    int seconds;
    int minutes;
    int hours;
};
void differenceBetweenTimePeriod(struct TIME t1, struct TIME t2, struct TIME *diff);

int main()
{
    struct TIME s1, s2, diff;
    scanf("%d %d %d", &s1.hours, &s1.minutes, &s1.seconds);
    scanf("%d %d %d", &s2.hours, &s2.minutes, &s2.seconds);
    differenceBetweenTimePeriod(s1, s2, &diff);
    printf("%d:%d:%d", diff.hours, diff.minutes, diff.seconds);
    return 0;
}

void differenceBetweenTimePeriod(struct TIME start, struct TIME stop, struct TIME *diff)
{
    while (stop.seconds > start.seconds)
    {
        --start.minutes;
        start.seconds += 60;
    }
    diff->seconds = start.seconds - stop.seconds;
    while (stop.minutes > start.minutes)
    {
        --start.hours;
        start.minutes += 60;
    }
    diff->minutes = start.minutes - stop.minutes;
    diff->hours = start.hours - stop.hours;
}