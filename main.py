import sys
from PySide6.QtWidgets import QApplication
from core.ui.main_window import MainWindow
from infra.config import Config

def main() -> None:
    cfg = Config.from_json_file("config.json")
    app_settings = cfg.application
    
    app = QApplication()

    window = MainWindow(title=app_settings.title, w=app_settings.width,
                        h=app_settings.height)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()