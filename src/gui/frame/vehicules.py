"""
Page proposant plusieurs modes de transports
"""
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.ttk import Style

from src.consts import ICON_FILE_ACCUEIL



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
    self.bouton_accueil = ttk.Button(frame, image=self.accueil, command=self.bouton_accueil) # type: ignore
    self.bouton_car = ttk.Button(frame, text="Car", command=self.bouton_car) # type: ignore
    self.bouton_bicycle = ttk.Button(frame, text="Bicycle", command=self.bouton_bicycle) # type: ignore
    self.bouton_foot = ttk.Button(frame, text="Foot", command=self.bouton_foot) # type: ignore

    # On change le style des widgets
    self.bouton_car["style"] = "mega.TButton" # type: ignore
    self.bouton_bicycle["style"] = "mega.TButton" # type: ignore
    self.bouton_foot["style"] = "mega.TButton" # type: ignore
    self.bouton_accueil["style"] = "acc.TButton" # type: ignore
    style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")
    style.configure('mega.TButton', font = "Verdana", foreground="gray", activebackground="white", relief="flat")
    
    self.bouton_accueil.pack(side="top", padx=5) # type: ignore
    self.bouton_car.pack(side="top", pady=15, padx=5) # type: ignore
    self.bouton_bicycle.pack(side="top", pady=15, padx=5) # type: ignore
    self.bouton_foot.pack(side="top", pady=15, padx=5) # type: ignore

    frame.pack(expand=True, fill="both")

  def bouton_car(self) -> None:
    """ Affiche la page Accueil"""
    self.controller.vehicule = 'car'
    self.controller.external_show_frame("AppAccueil")

  def bouton_bicycle(self) -> None:
    """ Affiche la page Accueil"""
    self.controller.vehicule = 'bike'
    self.controller.external_show_frame("AppAccueil")

  def bouton_foot(self) -> None:
    """ Affiche la page Accueil"""
    self.controller.vehicule = 'walk'
    self.controller.external_show_frame("AppAccueil")

  def bouton_accueil(self) -> None:
    """ Affiche la page d'accueil"""
    self.controller.external_show_frame("AppAccueil")

