
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition, RiseInTransition
#from io import BytesIO

class Screen_Coordinator():
    default_window_size = (1000, 800)

    #Class variables for Screen Coordinator Class
    screen_name = None
    screen_size = None
    screen_catch = None
    screen_buffer = None
    screen_transition = None
    #screen_img_buffer = BytesIO ()

    #Change screen method, called to shift between screens.
    def change_screen(self, screen_name, type_transition='Fade'):

        #Method Variables for the change_screen method.
        self.screen_name = screen_name
        self.screen_size = None

        #Crates a fade Transition between Screens
        if (type_transition == 'Fade'):
            self.manager.transition = FadeTransition()
            self.screen_name = screen_name
            self.screen_size = self.default_window_size
        else:
            self.manager.transition = NoTransition()


        self.manager.current = screen_name


    #For a later iteration of the program
    def create_new_screen(self):
        pass


screen_coordinator = Screen_Coordinator
