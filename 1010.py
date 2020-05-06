a, b = input().split(), input().split()

nmPeca1 = int(a[1])
vlrPeca1 = float(a[2])

nmPeca2 = int(b[1])
vlrPeca2 = float(b[2])

vlrPagar = ((nmPeca1*vlrPeca1)+(nmPeca2*vlrPeca2))

print('VALOR A PAGAR: R$ %.2f'%vlrPagar)