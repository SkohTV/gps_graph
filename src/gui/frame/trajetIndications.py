"""
Page proposant d'ajouter des warnings
"""

import tkinter as tk
from tkinter import ttk
from tkinter import font

class AppTrajetIndications(tk.Frame):
    """ 
    Page des indications du trajet
    Attributes:
    controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
    label_indications : Label montrant les différentes indications du trajet
    label_km_temps : Label montrant les kms et le temps restant
    bouton_center : Bouton recentrant la position
    Methods:
    __init__: Initialise l'objet
    bouton_center : Bouton recentrant la position
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
        frame = ttk.Frame(self)

        # On définit des widget
        self.label_indications = ttk.Label(frame, text="Indications", background="green", foreground="red")
        self.label_km_temps = ttk.Label(frame, text="Km/Temps", background="green", foreground="red")
        self.bouton_center = ttk.Button(frame, text="Center", command=self.bouton_center)

        # On change le style des widgets
        self.label_indications["font"] = font.Font(family="Verdana", weight="bold", size=30)
        self.label_km_temps["font"] = font.Font(family="Verdana", weight="bold", size=30)
        self.bouton_center["style"] = "giga.TButton"

        # On places les widgets dans la fenêtre à des endroits spécifiques
        self.label_indications.pack(side="top", fill="x", pady=10)
        self.bouton_center.pack(side="right", padx=15, pady=5)
        self.label_km_temps.pack(side="bottom", fill="x", pady=10)

        frame.pack()

    def bouton_center(self) -> None:
        """ Recentre sur la position """
        self.controller.external_show_frame("AppTrajetIndications")