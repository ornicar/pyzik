#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore

class translators():

    def __init__(self,app):
        self.app = app
        self.installedTranslators = []



    def installTranslator(self,filename,locale):
        translator = QtCore.QTranslator(self.app)
        translator.load('{0}_{1}.qm'.format(filename,locale))
        self.installedTranslators.append(translator)
        self.app.installTranslator(translator)


    def unInstallTranslators(self):
        for translator in self.installedTranslators:
            self.app.removeTranslator(translator)
        self.installedTranslators = []


    def installTranslators(self,locale):
        self.installTranslator("pyzik",locale)
        self.installTranslator("playlistWidget",locale)