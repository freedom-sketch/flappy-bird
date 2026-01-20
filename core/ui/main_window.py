from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLayoutItem
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon
from core.ui.scenes.menu import Menu
from infra.config import Config

class MainWindow(QMainWindow):
    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config

        self.setWindowTitle(config.application.title)
        self.setFixedSize(config.application.width, config.application.height)
        if config.application.icon_path:
            self.setWindowIcon(QIcon(config.application.icon_path))

        # Центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Создание основного вертикального лэйаута
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Изначальное состояние - меню
        self.game_state = "menu"

        # Создание цикла приложения
        self.game_timer = QTimer()
        self.game_timer.setInterval(16)
        self.game_timer.timeout.connect(self.update_game)

        self.show_menu()

    def update_game(self) -> None:
        pass

    def show_menu(self) -> None:
        # Очищение текущего виджета
        self.clear_current_widget()

        self.game_state = "menu"
        self.game_timer.stop()

        # Сцена меню
        menu_scene = Menu(config=self.config)
        self.main_layout.addWidget(menu_scene)

    def clear_current_widget(self) -> None:
        # Удаление текущего виджета из лэйаута
        if self.main_layout.count() > 0:
            # Берем первый элемент из лэйаута
            item: QLayoutItem = self.main_layout.takeAt(0)
            # Удаляем виджет, если он существует
            widget = item.widget()
            if widget:
                widget.deleteLater()