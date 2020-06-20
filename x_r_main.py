"""
Created on Wed Jun 16 03:12:24 2020

@author: Haseeb Khan
@Work: Workbench_comp1
:: Created using Standard and Imported Python Libraries
:: Created for educational purposes, feel free to use this code with appropriate citations
"""



from kivy.app import App
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage

# Imports into from uix
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

# For Using Kivy text in the .py file.
from kivy.properties import StringProperty
from kivy.lang import Builder
from io import BytesIO

# Custom Classes for Editor
from Editor import editor_instance
from ScreenCoordinator import screen_coordinator
# Builder imported from kivy.lang
# Imports and loads kivy file to Main
Builder.load_file('kvlang.kv')


#Screen Transitioner class inherits from the Screen Manager
class screen_transitioner(ScreenManager):
    def __init__(self,  ** kwargs):
        super().__init__(** kwargs)

# Main Screen Class :: MainScreen
# Produces the MainScreen of the program:
class MainScreen(Screen, screen_coordinator): #Changeamaze this part

    # Main Screen Initialization Method.
    def __init__(self, ** kwargs):
        super().__init__ (** kwargs)

        # Setting the window size and creating a window bindong to File Drop
        Window.size = (1000, 800)
        Window.clearcolor = 0.2, 0.2, 0.2, 0.2
        Window.bind(on_dropfile = self._on_file_drop)

        # Adding the First Text to the original window.
        text_1 = "Drag and Drop the X-Ray to this Window."
        l1 = Label(text = text_1)
        self.add_widget(l1)

    # Unpacks the file
    def unpack_file(self ,file_path):
        filepath = ""
        filepath = file_path.decode ('utf-8')
        return filepath


    # Called Once file is dropped into the window.
    def _on_file_drop(self, window, file_path):

        filepath = self.unpack_file(file_path)

        # Error Checking for file omening and format.
        if (editor_instance.upload_image(filepath) != True): # If file is invalid.
            self.change_label_text('[b] This is an invalid Image File!')

        # If file is valid.
        else:
            editor_screen = self.manager.get_screen('editor_screen')
            editor_screen.display_image()
            self.change_screen('editor_screen')

    # Called to change the label for the main window display text.
    def change_label_text(self, text):
        label1 = ""
        label1 = self.ids.message
        label1.text = text



# Image Editor Screen, Includes buttons for
class EditorScreen(Screen, screen_coordinator):

    # Calls on the Editor class to increase contrast
    def increase_contrast(self):
        editor_instance._increase_img_contrast()
        self.display_image()

    # Calls on the Editor class to decrease contrast
    def decrease_contrast(self):
        editor_instance._decrease_img_contrast()
        self.display_image()

    # Calls on the Editor class to increase sharpness
    def increase_sharpness(self):
        editor_instance._increase_img_sharpness()
        self.display_image()

    # Calls on the Editor class to decrease sharpness
    def decrease_sharpness(self):
        editor_instance._decrease_img_sharpness()
        self.display_image()

    # Custom funcion not supported by current python lib's need to create this
    def increase_shadows(self):
        pass

    # Custom funcion not supported by current python lib's need to create this
    def decrease_shadows(self):
        pass


    def display_image (self):
        # Set up the screen area to display the images
        area_image = self.ids.area_image
        area_image.clear_widgets()

        # Opening an Image Buffering for image rendering.
        # new_buffer = screen_coordinator.screen_img_buffer
        new_buffer = BytesIO()
        editor_instance.img.save (new_buffer, format = editor_instance.img_format)
        new_buffer.seek(0)

        # Using a CoreImage instance from the kivy.core.image class to render the display texture.
        core_img = CoreImage(new_buffer, ext = editor_instance.img_format.lower ())
        texture = core_img.texture
        new_buffer.close()

        # Displaying the buffered Image.
        img = Image()
        img.texture = texture

        # Adding the image widted to the Editor screen.
        area_image.add_widget(img)




#Running Everything here.
screen_T = screen_transitioner()
screen_T.add_widget(MainScreen(name='initial_screen'))
screen_T.add_widget(EditorScreen(name='editor_screen'))

class Program(App):
    title = 'Editor of Images'
    def build(self):
        return screen_T

if __name__ == '__main__':
    Program().run()
