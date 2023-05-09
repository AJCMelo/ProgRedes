import socket

#------------------------------------------------------------
def get_protnumber(prefix):
   return dict ((getattr(socket, a), a)
      for a in dir(socket)
         if a.startswith(prefix) )
#------------------------------------------------------------

proto_fam = get_protnumber('AF_')
types     = get_protnumber('SOCK_')
protocols = get_protnumber('IPPROTO_')

host  = input('\nInforme o nome do HOST ou URL do site: ')

infos = socket.getaddrinfo(host, 'http')

for info in infos:
   family, socktype, proto, canonname, sockaddr = info
   
   print('\n----------------------------------------')
   print(f'Info ...................: {info}')
   print(f'Family .................: {proto_fam[family]}')
   print(f'Type ...................: {types[socktype]}')
   print(f'Proto ..................: {protocols[proto]}')
   print(f'Canonical Name (CNAME) .: {canonname}')   
   print(f'SOCKET Address .........: {sockaddr}')

#importar soquete
#------------------------------------------------- -----------
#def get_protnumber(prefixo):
#  retornar ditado((getattr(soquete,a),a)
#     para a em dir(soquete)
#       se a.começa com(prefixo) )
#------------------------------------------------- -----------
#proto_fam = get_protnumber('AF_')
#tipos     = get_protnumber('MEIA_')
#protocolos = get_protnumber('IPPROTO_')
#hospedar  = entrada('\nInforme o nome do HOST ou URL do site: ')
#informações = soquete.getaddrinfo(hospedar,'http')
#para informação em informações:
   #família,tipo de meia,proto,nome canônico,sockaddr = informação
   #
   #imprimir('\n----------------------------------------')
   #imprimir(f'Info ...................:{informação}')
   #imprimir(f'Família ..............:{proto_fam[família]}')
   #imprimir(f'Tipo ...................:{tipos[tipo de meia]}')
   #imprimir(f'Proto ..............:{protocolos[proto]}')
   #imprimir(f'Nome canônico (CNAME).:{nome canônico}')   
   #imprimir(f'SOCKET Endereço .........:{sockaddr}')