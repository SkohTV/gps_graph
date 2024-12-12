"""
Page Proposant les différents itineraire du gps
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
        bouton_eviter : Bouton eviter
        bouton_go : Bouton pour démarer
        label_km_temps : Texte montrant le temps de trajet ainsi que le nombre de kilomètres
    Methods:
        __init__: Initialise l'objet
        bouton_eviter : Bouton eviter
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
        frame4 = ttk.Frame(self)

        # On définit des widget
        self.label_from_to = ttk.Label(frame1, text="from->to", background="purple", foreground="pink")
        self.bouton_eviter = ttk.Button(frame2, text="Avoid", command=self.bouton_eviter)
        self.bouton_go = ttk.Button(frame3, text="Go", command=self.bouton_go)
        self.label_km_temps = ttk.Label(frame4, text="km/temps", background="purple", foreground="pink")
        

