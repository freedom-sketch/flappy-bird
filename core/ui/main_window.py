from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLayoutItem
from PySide6.QtGui import QIcon, QPixmap

from core.ui.scenes.menu import Menu


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.set_title("Flappy Bird")
        self.set_window_size("assets/sprites/background-day.png")
        self.set_icon("assets/icon.ico")

        # Центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Создание основного вертикального лэйаута
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.game_state = "menu"

        self.show_menu()
    
    def set_window_size(self, background_path: str) -> None:
        size = QPixmap(background_path).size()
        self.setFixedSize(size.width(), size.height())
    
    def set_icon(self, icon_path: str) -> None:
        self.setWindowIcon(QIcon(icon_path))
    
    def set_title(self, title) -> None:
        self.setWindowTitle(title)

    def show_menu(self) -> None:
        # Очищение текущего виджета
        self.clear_current_widget()

        self.game_state = "menu"

        # Сцена меню
        menu_scene = Menu()
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