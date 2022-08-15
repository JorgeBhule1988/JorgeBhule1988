from tkinter import *
from tkinter import ttk
from formularios_punto_de_venta.repositorio_conexion import RepositorioConexionSQLite
from formularios_punto_de_venta.botones.botones_menus.botonesmenu_ron import BonotonesMenuRon
from formularios_punto_de_venta.botones.botones_menus.botonesmenu_comida import BonotonesMenuComida
from formularios_punto_de_venta.botones.botones_menus.botones_bebidas_no_alcohol import BotonesBebidas
from formularios_punto_de_venta.botones.botones_menus.botones_cerveza import BotonesCervezas
from formularios_punto_de_venta.botones.botones_menus.botones_cockteleria import BotonesCockteleria
from formularios_punto_de_venta.botones.botones_menus.botones_vino_tinto import BotonesVinoTinto
from formularios_punto_de_venta.botones.botones_menus.botones_vino_blanco import BotonesVinoBlanco
from formularios_punto_de_venta.botones.botones_menus.botones_vino_rosado import BotonesVinoRosado
from formularios_punto_de_venta.botones.botones_menus.botones_vodka import BotonesVodka
from formularios_punto_de_venta.botones.botones_menus.botones_whisky import BotonesWhisky
from formularios_punto_de_venta.botones.botones_menus.botones_mezcal import BotonesMezcal
from formularios_punto_de_venta.botones.botones_menus.botones_dijestivos import BotonesDojestivos
#from formularios_punto_de_venta.botones.botones_menus.botones_mesas import BotonesMesas
import mysql.connector

