def recursive_solution(number: int):
    """
    Solução mais comum para a série de fibonnaci.
    Usa de recursão para calcular os elementos anteriores e os soma.

    Mais simples, porém tem maior complexidade O(2^n)
    """
    if number <= 1:
        return number

    return recursive_solution(number - 1) + recursive_solution(number - 2)


def optimal_solution(number: int):
    """
    Solução um pouco mais refinada para a série de fibonnaci.
    Itera uma vez passando pelos elementos da lista, e calcula o novo valor com
    base nos dois últimos valores calculados.

    Mais complexa, porém menor complexidade O(n)
    """

    values = [0, 1]

    for i in range(2, number + 1):
        value = values[i - 2] + values[i - 1]
        values.append(value)

    return values[number]


if __name__ == "__main__":
    number = int(input("Insira um número: "))

    print("")
    print(f"Calculando Fibonnaci p/ número {number}:")

    print("Método Recursivo:", recursive_solution(number))
    print("Método Ótimo:", optimal_solution(number))
