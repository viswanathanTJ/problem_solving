#include <stdio.h>
#include <stdlib.h>

struct threeNum
{
    int n1, n2, n3;
};

int main()
{
    int n;
    struct threeNum num;
    FILE *fptr;

    if ((fptr = fopen("newFile.bin", "wb")) == NULL)
    {
        printf("Error! opening file");
        exit(1);
    }
    n = 5;
    fwrite(&n, sizeof(n), 1, fptr);
    for (n = 1; n < 5; ++n)
    {
        num.n1 = n;
        num.n2 = 5 * n;
        num.n3 = 5 * n + 1;
        fwrite(&num, sizeof(struct threeNum), 1, fptr);
    }
    fclose(fptr);
    if ((fptr = fopen("newFile.bin", "rb")) == NULL)
    {
        printf("Error! opening file");
        exit(1);
    }
    // fread(&n, sizeof(int), 1, fptr);
    // printf("n=%d\n", n);/
    fseek(fptr, sizeof(int), SEEK_SET);
    for (n = 1; n < 5; ++n)
    {
        fread(&num, sizeof(struct threeNum), 1, fptr);
        printf("n1: %d\tn2: %d\tn3: %d\n", num.n1, num.n2, num.n3);
    }
    fclose(fptr);
    return 0;
}