from kivy.app import App
from kivy.core import text
from kivy.core.text import markup
from numpy import source
import pytesseract
import pyperclip
from PIL import ImageGrab
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput, TextInputCutCopyPaste
from kivy.uix.relativelayout import RelativeLayout 

class ImagetoText(App):

    def build(self):
        self.window =RelativeLayout(size =(500, 500)) 
          
        self.window.rows=2
        
        self.window.size_hint=(1,1)
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}
        self.headd=Label(text="[color=FFFFFF]Image To [/color][color=FF69B4]Text Converter[/color]",
                                markup = True,
                            font_size=78,  
                            color="pink",
                            padding_y=(10,10),
                            pos_hint={"center_x":0.5,"center_y":0.9},
                            size_hint=(0.24,0.24)
                                   )
        self.window.add_widget(self.headd)
        self.window.add_widget(Image(source=r'D:\repeat\back.jpg',size_hint=(0.8,1),pos_hint={"center_x":0.30,"center_y":0.4}))
        self.userinput=TextInput(          
            size_hint=(0.42,0.52),
            background_color="white",
            background_normal = "white",
            pos_hint={"center_x":0.3,"center_y":0.40}

        )
        
     
      
        self.window.add_widget( self.userinput)                    
    
        
       
        self.buttondemo=Button(text="[color=000000]Get [/color][color=FF1493]Text[/color]",
                              markup=True,
                              font_size=50,
                               size_hint =(0.20,0.20),
                               
                               background_color="white",
                               background_normal=r'D:\repeat\eef.png',
                               color="black",
                               pos_hint={'center_x':0.85,'center_y':0.550}     ,
                               
          
                                  )
        self.buttondemo.bind(on_press=self.callback)
        self.window.add_widget(self.buttondemo)    
        self.buttoncopy=Button(text="[color=000000]Copy [/color][color=FF0000]Text[/color]",
                              markup=True,
                              font_size=50,
                               size_hint =(0.20,0.20),
                               
                               background_color="lightgreen",
                               background_normal=r'D:\repeat\ff.jpg',
                               color="black",
                               pos_hint={'center_x':0.85,'center_y':0.300}     ,
                               
          
                                  )
        self.buttoncopy.bind(on_press=self.copyer)
        self.window.add_widget(self.buttoncopy) 
        return self.window

    def copyer(self,instance):
        pyperclip.copy(self.userinput.text)
  

    def callback(self,instance):
        output_path=r'C:\Users\Vikram\Desktop\Calender\given.png'
        im=ImageGrab.grabclipboard()
        try:
            im.save(output_path,'PNG')
            try:
                from PIL import Image
            except ImportError:
                import Image 
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
            string=pytesseract.image_to_string(Image.open(output_path)).strip()
            self.userinput.text=string
            
        except:
            self.userinput.text="Image is not copied in clipboard"

if __name__ == "__main__":
    ImagetoText().run()

