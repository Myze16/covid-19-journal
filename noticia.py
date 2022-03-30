class Noticia:
    def __init__(self, id, data, titulo, conteudo, conteudo1, conteudo2, img):
        self.__id = id
        self.__data = data
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__conteudo1 = conteudo1
        self.__conteudo2 = conteudo2
        self.__img = img

    def get_id(self):
        return self.__id

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