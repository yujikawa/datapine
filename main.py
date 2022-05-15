import kivy
import japanize_kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from operators.sqlite_operator import SqliteOperator
from operators.db_connection import DBConnection

class DatapineApp(App):
    pass


if __name__ == '__main__':
    DatapineApp().run()
