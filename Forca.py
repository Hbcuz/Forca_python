#Nome: João Carlos Pereira Alves

import random
nome_arquivo = "./banco de palavras.txt" 


while True:
    acertos = []
    chances = []
    tentativas = 0

    anim = 0

    
    print('\nJogo da forca...')
    print('\nJogar... [J]')
    print('\nAdicionar palavra... [G]  ')
    print('\nSair... [S]')
    user = input('\nBem vindo ao menu da forca....').upper()
    
    teste = []
    
    if user == 'G':
        while True:
            arquivo = open(nome_arquivo, 'w')
            
            while True:
                loop = True
            
                print('\n--', teste, '--')
                text = str(input("\nDigite uma palavra: "))

                if text in teste:
                    loop = False

                else:
                    teste.append(text)
                    arquivo.write(text + '\n')
                    

                if loop == False:
                    print("\nVocê já adicionou esta palavra.")

                rep = str(input('\nDeseja adicionar outra palavra? [A] ou [SAIR] ')).upper()
                
                if rep != 'A':
                    break     
                
            print('\nPalavra adicionada com sucesso !')
            break
    
    if user == 'J':
        jg = input('\nDeseja ativar animações? [S/N] ').upper()
        dev = False
        if jg == 'S':
            dev = True
        
        arquivo = open(nome_arquivo, 'r')
        lista_de_palavras = arquivo.readlines()
        palavra_escolhida = random.choice(lista_de_palavras)
        for form in palavra_escolhida:
            form = palavra_escolhida.rstrip('\n')
        while True:

            achou = False
            letras_acertadas = ""
            
            for senha in form:
                letras_acertadas += senha if senha in acertos else '-'
            print('\n', letras_acertadas)

            if letras_acertadas == form:
                for i in range(0, 6):
                    print('.')
                    if i == 5:
                        print('\nVocê venceu !!!')
                replay = str(input('\nDeseja jogar novamente? [S/N] ')).upper()
                if replay == 'S':
                    break
                else:
                    print('\nJogo finalizado!')
                    exit(0)

            chute = input("\nQual letra? ")
            for letra in form:
                acertos += chute
                if chute.upper() == letra.upper():
                    achou = True

            if chute in chances:
                    print('\nVocê já usou a letra {}.'.format(chute))

            chances += chute

            if achou == False:
                anim += 1
                tentativas += 1

                print("\nNão tem a letra {}...".format(chute))

                print('\nRestam {} tentativas ! '.format(5 - tentativas))

                if dev == True:
                    if anim >= 1:
                        print('\n-----¬')
                    if anim >= 2:
                        print('    (@)')
                    if anim >= 3:
                        print('   \   /')
                    if anim >= 4:
                        print('    ( ) ')
                    if anim >= 5:
                        print('   /   \ ')
                if tentativas == 5:
                    print('\n Perdeu !')
                    replay = str(input('\nDeseja jogar novamente? [S/N] ')).upper()
                    if replay == 'S':
                        break
                    else:
                        print('\nJogo finalizado!')
                        exit(0)
           

 
    if user == 'S':
        print('\nJogo finalizado!\n')
        break
    if user != 'S' or 'J' or 'G' or 'SAIR' or 'A' or 'N':
        while True:
            print('\nNão entendi o que quis dizer...')
            print('\nTente novamente...')
            break

arquivo.close()