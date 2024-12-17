"""
Page proposant la recherche d'un trajet
"""

import os
ICON_DIR = os.path.join(os.getcwd(), 'icon')
ICON_FILE_ACCUEIL = os.path.join(ICON_DIR, 'accueil_resize.png')

import tkinter as tk
import tkintermapview
from tkinter import ttk
from tkinter import font
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter.ttk import Style

class AppSearch(tk.Frame):
    """ 
    Page Search 
    Attributes:
    controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
    zone_txt_where : Zone de texte pour rentrer une nouvelle adresse
    self.adresses_diff = une liste d'adresses
    frame_search : frame pour les différentes adresses
    bouton_accueil : Bouton envoyant sur la page d'accueil
    bouton_search : Bouton pour rechercher une adresse
    bouton_saved : Bouton pour cliquer sur une adresse déjà enregistrée
    bouton_recent : Bouton pour cliquer sur une adresse récente
    Methods:
    __init__: Initialise l'objet
    bouton_accueil : Bouton envoyant sur la page d'accueil
    bouton_search : Bouton pour afficher plusieurs adresses
    bouton_saved : Bouton pour cliquer sur une adresse déjà enregistrée
    bouton_recent : Bouton pour cliquer sur une adresse récente
    affiche_itineraire : Bouton pour afficher la page itineraire
    """

    def __init__(self, parent: tk.Frame, controller) -> None:
        """
        Initialisation de l'objet
        Args:
            parent (tk.Frame): Objet dont la classe inhérite\n
			controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
        """
        # On créer une frame
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.__zone_txt_where = StringVar()
        self.adresses_diff = []
        style = Style()

        # On créer différentes frames pour formatter l'affichage de la page
        frame = ttk.Frame(self)
        self.frame_search = ttk.Frame(frame)

        # On définit des widget
        self.accueil = PhotoImage(file=ICON_FILE_ACCUEIL)
        self.bouton_accueil = ttk.Button(frame, image=self.accueil, command=self.bouton_accueil)
        self.zone_txt_where = ttk.Entry(frame, textvariable=self.__zone_txt_where)
        self.bouton_search = ttk.Button(frame, text="🔍", command=self.bouton_search)
        self.bouton_saved = ttk.Button(frame, text="Saved", command=self.bouton_saved)
        self.bouton_recent = ttk.Button(frame, text="Recent", command=self.bouton_recent)

        # On change le style des widgets
        self.zone_txt_where.focus_set()
        self.bouton_search["style"] = "giga.TButton"
        self.bouton_saved["style"] = "giga.TButton"
        self.bouton_recent["style"] = "giga.TButton"
        self.bouton_accueil["style"] = "acc.TButton"
        style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")

        # On places les widgets dans la fenêtre à des endroits spécifiques
        self.bouton_accueil.pack(side="top", padx=5)
        self.zone_txt_where.pack(side="top", padx=15, pady=5)
        self.bouton_search.pack(side="top", padx=15, pady=5)
        self.bouton_saved.pack(side="top", padx=15, pady=5)
        self.bouton_recent.pack(side="top", padx=15, pady=10)

        frame.pack(expand=True, fill="both")
    
    def bouton_search(self) -> None:
        """ Affiche différents boutons avec plusieurs adresses proposées"""
        if self.adresses_diff: # on vérifie si la liste est rempli, si oui :
            for i in self.adresses_diff: # on supprime tous les éléments de la liste
                i.destroy() # enlever le pack
            self.adresses_diff.clear() # reset la liste car sinon il reste des boutons dans la liste 

        for i in range(11): # 10 boutons
            self.adresses_diff.append(ttk.Button(self.frame_search, text=i, command=self.affiche_itineraire)) # on créer pls boutons
            
        for i in self.adresses_diff: 
            i["style"] = "giga.TButton" # on change le style de chaque bouton
            i.pack() #chaque bouton va se placer
        self.frame_search.pack()


    def bouton_saved(self) -> None:
        """ Affiche la page TrajetIndication"""
        self.controller.external_show_frame("AppItineraire")

    def bouton_recent(self) -> None:
        """ Affiche la page TrajetIndication"""
        self.controller.external_show_frame("AppItineraire")

    def affiche_itineraire(self) -> None:
         """ Affiche la page TrajetIndication"""
         self.controller.external_show_frame("AppItineraire")

    def bouton_accueil(self) -> None:
        """ Affiche la page d'accueil"""
        self.controller.external_show_frame("AppAccueil")