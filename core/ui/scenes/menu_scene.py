from core.ui.scenes.base_scene import BaseScene
from PySide6.QtGui import QColor

class MenuScene(BaseScene):
    def __init__(self) -> None:
        super().__init__()
        self.setup_scene()

    def setup_scene(self) -> None:
        self.setBackgroundBrush(QColor(255, 255, 255))