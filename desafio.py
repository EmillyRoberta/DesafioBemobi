import re
import sys

brasil = [[], []]
chile = [[], []]
mexico = [[], []]

#arquivo recebe o primeiro argumento da linha do script
arquivo = str(sys.argv[1])

#cria o arquivo e grava nele a saida do programa
sys.stdout = open("resultado.txt", "a")

#verifica se caso o arquivo passado, nao tiver o .txt, terá acesso do mesmo jeito
if not '.' in arquivo:
    arquivo += '.txt'

#abre o arquivo para leitura e atraves do open foi iterado linha por linha
with open(arquivo, 'r') as f:
    for line in f:
        
        if re.search('^55', line): #verifica se no comeco da frase tem 55
           brasil[0].append(line) #adiciona a linha na lista brasil[0]
           if(re.findall('assinado', line)): #verifica se na linha tem assinado
               brasil[1].append(line) #adiciona a linha na lista brasil[1]
               
        if re.search('^56', line):
           chile[0].append(line)
           if(re.findall('assinado', line)):
               chile[1].append(line)

        if re.search('^52', line):
           mexico[0].append(line)
           if(re.findall('assinado', line)):
               mexico[1].append(line)

print("Brasil, " + str(len(brasil[0])) + ", " + str(len(brasil[1]))) 
print("Chile, " + str(len(chile[0])) + ", " + str(len(chile[1])))
print("Mexico, " + str(len(mexico[0])) + ", " + str(len(mexico[1]))) 