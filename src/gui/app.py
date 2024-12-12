"""
L'application composé de 6 frames où chaque frame est une page de l'application.
app est la classe principale de l'application.
"""

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
        