from config import DevConfig
from .Model.PaisModel import Pais
from .Model.AudioModel import Audio
from .Model.TecnologiaProyeccionModel import TecnologiaProyeccion
from .Model.ClasificacionModel import Clasificacion
from .Model.FormatoModel import Formato
from .connection_manager import SessionManager

session = SessionManager.getInstance()


class EntityManager():
    def seed_database():
        # connection_engine.execute(f"INSERT INTO {DevConfig.DATABASE_SCHEMA}.pais (nombre) VALUES ('Argentina');")
        # Pais
        session.add(Pais(nombre = 'Argentina'))
        session.add(Pais(nombre = 'Uruguay'))
        # Pais
        # Audio
        espanol = Audio(nombre = 'Español')
        session.add(espanol)
        espanolLatino = Audio(nombre = 'Español Latino')
        session.add(espanolLatino)
        ingles = Audio(nombre = 'Ingles')
        session.add(ingles)
        session.add(Audio(nombre = 'Ingles (Subtitulado)'))
        session.add(Audio(nombre = 'Frances'))
        session.add(Audio(nombre = 'Frances (Subtitulado)'))
        twoD   = TecnologiaProyeccion(nombre = '2D')
        threeD = TecnologiaProyeccion(nombre = '3D')
        session.add(twoD)
        session.add(threeD)
        session.add(Formato(nombre = f'{twoD.nombre} {espanol.nombre}',audio = espanol , tecnologiaProyeccion = twoD))
        session.add(Clasificacion(identificador ='ATP' ,
                    edadMinima = 'Apto para todo el público',
                    recomendacion='Apto para todo el público',
                    definicion ='Todas las edades pueden ver. No hay desnudez ni sangre y/o alcohol. El lenguaje es cortés sin el uso de insultos o con ofensas muy suaves que caen en lo gracioso.' ))
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

        # Audio
        session.commit()