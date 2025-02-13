while True:
    try:
        # Solicita a entrada dos números
        numero_1 = input('Digite um número: ')
        numero_2 = input('Digite outro número: ')

        # Transforma de str para float
        num1_float = float(numero_1)
        num2_float = float(numero_2)

        # Apresenta os operadores possíveis
        print('Escolha seu operador (+, -, *, /)')

        # Recebe o operador do usuário
        operador = input('Digite seu operador: ')

        # Condicionais para calcular o resultado
        if operador == '+':
            print('O resultado é:', num1_float + num2_float)
        elif operador == '-':
            print('O resultado é:', num1_float - num2_float)
        elif operador == '*':
            print('O resultado é:', num1_float * num2_float)
        elif operador == '/':
            if num2_float != 0:
                print('O resultado é:', num1_float / num2_float)
            else:
                print('Não é possível dividir por zero')
        else:
            print('Operador indisponível')

    except ValueError:
        print('Digite um número válido')
        continue

    # Repetir a operação
    repetir = input('Deseja repetir a operação? (sim/não): ').strip().lower()
    if repetir != 'sim':
        print('Encerrada a operação. Obrigado por usar!')
        break
