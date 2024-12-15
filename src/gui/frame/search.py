"""
Page proposant la recherche d'un trajet
"""

import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import StringVar

class AppSearch(tk.Frame):
    """ 
    Page Search 
    Attributes:
    controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
    zone_txt_where : Zone de texte pour rentrer une nouvelle adresse
    bouton_search : Bouton pour rechercher une adresse
    bouton_saved : Bouton pour cliquer sur une adresse déjà enregistrée
    bouton_recent : Bouton pour cliquer sur une adresse récente
    Methods:
    __init__: Initialise l'objet
    bouton_search : Bouton pour rechercher une adresse
    bouton_saved : Bouton pour cliquer sur une adresse déjà enregistrée
    bouton_recent : Bouton pour cliquer sur une adresse récente
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

        # On créer différentes frames pour formatter l'affichage de la page
        frame = ttk.Frame(self)

        # On définit des widget
        self.zone_txt_where = ttk.Entry(frame, textvariable=self.__zone_txt_where)
        self.bouton_search = ttk.Button(frame, text="Search", command=self.bouton_search)
        self.bouton_saved = ttk.Button(frame, text="Saved", command=self.bouton_saved)
        self.bouton_recent = ttk.Button(frame, text="Recent", command=self.bouton_recent)

        # On change le style des widgets
        self.zone_txt_where.focus_set()
        self.bouton_search["style"] = "giga.TButton"
        self.bouton_saved["style"] = "giga.TButton"
        self.bouton_recent["style"] = "giga.TButton"

        # On places les widgets dans la fenêtre à des endroits spécifiques
        self.zone_txt_where.pack(side="top", fill="x", pady=5)
        self.bouton_search.pack(side="top", padx=15, pady=5)
        self.bouton_saved.pack(side="bottom", padx=15, pady=5)
        self.bouton_recent.pack(side="bottom", padx=15, pady=10)

        frame.pack()

    def bouton_search(self) -> None:
        """ Affiche la page TrajetIndication"""
        self.controller.external_show_frame("AppTrajetIndications")

    def bouton_saved(self) -> None:
        """ Affiche la page TrajetIndication"""
        self.controller.external_show_frame("AppTrajetIndications")

    def bouton_recent(self) -> None:
            """ Affiche la page TrajetIndication"""
            self.controller.external_show_frame("AppTrajetIndications")

