from cgi import FieldStorage
from string import Template
from os import environ
import re

from core.db import DBQuery
from core.collector import Collector


class Producto(object):

    def __init__(self):
        self.producto_id = 0
        self.denominacion = ''
        self.precio = 0.0

    def insert(self):
        sql = """
            INSERT INTO producto
            (denominacion, precio)
            VALUES
            ('{}', {})
        """.format(self.denominacion, self.precio)
        self.producto_id = DBQuery().execute(sql)

    def update(self):
        sql = """
            UPDATE producto
            SET denominacion = '{}',
                precio = {}
            WHERE producto_id = {}
        """.format(self.denominacion, self.precio, self.producto_id)
        DBQuery().execute(sql)

    def select(self):
        sql = """
              SELECT denominacion, precio
              FROM producto
              WHERE producto_id = {}
        """.format(self.producto_id)
        resultado = DBQuery().execute(sql)[0]
        self.denominacion = resultado[0]
        self.precio = resultado[1]


    def delete(self):
        sql = """ DELETE FROM producto
                  WHERE producto_id = {}
        """.format(self.producto_id)
        DBQuery().execute(sql)


class ProductoView(object):

    def agregar(self):
        with open("/home/debian/server/crm/rootsystem/static/form.html", "r") as f:
            contenido = f.read()
        print "Content-type: text/html; charset=utf-8;"
        print ""
        print contenido

    def guardar(self):
        print "Content-type: text/html; charset=utf-8"
        print ""
        print "Producto Guardado"

    def ver(self, objeto):
        diccionario = vars(objeto)
        with open("/home/debian/server/crm/rootsystem/static/ver_producto.html")as f:
            html = f.read()
        render = Template(html).safe_substitute(diccionario)
        print "content-type: text/html; charset=utf-8"
        print ""
        print render

    def editar(self, objeto):
        diccionario = vars(objeto)
        with open("/home/debian/server/crm/rootsystem/static/editar_producto.html", "r") as f:
            html = f.read()
        render = Template(html).safe_substitute(diccionario)
        print "content-type: text/html; charset=utf-8"
        print ""
        print render

    def eliminar(self):
        with open("/home/debian/server/crm/rootsystem/static/eliminar_producto.html", "r") as f:
            html = f.read()
        print "Content-type: text/html; charset=utf-8"
        print ""
        print html

    def listar(self, coleccion):
        with open("/home/debian/server/crm/rootsystem/static/listar_producto.html") as f:
            html = f.read()
        regex = re.compile("<!--fila-->(.|\n){1,}<!--fila-->")
        bloque = regex.search(html).group(0)
        render = ''
        for objeto in coleccion:
            diccionario = vars(objeto)
            render += Template(bloque).safe_substitute(diccionario)
        render_final = html.replace(bloque, render)
        print "content-type: text/html; charset=utf-8"
        print ""
        print render_final

class ProductoController(object):

    def __init__(self):
        self.model = Producto()
        self.view = ProductoView()

    def agregar(self):
        self.view.agregar()

    def guardar(self):
        form = FieldStorage()
        denominacion = form['denominacion'].value
        precio = form['precio'].value

        self.model.denominacion = denominacion
        self.model.precio = precio

        self.model.insert()
        self.redirect()

    def ver(self):
        obj_id = int(environ['REQUEST_URI'].split('/')[-1])
        self.model.producto_id = obj_id
        self.model.select()
        self.view.ver(self.model)

    def editar(self):
        pid = int(environ['REQUEST_URI'].split('/')[-1])
        self.model.producto_id = pid
        self.model.select()
        self.view.editar(self.model)

    def actualizar(self):
        form = FieldStorage()
        producto_id = form["producto_id"].value
        denominacion = form["denominacion"].value
        precio = form["precio"].value

        self.model.producto_id = producto_id
        self.model.denominacion = denominacion
        self.model.precio = precio

        self.model.update()
        self.redirect()

    def eliminar(self):
        obj_id = int(environ['REQUEST_URI'].split('/')[-1])
        self.model.producto_id = obj_id
        self.model.delete()
        self.view.eliminar()
        self.redirect()

    def listar(self):
        obj = Collector()
        obj.get("Producto")
        self.view.listar(obj.coleccion)

    def redirect(self):
        print "Content-type: text/html; charset=utf-8"
        print "Location: http://crm.local/producto/listar"
        print ""


class ProductoHelper(object):
    pass
