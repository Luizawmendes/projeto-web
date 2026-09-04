from flask import Flask

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    # Rota raiz: exibida quando o usuário acessa http://localhost:5000/
    return '''
        <h1>Sistema de Gestão</h1>
        <p>Bem-vindo ao sistema.</p>
        <a href="/sobre">Sobre o sistema</a> |
        <a href="/contato">Contato</a>
    '''
    # Observe que usamos três aspas (''') para strings de múltiplas linhas em Python
    # Isso permite quebrar o HTML em várias linhas sem concatenação


@app.route('/sobre')
def sobre():
    # Rota /sobre: http://localhost:5000/sobre
    return '''
        <h1>Sobre o Sistema</h1>
        <p>Este sistema foi desenvolvido na disciplina Programação para Internet.</p>
        <a href="/">Voltar ao início</a>
    '''


@app.route('/contato')
def contato():
    # Rota /contato: http://localhost:5000/contato
    return '''
        <h1>Contato</h1>
        <p>Professor: Ronan Adriel Zenatti</p>
        <p>FATEC Jahu — Gestão da Tecnologia da Informação</p>
        <a href="/">Voltar ao início</a>
    '''


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/usuario/<nome>')
def perfil_usuario(nome):
    # <nome> na rota captura qualquer texto nessa posição da URL
    # Esse valor é passado automaticamente como parâmetro para a função
    # Exemplo: acessar /usuario/joao passa nome='joao' para esta função
    return f'<h1>Perfil do usuário: {nome}</h1><p>Olá, {nome}! Sua conta está ativa.</p>'
    # O 'f' antes das aspas cria uma f-string: permite inserir variáveis
    # Python diretamente no texto usando chaves {}

    # Importa Flask e também a função render_template
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    # render_template busca o arquivo na pasta templates/
    # e retorna seu conteúdo como resposta HTTP
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)