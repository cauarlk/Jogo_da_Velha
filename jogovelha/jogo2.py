# Importa os módulos necessários do Flask
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Criação da instância do Flask
app = Flask(__name__)

# Estado do jogo, com um dicionário que mantém as informações
jogo = {
    "tabuleiro": [""] * 9,  # Lista representando as 9 posições do tabuleiro (vazia no início)
    "jogador_atual": "X",  # O jogador que começa o jogo
    "vencedor": None,  # Indica se há um vencedor ou empate
    "jogo_ativo": True,  # Controla se o jogo está em andamento
    "simbolo_jogador": None  # O jogador escolhe entre "X" ou "O"
}

# Definição das combinações vencedoras possíveis no jogo
VITORIAS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
    [0, 4, 8], [2, 4, 6]  # Diagonais
]

# Função que verifica se há um vencedor ou empate
def checar_vencedor():
    # Verifica todas as combinações vencedoras
    for combinacao in VITORIAS:
        a, b, c = combinacao
        # Se as três posições da combinação forem iguais e não estiverem vazias
        if jogo["tabuleiro"][a] == jogo["tabuleiro"][b] == jogo["tabuleiro"][c] and jogo["tabuleiro"][a] != "":
            jogo["vencedor"] = jogo["tabuleiro"][a]  # Define o vencedor
            jogo["jogo_ativo"] = False  # Finaliza o jogo
            return

    # Se não houver mais espaços vazios no tabuleiro, o jogo empatou
    if "" not in jogo["tabuleiro"]:
        jogo["vencedor"] = "Empate"
        jogo["jogo_ativo"] = False  # Finaliza o jogo

# Rota inicial que renderiza o template HTML e passa o estado do jogo
@app.route("/")
def index():
    return render_template("index.html", jogo=jogo)

# Rota para o jogador escolher seu símbolo (X ou O)
@app.route("/escolher_simbolo", methods=["POST"])
def escolher_simbolo():
    simbolo = request.form["simbolo"]  # Obtém o símbolo escolhido do formulário
    jogo["simbolo_jogador"] = simbolo  # Define o símbolo do jogador
    jogo["jogador_atual"] = simbolo  # Define o jogador inicial (aquele que escolheu o símbolo)
    return redirect(url_for("index"))  # Redireciona de volta para a página inicial

# Rota para realizar uma jogada em uma posição do tabuleiro
@app.route("/jogada/<int:posicao>", methods=["POST"])
def jogada(posicao):
    # Verifica se o jogo está ativo, se a posição é válida e se está vazia
    if jogo["jogo_ativo"] and 0 <= posicao < 9 and jogo["tabuleiro"][posicao] == "":
        jogo["tabuleiro"][posicao] = jogo["jogador_atual"]  # Marca a posição com o símbolo do jogador atual
        checar_vencedor()  # Verifica se há vencedor após a jogada

        # Se o jogo ainda estiver ativo, muda para o próximo jogador
        if jogo["jogo_ativo"]:
            jogo["jogador_atual"] = "O" if jogo["jogador_atual"] == "X" else "X"

    return jsonify(jogo)  # Retorna o estado atualizado do jogo em formato JSON

# Rota para reiniciar o jogo, resetando o estado
@app.route("/reiniciar")
def reiniciar():
    jogo.update({
        "tabuleiro": [""] * 9,  # Reseta o tabuleiro
        "jogador_atual": "X",  # Reseta o jogador atual para X
        "vencedor": None,  # Remove o vencedor
        "jogo_ativo": True,  # Define o jogo como ativo novamente
        "simbolo_jogador": None  # Remove o símbolo do jogador
    })
    return redirect(url_for("index"))  # Redireciona para a página inicial

# Inicializa o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
    
    
