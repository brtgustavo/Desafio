while True:
    num = int(input("Digite um número ou 0 para sair: "))
    
    if num == 0:
        break
    
    fib1, fib2 = 0, 1
    
    while fib2 <= num:
        if fib2 == num:
            print(num, "pertence à sequência de Fibonacci.")
            break
        fib1, fib2 = fib2, fib1 + fib2
    else:
        print(num, "não pertence à sequência de Fibonacci.")
