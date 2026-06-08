from typing import Optional, TYPE_CHECKING
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QIcon

from src.config import WINDOW_WIDTH, WINDOW_HEIGHT

if TYPE_CHECKING:
    from src.engine import GameEngine

class MainWindow(QGraphicsView):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Flappy Bird")
        self.setWindowIcon(QIcon("assets/favicon.ico"))
        
        self.scene: QGraphicsScene = QGraphicsScene(self)
        self.setScene(self.scene)
        
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT) 
        self.scene.setSceneRect(0.0, 0.0, float(WINDOW_WIDTH), float(WINDOW_HEIGHT))
        
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.engine: Optional['GameEngine'] = None

    def set_engine(self, engine: 'GameEngine') -> None:
        self.engine = engine

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Space:
            if self.engine is not None:
                self.engine.handle_input()
        super().keyPressEvent(event)