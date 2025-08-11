#include<stdio.h>

int main() {
    char a[100], b[100];
    scanf("%s %s", a, b);
    printf("%s %s\n", a, b);
    int c[26] = {0};
    for(int i = 0; a[i] != '\0'; i++)
        c[a[i] - 'a']++;
    for(int i=0; b[i] != '\0'; i++)
        c[b[i]-'a']--;
    int count = 0;
    for(int i=0;i<26;i++)
        if(c[i])
            count += c[i] > 0 ? c[i] : -c[i];
    printf("Count is %d\n", count);
    char flames[] = "FLAMES";
    int l=1,k,fc=5;
    for (int i = 0;; i++)
    {
        if (l == count)
        {
            printf("i=%d", i);
            for (k = i; flames[k] != '\0'; k++) {
                if(flames[k+1])
                    printf(" %c=%c;", flames[k], flames[k+1]);
                flames[k] = flames[k + 1];
            }
            printf("\n");
            flames[k + 1] = '\0';
            fc = fc - 1;
            i = i - 1;
            l = 0;
        }
        if (i == fc)
            i = -1;
        if (fc == 0)
            break;
        l++;
    }
    printf("%c", flames[0]);
}