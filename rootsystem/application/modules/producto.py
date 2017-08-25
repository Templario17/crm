from cgi import FieldStorage

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
        pass

    def select(self):
        pass

    def delete(self):
        pass


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


class ProductoHelper(object):
    pass
