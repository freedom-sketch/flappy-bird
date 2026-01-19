import sys
from PySide6.QtWidgets import QApplication
from core.ui.main_window import MainWindow
from infra.config import Config

def main() -> None:
    # Загружаем конфигурацию
    cfg = Config.from_json_file("config.json")
    
    # Инициализация приложения
    app = QApplication()
    window = MainWindow(cfg)
    window.show()

    # Запуск главного цикла приложения
    sys.exit(app.exec())


if __name__ == "__main__":
    main()