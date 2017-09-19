from core.db import DBQuery

class Collector(object):

    def __init__(self):
        self.coleccion = []

    def get(self, clase):
        cls_lower = clase.lower()
        sql = "SELECT {cls}_id FROM {cls}".format(cls=cls_lower)
        resultados = DBQuery().execute(sql)

        exec "from modules.{} import {}".format(cls_lower, clase)

        for tupla in resultados:
            exec "obj = {}()".format(clase)
            exec "obj.{}_id = tupla[0]".format(cls_lower)
            obj.select()
            self.coleccion.append(obj)
            
