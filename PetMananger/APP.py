from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('seu_banco_de_dados.db')
    conn.row_factory = sqlite3.Row  # Para tratar as respostas como dicionários
    return conn

# Rota principal para renderizar o frontend
@app.route('/')
def index():
    return render_template('index.html')

# Rota para pegar todos os animais
@app.route('/animais', methods=['GET'])
def get_animais():
    conn = get_db_connection()
    animais = conn.execute('SELECT * FROM animais').fetchall()
    conn.close()
    return jsonify([dict(animal) for animal in animais])

# Rota para adicionar um animal
@app.route('/animais', methods=['POST'])
def add_animal():
    new_animal = request.get_json()
    nome = new_animal['nome']
    especie = new_animal['especie']
    raca = new_animal.get('raca')
    idade = new_animal.get('idade')

    conn = get_db_connection()
    conn.execute('INSERT INTO animais (nome, especie, raca, idade) VALUES (?, ?, ?, ?)', 
                 (nome, especie, raca, idade))
    conn.commit()
    conn.close()

    return jsonify({"message": "Animal adicionado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
