"""
Page proposant les différents itineraire du gps
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

class AppItineraire(tk.Frame):
    """ 
    Page Itineraire
    Attributes:
        controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
        label_from_to : Texte rappelant la destination et le départs
        bouton_accueil : Bouton envoyant sur la page d'accueil
        bouton_go : Bouton pour démarer
        label_km_temps : Texte montrant le temps de trajet ainsi que le nombre de kilomètres
    Methods:
        __init__: Initialise l'objet
        bouton_accueil : Bouton envoyant sur la page d'accueil
        bouton_go : Bouton pour démarer
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
        self.controller = controller

        style = Style()
        
        # On créer une frame pour formatter l'affichage de la page
        frame = ttk.Frame(self)
        container = ttk.Frame(frame, width=50, height=10)
        container.pack(fill="x", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # On définit des widget
        self.accueil = PhotoImage(file=ICON_FILE_ACCUEIL)
        self.bouton_accueil = ttk.Button(container, image=self.accueil, command=self.bouton_accueil)
        self.map_widget = tkintermapview.TkinterMapView(frame, width=2000, height=2000, corner_radius=0)
        self.label_from_to = ttk.Label(frame, text="from->to")
        self.bouton_go = ttk.Button(frame, text="Go", command=self.bouton_go)
        self.label_km_temps = ttk.Label(frame, text="km/temps")
 
        
        # On change le style des widgets
        self.label_from_to["font"] = font.Font(family="Verdana", weight="normal", size=10)
        self.bouton_go["style"] = "giga.TButton"
        self.label_km_temps["font"] = font.Font(family="Verdana", weight="normal", size=10)
        self.label_from_to.config(foreground="gray")
        self.label_km_temps.config(foreground="gray")
        self.bouton_accueil["style"] = "acc.TButton"
        style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")
        style.configure(self, background="black")

        # On places les widgets dans la fenêtre à des endroits spécifiques
        self.map_widget.set_position(49.183333,-0.35)  # Caen, France
        self.map_widget.set_zoom(17)
        self.bouton_accueil.pack(side="right", padx=5)
        self.label_from_to.pack(side="top", pady=10)
        self.bouton_go.pack(side="bottom", padx=15, pady=5)
        self.label_km_temps.pack(side="bottom", pady=10)
        self.map_widget.pack(fill="both")
        # self.map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        frame.pack(expand=True, fill="both")
        container.pack()

    def bouton_go(self) -> None:
        """ Affiche la frame warning """
        self.controller.external_show_frame("AppTrajetIndications")

    def bouton_accueil(self) -> None:
        """ Affiche la page d'accueil"""
        self.controller.external_show_frame("AppAccueil")



        
