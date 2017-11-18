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
"""
def select_all_tasks(conn):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM manga_list")
 
    rows = cur.fetchall()

    for row in rows:
        print(row)"""
"""
def main():
    #database = "C:\\sqlite\db\pythonsqlite.db"
    database= "C:\\Users\zfarley\Documents\Development\python_project\kivy-app\data\pythonDB.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("2. Query all tasks")
        select_all_tasks(conn)
 """
"""
if __name__ == '__main__':
    main()
"""
Builder.load_file('mangaAPPv1.kv')

class RootWidget(BoxLayout):
    name_input = ObjectProperty()
    url_input = ObjectProperty()
    manga_list = ObjectProperty()
    pic_input = ObjectProperty()
    row_label= []
    def select_all_tasks(self, conn):
           
        cur = conn.cursor()
        cur.execute("SELECT * FROM manga_list")
 
        rows = cur.fetchall()

        for row in rows:
            lbl= Label(text='[ref='']' + row[0]+'[/ref]', id=row[0], font_size=30, markup=True, on_ref_press=self.populate_delete_row)
            pic= AsyncImage(source=row[2])
            btn= Button(text='OPEN WEBPAGE', size_hint_y=None, id=row[1])
            btn.bind(on_release=self.open_url)
            
            self.ids.grid.add_widget(lbl)
            self.ids.grid.add_widget(pic)
            self.ids.grid.add_widget(btn)

    def __init__(self, **kw):
        super(RootWidget, self).__init__(**kw)
        #database = "C:\\sqlite\db\pythonsqlite.db"
        database= "C:\\Users\zfarley\Documents\Development\python_project\kivy-app\data\pythonDB.db"
        # create a database connection
        conn = create_connection(database)
        with conn:
            self.select_all_tasks(conn)
    def submit_manga(self):
        # Get the student name from the TextInputs
        manga_name = self.name_input.text
        pic_name= self.pic_input.text
        new_url= self.url_input.text
        
        database= "C:\\Users\zfarley\Documents\Development\python_project\kivy-app\data\pythonDB.db"
        # create a database connection
        conn = create_connection(database)
        cur = conn.cursor()
        cur.execute("INSERT INTO manga_list VALUES(?, ?, ?)", (manga_name, new_url, pic_name))
        with conn:
            self.select_all_tasks(conn)
        self.ids.name.text= ''
        self.ids.url.text=''
        self.ids.pic.text=''

    def open_url(self, weblink):
        webbrowser.open(weblink.id)

    def populate_delete_row(self, label_name, third):
        """This function only populates the items to delete once the delete button is pressed. It should 
        also change the color of the text to inidcate the item is set for deletion"""
        label_name.text= '[color=#5253e2]'+label_name.text+'[/color]'
        label_name.texture_update()
        self.row_label.append(label_name.id)
        
        

    def delete_row(self, **kwargs):
        """this function takes the click instance of a label and populates an array with the label text
        then a SQL DELETE statement runs using the label names within the array. Once the deletion finishes
        the array is then set to empty again"""
        array= self.row_label
        database= "C:\\Users\zfarley\Documents\Development\python_project\kivy-app\data\pythonDB.db"
        # create a database connection
        conn = create_connection(database)
        cur = conn.cursor()
        for row in array:
            cur.execute("DELETE FROM manga_list WHERE name in (?)", (row,))
            
        with conn:
            self.select_all_tasks(conn)
        self.row_label=[]

            



class MainApp(App):
    def build(self):
        return RootWidget()

application= MainApp()
application.run()

