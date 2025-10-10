using System;

class ProgramaMercado
{
    static void Main()
    {
        double total = 0;
        int qtdProdutos;

        Console.Write("Quantos produtos diferentes você vai comprar? ");
        qtdProdutos = int.Parse(Console.ReadLine());

        for (int i = 1; i <= qtdProdutos; i++)
        {
            Console.WriteLine($"\nProduto {i}:");

            Console.Write("Digite o nome do produto: ");
            string nome = Console.ReadLine();

            Console.Write("Digite o preço do produto: ");
            double preco = double.Parse(Console.ReadLine());

            Console.Write("Digite a quantidade comprada: ");
            int quantidade = int.Parse(Console.ReadLine());

            double subtotal = preco * quantidade; 
            total += subtotal;
            
            Console.WriteLine($"Subtotal de {nome}: R$ {subtotal:F2}");
        }

        Console.WriteLine($"\nTotal da compra: R$ {total:F2}");

        if (total > 100)
        {
            double desconto = total * 0.10;
            double totalComDesconto = total - desconto;
            Console.WriteLine($"Você ganhou 10% de desconto! Total final: R$
