def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError ):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n1


def leiaFloat(msg):
    while True:
        try:
            n1 = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n1