class BonotonesMenu(RepositorioConexionSQLite):

    def botonrodizio(self):

        BonotonesMenuComida.rodizio(self)


    def rodizio20descuento(self):

        BonotonesMenuComida.rodizio20(self)

        
    def botonrodiziol(self):

        BonotonesMenuComida.rodiziolocal(self)


    def botonrodiziom(self):
        
        BonotonesMenuComida.rodiziomenor(self)


    def botonrodizioml(self):

        BonotonesMenuComida.rodiziolocalmenor(self)


    def botonrodiziotg(self):

        BonotonesMenuComida.rodiziotogo(self)

    def botonpicana(self):

        BonotonesMenuComida.picana(self)


    def botonpicanatg(self):

        BonotonesMenuComida.picanatogo(self)


    def botontomahack(self):

        BonotonesMenuComida.tomahack(self)


    def botonburguer(self):

        BonotonesMenuComida.burguerpicana(self)
    

    def rodiziopassport(self):
        
        BonotonesMenuComida.rodipass(self)


    def rodiziocortesia(self):
        
        BonotonesMenuComida.rodicorte(self)


    def botonburguertg(self):

        BonotonesMenuComida.burguerpicatogo(self)


    def botagua(self):
        
        BotonesBebidas.botaguanat(self)


    def botonaguap(self):

        BotonesBebidas.agua(self)


    def botontopoc(self):

        BotonesBebidas.topochico(self)

    def botonlimonada(self):

        BotonesBebidas.limonada(self)

    def botonnaranjada(self):

        BotonesBebidas.naranjada(self)

    def botoncoca(self):

        BotonesBebidas.cocacola(self)
    
    def botoncocad(self):

        BotonesBebidas.cocaligth(self)
        
    def botonsprite(self):

        BotonesBebidas.sprite(self)

    def botonfresca(self):

        BotonesBebidas.fresca(self)


    def botonmundet(self):

        BotonesBebidas.mundet(self)


    def botonpinada(self):

        BotonesBebidas.pinada(self)


    def botonmojitov(self):

        BotonesBebidas.mojitov(self)

    
    def botonpituv(self):

        BotonesBebidas.pituv(self)


    def botonpacifico(self):

        BotonesCervezas.pacifico(self)

    
    def botonultra(self):

        BotonesCervezas.ultra(self)


    def botonpacificol(self):

        BotonesCervezas.pacificol(self)
    

    def botoncorona(self):

        BotonesCervezas.corona(self)

    
    def botonvictoria(self):

        BotonesCervezas.victoria(self)

    
    def botonartesanal(self):

        BotonesCervezas.artesanal(self)

    
    def botonegramodelo(self):

        BotonesCervezas.negramodelo(self)

    
    def botonmojito(self):

        BotonesCockteleria.mojito(self)


    def botonmezcalitaj(self):

        BotonesCockteleria.mezcalitaj(self)
    

    def botonmezcalitam(self):

        BotonesCockteleria.mezcalitam(self)


    def botoncaipirina(self):
        
        BotonesCockteleria.caipirina(self)
        
    
    def mojitotinto(self):
        
        BotonesCockteleria.mojitotinto1(self)


    def mojitosabores(self):

        BotonesCockteleria.mojitosabores1(self)


    def guanabanagin(self):

        BotonesCockteleria.guanabanagin1(self)


    def martinicoffe(self):
        
        BotonesCockteleria.martinicoffe1(self)

    
    def margaritarodizio(self):
        
        BotonesCockteleria.margaritarodizio1(self)

    
    def margaritamango(self):
        
        BotonesCockteleria.margaritamango1(self)


    def margaritaguanabana(self):

        BotonesCockteleria.margaritaguanabana1(self)

        
    def margaritamaracuya(self):
        
        BotonesCockteleria.margaritamaracuya1(self)

    
    def margaritatradicional(self):
        
        BotonesCockteleria.margaritatradicional1(self)

    
    def margaritacadillac(self):
        
        BotonesCockteleria.margaritacadillac1(self)

    
    def mezcalitatradicional(self):
        
        BotonesCockteleria.mezcalitatradicional1(self)


    def mezcalitamango(self):
        
        BotonesCockteleria.mezcalitamango1(self)

    
    def mezcalitamaracuya(self):
        
        BotonesCockteleria.mezcalitamaracuya1(self)

    
    def mezcalitaguanabana(self):
        
        BotonesCockteleria.mezcalitaguanabana1(self)


    def pitumango(self):
        
        BotonesCockteleria.pitumango1(self)


    def pitumaracuya(self):
        
        BotonesCockteleria.pitumaracuya1(self)


    def pituguanabana(self):
        
        BotonesCockteleria.pituguanabana1(self)
    

    def negroni(self):
        
        BotonesCockteleria.negroni1(self)

    
    def gintonic(self):
        
        BotonesCockteleria.gintonic1(self)

    
    def oldfashion(self):
        
        BotonesCockteleria.oldfashion1(self)


    def clericottinto(self):
        
        BotonesCockteleria.clericottinto1(self)

    
    def clericotrosado(self):
        
        BotonesCockteleria.clericotrosado1(self)

    
    def clericotblueberry(self):
        
        BotonesCockteleria.clericotblueberry1(self)

    
    def gavilan_reyes(self):
            
        BotonesCockteleria.gavilan_reyes1(self)

    
    def sangria(self):
        
        BotonesCockteleria.sangria1(self)

    
    def pina_colada(self):
        
        BotonesCockteleria.pina_colada1(self)


    def botoncopadevino(self):

        BotonesVinoTinto.copadevino(self)


    def bsanmartino(self):

        BotonesVinoTinto.bsanmartino1(self)


    def casamadero_3v(self):
        
        BotonesVinoTinto.casamadero_3v1(self)

    
    def casamadero(self):
        
        BotonesVinoTinto.casamadero1(self)
    

    def piccolo(self):
        
        BotonesVinoTinto.piccolo1(self)

    
    def criosblend(self):
        
        BotonesVinoTinto.criosblend1(self)
        

    def criosmalbec(self):
        
        BotonesVinoTinto.criosmalbec1(self)

    
    def crioscab(self):
        
        BotonesVinoTinto.crioscab1(self)

    
    def marcobonfante(self):
        
        BotonesVinoTinto.marcobonfante1(self)

    
    def neroavola(self):
        
        BotonesVinoTinto.neroavola1(self)
    

    def mongrasssyr(self):
        
        BotonesVinoTinto.mongrasssyr1(self)

    
    def mongrassblend(self):
        
        BotonesVinoTinto.mongrassblend1(self)

    
    def mongrasscab(self):

        BotonesVinoTinto.mongrasscab1(self)


    def decoy(self):
        
        BotonesVinoTinto.decoy1(self)

    
    def lomita(self):
        
        BotonesVinoTinto.lomita1(self)

    
    def castacardon(self):
        
        BotonesVinoTinto.castacardon1(self)

    
    def harasdepirque(self):
        
        BotonesVinoTinto.harasdepirque1(self)


    def harasgran(self):
        
        BotonesVinoTinto.harasgran1(self)

    
    def minimalista(self):
        
        BotonesVinoTinto.minimalista1(self)
    

    def domino(self):
        
        BotonesVinoTinto.domino1(self)

    
    def abbout(self):
        
        BotonesVinoTinto.abbout1(self)

    
    def bellaretta(self):
        
        BotonesVinoTinto.bellaretta1(self)


    def carlidge(self):
        
        BotonesVinoTinto.carlidge1(self)

    
    def gnarlyhead(self):
        
        BotonesVinoTinto.gnarlyhead1(self)

    
    def santacristina(self):
        
        BotonesVinoTinto.santacristina1(self)

    
    def colezionemolte(self):
        
        BotonesVinoTinto.colezionemolte1(self)
    

    def caracter(self):
        
        BotonesVinoTinto.caracter1(self)


    def tierraadentro(self):
        
        BotonesVinoTinto.tierraadentro1(self)


    def misassou(self):
        
        BotonesVinoTinto.misassou1(self)
    

    def kruguer(self):
        
        BotonesVinoTinto.kruguer1(self)

    
    def care(self):
        
        BotonesVinoTinto.care1(self)

    
    def cetto(self):
        
        BotonesVinoTinto.cetto1(self)

    
    def calycanto(self):
        
        BotonesVinoTinto.calycanto1(self)

    
    def cigliano(self):
        
        BotonesVinoTinto.cigliano1(self)


    def copablanco(self):
        
        BotonesVinoBlanco.copablanco1(self)


    def cavacordova(self):
       
       BotonesVinoBlanco.cavacordova1(self)
    

    def anniespecial(self):
        
        BotonesVinoBlanco.anniespecial1(self)

    
    def islanegra(self):
        
        BotonesVinoBlanco.islanegra1(self)
    

    def tantehue(self):
        
        BotonesVinoBlanco.tantehue1(self)

    
    def micheltorino(self):
        
        BotonesVinoBlanco.micheltorino1(self)
    

    def coparosado(self):
        
        BotonesVinoRosado.coparosado1(self)


    def bonina(self):
        
        BotonesVinoRosado.bonina1(self)

    
    def raza(self):
        
        BotonesVinoRosado.raza1(self)

    
    def porta(self):
        
        BotonesVinoRosado.porta1(self)

    
    def rincones(self):
        
        BotonesVinoRosado.rincones1(self)

    
    def espumosopaxx(self):
        
        BotonesVinoRosado.espumosopaxx1(self)

    
    def espumosopaxx_2(self):
        
        BotonesVinoRosado.espumosopaxx_2_1(self)


    def ronbaca(self):
        BonotonesMenuRon.ronbacardi(self)

    
    def ronbacaane(self):
        BonotonesMenuRon.ronbacardiane(self)


    def habanaclub(self):
        BonotonesMenuRon.ronhabana(self)

    
    def flor_cana(self):
        BonotonesMenuRon.ronflordecana(self)
    

    def malibu(self):
        BonotonesMenuRon.ronmalibu(self)

    
    def captain(self):
        BonotonesMenuRon.roncapitanmorgan(self)

    
    def zacapa(self):
        BonotonesMenuRon.ronzacapa(self)


    def titos(self):
        BotonesVodka.titos1(self)

    
    def adsolut(self):
        BotonesVodka.adsolut1(self)
    

    def citron(self):
        BotonesVodka.citron1(self)

    
    def pear(self):
        BotonesVodka.pear1(self)

    
    def mandarin(self):
        BotonesVodka.mandarin1(self)


    def ketelone(self):
        BotonesVodka.ketelone1(self)

    
    def greygoose(self):
        BotonesVodka.greygoose1(self)

    
    def smirnoff(self):
        BotonesVodka.smirnoff1(self)
    

    def crown(self):
        BotonesWhisky.crowroyal1(self)

    
    def red_label(self):
        BotonesWhisky.redlabel1(self)

    
    def black_label(self):
        BotonesWhisky.blacklabel1(self)

    
    def makers_mark(self):
        BotonesWhisky.makers1(self)

    
    def jack_daniel(self):
        BotonesWhisky.jack1(self)

    
    def jim_beam(self):
        BotonesWhisky.jimbeam1(self)


    def woodford(self):
        BotonesWhisky.woodford1(self)

    
    def macallan(self):
        BotonesWhisky.macallan1(self)

    
    def santori(self):
        BotonesWhisky.santori1(self)
    

    def cuatroconejos(self):
        BotonesMezcal.cuatroconejo1(self)


    def buensuceso(self):
        BotonesMezcal.buensuceso1(self)

    
    def aleron(self):
        BotonesMezcal.aleron1(self)

    
    def mitre(self):
        BotonesMezcal.mitre1(self)
    

    def casamezcal(self):
        BotonesMezcal.mezcalcasa1(self)


    def kalua(self):
        BotonesDojestivos.kahlua1(self)


    def licor_43(self):
        BotonesDojestivos.licor1(self)


    def baileys(self):
        BotonesDojestivos.baileys1(self)


    def disarono(self):
        BotonesDojestivos.disarono1(self)


    def zambuca(self):
        BotonesDojestivos.zambuca1(self)


    def zambuca_negro(self):
        BotonesDojestivos.zambucanegro1(self)


    def grandmarnier(self):
        BotonesDojestivos.marnier1(self)


    def frangelico(self):
        BotonesDojestivos.frangelico1(self)


    def courvusier(self):
        BotonesDojestivos.courvusier1(self)


    def azteca(self):
        BotonesDojestivos.azteca1(self)    
    
    
    def chichon(self):
        BotonesDojestivos.chichon1(self)


    def south(self):
        BotonesDojestivos.south1(self)
    

    def tradicional_reposado(self):
        BotonesTequila.tradicionalrep1(self)

    
    def tradicional_blanco(self):
        BotonesTequila.tradicionalblanco1(self)

    
    def jimador_blanco(self):
        BotonesTequila.jimadorblan1(self)

    
    def jimador_reposado(self):
        BotonesTequila.jimadorrep1(self)


    def hornitos_reposado(self):
        BotonesTequila.hornitosrep1(self)

    
    def blackbarrel(self):
        BotonesTequila.hornitosblack1(self)
    

    def centenario_anejo(self):
        BotonesTequila.centenario1(self)

    
    def anejo_1800(self):
        BotonesTequila.anejo_1800_1(self)


    def herradura_reposado(self):
        BotonesTequila.herradurarep1(self)

    
    def herradura_anejo(self):
        BotonesTequila.herraduraane1(self)

    
    def cazadores(self):
        BotonesTequila.cazadores1(self)


    def cazadores_anejo(self):
        BotonesTequila.cazadoresane1(self)

    
    def don_julio_blanco(self):
        BotonesTequila.donjulioblanco1(self)


    def don_julio_reposado(self):
        BotonesTequila.donjuliorep1(self)


    def don_julio_70(self):
        BotonesTequila.donjulio_70_1(self)


    def don_julio_1942(self):
        BotonesTequila.donjulio_1942_1(self)

    def limpiar(self):
        for i in self.captura.get_children():
            self.captura.delete(i)
    
    #Botones de mesas
    def mesa1(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))         
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa3(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '3')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '3'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa5(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '5')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '5'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa6(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '6')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '6'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa7(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '7')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '7'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    
    def mesa8(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '8')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '8'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa9(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '9')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '9'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa10(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '10')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '10'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()
    

    def mesa11(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '11')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '11'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa12(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '12')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '12'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesa13(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, '13')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = '13'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac1(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava1')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava1'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac2(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava2')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava2'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac3(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava3')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava3'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()

    
    def mesac4(self):
        self.limpiar()
        self.emesa.delete(0, END)
        self.emesa.insert(END, 'Cava4')
        self.emesero.delete(0, END)
        try:
            super().conetarse()
            cursor = self.connection.cursor()

            sql_select_query = "select cantidad, mesero, producto, precio_unitario, total from tabla_cobro WHERE mesa = 'Cava4'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_query)            
            records = cursor.fetchall()
            for row in records:
               self.captura.insert('', END, text = row[0], values = (row[2], row[3], row[4]))
            self.emesero.insert(END, row[1])
        except mysql.connector.Error as error:
            print(f"Fallo la insercion {error}")
        finally:
            self.cerrar_conexion()


    def __init__(self, v):

        cantidad = IntVar()
        lista_mesas = ['1', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Cava1', 'Cava2', 'Cava3', 'Cava4']
        lista_meseros = ['ERICK MARTINEZ', 'DIEGO HERNANDEZ', 'MANUEL FLORES', 'MIGUEL CORONA']

        self.captura = ttk.Treeview(v, columns=('#0', '#1', '#2'))
        self.ecantidad = Entry(v, textvariable = cantidad)
        self.emesa = ttk.Combobox(v, value = lista_mesas)
        self.emesero = ttk.Combobox(v, value = lista_meseros)
