# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telas/tela_cadastro_livro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Cadastro_Livro(object):
    def setupUi(self, Tela_Cadastro_Livro):
        Tela_Cadastro_Livro.setObjectName("Tela_Cadastro_Livro")
        Tela_Cadastro_Livro.resize(926, 547)
        Tela_Cadastro_Livro.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(Tela_Cadastro_Livro)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 152, 291, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(290, 183, 291, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.botao_salvar_livro = QtWidgets.QPushButton(self.centralwidget)
        self.botao_salvar_livro.setGeometry(QtCore.QRect(700, 340, 101, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/save_file_disk_open_searsh_loading_clipboard_1513.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_salvar_livro.setIcon(icon)
        self.botao_salvar_livro.setObjectName("botao_salvar_livro")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 218, 291, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.autor = QtWidgets.QLineEdit(self.centralwidget)
        self.autor.setGeometry(QtCore.QRect(290, 249, 291, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.autor.setFont(font)
        self.autor.setObjectName("autor")
        self.qtd_pag = QtWidgets.QLineEdit(self.centralwidget)
        self.qtd_pag.setGeometry(QtCore.QRect(615, 182, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.qtd_pag.setFont(font)
        self.qtd_pag.setObjectName("qtd_pag")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(615, 217, 169, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ano_publi = QtWidgets.QLineEdit(self.centralwidget)
        self.ano_publi.setGeometry(QtCore.QRect(615, 248, 188, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ano_publi.setFont(font)
        self.ano_publi.setObjectName("ano_publi")
        self.botao_selecionar_img = QtWidgets.QPushButton(self.centralwidget)
        self.botao_selecionar_img.setGeometry(QtCore.QRect(100, 340, 181, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.botao_selecionar_img.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/imageup_imagen_12892.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_selecionar_img.setIcon(icon1)
        self.botao_selecionar_img.setObjectName("botao_selecionar_img")
        self.colocar_imagem = QtWidgets.QLabel(self.centralwidget)
        self.colocar_imagem.setGeometry(QtCore.QRect(110, 130, 161, 201))
        self.colocar_imagem.setText("")
        self.colocar_imagem.setObjectName("colocar_imagem")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-20, 0, 951, 531))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 150, 221, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(90, 110, 751, 321))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 130, 161, 201))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 290, 291, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.isbn = QtWidgets.QLineEdit(self.centralwidget)
        self.isbn.setGeometry(QtCore.QRect(290, 320, 291, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.isbn.setFont(font)
        self.isbn.setObjectName("isbn")
        self.buttonVoltar = QtWidgets.QToolButton(self.centralwidget)
        self.buttonVoltar.setGeometry(QtCore.QRect(90, 60, 41, 41))
        self.buttonVoltar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/back_12955.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonVoltar.setIcon(icon2)
        self.buttonVoltar.setIconSize(QtCore.QSize(28, 28))
        self.buttonVoltar.setObjectName("buttonVoltar")
        self.textBrowser.raise_()
        self.label_2.raise_()
        self.textBrowser_3.raise_()
        self.label_7.raise_()
        self.titulo.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.qtd_pag.raise_()
        self.autor.raise_()
        self.ano_publi.raise_()
        self.botao_salvar_livro.raise_()
        self.botao_selecionar_img.raise_()
        self.textBrowser_2.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.isbn.raise_()
        self.colocar_imagem.raise_()
        self.buttonVoltar.raise_()
        Tela_Cadastro_Livro.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Cadastro_Livro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 22))
        self.menubar.setObjectName("menubar")
        Tela_Cadastro_Livro.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Cadastro_Livro)
        self.statusbar.setObjectName("statusbar")
        Tela_Cadastro_Livro.setStatusBar(self.statusbar)
        self.actionMOSTRAR_LIVROS_CADASTRADOS = QtWidgets.QAction(Tela_Cadastro_Livro)
        self.actionMOSTRAR_LIVROS_CADASTRADOS.setObjectName("actionMOSTRAR_LIVROS_CADASTRADOS")
        self.actionBUSCAR = QtWidgets.QAction(Tela_Cadastro_Livro)
        self.actionBUSCAR.setObjectName("actionBUSCAR")
        self.actionEDITAR = QtWidgets.QAction(Tela_Cadastro_Livro)
        self.actionEDITAR.setObjectName("actionEDITAR")
        self.actionLISTAR = QtWidgets.QAction(Tela_Cadastro_Livro)
        self.actionLISTAR.setObjectName("actionLISTAR")

        self.retranslateUi(Tela_Cadastro_Livro)
        QtCore.QMetaObject.connectSlotsByName(Tela_Cadastro_Livro)

    def retranslateUi(self, Tela_Cadastro_Livro):
        _translate = QtCore.QCoreApplication.translate
        Tela_Cadastro_Livro.setWindowTitle(_translate("Tela_Cadastro_Livro", "MainWindow"))
        self.label.setText(_translate("Tela_Cadastro_Livro", "Título:"))
        self.label_2.setText(_translate("Tela_Cadastro_Livro", "Dados do livro"))
        self.botao_salvar_livro.setText(_translate("Tela_Cadastro_Livro", "SALVAR"))
        self.label_3.setText(_translate("Tela_Cadastro_Livro", "Autor: "))
        self.label_5.setText(_translate("Tela_Cadastro_Livro", "Ano de publicação:"))
        self.botao_selecionar_img.setText(_translate("Tela_Cadastro_Livro", "SELECIONAR IMAGEM"))
        self.label_7.setText(_translate("Tela_Cadastro_Livro", "Quantidade de páginas:"))
        self.label_4.setText(_translate("Tela_Cadastro_Livro", "ISBN: "))
        self.actionMOSTRAR_LIVROS_CADASTRADOS.setText(_translate("Tela_Cadastro_Livro", "MOSTRAR LIVROS CADASTRADOS"))
        self.actionBUSCAR.setText(_translate("Tela_Cadastro_Livro", "BUSCAR"))
        self.actionEDITAR.setText(_translate("Tela_Cadastro_Livro", "EDITAR"))
        self.actionLISTAR.setText(_translate("Tela_Cadastro_Livro", "LISTAR LIVROS CADASTRADOS"))
