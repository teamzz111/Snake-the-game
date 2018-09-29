from cx_Freeze import setup, Executable
import sys
executables = [cx_Freeze.Executable("Snake.py", base = "Win32GUI")]

build_exe_options = {"packages": ["pygame"], "include_files": ["OpenSans-Light.ttf","25.jpg","icon.png","FONDO jp-01.png","song.ogg","Sonig.ogg"]}


cx_Freeze.setup(
    name = "Snake",
    version = "0.1",
    description = "Juego proporcionado por Andrés largo con los jóvenes programdores",
    options = {"build_exe": build_exe_options},
    executables = executables
)