from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QTransform

from src.config import PIPE_SPEED

class Pipe(QGraphicsPixmapItem):
    def __init__(self, x: float, y: float, is_top: bool = False) -> None:
        super().__init__()
        self.passed: bool = False
        self.is_top: bool = is_top
        
        pixmap: QPixmap = QPixmap("assets/sprites/pipe-green.png")
        
        if is_top:
            pixmap = pixmap.transformed(QTransform().scale(1.0, -1.0))
            
        self.setPixmap(pixmap)
        self.setPos(x, y)

    def update_pos(self) -> None:
        self.setX(self.x() - PIPE_SPEED)
        
    def is_offscreen(self) -> bool:
        return self.x() < -self.boundingRect().width()