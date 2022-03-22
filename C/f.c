#include<stdio.h>

int main() {
    FILE *fp = fopen("myfile.bin", "wb");

    fclose(fp);
}