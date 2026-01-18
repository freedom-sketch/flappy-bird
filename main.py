import sys
from PySide6.QtWidgets import QApplication
from core.ui.main_window import MainWindow


def main() -> None:
    app = QApplication()

    window = MainWindow(title="Flappy Bird")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()