"""This is version 4 TEST of the manga app ment to change the image load option from using a
web link to a local link. This will be testing the load file feature of kivy in 
attempt to load the picture using the image located in an image directory"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
from kivy.uix.image import AsyncImage
from sqlite3 import Error
import webbrowser
import os



def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "manga.db")
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()  # create sqlite cursor object allowing sql statements to be executed
        cur.execute("SELECT * FROM manga_list")
        imgdir= os.path.join(BASE_DIR, "images")
        if not os.path.exists(imgdir):
            os.makedirs(imgdir)
        return conn
    except Error as e:
        with conn:
            cur.execute("CREATE TABLE manga_list (id    INTEGER PRIMARY KEY,name  STRING,url   STRING,image STRING);")
        print("created previously missing table, please run application again")
        return None
Builder.load_string("""
#kivy `1.10.0`
<RootWidget>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    name_input: name
    url_input: url
    pic_input: pic
    BoxLayout:
        size_hint_y:None
        height: "40dp"
        Label:
            text: 'Name'
        TextInput:
            id: name
            focus: True
            hint_text: 'manga name'
        Label:
            text: 'Weblink'
        TextInput:
            id: url
            focus: True
            hint_text: 'manga url'
        Label:
            text:'Image url'
        TextInput:
            id: pic
            hint_text: 'image url'

    BoxLayout:
        size_hint_y:None
        height: "40dp"
        Button:
            text: 'Submit'
            size_hint_x: 15
            on_press: root.submit_manga()
        Button:
            text: 'Delete'
            size_hint_x: 15
            on_press: root.delete_row()
        Button:
            text: 'Instructions'
            size_hint_x: 15
            on_press: root.instructions()
        
    ScrollView:
        size_hint: (1, 1)
        height: 50
        id: scroll
        GridLayout:
            id: grid
            size_hint_y: None
            size_hint_x: 1
            height: self.minimum_height
            cols: 3
            padding: 10
            spacing: 10

    BoxLayout:
        size_hint_y:None
        height: "40dp"
        Button:
            text: 'Updates?'
            size_hint_x: 15
            on_press: root.manager.current = 'updates'
            
<update_screen>:
    # nam: str(updates)
    GridLayout:
        cols: 2

        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Show Data'
            on_press: app.show()
        ScrollView:
            size_hint: (1, 1)
            height: 50
            id: scroll
            GridLayout:
                id: grid
                size_hint_y: None
                size_hint_x: 1
                height: self.minimum_height
                cols: 3
                padding: 10
                spacing: 10

