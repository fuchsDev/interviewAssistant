# -- coding: utf-8 --

#Variable's
import os
probability = 0
dir_path = os.path.dirname(os.path.realpath(__file__)) #Get Current Directory
fileSave = open(dir_path+'/interview.txt', 'w')
text = []
clear = lambda: os.system('clear')


#Vectors   
questions = [
                "\n01 -FALE SOBRE VOCÊ E SUAS EXPERIÊNCIAS?"
                "\n02 -ESTUDA OU PRETENDE ESTUDAR? QUAL ÁREA DE INTERESSE?"
                "\n03 -CONHECE ALGUÉM QUE TRABALHA AQUI?"
                "\n04 -QUEM SÃO SEUS FAMILIARES E QUANTAS PESSOAS MORAM CONTIGO?"
                "\n05 -CONHECIMENTO EM VEÍCULOS, OU INFORMÁTICA?"
                "\n06 -POR QUE SAIU OU QUER SAIR DO SEU ÚLTIMO EMPREGO? COMO ERA TRABALHAR LÁ?"
                "\n07 -COMO ERA SEU RELACIONAMENTO COM SEUS COLEGAS DE EMPRESA? FEZ AMIZADES?"
                "\n08 -COMO DESCREVE A SUA PERSONALIDADE?"
                "\n09 -QUAIS SÃO SEUS OBJETIVOS A CURTO E LONGO PRAZO?"
                "\n10 -COMO SE MANTÉM INFORMADO SOBRE NOTÍCIAS? QUAL ASSUNTO PROCURA?"
                "\n11 -O QUE VOCÊ FAZ DURANTE SEU TEMPO LIVRE (HOBBIES)?"
                "\n12 -COMO É COM FINANÇAS PESSOAIS? SABE SEU CUSTO DE VIDA? PESQUISA DE CRÉDITO?"
                "\n13 -DESCREVA SEU CHEFE OU SUPERIOR ANTERIOR?"
                "\n14 -SE EU LIGAR AGORA PARA SUAS REFERÊNCIAS, O QUE DIRIAM SOBRE VOCÊ?"
                "\n15 -QUANDO AS PESSOAS NÃO GOSTAM DE VOCÊ, NORMALMENTE QUAL É O MOTIVO?"
                "\n16 -QUANDO AS PESSOAS GOSTAM DE VOCÊ, É GERALMENTE POR QUAL MOTIVO?"
                "\n17 -TEM ALGUM PROBLEMA DE SAÚDE, TOMA ALGUM REMÉDIO CONTROLADO? É FUMANTE?"
                "\n18 -O QUE É MAIS IMPORTANTE, DINHEIRO OU TRABALHO?"
            ]

evaluation = [
                "\n01 -IDADE: ",
                "\n02 -CONHECIMENTO BASICO (VEICULOS/INFORMATICA): ",
                "\n03 -CONHECIMENTO BASICO EM ATENDIMENTO: ",
                "\n04 -FINANCAS PESSOAIS: ",
                "\n05 -OBJETIVOS FINANCEIROS: ",
                "\n06 -DISPONIBILIDADE DE HORARIO: ",
                "\n07 -RELACIONAMENTO ESTAVEL: ",
                "\n08 -CASEIRO/FAMILIA: ",
                "\n09 -TER FILHO COM 2 ANOS OU MAIS / OU NÃO TER INTERESSE: ",
                "\n10 -ESCOLARIDADE: ",
                "\n11 -BUSCA POR APRENDIZADO: ",
                "\n12 -HISTORICO PROFISSIONAL: ",
                "\n13 -TRABALHO EM EQUIPE / SOCIALIZAÇÃO: ",
                "\n14 -COMUNICACAO E APARENCIA: ",
                "\n15 -POSTURA CORPORAL / DESCONTRAIDO: ",
                "\n16 -HUMILDADE: ",
                "\n17 -SORRIR DURANTE A ENTREVISTA: ",
                "\n18 -SAUDE: ",
                "\n19 -RELACAO COM FUMO/BEBIDA: ",
            ]
   
    
#Menu
clear() #Clean the Screen
print('\n******* CODE ENTREVISTA *******')
name = input('NOME: ')
date = input('DATA: ')
job = input('CARGO: ')
text.append('\n' + name)
text.append('\n' + date)
text.append('\n' + job + '\n')


#Displays Questions
for i in questions:
    print(i)


#Comments
print('\nOBSERVACOES:')
loop = str('S')
while (loop != 'N'):
    counter = 0
    while (counter < 5):
        note = input('\nDIGITE: \n')
        text.append('\n' + note)
        counter = counter + 1
    loop = str(input('\nCONTINUAR? (S/N) \n'))
    

#Test Result
print('\nRESULTADO TESTES: (BAIXO/MEDIO/ALTO)')
logicalTest = input('TESTE LOGICO : \n')
creativeTest = input('CRIATIVIDADE: \n')
text.append('\n' + '\nTESTE LOGICO = ' + logicalTest + '\n')
text.append('TESTE CRIATIVO = ' + creativeTest + '\n')


#Evaluation Result
print('\nAVALIAÇÃO GERAL: (REPROVADO / NEUTRO / APROVADO)')
for y in evaluation:
    answer = 'X'
    while(answer !='R' and answer !='N' and answer !='A'):
        print(y)
        answer = input('\nDIGITE A RESPOSTA (R, N ou A): ')
        if answer == 'R':
            probability = probability + 1
        elif answer == 'N':
            probability = probability + 3
        elif answer == 'A':
            probability = probability + 5
            
        text.append(y + answer)
  

#Save Results
print('\nPROBALIDADE/PONTUACAO: ' + str(probability))
text.append('\n' + '\nPROBALIDADE/PONTUACAO: ' +  str(probability))
    
    
#Finish
text.append('\n' + '\n"CONTRATE PERSONALIDADE E TREINE TECNICA" \n')
text.append('"REFERENCIAS SAO IMPORTANTES, AS PESSOAS TENDEM A REPETIR COMPORTAMENTOS" \n')
fileSave.writelines(text)               
fileSave.close()


#Raname File
old_file = os.path.join(dir_path, 'interview.txt')
new_file = os.path.join(dir_path, name+'.txt')
os.rename(old_file, new_file)