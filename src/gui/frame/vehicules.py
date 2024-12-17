"""
Page proposant plusieurs modes de transports
"""

import os
ICON_DIR = os.path.join(os.getcwd(), 'icon')
ICON_FILE_ACCUEIL = os.path.join(ICON_DIR, 'accueil_resize.png')

import tkinter as tk
import tkintermapview
from tkinter import ttk
from tkinter import font
from tkinter import PhotoImage
from tkinter.ttk import Style

class AppVehicules(tk.Frame):
    """ 
    Page Véhicules
    Attributes:
    controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
    bouton_accueil : Bouton envoyant sur la page d'accueil
    bouton_car : Bouton pour choisir le mode de transport voiture
    bouton_bicycle : Bouton pour choisir le mode de transport vélo
    bouton_foot : Bouton pour choisir le mode de transport pied
    Methods:
    __init__: Initialise l'objet
    bouton_accueil : Bouton envoyant sur la page d'accueil
    bouton_car : Bouton pour choisir le mode de transport voiture
    bouton_bicycle :Bouton pour choisir le mode de transport vélo
    bouton_foot : Bouton pour choisir le mode de transport pied
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
        style = Style()

        # On créer différentes frames pour formatter l'affichage de la page
        frame = ttk.Frame(self)

        # On définit des widget
        self.accueil = PhotoImage(file=ICON_FILE_ACCUEIL)
        self.bouton_accueil = ttk.Button(frame, image=self.accueil, command=self.bouton_accueil)
        self.bouton_car = ttk.Button(frame, text="Car", command=self.bouton_car)
        self.bouton_bicycle = ttk.Button(frame, text="Bicycle", command=self.bouton_bicycle)
        self.bouton_foot = ttk.Button(frame, text="Foot", command=self.bouton_foot)

        # On change le style des widgets
        self.bouton_car["style"] = "mega.TButton"
        self.bouton_bicycle["style"] = "mega.TButton"
        self.bouton_foot["style"] = "mega.TButton"
        self.bouton_accueil["style"] = "acc.TButton"
        style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")
        style.configure('mega.TButton', font = "Verdana", foreground="gray", activebackground="white", relief="flat")
        
        self.bouton_accueil.pack(side="top", padx=5)
        self.bouton_car.pack(side="top", pady=15, padx=5)
        self.bouton_bicycle.pack(side="top", pady=15, padx=5)
        self.bouton_foot.pack(side="top", pady=15, padx=5)

        frame.pack(expand=True, fill="both")

    def bouton_car(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.external_show_frame("AppAccueil")

    def bouton_bicycle(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.external_show_frame("AppAccueil")

    def bouton_foot(self) -> None:
            """ Affiche la page Accueil"""
            self.controller.external_show_frame("AppAccueil")

    def bouton_accueil(self) -> None:
        """ Affiche la page d'accueil"""
        self.controller.external_show_frame("AppAccueil")

