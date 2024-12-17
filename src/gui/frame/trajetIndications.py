"""
Page proposant d'ajouter des warnings
"""
import tkinter as tk
import tkintermapview
from tkinter import ttk
from tkinter import font
from tkinter import PhotoImage
from tkinter.ttk import Style

from src.consts import ICON_FILE_ACCUEIL
from src.utils import thread_me



class AppTrajetIndications(tk.Frame):
  """ 
  Page des indications du trajet
  Attributes:
  controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
  label_indications : Label montrant les différentes indications du trajet
  bouton_accueil : Bouton envoyant sur la page d'accueil
  label_km_temps : Label montrant les kms et le temps restant
  bouton_center : Bouton recentrant la position
  Methods:
  __init__: Initialise l'objet
  bouton_accueil : Bouton envoyant sur la page d'accueil
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
    self.it_path = None
    style = Style()

    # On créer différentes frames pour formatter l'affichage de la page
    frame = ttk.Frame(self)
    container = ttk.Frame(frame, width=50, height=10)
    container.pack(fill="x", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # On définit des widget
    self.accueil = PhotoImage(file=ICON_FILE_ACCUEIL)
    self.bouton_accueil = ttk.Button(container, image=self.accueil, command=self.bouton_accueil) # type: ignore
    self.map_widget = tkintermapview.TkinterMapView(frame, width=2000, height=2000, corner_radius=0)
    self.label_indications = ttk.Label(frame, text="Indications")
    self.label_km_temps = ttk.Label(frame, text="") # No time unfortunatly
    self.bouton_center = ttk.Button(frame, text="Center", command=self.bouton_center) # type: ignore

    # On change le style des widgets
    self.label_indications["font"] = font.Font(family="Verdana", weight="normal", size=15)
    self.label_km_temps["font"] = font.Font(family="Verdana", weight="normal", size=10)
    self.bouton_center["style"] = "giga.TButton" # type: ignore
    self.bouton_accueil["style"] = "acc.TButton" # type: ignore
    style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")
    self.label_indications.config(foreground="gray")
    self.label_km_temps.config(foreground="gray")

    # On places les widgets dans la fenêtre à des endroits spécifiques
    self.map_widget.set_position(49.183333,-0.35)  # Caen, France
    self.map_widget.set_zoom(17)
    self.bouton_accueil.pack(side="right", padx=5) # type: ignore
    self.label_indications.pack(side="top", pady=10)
    self.bouton_center.pack(side="bottom", padx=15, pady=5) # type: ignore
    self.label_km_temps.pack(side="bottom", pady=10)
    self.map_widget.pack(fill="both")

    frame.pack(expand=True, fill="both")
    container.pack()

    self.end_mark = None
    self.pos_marker = self.map_widget.set_marker(*self.controller.location)
    self.map_widget.set_position(*self.controller.location)
    self.stored_warnings = []
    self.render_dynamic_stuff()


  def bouton_center(self) -> None:
    """ Recentre sur la position """
    self.map_widget.set_position(*self.controller.location)

  def bouton_accueil(self) -> None:
    """ Affiche la page d'accueil"""
    self.controller.external_show_frame("AppAccueil")


  def compute_road(self) -> None:
    if self.it_path:
      self.it_path.delete() # type: ignore
      self.end_mark.delete() # type: ignore
      self.end_mark = None
      self.it_path = None

    if self.controller.itineraire and not self.it_path:
      self.it_path = self.map_widget.set_path(self.controller.itineraire)
      self.end_mark = self.map_widget.set_marker(*self.controller.last_address[0], marker_color_outside="blue")


  @thread_me
  def render_dynamic_stuff(self) -> None:

    if self.controller.current_frame == 'AppTrajetIndications':

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

