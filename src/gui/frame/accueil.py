"""
Page d'accueil de l'application
"""

import tkinter as tk
import tkintermapview 
from tkinter import ttk
from tkinter import font
from tkinter.ttk import Style

class AppAccueil(tk.Frame):
    """
    Page d'accueil
    Attributes: 
        controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
        label : Text de la page d'accueil
        map_widget : la carte
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

        # On créer une frame pour formatter l'affichage de la page
        frame = ttk.Frame(self)

        # On définit des widget
        self.bouton_mode_transport = ttk.Button(frame, text="Mode of transportation", command=self.bouton_mode_transport)
        self.map_widget = tkintermapview.TkinterMapView(frame, width=2000, height=2000, corner_radius=0)
        self.label = ttk.Label(frame, text="GPS")
        self.bouton_warning = ttk.Button(frame, text="Add Warning", command=self.bouton_warning)
        self.bouton_where = ttk.Button(frame, text="Where ?", command=self.bouton_where)

        # On change le style des widgets
        self.label["font"] = font.Font(family="Verdana", weight="bold", size=30)
        self.bouton_mode_transport["style"] = "giga.TButton"
        self.bouton_warning["style"] = "giga.TButton"
        self.bouton_where["style"] = "giga.TButton"
        style = Style()
        style.configure('giga.TButton', font = "Verdana", foreground="gray", activebackground="white", relief="flat")
        self.label.config(foreground="gray")

        # On places les widgets dans la fenêtre à des endroits spécifiques
        self.map_widget.set_position(49.183333,-0.35)  # Caen, France
        self.map_widget.set_zoom(17)
        self.map_widget.set_address("16 bis Quai Amiral Hamelin, caen, france")
        self.label.pack(side="top", pady=10)
        self.bouton_where.pack(side="bottom", padx=15, pady=10)
        self.bouton_warning.pack(side="bottom", padx=15, pady=5)
        self.bouton_mode_transport.pack(side="bottom", padx=15, pady=5)
        # self.map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.map_widget.pack(fill="both")

        # le marker prend la position
        self.map_widget.set_address("colosseo, rome, italy")
        marker_1 = self.map_widget.set_marker(52.516268, 13.377695, text="Brandenburger Tor")
        print(marker_1.position, marker_1.text)
        marker_1.set_text("Brandenburger Tor")

        frame.pack()

    def bouton_mode_transport(self) -> None:
        """ Affiche la frame vehicules """
        self.controller.external_show_frame("AppVehicules")

    def bouton_warning(self) -> None:
        """ Affiche la frame warning """
        self.controller.external_show_frame("AppWarning")

    def bouton_where(self) -> None:
        """ Affiche la frame search """
        self.controller.external_show_frame("AppSearch")

