import random
import funcoes

mais_opcao = 's'

while mais_opcao == 's':
    
    funcoes.menu()
    opcao_menu = input('Digite uma opção: ')
    try:
        opcao_int = int(opcao_menu)
        if opcao_int < 1 or opcao_int > 5:  # Verifica se está entre 1 e 5
            print("Digite apenas números de 1 a 5!")
            continue  # Volta pro início do loop
    except ValueError:  # Se não for número
        print("ERRO. Digite apenas números inteiros!")
        continue  # Volta pro início do loop

    if opcao_int == 1:
        funcoes.adicionar_titulo()
    elif opcao_int == 2:
        funcoes.marcar_como_assistido_lido()
    elif opcao_int == 3: 
        funcoes.lista_de_titulos()
    elif opcao_int == 4: 
        funcoes.recomendacao_aleatoria()
    elif opcao_int == 5: 
        funcoes.titulos_assistidos_lidos()
    
    funcoes.voltar_ao_menu()