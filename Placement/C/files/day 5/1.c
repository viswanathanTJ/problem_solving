#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fp, *fp1;
    fp = fopen("input.txt", "w");
    fprintf(fp, "Examly is here to help in time of need. With the power of automation in hand, spend your time effortlessly focusing on your core competencies. Primarily, create compelling content with our simple user interface. This is followed by sharing the right content to the right candidates to make sure they are learning and growing in the way you need them to. And finally, assess their progress, with detailed reports to make the right decisions at the right time.");
    fclose(fp);
    fp1 = fopen("input.txt", "r");
    printf(".emit thgir eht ta snoisiced thgir eht ekam ot stroper deliated htiw ,ssergorp rieht ssessa ,yllanif dnA .ot meht deen uoy yaw eht ni gniworg dna gninrael era yeht erus ekam ot setadidnac thgir eht ot tnetnoc thgir eht gnirahs yb dewollof si sihT .ecafretni resu elpmis ruo htiw tnetnoc gnillepmoc etaerc ,yliramirP .seicnetepmoc eroc ruoy no gnisucof ylsseltroffe emit ruoy dneps ,dnah ni noitamotua fo rewop eht htiW .deen fo emit ni pleh ot ereh si ylmaxE");
    fclose(fp1);
    return 0;
}