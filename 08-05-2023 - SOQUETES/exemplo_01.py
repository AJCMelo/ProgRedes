import socket
# importar soquete

host = input('\nInforme o nome do HOST ou URL do site: ')
# hospedar = entrada('\nInforme o nome do HOST ou URL do site: ')

ip_host = socket.gethostbyname(host)
# ip_host = soquete.gethostbyname(hospedar)

print(f'\nO IP é {ip_host}')
# imprimir(f'\nO IP é{ip_host}')
