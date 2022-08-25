// Задача 66 Задайте значения M и N.
// Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N

Console.Clear();
Console.WriteLine($"Задача 66.");
Console.WriteLine("Программа выводит сумму натуральных чисел между Стартовым и Конечным числом");
Console.WriteLine("Введите Стартовое число: ");
int numberM = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите Конечное число: ");
int numberN = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(SumEvenNumberFromMtoN(numberM, numberN));

int SumEvenNumberFromMtoN(int numberM, int numberN)
{
    if (numberM == numberN)
    {
        return numberM;
    }
    else if (numberM > numberN)
    {
        return numberM + SumEvenNumberFromMtoN(numberM - 1, numberN);
    }
    else
    {
        return numberM + SumEvenNumberFromMtoN(numberM + 1, numberN);
    }
}


// Задача 68. Напишите программу вычисления функции Аккермана с помощью рекурсии.
// Даны два неотрицательных числа m и n.

Console.Clear();
Console.WriteLine($"Задача 68.");
Console.WriteLine("Программа выводит функцию Аккермана");
Console.WriteLine("Введите число M: ");
int numberM = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число N: ");
int numberN = Convert.ToInt32(Console.ReadLine());

Console.WriteLine(AkkermanFunction(numberM, numberN));

int AkkermanFunction(int m, int n)
{
    if (m == 0)
    {
        return n + 1;
    }
    else if (m > 0 & n == 0)
    {
        return AkkermanFunction(m-1, 1);
    }
    else if (m > 0 & n > 0)
     {
        return AkkermanFunction(m-1, AkkermanFunction(m, n-1));
    }

    return 0;
}