""")
class MenuScreen(Screen):
    pass
class update_screen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(update_screen(name='updates'))

class RootWidget(BoxLayout):
    """The below OjectProperty variables are used to create a reference to the input widgets
    within the mangaAPPv1.kv file."""
    name_input = ObjectProperty()
    url_input = ObjectProperty()
    pic_input = ObjectProperty()
    delete_list= []#array used to create a delete list to remove multiple rows when pressing delete button. #NOTE- currently not functioning
    #database= "pythonDB_TEST.db"#database containing app data
    img_delete_list=[]
    os.environ['KIVY_IMAGE']= 'pil,sdl2'
    database= "manga.db"
 
        
    def select_all_tasks(self, conn):
        """This method performs a select all SQL statment and populates the BoxLayout
        With the Button, Label and AsyncPicture widgets."""
        cur = conn.cursor()#create sqlite cursor object allowing sql statements to be executed
        
        cur.execute("SELECT * FROM manga_list")
        db_list = cur.fetchall()#creates list of manga_list table allowing for loop to run and populate the BoxLayout 
        """if statement added below is a test function that is going to be used all lbl, pic and btn
        widgets before repopulating them again. The function looks for the boolean var function_run to see
        if the function delete_row() has ran. *NOTE: Functionality still under works"""
        
        for row in db_list:
            """Label widget generated with font 30px and markup property. The markup allows the
            func. populate_delete_row to run when label is pressed"""
            lbl= Label(text='[ref='']' + row[1]+'[/ref]', id=row[1], font_size=30, markup=True, on_ref_press= self.populate_delete_row)
            pic= AsyncImage(source='images/' + row[3])#picture widgetmade with image address given by user located in col 3
            btn= Button(text='OPEN WEBPAGE', size_hint_y=None, id=row[2])#button widget 
            btn.bind(on_release=self.open_url)#gives btn widget action to run open_url method when pressed

            #The below is used to place the newly declared widgets onto the BoxLayout
            self.ids.grid.add_widget(lbl)
            self.ids.grid.add_widget(pic)
            self.ids.grid.add_widget(btn)

    def __init__(self, **kw):
        super(RootWidget, self).__init__(**kw)
        #database = "C:\\sqlite\db\pythonsqlite.db"
        #database= "C:\\Users\zfarley\Documents\Development\python_project\kivy-app\data\pythonDB.db"#location 1 DB connection

        # create a database connection
        conn = create_connection(self.database)
        with conn:
            self.select_all_tasks(conn)
    def submit_manga(self):
        """This function is called when the submit button is pressed. When pressed the user inputs are assigned to the below
        variables then an INSERT sql statement is called which adds the input into the manga_list table. Once the items are added to
        the table a new widget instance for lbl, btn and asnycimage is created and populated onthe BoxLayout. After adding the widgets
        the form inputs are set to NULL."""
        # The below variables are used to obtain the 3 inputs from the users
        manga_name = self.name_input.text
        pic_name= self.pic_input.text
        new_url= self.url_input.text
        
        # create a database connection
        conn = create_connection(self.database)
        cur = conn.cursor()
        cur.execute("INSERT INTO manga_list VALUES(NULL, ?, ?, ?)", (manga_name, new_url, pic_name))
        self.ids.grid.clear_widgets()#removes widgets from scroll view id of grid
        with conn:
            self.select_all_tasks(conn)
        """cur.execute("SELECT * FROM manga_list ORDER BY id DESC limit 1")
        new_line= cur.fetchall()#using previous SELECT statment this turns the data into an iterable list
        for item in new_line:
            lbl= Label(text='[ref='']' + item[1]+'[/ref]', id=item[1], font_size=30, markup=True, on_ref_press=self.populate_delete_row)
            pic= AsyncImage(source=item[3])#picture widgetmade with image address given by user located in col 3
            btn= Button(text='OPEN WEBPAGE', size_hint_y=None, id=item[2])#button widget 
            btn.bind(on_release=self.open_url)#gives btn widget action to run open_url method when pressed
                
            #The below is used to place the newly declared widgets onto the BoxLayout
            self.ids.grid.add_widget(lbl)
            self.ids.grid.add_widget(pic)
            self.ids.grid.add_widget(btn)"""
            
        #The below declaration sets the text value for all inuts to empty
        self.ids.name.text= ''
        self.ids.url.text=''
        self.ids.pic.text=''

    def open_url(self, weblink):
        """This function opens a url given by the user"""
        webbrowser.open(weblink.id)

    def populate_delete_row(self, label_name, third):
        """This function populates the array 'delete_list' to remove items when delete button is pressed.
        Pressing the DELETE button will also change the color of the text to inidcate the item is set for deletion
        *NOTE: Functionality still under works"""
        if (label_name.id in self.delete_list):
            #looks to see if label_name.id is in delete list is True if true then runs remove_delete_row function
            self.remove_delete_object(label_name)
            print('if statement in populate delete row')
        else:
            print('else statement in populate delete row')
            label_name.text= '[b][color=#5253e2][ref=]'+label_name.id+'[/ref][/color][/b]'#change color of text
            label_name.texture_update()#updates color change 
            self.delete_list.append(label_name.id)#append selected item to delete_list
       
    def remove_delete_object(self, label_name): 
        """This function removes a label_name.id from the deleted list global variable. This function
        also changes the color back the original white color when the label is first populated
        *NOTE- currently under development only works partially""" 
        print ('remove delete object ran')
        label_name.text='[color=#ffffff][ref=]'+label_name.id+'[/ref][/color]' #change color of text back to white color
        label_name.texture_update()#updates label widget texture
        self.delete_list.remove(label_name.id)#removes label_name.id from delete list
        print(self.delete_list)
        self.function_run= True

    def delete_row(self, **kwargs):
        """This function uses the delete list array to execute a delete statement according to the label ID of the 
        items within the list. *NOTE: Currently not functioning need to include a DELETE widget functionility to remove
        widgets that are no longer within the manga_list table """
        array= self.delete_list

        # create a database connection
        conn = create_connection(self.database)
        cur = conn.cursor()
        for row in array:
            cur.execute("SELECT image FROM manga_list WHERE name in (?)", (row,))
            img_list= cur.fetchall()
            img_string= str(img_list).strip('([,\'])')
            os.remove('images/' + img_string)
            print(img_string)
            cur.execute("DELETE FROM manga_list WHERE name in (?)", (row,))
            
        self.ids.grid.clear_widgets()#removes widgets from scroll view id of grid    
        with conn:
            self.select_all_tasks(conn)
        self.delete_list=[]#empty delete list for future use
    def instructions(self, **kwargs):
        popup = Popup(title='Instructions',
        content=Label(
            text='WELCOME TO THE MANGA APP!!! \nTo use this app you need 3 things\n1. title \n2.a web URL\n3.Image name (*include extension .png, .img...etc)\n(*see note below) \nOnce you save a new line will appear in the menu.\n*NOTE: You must manually save an image\nto the images directory\nfor the pic to appear in the app \nENJOY!!'),
        size_hint=(None, None), size=(400, 300))
        popup.open()
        
        

class MainApp(App):
    def build(self):
        return RootWidget()

application= MainApp()
application.run()

