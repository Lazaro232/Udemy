from flask import Flask, render_template, request, url_for, redirect

# O objeto Flask deve ÚNICO. Para garantir isso, usa-se o nome
# da aplicação que está rodando (__main__, por exemplo )
app = Flask(__name__)

# Dicionário que simula um banco de dados
posts = {
    0: {
        'post_id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')  # Página inicial
def home():
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')  # Página de posts (Ex.: /post/0)
def post(post_id):
    # get --> Tenta recuperar a KEY e ...
    # retorna None se não encontrar nada
    post = posts.get(post_id)
    # Adicionando página de erro
    if not post:  # post=None se não for encontrado; not None = True
        return render_template('404.html',
                               message=f'A post with id {post_id} was not found.')

    return render_template('post.html', post=post)
    # Igual a:
    # return render_template('post.html', post=post = posts.get(post_id))


# Página para onde o conteúdo de /post/form é enviado ao se cliclar em submit
@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':  # Se for um POST
        title = request.form.get('title')  # Recebe o título do formulário
        content = request.form.get('content')  # Recebe o título do formulário
        # Adicionando o POST (título e conteúdo) ao banco de dados (dicionário 'posts')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post', post_id=post_id))

    # Se NÃO  for um POST (ou seja, é um GET) entra na página do formulário
    return render_template('create.html')


# Garante que quem está rodando é o MAIN
if __name__ == '__main__':
    app.run(debug=True)


# ANOTAÇÕES

# return render_template('post.html', post=post)
'''
    O primeiro 'post' é o que está no arquivo .html
    O segundo é a variável post acima
    Ou seja, a variável post de post.html recebe o valor ...
    de post, em que post = posts.get(post_id)
'''


# title = request.args.get('title')
'''
    request --> Funciona como uma variável global. Ela recebe o que o formulário
    envia, por exemplo: http://127.0.0.1:5000/post/form?title=My+first+blog+post&content=How+are+u%3F
    dentro dela há alguns argumentos (.args) e estão expressos ao lado do símbolo '='
    Neste caso é 'title' e 'content'
'''

# title = request.form.get('title')
'''
    Utilizando o.form ao invés do .args, a string contendo as informações do
    formulário não estarão mais disponíveis no URL. Isso garante uma certa
    segurança ao formulário, pois os dados contidos no URL poderiam ser
    acessados relativamente fácil por alguém utilizando a mesma rede wifi, por exemplo.
'''

# return redirect(url_for('post', post_id=post_id))
'''
    url_for() recebe uma FUNÇÃO. Ou seja, 'post' é o end point/função criado acima.
    post_id=post_id --> Informa que o parâmetro post_id que deve ser passado para ...
    a função 'post' é igual a variável local (dentro de 'create') chamada post_id

    Ao invés de passar o end point da função 'post' dentro do redirect, usa-se o ...
    url_for(), pois caso o url da função 'post' mude, o redirect também mudará, pois
    é feita um referência a função e não ao end point (url) da função.
'''
