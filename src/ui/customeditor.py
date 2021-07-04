# -*- coding:utf-8 -*-
"""editor for custom widget preview panel
"""
import os
import sys
from os import path
from importlib import import_module, reload
from CodeEditor import Editor
from PyQt5.Qsci import QsciLexer, QsciLexerPython
from PyQt5.QtWidgets import QMessageBox, QWidget
from data import cache


class SrcEditor(Editor):
    def __init__(self):
        super().__init__()
        self.dir = path.join(path.dirname(__file__),"../data/custompreview")
        self.file=path.join(self.dir,"__init__.py")
        self.cachedir = path.join(self.dir,"../cache")
        self.cachefile = path.join(self.cachedir,"custom.py")
        self.setLexer(QsciLexerPython(self))
        self.load(self.file)
        self.custom = None

    def preview(self):
        with open(self.cachefile, 'w', newline='') as file:
            # 不指定newline，则换行符为各系统默认的换行符（\n, \r, or \r\n, ）
            # newline=''表示不转换
            pretext="""# -*- coding: utf-8 -*-
\"""Qss preview for Custom QtWidgets\"""

import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
"""
            file.write(pretext)
            file.write(self.text())

        dir1 = os.getcwd()
        try:
            os.chdir(self.dir)
            self.custom = import_module(".cache.custom", "data")
            reload(self.custom)
            #sys.modules.pop("data.cache.custom")
            #self.custom = import_module(".custom", "data.cache")
            if (hasattr(self.custom, "MainWindow")):
                self.w = self.custom.MainWindow()
                self.w.setMinimumSize(400,280)
                self.w.show()
            else:
                raise
            #w.raise_()
        except Exception:
            #del self.custom
            #del self.w
            QMessageBox.information(self, "Error", self.tr("Preview error, please check the code."),
                                    QMessageBox.Ok, QMessageBox.Ok)
        finally:
            os.chdir(dir1)