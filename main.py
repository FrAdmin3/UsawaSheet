import pyodbc
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

KV= """
MDScreen:
    name:"login"
    MDFloatLayout:
        MDLabel:
            id: Text_usawa
            text: "USAWA TIMESHEET"
            font_size: dp(20)
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            margin_y: 50
            padding_y: 50
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            color: "#F11E21"
        Image:
            source: "usawasheet.png"
            size_hint: (1, 0.3)
            halign: 'center'
            pos_hint: {"center_x": .5, "center_y": .85}
        MDTextField:
            id: EmployeeID
            hint_text: " Saisir matricule svp !"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: None
            icon_right: "account"
            width: dp(250)
            spacing:[dp(1), dp(1)]
        MDTextField:
            id: EmployeeID
            hint_text: " Saisir Mot de passe svp !"
            password: True
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            max_text_length: 15
            icon_right: "eye-off"
            width: dp(250)
        MDLabel:
            id: Text_usawa_footer
            text: "Copyright Kamoa SA"
            font_size: dp(15)
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {'center_x': 0.5, 'y': 0.09}
            color: 1, 0, 0.129,1
        MDRaisedButton:
            style: "filled"
            text: "Connexion"
            size_hint: None,None
            width:dp(150)
            height: dp(20)
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            on_release: root.authenticate(EmployeeID.text)

"""
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
        screen = Builder.load_string(KV)
        self.theme_cls.primary_palette ="Pink"
        self.theme_cls.primary_light_hue ="300"
        self.theme_cls.accent_palette ="Gray"
        self.theme_cls.accent_light_hue ="50"
        self.theme_cls.accent_hue ="700"
        self.theme_cls.material_style = "M2"
        return screen


UsawaApp().run()