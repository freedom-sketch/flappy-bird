import sys
from PySide6.QtWidgets import QApplication
from src.mainwindow import MainWindow

from src.engine import GameEngine

def main() -> None:
    app: QApplication = QApplication(sys.argv)
    
    window: MainWindow = MainWindow()
    engine: GameEngine = GameEngine(window)
    
    window.set_engine(engine)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()