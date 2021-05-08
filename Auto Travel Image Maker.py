from PIL import Image
import random
random.random()
Backgrounds = ('Stock/Blue Background.jpg',
               'Stock/Blue Background.jpg',
               'Stock/RainBow Background Image.jpeg',
               'Stock/Russia.jpg',
               'Stock/Haunted_Image.jpg',
               'Stock/Garden.jpg')
My_Image = Image.open('Stock\My_Picture.png')
Random_Background = random.choice(Backgrounds)
Background = Image.open(Random_Background)
Background = Background.resize((610, 386))
Background.paste(My_Image, (0, 0), My_Image)
Background.show()
