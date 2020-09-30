from .Minmax import MinMaxUi
from .Minmax import MinMax
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys

    ## Starting the QT5based application 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ## Creating Board object
    board = MinMax.Board()

    ## Creating MinMaxUi object
    ui = MinMaxUi.Ui_MainWindow(board)

    ## Creating the layout 
    ui.setupUi(MainWindow)

    ## Displaying the layout 
    MainWindow.show()

    ## Starting the game
    ui.start()

    ##Exit
    sys.exit(app.exec_())