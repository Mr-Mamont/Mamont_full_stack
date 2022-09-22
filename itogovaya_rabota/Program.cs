string[] Array1 = new string[6] {"123", "23", "hello", "world", "rus", "=+12(0"};
string[] Array2 = new string[Array1.Length];
void SecondArrayWithIF(string[] Array1, string[] Array2)
{
    int count = 0;
    for (int i = 0; i < Array1.Length; i++)
    {
    if(Array1[i].Length <= 3)
        {
        Array2[count] = Array1[i];
        count++;
        }
    }
}
void PrintArray(string[] Array)
{
    for (int i = 0; i < Array.Length; i++)
    {
        Console.Write($"{Array[i]} ");
    }
    Console.WriteLine();
}
SecondArrayWithIF(Array1, Array2);
PrintArray(Array2);
