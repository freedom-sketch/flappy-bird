from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QGraphicsView,
    QGraphicsView, QLayoutItem
)
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter
from core.ui.scenes.menu_scene import MenuScene

class MainWindow(QMainWindow):
    def __init__(self, title: str, w: int, h: int) -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(w, h)

        # Устанавливаем центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(5)

        # Создаем атрибут сцены и ее отображателя
        self.current_scene = None
        self.view = QGraphicsView()
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing |
                                QPainter.RenderHint.TextAntialiasing |
                                QPainter.RenderHint.SmoothPixmapTransform |
                                QPainter.RenderHint.LosslessImageRendering, True)
        
        self.game_state = "menu"

        # Создаем цикл приложения
        self.game_timer = QTimer()
        self.game_timer.setInterval(16)
        self.game_timer.timeout.connect(self.update_game)

        # Отображаем меню
        self.show_menu()
    
    def update_game(self) -> None:
        if self.current_scene:
            self.current_scene.update()
    
    def show_menu(self) -> None:
        # Очищаем сцену и останавливаем таймер
        self.clear_current_scene()

        self.game_state = "menu"
        self.game_timer.stop()
        self.current_scene = MenuScene()

        self.view.setScene(self.current_scene)
        self.view.fitInView(self.current_scene.sceneRect())
        self.view.setFocus()
 
        self.main_layout.addWidget(self.view)

    
    def clear_current_scene(self) -> None:
        if self.main_layout.count() > 0:
            item: QLayoutItem = self.main_layout.takeAt(0)

            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.current_scene = None