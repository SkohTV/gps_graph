"""
Page d'accueil de l'application
"""
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.ttk import Style
from tkinter import PhotoImage

import tkintermapview 

from src.utils import thread_me
from src.consts import ICON_FILE_ACCUEIL



class AppAccueil(tk.Frame):
  """
  Page d'accueil
  Attributes: 
      controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
      label : Text de la page d'accueil
      map_widget : la carte
      bouton_accueil : Bouton envoyant sur la page d'accueil
      bouton_mode_transport : Bouton pour choisir le mode de transport
      bouton_warning : Bouton pour ajouter des warnings
      bouton_where : Bouton pour rechercher une adresse
  Methods: 
      __init__: Initialise l'objet
      bouton_accueil : Bouton envoyant sur la page d'accueil
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
    container = ttk.Frame(frame, width=50, height=10)
    container.pack(fill="x", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # On définit des widget
    self.accueil = PhotoImage(file=ICON_FILE_ACCUEIL)
    self.bouton_accueil = ttk.Button(container, image=self.accueil, command=self.bouton_accueil) # type: ignore
    self.bouton_mode_transport = ttk.Button(frame, text="Mode of transportation", command=self.bouton_mode_transport) # type: ignore
    self.map_widget = tkintermapview.TkinterMapView(frame, width=2000, height=2000, corner_radius=0) # type: ignore
    self.label = ttk.Label(container, text="GPS") # type: ignore
    self.bouton_warning = ttk.Button(frame, text="Add Warning", command=self.bouton_warning) # type: ignore
    self.bouton_where = ttk.Button(frame, text="Where ?", command=self.bouton_where) # type: ignore

    # On change le style des widgets
    self.label["font"] = font.Font(family="Verdana", weight="bold", size=30)
    self.bouton_mode_transport["style"] = "giga.TButton" # type: ignore
    self.bouton_warning["style"] = "giga.TButton" # type: ignore
    self.bouton_where["style"] = "giga.TButton" # type: ignore
    self.bouton_accueil["style"] = "acc.TButton" # type: ignore
    style = Style()
    style.configure('giga.TButton', font = "Verdana", foreground="gray", activebackground="white", relief="flat")
    style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")
    self.label.config(foreground="gray")

    # On places les widgets dans la fenêtre à des endroits spécifiques
    self.map_widget.set_position(49.183333,-0.35)  # Caen, France
    self.map_widget.set_zoom(17)
    self.label.pack(side="top", pady=10)
    self.bouton_accueil.pack(side="right", padx=5) # type: ignore
    self.bouton_where.pack(side="bottom", padx=15, pady=10) # type: ignore
    self.bouton_warning.pack(side="bottom", padx=15, pady=5) # type: ignore
    self.bouton_mode_transport.pack(side="bottom", padx=15, pady=5) # type: ignore
    self.map_widget.pack(fill="both")

    frame.pack(expand=True, fill="both")
    container.pack()

    self.pos_marker = self.map_widget.set_marker(*self.controller.location)
    self.map_widget.set_position(*self.controller.location)
    self.stored_warnings = []
    self.render_dynamic_stuff()



  def bouton_mode_transport(self) -> None:
    """ Affiche la frame vehicules """
    self.controller.external_show_frame("AppVehicules")

  def bouton_warning(self) -> None:
    """ Affiche la frame warning """
    self.controller.external_show_frame("AppWarning")

  def bouton_where(self) -> None:
    """ Affiche la frame search """
    self.controller.external_show_frame("AppSearch")

  def bouton_accueil(self) -> None:
    """ Affiche la page d'accueil"""
    self.controller.external_show_frame("AppAccueil")


  @thread_me
  def render_dynamic_stuff(self) -> None:

    if self.controller.current_frame == 'AppAccueil':

      if self.pos_marker and self.pos_marker.position != self.controller.location:
        new_marker = self.map_widget.set_marker(*self.controller.location)
        self.pos_marker.delete()
        self.pos_marker = new_marker

      if len(self.stored_warnings) != len(self.controller.warnings):

        if self.stored_warnings:
          for i in self.stored_warnings:
            i.delete()

        for i in self.controller.warnings:
          self.stored_warnings.append(
            self.map_widget.set_marker(*self.controller.parse_warning(i), marker_color_outside='yellow')
          )

