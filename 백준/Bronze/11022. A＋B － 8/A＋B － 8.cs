string n_input = Console.ReadLine();
int n = int.Parse(n_input);

for (int i=1; i<=n; i++) {
    string input = Console.ReadLine();
    string[] split = input.Split(' ');
    int a = int.Parse(split[0]);
    int b = int.Parse(split[1]);
    
    Console.WriteLine($"Case #{i}: {a} + {b} = {a+b}");
}