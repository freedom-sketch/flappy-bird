from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtCore import Signal
from abc import abstractmethod

class BaseScene(QGraphicsScene):
    """Базовый класс сцены"""
    scene_change_signal = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setup_scene()
    
    @abstractmethod
    def setup_scene(self) -> None:
        pass