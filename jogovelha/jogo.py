from flask import Flask
import os  # Para limpar o terminal 


app = Flask(__name__)



def print_borda(borda):  # Função para mostrar o tabuleiro
    print(f"\n {borda[0]} | {borda[1]} | {borda[2]}")
    print("---+---+---")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    print(f" {borda[3]} | {borda[4]} | {borda[5]}")
    print("---+---+---")
    print(f" {borda[6]} | {borda[7]} | {borda[8]}\n")

def checar_vencedor(borda, jogador):  # Verifica se um jogador venceu
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]  # Diagonais
    ]
    return any(all(borda[i] == jogador for i in condition) for condition in win_conditions)

def bordacheia(borda):  # Verifica se o tabuleiro está cheio (empate)
    return all(cell in ['X', 'O'] for cell in borda)

def main():  # Função principal do jogo
    while True:  # Loop para reiniciar o jogo
        borda = [' ' for _ in range(9)]  # Tabuleiro vazio
        jogadoratual = 'X'  # Jogador que começa

        print("\nBem-vindo ao Jogo da Velha!")
        print_borda(borda)

        while True:  # Loop da partida
            try:
                move = int(input(f"Jogador {jogadoratual}, escolha uma posição (1-9): ")) - 1

                if move < 0 or move > 8 or borda[move] != ' ':
                    print("Escolha inválida! Tente novamente.")
                    continue
                

                borda[move] = jogadoratual  # Marca a jogada
                os.system("cls")  # Limpa o terminal (Windows)
                print_borda(borda)

                if checar_vencedor(borda, jogadoratual):  
                    print(f"Parabéns, Jogador {jogadoratual}! Você venceu!")
                    break

                if bordacheia(borda):  
                    print("Empate! O tabuleiro está cheio.")
                    break

                jogadoratual = 'O' if jogadoratual == 'X' else 'X'  # Alterna jogadores

            except ValueError:
                print("Entrada inválida! Digite um número entre 1 e 9.")

        # Perguntar se deseja jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':  
            print("Obrigado por jogar! Até a próxima.")
            break  # Sai do loop e encerra o jogo

if __name__ == "__main__":  # Corrigido erro do nome da variável
    main()
