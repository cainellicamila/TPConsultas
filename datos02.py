from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Datos.datos01 import Base, Consulta
from sqlalchemy import func

class DatosConsulta(object):

    def __init__(self):
        engine = create_engine('sqlite:///Consulta.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        self.session = DBSession()
        Base.metadata.create_all(engine)

    def alta(self, con):
        try:
            self.session.add(con)
            self.session.commit()
            print('True')

        except:
            print('False')


    def cant_elecc(self, elecc):

        cant=self.session.query(Consulta).filter(Consulta.eleccion==elecc).all()

        return cant

    def todos(self):
        ps= self.session.query(Consulta).all()
        return ps

    def borrar_todos(self):
        try:
            per=self.session.query(Consulta).all()
            for s in per:
                self.session.delete(s)
            self.session.commit()
            return True

        except:
            return False


    def histograma(self, elecc):
        try:
            consultas = self.session.query(func.count(Consulta.eleccion), Consulta.eleccion, func.date(Consulta.hora)).group_by(func.date(Consulta.hora)).filter(Consulta.eleccion==elecc).all()
            return consultas
        except:
            return None
