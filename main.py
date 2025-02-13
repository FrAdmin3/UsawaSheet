import pyodbc
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen


Window.softinput_mode = "below_target"
class Login(MDScreen):
    def __init__(self,**kwargs):
        super(Login,self).__init__(**kwargs)
        Window.bind(on_keyboard =self.quit)
    def quit(self,window,key,*args):
        if (key == 27):
            MDApp.get_running_app().stop()
    def authenticate(self, EmployeeID):
        if EmployeeID == '' or EmployeeID != EmployeeID:
            self.show_dialog("Echec de Connection",
                               "Veuillez saisir correctement votre matricule ou votre mot de passe")
        else:
            try:
                conn = pyodbc.connect(
                    'DRIVER={SQL Server};'
                    'SERVER=KAMWVTASQL01;'
                    'DATABASE=Pointage;'
                    'UID=Developpeur;'
                    'PWD=123'
                )
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM dbo.Pointage WHERE EmployeeID=? ", EmployeeID)
                result = cursor.fetchone()
                if result:
                    #self.switch_to('data')
                    self.show_dialog("Echec de Connection",
                                     " vous etez connecter ")
                else:
                    pass
                conn.close()
            except pyodbc.Error as e:
                self.show_dialog("Echec de Connection",
                                 "la base de donnee est indisponible pour l'instant  "
                                  "Veuillez conctatez l'equipe T&A svp !")

    def show_dialog(self,title,text):
            self.dialog = MDDialog(
                title=title,
                text=text,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss()  # Fermer la boîte de dialogue
                    ),
                ],
            )
            self.dialog.open()

class UsawaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette ="Pink"
        self.theme_cls.primary_light_hue ="300"
        self.theme_cls.accent_palette ="Gray"
        self.theme_cls.accent_light_hue ="50"
        self.theme_cls.accent_hue ="700"
        self.theme_cls.material_style = "M2"


UsawaApp().run()