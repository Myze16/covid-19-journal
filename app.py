from flask import Flask, render_template
from noticia import Noticia
from estado import Estado

app = Flask(__name__)

ac = Estado(0, 'Acre', 'AC')
al = Estado(1, 'Alagoas', 'AL')
ap = Estado(2, 'Amapá', 'AP')
am = Estado(3, 'Amazonas', 'AM')
ba = Estado(4, 'Bahia', 'BA')
ce = Estado(5, 'Ceára', 'CE')
es = Estado(6, 'Espírito Santo', 'ES')
go = Estado(7, 'Goiás', 'GO')
ma = Estado(8, 'Maranhão', 'MA')
mt = Estado(9, 'Mato Grosso', 'MT')
ms = Estado(10, 'Mato Grosso do Sul', 'MS')
mg = Estado(11, 'Minas Gerais', 'MG')
pa = Estado(12, 'Pará', 'PA')
pb = Estado(13, 'Paraíba', 'PB')
pr = Estado(14, 'Paraná', 'PR')
pe = Estado(15, 'Pernambuco', 'PE')
pi = Estado(16, 'Piauí', 'PI')
rj = Estado(17, 'Rio de Janeiro', 'RJ')
rn = Estado(18, 'Rio Grande do Norte', 'RN')
rs = Estado(19, 'Rio Grande do Sul', 'RS')
ro = Estado(20, 'Rondônia', 'RO')
rr = Estado(21, 'Roraima', 'RR')
sc = Estado(22, 'Santa Catarina', 'SC')
sp = Estado(23, 'São Paulo', 'SP')
se = Estado(24, 'Sergipe', 'SE')
to = Estado(25, 'Tocantins', 'TO')
df = Estado(26, 'Distrito Federal', 'DF')

lista_noticias = [
    Noticia(0, '05/04/2022', 'Lorem ipsum dolor sit amet consectetur.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam corrupti nostrum iure sint numquam recusandae impedit delectus.', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolores qui aspernatur id beatae. Dolorum qui velit, ipsum molestias ab eius soluta officiis, animi harum suscipit amet quos doloremque impedit hic?Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolores qui aspernatur id beatae. Dolorum qui velit, ipsum molestias ab eius soluta officiis, animi harum suscipit amet quos doloremque impedit hic?Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.', 'https://www.severianodealmeida.rs.gov.br/uploads/noticiascontroller/624/upload20200409151118.jpg', rj),
    Noticia(1, '15/04/2022', 'Lorem ipsum dolor sit amet consectetur.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam corrupti nostrum iure sint numquam recusandae impedit delectus.', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolores qui aspernatur id beatae. Dolorum qui velit, ipsum molestias ab eius soluta officiis, animi harum suscipit amet quos doloremque impedit hic?Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolores qui aspernatur id beatae. Dolorum qui velit, ipsum molestias ab eius soluta officiis, animi harum suscipit amet quos doloremque impedit hic?Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.', 'https://www.severianodealmeida.rs.gov.br/uploads/noticiascontroller/624/upload20200409151118.jpg', ac),
    Noticia(2, '25/04/2022', 'Lorem ipsum dolor sit amet consectetur.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam corrupti nostrum iure sint numquam recusandae impedit delectus.', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolores qui aspernatur id beatae. Dolorum qui velit, ipsum molestias ab eius soluta officiis, animi harum suscipit amet quos doloremque impedit hic?Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Dolores qui aspernatur id beatae. Dolorum qui velit, ipsum molestias ab eius soluta officiis, animi harum suscipit amet quos doloremque impedit hic?Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam eos culpa nobis quidem quasi voluptatum! Cupiditate perferendis eligendi et mollitia iste odio libero recusandae non molestiae. Voluptas non magnam reprehenderit.', 'https://www.severianodealmeida.rs.gov.br/uploads/noticiascontroller/624/upload20200409151118.jpg', pb)
]

lista_estados = [
    ac,
    al,
    ap,
    am,
    ba,
    ce,
    es,
    go,
    ma,
    mt,
    ms,
    mg,
    pa,
    pb,
    pr,
    pe,
    pi,
    rj,
    rn,
    rs,
    ro,
    rr,
    sc,
    sp,
    se,
    to,
    df
]

@app.route('/')
def eu_apoio_debug_com_print():
    return render_template('home.html', noticias=lista_noticias)
    
@app.route('/info/<id>')
def noticia(id):
    for i in lista_noticias:
        if int(i.get_id()) == int(id):
            return render_template('info.html', noticia=lista_noticias[int(id)])
    return render_template('erro.html')

@app.route('/estado/<string:uf>')
    for estado in lista_estados:
        if 


app.run(debug=True)