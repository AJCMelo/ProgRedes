import socket, sys

host = input('\nInforme o nome do HOST ou URL do site: ')
port = 80 # Porta HTTP

server_conn = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
   sock.connect(server_conn)
except:
   print(f'\nErro.... {sys.exc_info()}')
else:
   print('\nConexão OK')
   sock.close()

#importar soquete,sistema
#hospedar = entrada('\nInforme o nome do HOST ou URL do site: ')
#porta = 80 # Porta HTTP
#server_conn =(hospedar,porta)
   #meia = soquete.soquete(soquete.AF_INET,soquete.SOCK_STREAM)
#tentar:
   #meia.conectar(server_conn)
#exceto:
   #imprimir(f'\nErro....{sistema.exc_info()}')
#outro:
   #imprimir('\nConexão OK')
   #meia.fechar()