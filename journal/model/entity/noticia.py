class Noticia:
    def __init__(self, id, views, data, titulo, conteudo, conteudo1, conteudo2, img, estado):
        self.__id = id
        self.__views = views
        self.__data = data
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__conteudo1 = conteudo1
        self.__conteudo2 = conteudo2
        self.__img = img
        self.__estado = estado
        self.__likes = 0
        self.__curtido = False
        self.__comentarios = []

    def get_id(self):
        return self.__id

    def get_views(self):
        return self.__views

    def get_data(self):
        return self.__data

    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_conteudo1(self):
        return self.__conteudo1

    def get_conteudo2(self):
        return self.__conteudo2

    def get_img(self):
        return self.__img

    def get_estado(self):
        return self.__estado

    @property
    def comentarios(self):
        return self.__comentarios

    @property
    def likes(self):
        return self.__likes

    @property
    def curtido(self):
        return self.__curtido

    def inserir_comentario(self, comentario):
        self.__comentarios.append(comentario)

    def inserir_like(self):
        self.__likes += 1
        self.__curtido = True

    def deslike(self):
        self.__likes -= 1
        self.__curtido = False


class Comentario:
    def __init__(self, noticia, nome, email, texto):
        self._id = noticia.comentarios[-1].id + 1 if noticia.comentarios else 0
        self._nome = nome
        self._texto = texto
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def texto(self):
        return self._texto
