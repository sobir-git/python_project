"""This is the version 5 Production version of the manga app current updates include 
a second screen to pull in updated "hot" updates from the source mangatown.com. After
running reload a label and button populate where the button opens the url leading to the
new update"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
from kivy.uix.image import AsyncImage
from sqlite3 import Error
import webbrowser
import os
import urllib.request
from bs4 import BeautifulSoup


def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """

    # try two times
    for i in (1, 2):
        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "manga.db")
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()  # create sqlite cursor object allowing sql statements to be executed
            cur.execute("SELECT * FROM manga_list")
            imgdir = os.path.join(BASE_DIR, "images")
            if not os.path.exists(imgdir):
                os.makedirs(imgdir)
            return conn
        except Error as e:
            with conn:
                cur.execute("CREATE TABLE manga_list (id    INTEGER PRIMARY KEY,name  STRING,url   STRING,image STRING);")
            print("created previously missing table, please run application again")
    return None


# Below is the Kivy layout of the GUI for the App
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
            on_press: root.delete_selection()
        Button:
            text: 'Instructions'
            size_hint_x: 15
            on_press: root.instructions()
        
    ScrollView:
        size_hint: (1, 1)
        height: 50
        id: scroll
        BoxLayout:
            id: box
            orientation: 'vertical'
            size_hint_y: None
            size_hint_x: 1
            height: self.minimum_height
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
    
    BoxLayout:
        id: update_grid
        padding: 10
        spacing: 10
        orientation: "vertical"
        Button:
            text: 'Back to menu'
            size_hint: (1, 0.25)
            on_press: root.manager.current = 'main'
        Button:
            text: 'RELOAD DATA'
            size_hint: (1, 0.25)
            on_press: root.update_list()
        ScrollView:
            size_hint: (1, 1)
            height: 50
            GridLayout:
                id: grid
                size_hint_y: None
                size_hint_x: 1
                height: self.minimum_height
                cols: 2
                padding: 10
                spacing: 10


<Row>:
    canvas:
        Color:
            rgb: (.3, .3, .3) if self.selected else (.1, .1, .1)
        Rectangle:
            size: self.size
            pos: self.pos

    orientation: 'horizontal'
    size_hint_y: None
    height: 100
    padding: 5
    spacing: 5
    Label:
        text: root.name
    AsyncImage:
        source: root.image
    Button:
        text: "Open Webpage"
        on_release: root.open_url()

