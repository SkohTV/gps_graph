"""
Page proposant d'ajouter des warnings
"""

import tkinter as tk
import tkintermapview
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
        self.map_widget = tkintermapview.TkinterMapView(frame, width=2000, height=2000, corner_radius=0)
        self.label_indications = ttk.Label(frame, text="Indications")
        self.label_km_temps = ttk.Label(frame, text="Km/Temps")
        self.bouton_center = ttk.Button(frame, text="Center", command=self.bouton_center)

        # On change le style des widgets
        self.label_indications["font"] = font.Font(family="Verdana", weight="normal", size=15)
        self.label_km_temps["font"] = font.Font(family="Verdana", weight="normal", size=10)
        self.bouton_center["style"] = "giga.TButton"
        self.label_indications.config(foreground="gray")
        self.label_km_temps.config(foreground="gray")

        # On places les widgets dans la fenêtre à des endroits spécifiques
        self.map_widget.set_position(49.183333,-0.35)  # Caen, France
        self.map_widget.set_zoom(17)
        self.label_indications.pack(side="top", pady=10)
        self.bouton_center.pack(side="bottom", padx=15, pady=5)
        self.label_km_temps.pack(side="bottom", pady=10)
        self.map_widget.pack(fill="both")

        frame.pack()

    def bouton_center(self) -> None:
        """ Recentre sur la position """
        self.controller.external_show_frame("AppTrajetIndications")