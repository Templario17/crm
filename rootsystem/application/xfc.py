#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ

# URL = <protocolo>://<host>/<uri>
# URI: /<modulo>/<recurso>
# Recurso = función del controlador de un módulo
# /producto/agregar

uri = environ['REQUEST_URI'].split('/')
modulo = uri[1]
recurso = uri[2]
controlador = "{}Controller".format(modulo.title())

m = __import__("modules.{}".format(modulo), fromlist=[controlador])
c = getattr(m, controlador)()
getattr(c, recurso)()

