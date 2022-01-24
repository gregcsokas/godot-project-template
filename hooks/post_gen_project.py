import shutil

from pathlib import Path
from collections import OrderedDict  # noqa

user_answers = dict(eval("{{cookiecutter}}"))

if user_answers["gdnative_libs"] != "yes":
    directory_path = Path().cwd() / 'gdnative_libs'
    if directory_path.exists() and directory_path.is_dir():
        shutil.rmtree(directory_path)

if user_answers["godot_4_project"] != "yes":
    directory_path = Path().cwd() / '.godot'
    if directory_path.exists() and directory_path.is_dir():
        shutil.rmtree(directory_path)