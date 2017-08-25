from cgi import FieldStorage

from core.db import DBQuery


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
            (numero, puerta, calle, piso, cuidad, cp)
            VALUES
            ("{}", "{}", "{}", {}, "{}", "{}")
        """.format(self.numero, self.puerta, self.calle, self.piso, self.ciudad, self.cp)
        self.domicilio_id = DBQuery().execute(sql)

    def update(self):
        pass

    def select(self):
        pass

    def delete(self):
        pass

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

class DomicilioHelper(object):
    pass
