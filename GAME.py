import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QLabel, QHBoxLayout


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Press Ctrl + O', self)

        self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_open.activated.connect(self.on_open)

        self.shortcut_close = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_close.activated.connect(self.closeApp)  # or lambda : app.quit()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.resize(150, 150)

    def on_open(self):
        print('Ctrl O has been fired')

    def closeApp(self):
        app.quit()


app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())