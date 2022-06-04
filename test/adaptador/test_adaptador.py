from app.infraestructura.adaptador.mysql.adaptador_mysql import AdaptadorMysql
from app.dominio.modelo.arrendatario_dto import ArrendatarioDto


def test_vote_save():
    adaptador = AdaptadorMysql()
    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)
    assert isinstance(adaptador, AdaptadorMysql)
