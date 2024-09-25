from cx_Freeze import setup, Executable
import sys
import os

build_exe_options = {
    "packages": ["os", "sys", "pystyle", "PyQt5", "PyQt5.QtWebEngineWidgets"],
    "include_files": [] 
}

setup(
    name="NebulaBrowser",
    version="0.1",
    description="A simple web browser using PyQt5. Open-sourced.",
    options={"build_exe": build_exe_options},
    executables=[Executable("nebula.py", base=None)]
)
