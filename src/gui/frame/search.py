"""
Page proposant la recherche d'un trajet
"""
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter.ttk import Style

from src.gui.frame.itineraire import AppItineraire
from src.consts import ICON_FILE_ACCUEIL



class AppSearch(tk.Frame):
  """ 
  Page Search 
  Attributes:
  controller (src.app.App): Classe tk.Tk principale qui controle la tk.Frame
  zone_txt_where : Zone de texte pour rentrer une nouvelle adresse
  self.adresses_diff = une liste d'adresses
  frame_search : frame pour les différentes adresses
  bouton_accueil : Bouton envoyant sur la page d'accueil
  bouton_search : Bouton pour rechercher une adresse
  bouton_last_search : Bouton pour cliquer sur une adresse récente
  Methods:
  __init__: Initialise l'objet
  bouton_accueil : Bouton envoyant sur la page d'accueil
  bouton_search : Bouton pour afficher plusieurs adresses
  bouton_last_search : Bouton pour cliquer sur une adresse récente
  affiche_itineraire : Bouton pour afficher la page itineraire
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
    self.__zone_txt_where = StringVar()
    self.adresses_diff = []
    self.possible_addresses = []
    style = Style()

    # On créer différentes frames pour formatter l'affichage de la page
    frame = ttk.Frame(self)
    self.frame_search = ttk.Frame(frame)

    # On définit des widget
    self.accueil = PhotoImage(file=ICON_FILE_ACCUEIL)
    self.bouton_accueil = ttk.Button(frame, image=self.accueil, command=self.bouton_accueil) # type: ignore
    self.zone_txt_where = ttk.Entry(frame, textvariable=self.__zone_txt_where) # type: ignore
    self.bouton_search = ttk.Button(frame, text="🔍", command=self.bouton_search) # type: ignore
    self.bouton_last_search = ttk.Button(frame, text="Last Search", command=self.bouton_last_search) # type: ignore

    # On change le style des widgets
    self.zone_txt_where.focus_set()
    self.bouton_search["style"] = "giga.TButton" # type: ignore
    self.bouton_last_search["style"] = "giga.TButton" # type: ignore
    self.bouton_accueil["style"] = "acc.TButton" # type: ignore
    style.configure('acc.TButton', font = "Verdana", foreground="gray", activebackground="black", relief="flat")

    # On places les widgets dans la fenêtre à des endroits spécifiques
    self.bouton_accueil.pack(side="top", padx=5) # type: ignore
    self.zone_txt_where.pack(side="top", padx=15, pady=5) # type: ignore
    self.bouton_search.pack(side="top", padx=15, pady=5) # type: ignore
    self.bouton_last_search.pack(side="top", padx=15, pady=10) # type: ignore

    frame.pack(expand=True, fill="both")

  
  def bouton_search(self) -> None:
    """ Affiche différents boutons avec plusieurs adresses proposées"""
    search = self.zone_txt_where.get()
    possible_addresse = self.controller.bridge_api.get_possible_addresse(search)

    if self.adresses_diff: # on vérifie si la liste est rempli, si oui :
      for i in self.adresses_diff: # on supprime tous les éléments de la liste
        i.destroy() # enlever le pack
      self.adresses_diff.clear() # reset la liste car sinon il reste des boutons dans la liste 

    for pos, name, key in possible_addresse: # 10 boutons
      self.adresses_diff.append(
        ttk.Button(self.frame_search, text=name, command=lambda: self.affiche_itineraire(pos, key))
      ) # on créer pls boutons
        
    for i in self.adresses_diff: 
      i["style"] = "giga.TButton" # on change le style de chaque bouton
      i.pack() #chaque bouton va se placer
    self.frame_search.pack()


  def bouton_last_search(self) -> None:
    """ Affiche la page TrajetIndication"""
    if self.controller.last_address is not None:
      self.controller.external_show_frame("AppItineraire")
      self.controller.frames[AppItineraire].compute_road()

  def affiche_itineraire(self, pos: tuple[float, float], key: int) -> None:
    """ Affiche la page TrajetIndication"""
    self.controller.last_address = (pos, key)
    self.controller.external_show_frame("AppItineraire")
    self.controller.frames[AppItineraire].compute_road()

  def bouton_accueil(self) -> None:
    """ Affiche la page d'accueil"""
    self.controller.external_show_frame("AppAccueil")

