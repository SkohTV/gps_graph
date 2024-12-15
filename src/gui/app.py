"""
L'application composé de 6 frames où chaque frame est une page de l'application.
app est la classe principale de l'application.
"""

import sys
import tkinter as tk    
from src.gui.frame.accueil import AppAccueil
from src.gui.frame.itineraire import AppItineraire
from src.gui.frame.search import AppSearch
from src.gui.frame.trajetIndications import AppTrajetIndications
from src.gui.frame.vehicules import AppVehicules
from src.gui.frame.warning import AppWarning

class App(tk.Tk):

    """
    classe principale de l'application

    Attributs :
    style (ttkStyle): Style de l'application
    back_button (PhotoImage): Icône de retour

    Méthode :
    __init__: Initialise l'objet
    show_frame: Affiche une frame
    external_show_frame: Affiche une frame depuis une autre frame
    on_close: Ferme l'application
    """

    def __init__(self) -> None:

        """Initialisation de l'objet"""

        # On utilise l'init de l'objet Tkinter de base
        tk.Tk.__init__(self)

        # Valeurs réutilisées dans des frames, nécessaires ici pour y accéder
        self.back_button = tk.PhotoImage(file="icone/back.png")

        # On attrape l'event de fermeture de la fenêtre, pour pouvoir clore le script
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Change les paramètres basiques de la fenêtre
        self.resizable(False, False)
        
        # On crée un pack pour englober la frame
        container = tk.Frame(self, height=1800, width=1500)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # on ajoute les frames à un dictionnaire
        self.frames = {}
        for item in (AppAccueil, AppItineraire, AppSearch, AppVehicules, AppWarning, AppTrajetIndications):
            print(item)
            frame = item(container, self)
            self.frames[item] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # On affiche la frame de l'accueil
        self.show_frame(AppAccueil)

    def show_frame(self, cont: tk.Frame) -> None:
        """Affiche une frame de la fenêtre Tkinter (voir fichiers dans frames)\n

        Args:
            cont (tk.Frame): Frame à afficher\n
        """

        # On récupère la frame dans le dictionnaire
        frame = self.frames[cont]

        # On met la frame en grand
        self.title("GPS")
        self.geometry("1500x1800")

        # On l'affiche
        frame.tkraise()

    def external_show_frame(self, text_frame: str) -> None:
        """
        On affiche une frame depuis une autre frame
        Args :
            text_frame (str) : Nom de la fenêtre à afficher
        """

        match text_frame:
            case "AppItineraire":
                self.show_frame(AppItineraire)
            case "AppSearch":
                self.show_frame(AppSearch)
            case "AppTrajetIndications":
                self.show_frame(AppTrajetIndications)
            case "AppVehicules":
                self.show_frame(AppVehicules)
            case "AppWarning":
                self.show_frame(AppWarning)
            case "AppAccueil":
                self.show_frame(AppAccueil)
    
    def on_close(self) -> None:
        """ Ferme la fenêtre """
        self.destroy()
        sys.exit()

    def send_event(self, event: str) -> None:
        """
        Envoi un event au niveau de la fenêtre (utilisée à partir d'une Frame)
		Args:
			event (str): Nom de l'event à envoyer
		"""
        self.event_generate(f"<<{event}>>")