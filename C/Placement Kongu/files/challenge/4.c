target = fopen("source_file.txt", "r");
char c;
while ((c = fgetc(target)) != EOF)
    printf("%c", c);
