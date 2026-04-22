# EOF : END OF FILE
`fgetc` returns EOF when all the characters from a file have been read. So, we can write a check like below to detect end of file:

```c
while(1)
{
    ch = fgetc(ptr); // when all the content of a file has been read break the loop!
    if (ch == EOF)
    {
        break;
    }
    // code
}
```
