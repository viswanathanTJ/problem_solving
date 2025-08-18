#include<stdio.h>

struct stu {
    char name[50], gender[50];
    float cut;
};

int main() {
    int n,i,t;
    scanf("%d", &n);
    struct stu s[n];
    for (i = 0; i < n;i++) {
        scanf("%s %s %f", s[i].name, s[i].gender, &s[i].cut);
        t = s[i].cut;
        if(t>=195)
            printf(" Course alloted for %s is ECE", s[i].name);
        else if(t>=190 && t < 195)
            printf(" Course alloted for %s is MECH", s[i].name);
        else if(t>=185 && t < 190)
            printf(" Course alloted for %s is EEE", s[i].name);
        else if(t>=180 && t <= 184)
            printf(" Course alloted for %s is CIVIL", s[i].name);
        else
            printf(" Course alloted for %s is CSE and IT", s[i].name);
        printf("\n");
    }

}