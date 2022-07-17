// Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, 
// какое число большее, а какое меньшее.
// a = 5; b = 7 -> max = 7
// a = 2 b = 10 -> max = 10
// a = -9 b = -3 -> max = -3

Console.WriteLine("Пожалуйста введите 2 числа,");
    Console.WriteLine("чтобы узнать какое большее, а какое меньшее.");
    Console.Write("Введите первое число: ");
    int a = int.Parse(Console.ReadLine());
    Console.Write("Введите второе число: ");
    int b = int.Parse(Console.ReadLine());
    if (a > b)
    {
        Console.WriteLine("Число " + a + " большее");
        Console.Write("Число " + b + " меньшее");
    }
    else if (a == b)
    {
        Console.WriteLine("Число " + a + " равно числу " + b);
    }
    else
    {
        Console.WriteLine("Число " + b + " большее");
        Console.Write("Число " + a + " меньшее");
    }



// Задача 4. Напишите программу, которая принимает на вход три числа 
// и выдаёт максимальное из этих чисел.
// 2, 3, 7 -> 7
// 44 5 78 -> 78
// 22 3 9 -> 22

Console.WriteLine("Введите три числа, и узнайте, ");
    Console.WriteLine("какое из них имеет максимальное значение.");
    Console.Write("Введите первое число и нажмите ENTER: ");
    int num1 = int.Parse(Console.ReadLine());
    Console.Write("Введите второе число и нажмите ENTER: ");
    int num2 = int.Parse(Console.ReadLine());
    Console.Write("Введите третье число и нажмите ENTER: ");
    int num3 = int.Parse(Console.ReadLine());
    int maxNum = 0;
    if (num1 > maxNum) maxNum = num1;
    if (num2 > maxNum) maxNum = num2;
    if (num3 > maxNum) maxNum = num3;
    Console.Write("Максимальное значение имеет число " + maxNum);




// Задача 6: Напишите программу, которая на вход принимает число и выдаёт, 
// является ли число чётным (делится ли оно на два без остатка).
// 4 -> да
// -3 -> нет
// 7 -> нет

Console.Write("Введите число и получите результат: ");
    int number = int.Parse(Console.ReadLine());
    int remain = number % 2;
    if (remain == 0)
    {
        Console.WriteLine("Число " + number + " четное?");
        Console.WriteLine("ДА!");
    }
    else
    {
        Console.WriteLine("Число " + number + " четное?");
        Console.WriteLine("НЕТ!");
    }




// Задача 8: Напишите программу, которая на вход принимает число (N), 
// а на выходе показывает все чётные числа от 1 до N.
// 5 -> 2, 4
// 8 -> 2, 4, 6, 8

Console.Write("Введите число: ");
    int num = int.Parse(Console.ReadLine());
    int even = 2;
    
    while (num >= even)
    {
        Console.Write(even + ", ");
        even = even + 2;
    }
