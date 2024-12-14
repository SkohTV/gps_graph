"""
Page d'accueil de l'application
"""

import tkinter as tk
from tkinter import ttk
from tkinter import font

class AppAccueil(tk.Frame):
    """
    Page d'accueil
    Attributes: 
        controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
        label : Text de la page d'accueil
        bouton_mode_transport : Bouton pour choisir le mode de transport
        bouton_warning : Bouton pour ajouter des warnings
        bouton_where : Bouton pour rechercher une adresse
    Methods: 
        __init__: Initialise l'objet
        bouton_mode_transport : Bouton pour choisir le mode de transport
        bouton_warning : Bouton pour ajouter des warnings
        bouton_where : Bouton pour rechercher une adresse
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

        # On créer différentes frames pour formatter l'affichage de la page
        frame1 = ttk.Frame(self)
        frame2 = ttk.Frame(self)
        frame3 = ttk.Frame(self)
        frame4 = ttk.Frame(self)

        # On définit des widget
        self.label = ttk.Label(frame1, text="GPS", background="green", foreground="red")
        self.bouton_mode_transport = ttk.Button(frame2, text="Mode of transportation", command=self.bouton_mode_transport)
        self.bouton_warning = ttk.Button(frame3, text="Add Warning", command=self.bouton_warning)
        self.bouton_where = ttk.Button(frame4, text="Where", command=self.bouton_where)

        # On change le style des widgets
        self.label["font"] = font.Font(family="Verdana", weight="bold", size=30)
        self.bouton_mode_transport["style"] = "giga.TButton"
        self.bouton_warning["style"] = "giga.TButton"
        self.bouton_where["style"] = "giga.TButton"

        # On places les widgets dans la fenêtre à des endroits spécifiques
        self.label.pack(side="top", pady=10)
        self.bouton_mode_transport.pack(side="left", padx=15, pady=5)
        self.bouton_warning.pack(side="right", padx=15, pady=5)
        self.bouton_where.pack(side="bottom", fill="x", pady=10)

        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()

    def bouton_mode_transport(self) -> None:
        """ Affiche la frame vehicules """
        self.controller.external_show_frame("AppVehicules")

    def bouton_warning(self) -> None:
        """ Affiche la frame warning """
        self.controller.external_show_frame("AppWarning")

    def bouton_where(self) -> None:
        """ Affiche la frame search """
        self.controller.external_show_frame("AppSearch")

