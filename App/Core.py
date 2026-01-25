from abc import ABC, abstractmethod

from PySide6.QtCore import QRectF, QPointF
from PySide6.QtGui import QPixmap, QPainter, QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLayoutItem

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


class Sprite(ABC):
    def __init__(self, image_path: str | None, x: float=0, y: float=0) -> None:
        # Накладываем текстуру спрайту, если путь к изображению задан
        self.image_path = image_path
        if image_path:
            self.pixmap = QPixmap(image_path)
        else:
            # Если изображения нет, создаем пустое изображение-заглушку размером 64x64
            self.pixmap = QPixmap(64, 64)
        # Прямоугольник спрайта
        self.rect = QRectF(x, y, self.pixmap.width(), self.pixmap.height())
        self._visible: bool = True
        self._angle: float = 0.0
    
    @abstractmethod
    def update(self) -> None:
        pass

    def move_to(self, x: float, y: float) -> None:
        self.rect.moveTo(x, y)

    def draw(self, painter: QPainter) -> None:
        if not self._visible:
            return None

        # Сохранение текущего состояния рисовальщика
        painter.save()
        # Поворот рисовальщика относительно центра спрайта
        painter.translate(self.rect.center())
        # Поворот на заданный угол
        painter.rotate(self._angle)

        # Начальная точка рисования спрайта по x и y
        starting_x: int = int(-self.rect.width() / 2)
        starting_y: int = int(-self.rect.height() / 2)
        # Рисование спрайта
        painter.drawPixmap(starting_x, starting_y, self.pixmap)
    
    @property
    def x(self) -> float:
        return self.rect.x()

    @property
    def y(self) -> float:
        return self.rect.y()

    @property
    def center(self) -> QPointF:
        return self.rect.center()

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, a: float) -> None:
        self._angle = a

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, v: bool) -> None:
        self._visible = v