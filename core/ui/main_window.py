from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QGraphicsView,
    QGraphicsView, QLayoutItem
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QColor, QPalette, QPainter


class MainWindow(QMainWindow):
    def __init__(self, title: str="App", w: int=900, h: int=600) -> None:
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

        # Создаем цикл игры
        self.game_timer = QTimer()
        self.game_timer.setInterval(16)
        self.game_timer.timeout.connect(self.update_game)

        # Отображаем меню
        self.show_menu()
    
    def update_game(self) -> None:
        if self.game_state == "playing" and self.current_scene:
            self.current_scene.update()
    
    def show_menu(self) -> None:
        # Очищаем сцену и останавливаем таймер
        self.clear_current_scene()
        self.game_state = "menu"
        self.game_timer.stop()

        #                    ⬇⬇⬇⬇⬇⬇⬇⬇⬇ Добавлю позже
        self.current_scene = MenuScene()
        self.view.setScene(self.current_scene)

        self.main_layout.addWidget(self.view)
        self.view.setFocus()
    
    def clear_current_scene(self) -> None:
        if self.main_layout.count() > 0:
            item: QLayoutItem = self.main_layout.takeAt(0)

            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.current_scene = None