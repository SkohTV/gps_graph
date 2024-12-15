"""
Page proposant les différents itineraire du gps
"""
import tkinter as tk
from tkinter import ttk
from tkinter import font

class AppItineraire(tk.Frame):
    """ 
    Page Itineraire
    Attributes:
        controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
        label_from_to : Texte rappelant la destination et le départs
        bouton_go : Bouton pour démarer
        label_km_temps : Texte montrant le temps de trajet ainsi que le nombre de kilomètres
    Methods:
        __init__: Initialise l'objet
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

        # On créer différentes frames pour formatter l'affichage de la page
        frame1 = ttk.Frame(self)
        frame2 = ttk.Frame(self)
        frame3 = ttk.Frame(self)

        # On définit des widget
        self.label_from_to = ttk.Label(frame1, text="from->to", background="purple", foreground="pink")
        self.bouton_go = ttk.Button(frame2, text="Go", command=self.bouton_go)
        self.label_km_temps = ttk.Label(frame3, text="km/temps", background="purple", foreground="pink")
        
        # On change le style des widgets
        self.label_from_to["font"] = font.Font(family="Verdana", weight="bold", size=30)
        self.bouton_go["style"] = "giga.TButton"
        self.label_km_temps["font"] = font.Font(family="Verdana", weight="bold", size=30)

         # On places les widgets dans la fenêtre à des endroits spécifiques
        self.label_from_to.pack(side="top", pady=10)
        self.bouton_go.pack(side="right", padx=15, pady=5)
        self.label_km_temps.pack(side="bottom", pady=10)

        frame1.pack()
        frame2.pack()
        frame3.pack()

    def bouton_go(self) -> None:
        """ Affiche la frame warning """
        self.controller.external_show_frame("AppTrajetIndications")



        
