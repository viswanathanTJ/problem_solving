#include <stdio.h>
#define MAX_FILE_NAME 100

int main()
{
    FILE *fp;
    int count = 0, n = 0; // Line counter (result)
    char c;               // To store a character read from file
    char ch[100];
    scanf("%d", &n);

    // Open the file
    fp = fopen("input.txt", "w");
    fputs(" The Paleocene is a geological epoch that started \n66 million years ago with the Cretaceous–Paleogene \nextinction of non-avian dinosaurs and 75 percent of all species.\n The Paleocene was marked by the recovery of the biosphere, with dense forests worldwide, while small mammals and birds rapidly evolved to take advantage of the mass extinction. In the seas, ray-finned fish rose to dominance.\n The supercontinents Laurasia and Gondwana were still separating, the Rocky", fp);

    fclose(fp);
    fp = fopen("input.txt", "r");
    for (int i = 0; i < n; i++)
    {
        fgets(ch, 100, fp);
        printf("%s", ch);
    }
    fclose(fp);
}