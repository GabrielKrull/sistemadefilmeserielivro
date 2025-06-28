import sys
import random
lido = "s"

catalogo = {}  # Dicionário que armazena todos os títulos (filmes, séries, livros)  
def menu():
    # Mostra as opções do programa de forma organizada  
    print("\n========== GERENCIADOR DE FILMES/SÉRIES ASSISTIDOS ==========")
    print("1. Adicionar título")
    print("2. Marcar como assistido/lido")
    print("3. Lista de títulos")
    print("4. Recomendação aleatória")
    print("5. Títulos assistidos/lidos")

def adicionar_titulo():  
    # Pede categoria (filme, série ou livro) e valida  
    while True:  
        categoria = input("Digite a categoria (filme/serie/livro): ").strip().lower()  
        if categoria in ['filme', 'serie', 'livro']:  
            break  
        print("Categoria inválida! Digite filme, serie ou livro")  

    # Pede nome do título e gênero  
    titulo = input("Digite o nome do título: ").strip().lower()  
    genero = input("Digite o gênero do título: ").strip().lower()  

    # Se for filme ou série pergunta se foi assistido  
    if categoria in ['filme', 'serie']:  
        while True:  
            assistido = input("Este título foi assistido (s/n): ").lower()  
            if assistido in ['s', 'n']:  
                break  
            print("Digite uma opção válida (s/n).")  

        # Salva no catálogo  
        status = "assistido" if assistido == 's' else "não assistido"  
        catalogo[titulo] = {"categoria": categoria.replace('serie', 'série'),"assistido": assistido == 's', "genero": genero  }  # Ajusta "serie" para "série" # Converte 's' em True, 'n' em False
        print(f"Título {titulo} ({status}) adicionado com sucesso!")  

    # Se for livro pergunta se foi lido  
    elif categoria == 'livro':  
        while True:  
            lido = input("Este livro foi lido (s/n): ").lower()  
            if lido in ['s', 'n']:  
                break  
            print("Digite uma opção válida (s/n).")  

        #Salva no catálogo  
        status = "lido" if lido == 's' else "não lido"  
        catalogo[titulo] = { "categoria": categoria, "lido": lido == 's', "genero": genero  }  # Converte s em True, n em False  
        print(f"Título {titulo} ({status}) adicionado com sucesso!")  

def marcar_como_assistido_lido():  
    titulo = input("Digite o nome do título que deseja marcar: ").strip().lower()  

    if titulo in catalogo:  
        # Se for filme ou série marca como assistido  
        if catalogo[titulo]['categoria'] in ['filme', 'série']:  
            catalogo[titulo]["assistido"] = True  
            print(f"'{titulo}' marcado como assistido!")  
        # Se for livro marca como lido  
        else:  
            catalogo[titulo]["lido"] = True  
            print(f"'{titulo}' marcado como lido!")  
    else:  
        print("Título não encontrado!")  

def lista_de_titulos():  
    if not catalogo:  # Se o catálogo estiver sem nada 
        print("Nenhum título cadastrado!")  
        return  

    print("\n=== TODOS OS TÍTULOS ===")  
    for titulo, info in catalogo.items():  
        # Verifica se é assistido (filme/série) ou lido (livro)  
        status = (  
            "Assistido" if info.get('assistido', False)  
            else "Lido" if info.get('lido', False)  
            else "Não lido"  
        )  
        print(f"{titulo} ({info['categoria']}, {info['genero']}) - {status}")  

def recomendacao_aleatoria():  
    if not catalogo:  
        print("Nenhum título cadastrado no catálogo!")  
        return  

    recomendacoes = []  

    # Procura filmes e séries não assistidos e livros não lidos  
    for titulo, info in catalogo.items():  
        if info['categoria'] in ['filme', 'série'] and not info.get('assistido', False):  
            recomendacoes.append((titulo, info, 'assistir'))  
        elif info['categoria'] == 'livro' and not info.get('lido', False):  
            recomendacoes.append((titulo, info, 'ler'))  

    if not recomendacoes:  
        print("\nParabéns! Você já consumiu todos os títulos!")  
        return  

    # Escolhe uma recomendação aleatória  
    titulo, info, acao = random.choice(recomendacoes)  
    print(f" RECOMENDAÇÃO:")  
    print(f"Título: {titulo.title()} é um(a) {info['categoria'].title()} ideal para você hoje, do gênero {info['genero'].title()}. Embarque nessa aventura e aproveite!")  

def titulos_assistidos_lidos():  
    if not catalogo:  
        print("Nenhum título cadastrado!")  
        return  

    print("\n=== TÍTULOS CONSUMIDOS ===")  
    for titulo, info in catalogo.items():  
        if info.get('assistido', False) or info.get('lido', False):  
            print(f"{titulo} ({info['categoria']}, {info['genero']})")  

def voltar_ao_menu():
    global mais_opcao  #Transforma a variável em global (passei raiva com isso)
    mais_opcao = input("Deseja digitar mais uma opção? (s/n): ").lower()
    if mais_opcao == "n":
        print("Obrigado terráqueo por utilizar nosso catálogo de filmes!.")
        sys.exit() #Esse foi o único maldito jeito que encontrei pra parar o do código
        