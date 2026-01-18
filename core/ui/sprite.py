from PySide6.QtCore import QRectF, QPointF
from PySide6.QtGui import QPixmap, QPainter
from abc import ABC, abstractmethod


class Sprite(ABC):
    def __init__(self, image_path: str | None, x: float=0, y: float=0) -> None:
        self.image_path = image_path
        if image_path:
            self.pixmap = QPixmap(image_path)
        else:
            QPixmap(64, 64)
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

        painter.save()
        painter.translate(self.rect.center())
        painter.rotate(self._angle)

        starting_x: int = int(-self.rect.width() / 2)
        starting_y: int = int(-self.rect.height() / 2)
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