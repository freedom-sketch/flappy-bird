from core.ui.scenes.base_scene import BaseScene
from PySide6.QtGui import QColor

class MenuScene(BaseScene):
    def setup_scene(self) -> None:
        self.setBackgroundBrush(QColor(255, 255, 255))