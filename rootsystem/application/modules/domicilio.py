from cgi import FieldStorage
from string import Template
from os import environ
import re

from core.db import DBQuery
from core.collector import Collector


class Domicilio(object):

    def __init__(self):
        self.domicilio_id = ""
        self.numero = ""
        self.puerta = ""
        self.calle = ""
        self.piso = 0
        self.ciudad = ""
        self.cp = ""

    def insert(self):
        sql = """
            INSERT INTO domicilio
            (numero, puerta, calle, piso, ciudad, cp)
            VALUES
            ("{}", "{}", "{}", {}, "{}", "{}")
        """.format(self.numero, self.puerta, self.calle, self.piso, self.ciudad, self.cp)
        self.domicilio_id = DBQuery().execute(sql)

    def update(self):
        sql = """
            UPDATE domicilio
            SET numero = "{}",
                puerta = "{}",
                calle = "{}",
                piso = {},
                ciudad = "{}",
                cp = "{}"
            WHERE domicilio_id ={}
        """.format(self.numero, self.puerta, self.calle, self.piso, self.ciudad, self.cp, self.domicilio_id)
        DBQuery().execute(sql)

    def select(self):
        sql = """
            SELECT numero , puerta, calle, piso, ciudad, cp
            FROM   domicilio
            WHERE  domicilio_id = {}
        """.format(self.domicilio_id)
        resultado = DBQuery().execute(sql)[0]
        self.numero = resultado[0]
        self.puerta = resultado[1]
        self.calle = resultado[2]
        self.piso = resultado[3]
        self.ciudad = resultado[4]
        self.cp = resultado[5]

    def delete(self):
        sql = """
              DELETE FROM domicilio
              WHERE domicilio_id = {}
        """.format(self.domicilio_id)
        DBQuery().execute(sql)

class DomicilioView(object):

    def agregar(self):
        with open("/home/debian/server/crm/rootsystem/static/form_2.html") as f:
            formulario = f.read()
        print "content-type: text/html; charset=utf-8"
        print ""
        print formulario

    def guardar(self):
        print "content-type: text/html; charset=utf-8"
        print ""
        print "Domicilio Guardado"

    def ver(self, objeto):
        diccionario = vars(objeto)
        with open("/home/debian/server/crm/rootsystem/static/ver_domicilio.html") as f:
            html = f.read()
        render = Template(html).safe_substitute(diccionario)
        print "content-type: text/html; charset=utf-8"
        print ""
        print render

    def editar(self, objeto):
        diccionario = vars(objeto)
        with open("/home/debian/server/crm/rootsystem/static/editar_domicilio.html") as f:
            html = f.read()
        render = Template(html).safe_substitute(diccionario)
        print "content-type: text/html; charset=utf-8"
        print ""
        print render

    def eliminar(self):
        with open("/home/debian/server/crm/rootsystem/static/eliminar_domicilio.html") as f:
            html = f.read()
        print "content-type: text/html; charset=utf-8"
        print ""
        print html

    def listar(self, coleccion):
        with open("/home/debian/server/crm/rootsystem/static/listar_domicilio.html", "r") as f:
            html = f.read()
        regex = re.compile("<!--fila-->(.|\n){1,}<--fila-->")
        bloque = regex.search(html).group(0)
        render = ''
        for objeto in coleccion:
            dicc = vars(objeto)
            render += Template(bloque).safe_substitute(dicc)
        render_final = html.replace(bloque, render)
        print "Content-type: text/html; charset=utf-8"
        print ""
        print render_final



class DomicilioController(object):

    def __init__(self):
        self.model = Domicilio()
        self.view = DomicilioView()

    def agregar(self):
        self.view.agregar()

    def guardar(self):
        form = FieldStorage()
        numero = form['numero'].value
        puerta = form['puerta'].value
        calle = form['calle'].value
        piso = form['piso'].value
        ciudad = form['ciudad'].value
        cp = form['cp'].value

        self.model.numero = numero
        self.model.puerta = puerta
        self.model.calle = calle
        self.model.piso = piso
        self.model.ciudad = ciudad
        self.model.cp = cp

        self.model.insert()
        self.view.guardar()

    def ver(self):
        obj_id = int(environ['REQUEST_URI'].split("/")[-1])
        self.model.domicilio_id = obj_id
        self.model.select()
        self.view.ver(self.model)

    def editar(self):
        obj_id = int(environ['REQUEST_URI'].split('/')[-1])
        self.model.domicilio_id = obj_id
        self.model.select()
        self.view.editar(self.model)

    def actualizar(self):
        form = FieldStorage()
        domicilio_id = form["domicilio_id"].value
        numero = form["numero"].value
        puerta = form["puerta"].value
        calle = form["calle"].value
        piso = form["piso"].value
        ciudad = form["ciudad"].value
        cp = form["ciudad"].value

        self.model.domicilio_id = domicilio_id
        self.model.numero = numero
        self.model.puerta = puerta
        self.model.calle = calle
        self.model.piso = piso
        self.model.ciudad = ciudad
        self.model.cp = cp

        self.model.update()
        self.view.ver(self.model)

    def eliminar(self):
        obj_id = int(environ['REQUEST_URI'].split('/')[-1])
        self.model.domicilio_id = obj_id
        self.model.delete()
        self.view.eliminar()

    def listar(self):
        obj = Collector()
        obj.get("Domicilio")

        self.view.listar(obj.coleccion)


class DomicilioHelper(object):
    pass
