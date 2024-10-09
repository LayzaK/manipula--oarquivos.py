arq = open('arquivo.txt','w')

# - write -
# arq.write('olá mundo')

# - writelines -
# lista = ['Layza','18','2006']
# arq.writelines(lista)

# - quebra de linhas com write -
nomes = ['Layza', 'Victor', 'Julia']
for n in nomes:
    arq.write(n + '\n')