from .Model.PaisModel import Pais
from .Model.AudioModel import Audio
from .Model.TecnologiaProyeccionModel import TecnologiaProyeccion
from .Model.ClasificacionModel import Clasificacion
from .Model.FormatoModel import Formato
from .Model.GeneroModel import Genero
from .Model.PeliculaModel import Pelicula
from .Model.ComplejoModel import Complejo
from .Model.SalaModel import Sala
from .Model.FuncionModel import Funcion
from .Model.CiudadModel import Ciudad
from .Model.AsientoModel import Asiento
from .Model.PrecioModel import Precio
from .Model.TipoPrecioModel import TipoPrecio
from .Model.UsuarioModel import Usuario
from .Model.TicketModel import Ticket
from .Model.CompraModel import Compra
from .connection_manager import SessionManager
from datetime import date, datetime

session = SessionManager.getInstance()


class EntityManager():
    def seed_database():
        # connection_engine.execute(f"INSERT INTO {DevConfig.DATABASE_SCHEMA}.pais (nombre) VALUES ('Argentina');")
        # Pais
        # BORRAR CUANDO SE ELIMINEN LAS ENTIDADES PARA TESTEAR
        pais = Pais(nombre = 'Argentina',codigo="AR")
        session.add(pais) # session.add(Pais(nombre = 'Argentina'))
        session.add(Pais(nombre = 'Uruguay',codigo="UY"))
        session.add(Pais(nombre = 'Estados Unidos',codigo="US"))
        session.add(Pais(nombre = 'Brasil',codigo="BR"))
        session.add(Pais(nombre = 'Chile',codigo="CL"))
        session.add(Pais(nombre = 'Italia',codigo="IT"))
        session.add(Pais(nombre = 'Francia',codigo="FR"))
        session.add(Pais(nombre = 'Belgica',codigo="BE"))
        session.add(Pais(nombre = 'Holanda',codigo="HO"))
        session.add(Pais(nombre = 'Alemania',codigo="AL"))
        # Ciudad
        ciudad = Ciudad(nombre = 'Rosario',pais = pais)
        session.add(ciudad)
        session.add(Ciudad(nombre = 'Buenos Aires',pais = pais))
        session.add(Ciudad(nombre = 'Cordoba',pais = pais))
        session.add(Ciudad(nombre = 'Santa Fe',pais = pais))
        # Complejo
        complejo=Complejo(nombre = 'Complejo Rosario Centro',ciudad = ciudad,gerente='GerenteNombre')
        session.add(complejo)
        session.add(Complejo(nombre = 'Complejo Cordoba',ciudad = Ciudad(nombre = 'Cordoba',pais = pais),gerente='Gerente Cordoba'))
        session.add(Complejo(nombre = 'Complejo Buenos Aires',ciudad = Ciudad(nombre = 'Buenos Aires',pais = pais), gerente='Gerente Buenos Aires'))

        # Audio
        espanol = Audio(nombre = 'Español')
        session.add(espanol)
        espanolLatino = Audio(nombre = 'Español Latino') # BORRAR CUANDO SE ELIMINEN LAS ENTIDADES PARA TESTEAR
        session.add(espanolLatino)
        # session.add(Audio(nombre = 'Español Latino'))
        ingles = Audio(nombre = 'Ingles') # BORRAR CUANDO SE ELIMINEN LAS ENTIDADES PARA TESTEAR
        session.add(ingles)
        # session.add(Audio(nombre = 'Ingles'))
        session.add(Audio(nombre = 'Ingles (Subtitulado)'))
        session.add(Audio(nombre = 'Frances'))
        session.add(Audio(nombre = 'Frances (Subtitulado)'))
        session.add(Audio(nombre = 'Italiano'))
        session.add(Audio(nombre = 'Italiano (Subtitulado)'))
        session.add(Audio(nombre = 'Portugues'))
        session.add(Audio(nombre = 'Portugues (Subtitulado)'))
        twoD   = TecnologiaProyeccion(nombre = '2D')
        threeD = TecnologiaProyeccion(nombre = '3D')
        session.add(twoD)
        session.add(threeD)
        formato = Formato(nombre = f'{twoD.nombre} {espanol.nombre}',audio = espanol , tecnologiaProyeccion = twoD) # BORRAR CUANDO SE ELIMINEN LAS ENTIDADES PARA TESTEAR
        # session.add(Formato(nombre = f'{twoD.nombre} {espanol.nombre}',audio = espanol , tecnologiaProyeccion = twoD))
        session.add(formato)
        asientos = [
                Asiento(columna=1,fila=1,nombre="A-1",adaptado=True),
                Asiento(columna=2,fila=1,nombre="A-2",adaptado=True),
                Asiento(columna=3,fila=1,nombre="A-3",adaptado=True),
                Asiento(columna=4,fila=1,nombre="A-4",adaptado=True),
                Asiento(columna=5,fila=1,nombre="A-5",adaptado=True),
                Asiento(columna=6,fila=1,nombre="A-6",adaptado=True),
                Asiento(columna=7,fila=1,nombre="A-7",adaptado=True),
                Asiento(columna=8,fila=1,nombre="A-8",adaptado=True),
                Asiento(columna=9,fila=1,nombre="A-9",adaptado=True),
                Asiento(columna=10,fila=1,nombre="A-10",adaptado=True),
                Asiento(columna=1,fila=2,nombre="B-1",adaptado=False),
                Asiento(columna=2,fila=2,nombre="B-2",adaptado=False),
                Asiento(columna=3,fila=2,nombre="B-3",adaptado=False),
                Asiento(columna=4,fila=2,nombre="B-4",adaptado=False),
                Asiento(columna=5,fila=2,nombre="B-5",adaptado=False),
                Asiento(columna=6,fila=2,nombre="B-6",adaptado=False),
                Asiento(columna=7,fila=2,nombre="B-7",adaptado=True),
                Asiento(columna=8,fila=2,nombre="B-8",adaptado=True),
                Asiento(columna=9,fila=2,nombre="B-9",adaptado=False),
                Asiento(columna=10,fila=2,nombre="B-10",adaptado=False),
                Asiento(columna=1,fila=3,nombre="C-1",adaptado=False),
                Asiento(columna=2,fila=3,nombre="C-2",adaptado=False),
                Asiento(columna=3,fila=3,nombre="C-3",adaptado=False),
                Asiento(columna=4,fila=3,nombre="C-4",adaptado=True),
                Asiento(columna=5,fila=3,nombre="C-5",adaptado=True),
                Asiento(columna=6,fila=3,nombre="C-6",adaptado=False),
                Asiento(columna=7,fila=3,nombre="C-7",adaptado=False),
                Asiento(columna=8,fila=3,nombre="C-8",adaptado=False),
                Asiento(columna=9,fila=3,nombre="C-9",adaptado=False),
                Asiento(columna=10,fila=3,nombre="C-10",adaptado=False),
                Asiento(columna=1,fila=4,nombre="D-1",adaptado=False),
                Asiento(columna=2,fila=4,nombre="D-2",adaptado=False),
                Asiento(columna=3,fila=4,nombre="D-3",adaptado=False),
                Asiento(columna=4,fila=4,nombre="D-4",adaptado=False),
                Asiento(columna=5,fila=4,nombre="D-5",adaptado=False),
                Asiento(columna=6,fila=4,nombre="D-6",adaptado=False),
                Asiento(columna=7,fila=4,nombre="D-7",adaptado=False),
                Asiento(columna=8,fila=4,nombre="D-8",adaptado=False),
                Asiento(columna=9,fila=4,nombre="D-9",adaptado=False),
                Asiento(columna=10,fila=4,nombre="D-10",adaptado=False),
                Asiento(columna=1,fila=5,nombre="E-1",adaptado=False),
                Asiento(columna=2,fila=5,nombre="E-2",adaptado=False),
                Asiento(columna=3,fila=5,nombre="E-3",adaptado=False),
                Asiento(columna=4,fila=5,nombre="E-4",adaptado=False),
                Asiento(columna=5,fila=5,nombre="E-5",adaptado=False),
                Asiento(columna=6,fila=5,nombre="E-6",adaptado=False),
                Asiento(columna=7,fila=5,nombre="E-7",adaptado=False),
                Asiento(columna=8,fila=5,nombre="E-8",adaptado=False),
                Asiento(columna=9,fila=5,nombre="E-9",adaptado=False),
                Asiento(columna=10,fila=5,nombre="E-10",adaptado=False)
                ]
        asientos2 = [
                Asiento(columna=1,fila=1,nombre="A-1",adaptado=True),
                Asiento(columna=2,fila=1,nombre="A-2",adaptado=True),
                Asiento(columna=3,fila=1,nombre="A-3",adaptado=True),
                Asiento(columna=4,fila=1,nombre="A-4",adaptado=True),
                Asiento(columna=5,fila=1,nombre="A-5",adaptado=True),
                Asiento(columna=6,fila=1,nombre="A-6",adaptado=True)
                ]
        # Sala
        sala=Sala(numero = 1,complejo = complejo,formatos=[formato],asientos=asientos)
        sala2=Sala(numero = 2,complejo = complejo,formatos=[formato],asientos=asientos2)
        session.add(sala)
        session.add(sala2)
        clasificacion = Clasificacion(identificador ='ATP' ,
                    edadMinima = 'Apto para todo el público',
                    recomendacion='Apto para todo el público',
                    definicion ='Todas las edades pueden ver. No hay desnudez ni sangre y/o alcohol. El lenguaje es cortés sin el uso de insultos o con ofensas muy suaves que caen en lo gracioso.' ) # BORRAR CUANDO SE ELIMINEN LAS ENTIDADES PARA TESTEAR
        # session.add(Clasificacion(identificador ='ATP' ,
        #             edadMinima = 'Apto para todo el público',
        #             recomendacion='Apto para todo el público',
        #             definicion ='Todas las edades pueden ver. No hay desnudez ni sangre y/o alcohol. El lenguaje es cortés sin el uso de insultos o con ofensas muy suaves que caen en lo gracioso.' ))
        session.add(Clasificacion(identificador ='+13' ,
                    edadMinima = '+13 años',
                    recomendacion='Apta para mayores de 13 años.',
                    definicion ='Desnudez fuerte y explícita —pero no pornográfica—, escenas fuertes, alcohol y drogas, insultos, imágenes muy intensas, muertes muy violentas y sangre en mucha cantidad —gore—. Se recomienda discreción para los menores de 16 años.' ))
        session.add(Clasificacion(identificador ='+16',
                            edadMinima = '+16 años',
                            recomendacion='Apta para mayores de 16 años.',
                            definicion ='Desnudez parcial, sangre leve, muertes poco violentas, lenguaje regularizado e imágenes intensas suelen aparecer en las películas de esta clasificación. Pueden ingresar menores si van acompañados por un familiar o tutor.' ))

        session.add(Clasificacion(identificador ='+18',
                            edadMinima = '+18 años',
                            recomendacion='Apta para mayores de 18 años.',
                            definicion ='Los menores de edad no están destinados a ver la película. Desnudez fuerte —pornografía—, violencia extrema, muertes extremadamente violentas, lenguaje ofensivo, derramamiento de sangre —gore extremo—, imágenes intensas frecuentes, escenas intensamente fuertes, insultos intensos y alcohol, drogas y tabaco.' ))

        session.add(Clasificacion(identificador ='C',
                            edadMinima = '+18 años',
                            recomendacion='Exhibición condicionada.',
                            definicion ='Adecuado para mayores de 18 años. Restringido a lugares especialmente autorizados. Los menores de edad no están destinados a ver la película. Los mayores de edad tampoco están destinados a ver esto en cines autorizados.' ))

        genero = Genero(nombre='Comedia')
        session.add(Genero(nombre='Acción'))
        session.add(Genero(nombre='Aventuras'))
        session.add(Genero(nombre='Ciencia Ficción'))
        session.add(Genero(nombre='Comedia.'))
        session.add(Genero(nombre='No-Ficción / documental'))
        session.add(Genero(nombre='Drama'))
        session.add(Genero(nombre='Fantasía'))
        session.add(Genero(nombre='Musical'))
        session.add(Genero(nombre='Terror'))
        session.add(Genero(nombre='Suspenso'))
        session.add(genero)
        # session.add(Genero(nombre='comedia')) BORRAR CUANDO SE ELIMINEN LAS ENTIDADES PARA TESTEAR
        pelicula = Pelicula(
            tituloOriginal = 'Original',
            tituloPais = 'Pais',
            fechaEstreno = date.today(),
            duracion=108,
            sinopsis='sinopsis',
            formatos = [formato],
            clasificacion = clasificacion,
            genero = genero,
            pais = pais )
        session.add(pelicula)

        funcion = Funcion(nombre="TEST Nombre Funcion",pelicula=pelicula,sala=sala,formato=formato,fechaInicio=datetime.now().date(),horaInicio=datetime.now().time())
        session.add(funcion)
        adulto = TipoPrecio(nombre="Adulto",codigo="ADULTO")
        nino =TipoPrecio(nombre="Niños",codigo="NINO")
        jubi =TipoPrecio(nombre="Jubilado",codigo="JUBILADO")

        session.add(Precio(nombre="A",codigo="A",valor=150,tipoPrecio=nino,activo=True))
        session.add(Precio(nombre="B",codigo="B",valor=300,tipoPrecio=adulto,activo=True))
        session.add(Precio(nombre="C",codigo="C",valor=200,tipoPrecio=jubi,activo=True))
        session.add(Compra(email="asdas@asdasd.com",funcion=funcion))
        session.commit()