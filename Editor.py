from os import path
from PIL import Image, ImageEnhance

class Editor_Class():#Editor Class Variables.
    img = None
    img_name = None
    img_format = None
    img_directory = None
    img_extension = None
    img_resolution = None

    #Change this name
    def restart(self):
        self.img = None
        self.img_name = None
        self.img_format = None
        self.img_directory = None
        self.img_extension = None
        self.img_resolution = None

    # Increases the contrast of the image by 10%
    def _increase_img_contrast(self):
        img_contrast_factor = 1.1
        working_img = ImageEnhance.Contrast(self.img)
        sharpened_image = working_img.enhance(img_contrast_factor)
        self.img = sharpened_image

    # Decreases the contrast of the image by 10%
    def _decrease_img_contrast(self):
        img_contrast_factor = 0.9
        working_img = ImageEnhance.Contrast(self.img)
        unsharpened_image = working_img.enhance(img_contrast_factor)
        self.img = unsharpened_image

    # Increases the sharpness of the image by 10%
    def _increase_img_sharpness(self):
        img_sharpenss_factor = 1.5
        working_img = ImageEnhance.Sharpness(self.img)
        sharpened_image = working_img.enhance(img_sharpenss_factor)
        self.img = sharpened_image

    # Decreases the sharpness of the image by 10%
    def _decrease_img_sharpness(self):
        img_sharpenss_factor = 0.5
        working_img = ImageEnhance.Sharpness(self.img)
        unsharpened_image = working_img.enhance(img_sharpenss_factor)
        self.img = unsharpened_image

    # Custom function not supported by python, will be added in later update.
    def increase_shadows():
        pass


    # Custom function not supported by python, will be added in later update.
    def decrease_shadows():
        pass


    # Uploads the image f
    def upload_image(self, image):#Edit this methid
        success_str = 'Image Opened Successfully!'
        failure_srt = 'Failed to Open Image.'
        try:
            self.img = Image.open(image)
            self.img_format = self.img.format
            self.img_directory = path.dirname(path.realpath(image))
            self.img_name, self.img_extension = path.splitext(path.basename(image))
            print(success_str)
            return True
        except:
            print(failure_srt)
            return False




editor_instance = Editor_Class()
