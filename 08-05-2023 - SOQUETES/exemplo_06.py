import socket, sys

host = input('\nInforme o nome do HOST ou URL do site: ')
port = 22 # Porta SSH

server_conn = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

try:
   sock.connect(server_conn)
except socket.gaierror:
   print('\nErro no HOST...')
except:
   print(sys.exc_info())
else:
   print('\nConexão OK...')
   sock.close()

   #importar soquete,sistema
#hospedar = entrada('\nInforme o nome do HOST ou URL do site: ')
#porta = 22 # Porta SSH
#server_conn =(hospedar,porta)
#meia = soquete.soquete(soquete.AF_INET,soquete.SOCK_STREAM)
#meia.definir tempo limite(3)
#tentar:
 #  meia.conectar(server_conn)
#exceto soquete.gaierror:
 #  imprimir('\nErro no HOST...')
#exceto:
 #  imprimir(sistema.exc_info())
#outro:
  #imprimir('\nConexão OK...')
  # meia.fechar()