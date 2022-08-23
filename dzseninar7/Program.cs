// Задача 47: Задайте двумерный массив размером m×n, заполненный 
// случайными вещественными числами.
// m = 3, n = 4.
// 0,5 7 -2 -0,2
// 1 -3,3 8 -9,9
// 8 7,8 -7,1 9

Console.WriteLine($"Задача 47:");

Console.Write("Введите m: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите n: ");
int n = Convert.ToInt32(Console.ReadLine());

Console.Clear();
Console.WriteLine($"m = {m}, n = {n}.");

double[,] array = new double[m, n];

CreateArrayDouble(array);

WriteArray(array);

Console.WriteLine();

void CreateArrayDouble(double[,] array)
{
  for (int i = 0; i < m; i++)
  {
    for (int j = 0; j < n; j++)
    {
      array[i, j] = new Random().NextDouble() * 20 - 10;
    }
  }
}

void WriteArray (double[,] array){
for (int i = 0; i < m; i++)
  {
      for (int j = 0; j < n; j++)
      {
        double alignNumber = Math.Round(array[i, j], 1);
        Console.Write(alignNumber + " ");
      }
      Console.WriteLine();
  }
}



// Задача 50: Напишите программу, которая на вход принимает позиции 
// элемента в двумерном массиве, и возвращает значение этого элемента 
// или же указание, что такого элемента нет.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 17 -> такого числа в массиве нет

Console.WriteLine($"Задача 50:");

Console.WriteLine ("Введите число строк: ");
int m = Convert.ToInt32 (Console.ReadLine());
Console.WriteLine ("Введите число стодбцов: ");
int n = Convert.ToInt32 (Console.ReadLine());
int[,] array = new int [m,n];
for (int i = 0; i < m; i++)
{
    for (int j = 0; j < n; j++)
    {
        array[i,j] = new Random().Next (-10, 10);
        Console.Write (array[i,j]+" ");
    }
    Console.WriteLine();
}

Console.WriteLine ("Введите строку элемента: ");
int row = Convert.ToInt32 (Console.ReadLine());
Console.WriteLine ("Введите столбец элемента: ");
int column = Convert.ToInt32 (Console.ReadLine());
if (row < m && column < n) Console.WriteLine ("Элемент массива с такими позициями существует: "+array[row,column]);
else Console.WriteLine ("Элемент массива с такими позициями не существует");



// Задача 52: Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4

// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3

Console.WriteLine ("Введите число строк: ");
int m = Convert.ToInt32 (Console.ReadLine());
Console.WriteLine ("Введите число столбцов: ");
int n = Convert.ToInt32 (Console.ReadLine());
int[,] massive = new int [m,n];
for (int i = 0; i < m; i++)
{
    for (int j = 0; j < n; j++)
    {
        massive[i,j] = new Random().Next (-10, 10);
        Console.Write (massive[i,j]+" ");
    }
    Console.WriteLine();
}

double result = 0;

for (int j = 0; j < n; j++)
{
    result = Average(j);
    Console.WriteLine(result);
}

double Average(int column)
{
    double average = 0;
    double x = 0;
    for (int i = 0; i < m; i++)
{
    average += massive[i, column];
}
x = average / m;
return x;
}