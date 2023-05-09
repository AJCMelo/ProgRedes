import socket
#importar soquete

host = input('\nInforme o nome do HOST ou URL do site: ')
#hospedar = entrada('\nInforme o nome do HOST ou URL do site: ')

retorno = socket.gethostbyname_ex(host)
#retorno = soquete.gethostbyname_ex(hospedar)

print(retorno)
#imprimir(retorno)