import socket                                                     # importar soquete

host  = input('\nInforme o nome do HOST ou URL do site: ')        #hospedar  = entrada('\nInforme o nome do HOST ou URL do site: ')

infos = socket.getaddrinfo(host, 'http')                          #informações = soquete.getaddrinfo(hospedar,'http')

for info in infos:                                                #para informação em informações:
   print('\n----------------------------------------')                 # imprimir('\n----------------------------------------')
   print(f'Info ...................: {info}')                          # imprimir(f'Info ...................:{informação}')
   print(f'Family .................: {info[0]}')                       #imprimir(f'Família ..............:{informação[0]}')
   print(f'Type ...................: {info[1]}')                       #imprimir(f'Tipo ...................:{informação[1]}')
   print(f'Proto ..................: {info[2]}')                       #imprimir(f'Proto ..............:{informação[2]}')
   print(f'Canonical Name (CNAME) .: {info[3]}')                       #imprimir(f'Nome canônico (CNAME).:{informação[3]}')
   print(f'SOCKET Address .........: {info[4]}')                       #imprimir(f'SOCKET Endereço .........:{informação[4]}')