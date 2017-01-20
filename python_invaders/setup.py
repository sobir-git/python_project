application_title="Space Invaders" #name of application
main_python_file="space_invaders.py"#Name of python application
icon="spaceship_icon.png"#icon of application
include_files=["ammo.png", "ship.png", "ufo.png"]#files needed for applicatino
your_name= "Zachary Farley"
program_description="The retro space invaders game"

import sys

from cx_Freeze import setup, Executable

base=None
if sys.platform=="win32":
    base="Win32GUI"

setup (
            name= application_title
            version= "1.0"
            description=program_description
            author=your_name
            options-{"build_exe":{"icon":icon, "include_files":include_files}},
                executables=[Executable(main_python_file,base-base)]
)