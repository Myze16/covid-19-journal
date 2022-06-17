from journal.model.entity.estado import Estado
from journal.model.entity.noticia import Noticia

ac = Estado(0, 'Acre', 'AC', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Acre.png')
al = Estado(1, 'Alagoas', 'AL', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Alagoas-300x200.png')
ap = Estado(2, 'Amapá', 'AP', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amapa-300x210.png')
am = Estado(3, 'Amazonas', 'AM', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amazonas-300x214.png')
ba = Estado(4, 'Bahia', 'BA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Bahia-300x200.png')
ce = Estado(5, 'Ceára', 'CE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Ceara-300x210.png')
es = Estado(6, 'Espírito Santo', 'ES', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Espirito_Santo-300x210.png')
go = Estado(7, 'Goiás', 'GO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Goias-300x210.png')
ma = Estado(8, 'Maranhão', 'MA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Maranhao-300x200.png')
mt = Estado(9, 'Mato Grosso', 'MT', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso-300x210.png')
ms = Estado(10, 'Mato Grosso do Sul', 'MS', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso_do_Sul-300x210.png')
mg = Estado(11, 'Minas Gerais', 'MG', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Minas_Gerais-300x210.png')
pa = Estado(12, 'Pará', 'PA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Para-300x200.png')
pb = Estado(13, 'Paraíba', 'PB', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Paraiba-300x210.png')
pr = Estado(14, 'Paraná', 'PR', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Parana-300x210.png')
pe = Estado(15, 'Pernambuco', 'PE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Pernambuco-300x210.png')
pi = Estado(16, 'Piauí', 'PI', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Piaui-300x200.png')
rj = Estado(17, 'Rio de Janeiro', 'RJ', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Rio_de_Janeiro-300x210.png')
rn = Estado(18, 'Rio Grande do Norte', 'RN', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Norte-300x200.png')
rs = Estado(19, 'Rio Grande do Sul', 'RS', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Sul-300x210.png')
ro = Estado(20, 'Rondônia', 'RO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Rondonia-300x210.png')
rr = Estado(21, 'Roraima', 'RR', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Roraima-300x200.png')
sc = Estado(22, 'Santa Catarina', 'SC', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Santa_Catarina-300x218.png')
sp = Estado(23, 'São Paulo', 'SP', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Sao_Paulo-300x200.png')
se = Estado(24, 'Sergipe', 'SE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Sergipe-300x210.png')
to = Estado(25, 'Tocantins', 'TO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Tocantins-300x210.png')
df = Estado(26, 'Distrito Federal', 'DF', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Distrito_Federal_Brasil-300x210.png')

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

class EstadoDAO:
    def listar_estados(self):
        return lista_estados
    