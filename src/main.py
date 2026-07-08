def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b

if __name__ == "__main__":
    print("EXECUTANDO APLICAÇÃO CONTEINERIZADA")
    print(f" - Teste de soma (2 + 3): {somar(2, 3)}")
    print(f" - Teste de multiplicação (2 * 3): {multiplicar(2, 3)}")
    print(f" - Teste de divisão (10 / 2): {dividir(10, 2)}")
    print("Pipeline executado com sucesso e contêiner ativo!")