#-*- coding:utf-8 -*-

from cgi import FieldStorage
from string import Template
from os import environ
from string import Template
import re

from core.db import DBQuery
from core.collector import Collector


class DatoDeContacto(object):

    def __init__(self):
        self.datodecontacto_id = 0
        self.denominacion = ""
        self.valor = ""

    def insert(self):
        sql = """
            INSERT INTO datodecontacto (denominacion, valor)
            VALUES ("{}", "{}")
        """.format(self.denominacion, self.valor)
        self.datodecontacto_id = DBQuery().execute(sql)

    def update(self):
        sql = """
            UPDATE datodecontacto
            SET denominacion = "{}",
                valor = "{}"
            WHERE datodecontacto_id = {}
        """.format(self.denominacion, self.valor, self.datodecontacto_id)
        DBQuery().execute(sql)

    def select(self):
        sql = """
            SELECT denominacion, valor
            FROM datodecontacto
            WHERE datodecontacto_id = {}
        """.format(self.datodecontacto_id)
        resultado = DBQuery().execute(sql)[0]
        self.denominacion = resultado[0]
        self.valor = resultado[1]

    def delete(self):
        sql = """
            DELETE FROM datodecontacto WHERE datodecontacto_id = {}
        """.format(self.datodecontacto_id)
        DBQuery().execute(sql)

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


    def ver(self, objeto):
        dicc = vars(objeto)
        with open("/home/debian/server/crm/rootsystem/static/ver_datodecontacto.html", "r") as f:
            html = f.read()
        render = Template(html).safe_substitute(dicc)
        print "Content-type: text/html; charset=utf-8"
        print ""
        print render

    def editar(self, objeto):
        diccionario = vars(objeto)
        with open("/home/debian/server/crm/rootsystem/static/editar_datodecontacto.html", "r") as f:
            html = f.read()
        render = Template(html).safe_substitute(diccionario)
        print "Content-type: text/html; charset=utf-8"
        print ""
        print render


    def eliminar(self):
        print "content-type: text/html; charset=utf-8"
        print ""
        print "dato elimindo de la base de datos "

    def listar(self, coleccion):
        with open("/home/debian/server/crm/rootsystem/static/listar_datodecontacto.html", "r") as f:
            html = f.read()
        regex = re.compile("<!--fila-->(.|\n){1,}<!--fila-->")
        bloque = regex.search(html).group(0)
        render = ''
        for objeto in coleccion:
            dicc = vars(objeto)
            render += Template(bloque).safe_substitute(dicc)
        render_final = html.replace(bloque, render)
        print "content-type: text/html; charset=utf-8"
        print ""
        print render_final



class DatodecontactoController(object):

    def __init__(self):
        self.model = DatoDeContacto()
        self.view = DatoDeContactoView()

    def agregar(self):
        self.view.agregar()

    def guardar(self):
        form = FieldStorage()
        denominacion = form["denominacion"].value
        valor = form["valor"].value

        self.model.denominacion = denominacion
        self.model.valor = valor

        self.model.insert()
        self.redirect()


    def ver(self):
        obj_id = int(environ['REQUEST_URI'].split('/')[-1])
        self.model.datodecontacto_id = obj_id
        self.model.select()
        self.view.ver(self.model)

    def editar(self):
        p_id = int(environ['REQUEST_URI'].split('/')[-1])
        self.model.datodecontacto_id = p_id
        self.model.select()
        self.view.editar(self.model)
        

    def actualizar(self):
        form = FieldStorage()
        propiedad_id = form["datodecontacto_id"].value
        denominacion = form["denominacion"].value
        valor = form["valor"].value

        self.model.datodecontacto_id = propiedad_id
        self.model.denominacion = denominacion
        self.model.valor = valor

        self.model.update()
        self.redirect()


    def eliminar(self):
        obj_id = int(environ["REQUEST_URI"].split("/")[-1])
        self.model.datodecontacto_id = obj_id

        self.model.delete()
        self.redirect()
        

    def listar(self):
        obj = Collector()
        obj.get("DatoDeContacto")
        self.view.listar(obj.coleccion)
    
    def redirect(self):
        print "Content-type: text/html; charset=utf-8"
        print "Location: http://crm.local/datodecontacto/listar"
        print ""


class DatoDeContactoHelper(object):
    pass
