string a_input = Console.ReadLine();
string b_input = Console.ReadLine();
int a = int.Parse(a_input);
int b = int.Parse(b_input);

if (a > 0) {
    if (b > 0) {
        Console.WriteLine(1);
    }
    else {
        Console.WriteLine(4);
    }
}
else {
    if (b > 0) {
        Console.WriteLine(2);
    }
    else {
    Console.WriteLine(3);
    }
}