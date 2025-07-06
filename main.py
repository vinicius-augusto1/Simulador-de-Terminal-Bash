from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')


@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

@app.route('/api/command', methods=['POST'])
def execute_command():
    data = request.get_json()
    command_input = data.get('command', '').strip()
    command = command_input.split()

    if not command:
        return jsonify({'output': ''})

    cmd = command[0].lower()

    try:
        if cmd == 'mkdir':
            if len(command) > 1:
                dirname = '_'.join(command[1:])
                if os.path.exists(dirname):
                    return jsonify({'output': f'O diretório "{dirname}" já existe.'})
                os.mkdir(dirname)
                return jsonify({'output': f'Diretório "{dirname}" criado com sucesso.'})
            return jsonify({'output': 'Uso correto: mkdir <nome_do_diretório>'})

        elif cmd == 'touch':
            if len(command) > 1:
                filename = '_'.join(command[1:])
                if os.path.exists(filename):
                    return jsonify({'output': f'O arquivo "{filename}" já existe.'})
                open(filename, 'x').close()
                return jsonify({'output': f'Arquivo "{filename}" criado com sucesso.'})
            return jsonify({'output': 'Uso correto: touch <nome_do_arquivo>'})

        elif cmd == 'pwd':
            return jsonify({'output': os.getcwd()})

        elif cmd == 'ls':
            files = os.listdir()
            return jsonify({'output': '\n'.join(files)})

        elif cmd in ('exit', 'quit'):
            return jsonify({'output': 'Saindo do terminal...'})

        else:
            return jsonify({'output': f'Comando não encontrado: {cmd}'})

    except Exception as e:
        return jsonify({'output': f'Erro: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
