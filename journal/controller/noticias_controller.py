from urllib import response
from journal import app
from flask import render_template, request, jsonify
from journal.model.dao.estado_dao import EstadoDAO
from journal.model.dao.noticia_dao import NoticiaDAO


@app.route('/')
def home():
    estados = EstadoDAO().listar_estados()
    lista_noticias = NoticiaDAO().listar_noticias()
    return render_template('home.html', noticias=lista_noticias, estados=estados)


@app.route('/info/<id>')
def noticia(id):
    estados = EstadoDAO().listar_estados()
    noticia = NoticiaDAO().encontrar_noticia(id)
    if noticia:
        return render_template('info.html', noticia=noticia, estados=estados)
    return render_template('erro.html')


@app.route('/comentarios/<id>', methods=["POST"])
def comentar(id):
    if request.method == "POST":
        nome = request.form.get('nome', None)
        texto = request.form.get('texto', None)
        email = request.form.get('email', None)
        noticia = NoticiaDAO().encontrar_noticia(id)
        NoticiaDAO().registrar_comentario(noticia, nome, email, texto)
        return jsonify({'name': nome, 'email': email,'text': texto})
    return jsonify({'error': 'F familia'})


@app.route('/curtir/<id>')
def curtir(id):
    noticia = NoticiaDAO().encontrar_noticia(id)
    if not noticia.curtido:
        noticia.inserir_like()
    else:
        noticia.deslike()
    return jsonify({'likes': noticia.likes, 'curtido': noticia.curtido})

@app.route('/estado/<string:uf>')
def noticia_estado(uf):
    estados = EstadoDAO().listar_estados()
    lista_noticias = NoticiaDAO().listar_noticias()
    noticia_estados = []
    for estado in estados:
        if estado.get_uf() == uf:
            for i in lista_noticias:
                if i.get_estado().get_uf() == uf:
                    noticia_estados.append(i)
            print(noticia_estados)
            return render_template('estados.html', noticia_estado=noticia_estados, estados=estados)
    return render_template('erro.html')
