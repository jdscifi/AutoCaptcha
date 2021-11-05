from PIL import Image
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class AutoCaptcha:
    def __init__(self, imagePath=""):
        try:
            # use the image object for your operations
            self.imageObject = Image.open(imagePath)
        except Exception as e:
            logging.exception("Exception Image constructor", exc_info=True)
            print(e)

    def ImageShow(self):
        try:
            self.imageObject.show()
        except Exception as e:
            logging.exception("Exception Image Show", exc_info=True)
            print(e)

    def GrayUpScale(self):
        try:
            pass
            ## Smriti Code
        except Exception as e:
            logging.exception("Exception GrayUpScale", exc_info=True)
            print(e)
