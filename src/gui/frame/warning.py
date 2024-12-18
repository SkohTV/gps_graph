"""
Page proposant d'ajouter des warnings
"""
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Style

from src.consts import ICON_FILE_ACCUEIL



class AppWarning(tk.Frame):
    """ 
    Page warning
    Attributes:
    controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
    bouton_accueil : Bouton envoyant sur la page d'accueil
    bouton_police : Bouton pour choisir le warning police
    bouton_travaux : Bouton pour choisir le warning travaux
    bouton_embouteillage : Bouton pour choisir le warning embouteillage
    bouton_accident : Bouton pour choisir le warning accident
    bouton_mauvais_temps : Bouton pour choisir le warning mauvais temps
    bouton_danger : Bouton pour choisir le warning danger
    bouton_vehicule_arrete : Bouton pour choisir le warning vehicule arrete 
    Methods: 
    __init__: Initialise l'objet
    bouton_accueil : Bouton envoyant sur la page d'accueil
    bouton_police : Bouton pour choisir le warning police
    bouton_travaux : Bouton pour choisir le warning travaux
    bouton_embouteillage : Bouton pour choisir le warning embouteillage
    bouton_accident : Bouton pour choisir le warning accident
    bouton_mauvais_temps : Bouton pour choisir le warning mauvais temps
    bouton_danger : Bouton pour choisir le warning danger
    bouton_vehicule_arrete : Bouton pour choisir le warning vehicule arrete 
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
        self.bouton_police = ttk.Button(frame, text="Police", command=self.bouton_police)
        self.bouton_travaux = ttk.Button(frame, text="Travaux", command=self.bouton_travaux)
        self.bouton_embouteillage = ttk.Button(frame, text="Embouteillage", command=self.bouton_embouteillage)
        self.bouton_accident = ttk.Button(frame, text="Accident", command=self.bouton_accident)
        self.bouton_mauvais_temps = ttk.Button(frame, text="Mauvais Temps", command=self.bouton_mauvais_temps)
        self.bouton_danger = ttk.Button(frame, text="Danger", command=self.bouton_danger)
        self.bouton_vehicule_arrete = ttk.Button(frame, text="Véhicule Arrêté", command=self.bouton_vehicule_arrete)

         # On change le style des widgets
        self.bouton_police["style"] = "giga.TButton"
        self.bouton_travaux["style"] = "giga.TButton"
        self.bouton_embouteillage["style"] = "giga.TButton"
        self.bouton_accident["style"] = "giga.TButton"
        self.bouton_mauvais_temps["style"] = "giga.TButton"
        self.bouton_danger["style"] = "giga.TButton"
        self.bouton_vehicule_arrete["style"] = "giga.TButton"
        self.bouton_accueil["style"] = "acc.TButton"
        style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")

        # On places les widgets dans la fenêtre à des endroits spécifiques
        self.bouton_accueil.pack(side="top", padx=5)
        self.bouton_police.pack(side="top", padx=15, pady=5)
        self.bouton_travaux.pack(side="top", padx=15, pady=5)
        self.bouton_embouteillage.pack(side="top", padx=15, pady=10)
        self.bouton_accident.pack(side="top", padx=15, pady=10)
        self.bouton_mauvais_temps.pack(side="top", padx=15, pady=10)
        self.bouton_danger.pack(side="top", padx=15, pady=10)
        self.bouton_vehicule_arrete.pack(side="top", padx=15, pady=10)

        frame.pack(expand=True, fill="both")

    def bouton_police(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.warnings.append(('Police', self.controller.location))
        self.controller.external_show_frame("AppAccueil")

    def bouton_travaux(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.warnings.append(('Travaux', self.controller.location))
        self.controller.external_show_frame("AppAccueil")

    def bouton_embouteillage(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.warnings.append(('Embouteillage', self.controller.location))
        self.controller.external_show_frame("AppAccueil")

    def bouton_accident(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.warnings.append(('Accident', self.controller.location))
        self.controller.external_show_frame("AppAccueil")

    def bouton_mauvais_temps(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.warnings.append(('Mauvais temps', self.controller.location))
        self.controller.external_show_frame("AppAccueil")

    def bouton_danger(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.warnings.append(('Danger', self.controller.location))
        self.controller.external_show_frame("AppAccueil")

    def bouton_vehicule_arrete(self) -> None:
        """ Affiche la page Accueil"""
        self.controller.warnings.append(('Véhicule arrêté', self.controller.location))
        self.controller.external_show_frame("AppAccueil")

    def bouton_accueil(self) -> None:
        """ Affiche la page d'accueil"""
        self.controller.external_show_frame("AppAccueil")
