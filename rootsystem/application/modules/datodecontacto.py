from cgi import FieldStorage
from string import Template
from os import environ

from core.db import DBQuery


class DatoDeContacto(object):

    def __init__(self):
        self.datodecontacto_id = ""
        self.nombre = ""
        self.mail = ""
        self.telefono = ""

    def insert(self):
        sql = """
            INSERT INTO datodecontacto (nombre, mail, telefono)
            VALUES ("{}", "{}", "{}")
        """.format(self.nombre, self.mail, self.telefono)
        self.datodecontacto_id = DBQuery().execute(sql)

    def update(self):
        pass

    def select(self):
        pass

    def delete(self):
        pass

class DatoDeContactoView(object):

    def agregar(self):
        with open("/home/debian/server/crm/rootsystem/static/agregar_datodecontacto.html", "r") as f:
            formulario = f.read()
        print "Content-type: text/html; charset=utf-8"
        print ""
        print formulario

    def guardar(self):
        print "Content-type: text/html; charset=utf-8"
        print ""
        print "Datos de contacto han sido guardados en la base de datos"

    def ver(self):
        pass

    def editar(self):
        pass

    def eliminar(self):
        pass


class DatodecontactoController(object):

    def __init__(self):
        self.model = DatoDeContacto()
        self.view = DatoDeContactoView()

    def agregar(self):
        self.view.agregar()

    def guardar(self):
        form = FieldStorage()
        nombre = form['nombre'].value
        mail = form['mail'].value
        telefono = form['telefono'].value

        self.model.nombre = nombre
        self.model.mail = mail
        self.model.telefono = telefono

        self.model.insert()
        self.view.guardar()

class DatoDeContactoHelper(object):
    pass
