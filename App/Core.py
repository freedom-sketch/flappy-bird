from PySide6.QtCore import QRectF, QPointF, Qt
from PySide6.QtGui import QPixmap, QPainter, QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLayoutItem, QGraphicsPixmapItem

from App.Scenes import Menu


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


class Bird(QGraphicsPixmapItem):
    def __init__(self, pixmap, x, y) -> None:
        super().__init__(pixmap)
        self.setPos(x, y)
        self.setTransformationMode(Qt.TransformationMode.SmoothTransformation)

        self.speed_y = 0
        self.gravity = 0.5
        self.flap_power = -9.0
        self.max_fall_speed = 12.0

    def update(self) -> None:
        self.speed_y += self.gravity
        self.speed_y = min(self.speed_y, self.max_fall_speed)
        
        new_y = self.y() + self.speed_y
        self.setPos(self.x(), new_y)