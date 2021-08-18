from pytube import YouTube
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os


def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path


def down_load_video():
    url = line.text()
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(file_path())


app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(200, 200, 500, 400)
win.setWindowTitle("YT Downloader")

line = QtWidgets.QLineEdit(win)
line.setFixedWidth(300)
line.move(100, 80)

button = QtWidgets.QPushButton(win)
button.setText("Submit")
button.clicked.connect(down_load_video)
button.move(100, 150)

win.show()
sys.exit(app.exec_())








