from cgi import FieldStorage
from string import Template
from os import environ

from core.db import DBQuery


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
                  WHERE {}
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
        self.view.guardar()

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
        self.view.editar(self.model)

    def eliminar(self):
        obj_id = int(environ['REQUEST_URI'].split('/')[-1])
        self.model.producto_id = obj_id
        self.model.delete()
        self.view.eliminar()


class ProductoHelper(object):
    pass
