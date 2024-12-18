"""
Page proposant les différents itineraire du gps
"""
import tkinter as tk
import tkintermapview
from tkinter import ttk
from tkinter import font
from tkinter import PhotoImage
from tkinter.ttk import Style

from src.gui.frame.trajetIndications import AppTrajetIndications
from src.consts import ICON_FILE_ACCUEIL
from src.utils import thread_me



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
    self.it_path = None

    style = Style()
    
    # On créer une frame pour formatter l'affichage de la page
    frame = ttk.Frame(self)
    container = ttk.Frame(frame, width=50, height=10)
    container.pack(fill="x", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # On définit des widget
    self.accueil = PhotoImage(file=ICON_FILE_ACCUEIL)
    self.bouton_accueil = ttk.Button(container, image=self.accueil, command=self.bouton_accueil) # type: ignore
    self.map_widget = tkintermapview.TkinterMapView(frame, width=2000, height=2000, corner_radius=0)
    self.label_from_to = ttk.Label(frame, text="from->to")
    self.bouton_go = ttk.Button(frame, text="Go", command=self.bouton_go) # type: ignore
    self.label_km_temps = ttk.Label(frame, text="") # No time sadly

    
    # On change le style des widgets
    self.label_from_to["font"] = font.Font(family="Verdana", weight="normal", size=10)
    self.bouton_go["style"] = "giga.TButton" # type: ignore
    self.label_km_temps["font"] = font.Font(family="Verdana", weight="normal", size=10)
    self.label_from_to.config(foreground="gray")
    self.label_km_temps.config(foreground="gray")
    self.bouton_accueil["style"] = "acc.TButton" # type: ignore
    style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")
    style.configure(self, background="black")

    # On places les widgets dans la fenêtre à des endroits spécifiques
    self.map_widget.set_position(49.183333,-0.35)  # Caen, France
    self.map_widget.set_zoom(17)
    self.bouton_accueil.pack(side="right", padx=5) # type: ignore
    self.label_from_to.pack(side="top", pady=10)
    self.bouton_go.pack(side="bottom", padx=15, pady=5) # type: ignore
    self.label_km_temps.pack(side="bottom", pady=10)
    self.map_widget.pack(fill="both")

    frame.pack(expand=True, fill="both")
    container.pack()

    self.end_mark = None
    self.pos_marker = self.map_widget.set_marker(*self.controller.location)
    self.map_widget.set_position(*self.controller.location)
    self.stored_warnings = []
    self.render_dynamic_stuff()
    

  def bouton_go(self) -> None:
    """ Affiche la frame warning """
    self.controller.external_show_frame("AppTrajetIndications")

  def bouton_accueil(self) -> None:
    """ Affiche la page d'accueil"""
    self.controller.external_show_frame("AppAccueil")


  def compute_road(self) -> None:

    if self.it_path:
      self.it_path.delete() # type: ignore
      self.end_mark.delete() # type: ignore
      self.it_path = None
      self.end_mark = None

    self.controller.itineraire = None

    if self.controller.current_frame == 'AppItineraire':
      self.controller.itineraire = self.controller.bridge_api.get_path_to_dest(
        self.controller.location, self.controller.last_address[1], self.controller.vehicule
      )

    if self.controller.itineraire and not self.it_path:
      self.it_path = self.map_widget.set_path(self.controller.itineraire)
      self.end_mark = self.map_widget.set_marker(*self.controller.last_address[0], marker_color_outside="blue")


  @thread_me
  def render_dynamic_stuff(self) -> None:

    if self.controller.current_frame == 'AppItineraire':

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
