"""For the program to run you must install kivy and sqlite3. This application is the most recent stable version of the manga app.
All button functionality works as expected if a bug is discovered while using this application please open and issue through the github
page and I will address it. Thanks!!
Future version improvements will be worked on in the TEST environment"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
import sqlite3
from kivy.uix.image import AsyncImage
from sqlite3 import Error
import webbrowser

def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return None
Builder.load_file('mangaAPPv2.kv')#file contains .kv builder fiel for GUI

class RootWidget(BoxLayout):
    """The below OjectProperty variables are used to create a reference to the input widgets
    within the mangaAPPv1.kv file."""
    name_input = ObjectProperty() 
    url_input = ObjectProperty()
    pic_input = ObjectProperty()
    delete_list= []#array used to create a delete list to remove multiple rows when pressing delete button. #NOTE- currently not functioning
    database= "data\pythonDB.db"#database containing app data
    
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
            pic= AsyncImage(source=row[3])#picture widgetmade with image address given by user located in col 3
            btn= Button(text='OPEN WEBPAGE', size_hint_y=None, id=row[2])#button widget 
            btn.bind(on_release=self.open_url)#gives btn widget action to run open_url method when pressed

            #The below is used to place the newly declared widgets onto the BoxLayout
            self.ids.grid.add_widget(lbl)
            self.ids.grid.add_widget(pic)
            self.ids.grid.add_widget(btn)

    def __init__(self, **kw):
        super(RootWidget, self).__init__(**kw)

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
            
        #The below declaration sets the text value for all inuts to empty
        self.ids.name.text= ''
        self.ids.url.text=''
        self.ids.pic.text=''

    def open_url(self, weblink):
        """This function opens a url given by the user after pressing the "open webpage" button"""
        webbrowser.open(weblink.id)

    def populate_delete_row(self, label_name, third):
        """This function populates the global variable array 'delete_list' to remove items when delete button is pressed.
        Pressing the label will change the color of the text to inidcate the item is set for deletion"""
        if (label_name.id in self.delete_list):
            #looks to see if label_name.id is in delete list is True if true then runs remove_delete_row function
            self.remove_delete_object(label_name)     
        else:
            label_name.text= '[b][color=#5253e2][ref=]'+label_name.id+'[/ref][/color][/b]'#change color of text
            label_name.texture_update()#updates color change 
            self.delete_list.append(label_name.id)#append selected item to delete_list
       
    def remove_delete_object(self, label_name): 
        """This function removes a label_name.id from the deleted list global variable. This function
        also changes the color back the original white color when the label is first populated""" 
        label_name.text='[color=#ffffff][ref=]'+label_name.id+'[/ref][/color]' #change color of text back to white color
        label_name.texture_update()#updates label widget texture
        self.delete_list.remove(label_name.id)#removes label_name.id from delete list

    def delete_row(self, **kwargs):
        """This function uses the delete list array to execute a delete statement according to the label ID of the 
        items within the list. """
        array= self.delete_list

        # create a database connection
        conn = create_connection(self.database)
        cur = conn.cursor()
        for row in array:
            cur.execute("DELETE FROM manga_list WHERE name in (?)", (row,))
        self.ids.grid.clear_widgets()#removes widgets from scroll view id of grid    
        with conn:
            self.select_all_tasks(conn)
        self.delete_list=[]#empty delete list for future use

class MainApp(App):
    def build(self):
        return RootWidget()

application= MainApp()
application.run()
