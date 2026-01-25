import sys

from PySide6.QtWidgets import QApplication

from core.ui.main_window import MainWindow


def main() -> None:
    # Инициализация приложения
    app = QApplication()
    window = MainWindow()
    window.show()

    # Запуск главного цикла приложения
    sys.exit(app.exec())


if __name__ == "__main__":
    main()