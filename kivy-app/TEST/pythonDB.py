from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
import sqlite3
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
Builder.load_file('pythonDB.kv')

class RootWidget(BoxLayout):
    name_input = ObjectProperty()
    url_input = ObjectProperty()
    manga_list = ObjectProperty()
    def select_all_tasks(self, conn):
           
        cur = conn.cursor()
        cur.execute("SELECT * FROM manga_list")
 
        rows = cur.fetchall()

        for row in rows:
            lbl= Label(text=row[0])
            btn= Button(text='OPEN WEBPAGE', height=40, size_hint_y=None, id=row[1])
            btn.bind(on_press=self.open_url)
            print(row[1])
            self.ids.grid.add_widget(lbl)
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
        new_name= self.name_input.text
        new_url= self.url_input.text
        new_row=[new_name,new_url]
        database= "C:\\Users\zfarley\Documents\Development\python_project\kivy-app\data\pythonDB.db"
        # create a database connection
        conn = create_connection(database)
        cur = conn.cursor()
        cur.execute("INSERT INTO manga_list VALUES(?, ?)", (manga_name, new_url))
        with conn:
            self.select_all_tasks(conn)
        self.ids.name.text= ''
        self.ids.url.text=''

    def open_url(self, weblink):
        database= "C:\\Users\zfarley\Documents\Development\python_project\kivy-app\data\pythonDB.db"
        # create a database connection
        conn = create_connection(database)
        cur = conn.cursor()
        print(self.ids)
        """webaddress= cur.execute("SELECT url FROM manga_list WHERE url='?'", (weblink))
        webbrowser.open(weblink)"""



class MainApp(App):
    def build(self):
        return RootWidget()

application= MainApp()
application.run()