""")

"""The below class is the second screen that appears when pressing the "updates?" button
The class runs function that web crawls through the url https://www.mangatown.com/latest/text
once in the website it pulls down the HOT updates from the website and takes the name and url
and adds a txt and button widget to the screen respectively."""

class update_screen(Screen):
    def update_list(self, **kwargs):
        url = 'http://www.mangatown.com/latest/text/'  # URL to pull information from
        # add header to prevent web crawl from being blockeds
        request = urllib.request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response, 'html.parser')  # Parse entire webpage

        # finds div that contains chapter updates
        chapter_list = soup.find('div', attrs={'class': 'manga_text_content'})

        # compiles chapter_list and find all 'HOT' updates
        hot_updates = chapter_list.find_all('span', attrs={'class': 'hot'})
        """Below loop iterates through the list of updates and takes the parent 
        HTMl tag of <span class="hot">HOT</span> Then obtains the hyperlink and name of the items
        within the hot chapter list"""
        self.ids.grid.clear_widgets()#removes widgets from scroll view id of grid

        for item in hot_updates:
            parent_of_updates = item.parent  # obtain parent tag of class="hot" tag
            content_of_parent = parent_of_updates.contents  # display contents of parent tag
            # contains url of updated manga
            update_url = content_of_parent[1]['href']

            # if url is like "//www.google.com", then remove first two chars
            if update_url.startswith('//'):
                update_url = update_url[2:]

            # contains name of updated manga
            updated_name = content_of_parent[1]['rel']
            lbl = Label(text=str(updated_name).strip('([,\'])'), font_size=30)
            # adds button with url as ID and text Open webpage
            btn = Button(text='Open Webpage', id=update_url, size_hint_y=None)
            # run open_url function when selecting button
            btn.bind(on_release=self.open_url)

            # populate widgets to screen
            self.ids.grid.add_widget(lbl)
            self.ids.grid.add_widget(btn)

    def open_url(self, button):
        """This function opens a url of the updated manga"""
        webbrowser.open(button.id)

    pass


class Row(BoxLayout):
    """This class represents the entries in a row, containing manga name, manga image, manga url.
    Subclasses BoxLayout, contains three fields.
    Attributes:
        name: name of manga (StringProperty)
        image: image filename (StringProperty)
        url: (StringProperty)
        ID: corresponding id in database (NumericProperty)
        selected: state of being selected (BooleanProperty)
    """
    name = StringProperty()
    image = StringProperty()
    url = StringProperty()
    ID = NumericProperty()
    selected = BooleanProperty(False)

    def open_url(self, *args):
        """This function opens a url given by the user"""
        webbrowser.open(self.url)

    def on_touch_down(self, touch):
        """ This function changes self.selected attribute when row is touched(or clicked) """
        if super().on_touch_down(touch):
            return True

        if self.collide_point(*touch.pos):
            self.selected = (True, False)[self.selected]
            return True

class main_screen(Screen):
    pass


class MenuScreen(Screen):
    pass


class RootWidget(BoxLayout, Screen):
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
        cur = conn.cursor()  # create sqlite cursor object allowing sql statements to be executed

        cur.execute("SELECT * FROM manga_list")
        # creates list of manga_list table allowing for loop to run and
        # populate the BoxLayout
        db_list = cur.fetchall()
        """if statement added below is a test function that is going to be used all lbl, pic and btn
        widgets before repopulating them again. The function looks for the boolean var function_run to see
        if the function delete_row() has ran. *NOTE: Functionality still under works"""

        for row in db_list:
            """Label widget generated with font 30px and markup property. The markup allows the
            func. populate_delete_row to run when label is pressed"""
            # picture widgetmade with image address given by user located in
            # col 3

            # check if the file is local, i.e in 'images' folder then load it
            # otherwise treat the path like web url
            local_path = os.path.join('images', row[3])
            if os.path.exists(local_path):
                image_path = local_path
            else:
                image_path = row[3]

            # create row
            row = Row(ID=row[0], name=row[1], image=image_path, url=row[2])
            row.bind(selected=self.update_delete_list)
            self.ids.box.add_widget(row)


    def __init__(self, **kw):
        super(RootWidget, self).__init__(**kw)
        #database = "C:\\sqlite\db\pythonsqlite.db"
        # database= "C:\\Users\zfarley\Documents\Development\python_project\kivy-app\data\pythonDB.db"#location 1 DB connection
        # create a database connection
        conn = create_connection(self.database)
        with conn:
            self.select_all_tasks(conn)

    def submit_manga(self):
        """This function is called when the submit button is pressed. When pressed the user inputs are assigned to the below
        variables then an INSERT sql statement is called which adds the input into the manga_list table. Once the items are added to
        the table a new row widget instance is created and populated on the BoxLayout. After adding the widgets
        the form inputs are set to NULL."""
        # The below variables are used to obtain the 3 inputs from the users
        manga_name = self.name_input.text
        pic_name = self.pic_input.text
        new_url = self.url_input.text

        # create a database connection
        conn = create_connection(self.database)
        cur = conn.cursor()
        if(manga_name == '' or pic_name =='' or new_url== ''):
            popup = Popup(title='WARNING',
            content=Label(
            text='Please enter a value in ALL fields!!'),
            size_hint=(None, None), size=(400, 300))
            popup.open()
        else:
            cur.execute("INSERT INTO manga_list VALUES(NULL, ?, ?, ?)", (manga_name, new_url, pic_name))
            self.ids.box.clear_widgets() #removes widgets from scroll view id of grid
            with conn:
                self.select_all_tasks(conn)

            #The below declaration sets the text value for all inuts to empty
            self.ids.name.text= ''
            self.ids.url.text=''
            self.ids.pic.text=''
        
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
            

    def open_url(self, weblink):
        """This function opens a url given by the user"""
        webbrowser.open(weblink.id)

    def update_delete_list(self, row, selected):
        """This function populates the array 'delete_list' to remove
        rows when delete button is pressed."""

        if selected:
            self.delete_list.append(row)
        else:
            self.delete_list.remove(row)

    def delete_selection(self):
        """ The function handles deletion of selected rows.
        It deletes corresponding widgets.
        It deletes corresponding data from database.

        Note: For now it is not deleting from database, I don't know why :(.
        """

        # delete selected widgets(stored in self.delete_list) from scrollview
        box = self.ids.box
        for row in self.delete_list:
            box.remove_widget(row)

        # delete from database
        conn = create_connection(self.database)
        cur = conn.cursor()
        for row in self.delete_list:
            cur.execute(
                "SELECT image FROM manga_list WHERE id == ?", (row.ID, ))
            img_string = cur.fetchall()[0][0]

            cur.execute("DELETE FROM manga_list WHERE id == ?", (row.ID,))

            # try to delete image
            try:
                os.remove(os.path.join('images', img_string))
            except FileNotFoundError:  # prevent crash on finding file
                pass

        self.delete_list.clear()

    def instructions(self, **kwargs):
        popup = Popup(title='Instructions',
                      content=Label(
                          text='WELCOME TO THE MANGA APP!!! \nTo use this app you need 3 things\n1. title \n2.a web URL\n3.Image name (*include extension .png, .img...etc)\n(*see note below) \nOnce you save a new line will appear in the menu.\n*NOTE: You must manually save an image\nto the images directory\nfor the pic to appear in the app \nENJOY!!'),
                      size_hint=(None, None), size=(400, 300))
        popup.open()

    def update_list(self, **kwargs):
        url= 'http://www.mangatown.com/latest/text/'#URL to pull information from
        request= urllib.request.Request(url)
        response= urllib.request.urlopen(request)
        soup = BeautifulSoup(response, 'html.parser')#Parse entire webpage

        chapter_list = soup.find('div', attrs={'class':'manga_text_content'})#finds div that contains chapter updates

        hot_updates = chapter_list.find_all('span', attrs={'class':'hot'})#compiles chapter_list and find all 'HOT' updates

        """Below loop iterates through the list of updates and takes the parent HTMl
        tag of <span class="hot">HOT</span> Then obtains the hyperlink and name of the items
        within the hot chapter list"""
        for item in hot_updates:
            parent_of_updates= item.parent #obtain parent tag of class="hot" tag
            content_of_parent= parent_of_updates.contents #display contents of parent tag
            update_url= content_of_parent[1]['href'] #contains url of updated manga
            updated_name= content_of_parent[1]['rel']#contains name of updated manga
            lbl= Label(text=updated_name, font_size=30)
            self.ids.update_grid.add_widget(lbl)
            print('url: ' + update_url + ' Name: ' + str(updated_name))


sm = ScreenManager()
#Ssm.add_widget(MenuScreen(name='menu'))
sm.add_widget(RootWidget(name='main'))
sm.add_widget(update_screen(name='updates'))


class MainApp(App):
    def build(self):
        app_class = RootWidget()
        return sm


if __name__ == '__main__':
    MainApp().run()
