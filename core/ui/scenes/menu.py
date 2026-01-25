from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QPalette


class Menu(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Устанавливаем фон
        background_size = self.set_background("assets/sprites/background-day.png")
        # Устанавливаем фиксированный размер виджета
        self.setFixedSize(background_size.width(), background_size.height())
        # Устанавливаем лэйаут
        vbox_layout = self.set_vbox_layout()

        # Добавляем изображение "Get Ready" и "Tap"
        get_ready_label = self.set_central_label("assets/sprites/get_ready.png")
        tap_label = self.set_central_label("assets/sprites/tap.png")

        vbox_layout.addWidget(get_ready_label)
        vbox_layout.addWidget(tap_label)

    def set_background(self, image_path: str) -> QSize:
        pixmap = QPixmap(image_path)
        # Настраиваем палитру для фона
        palette = self.palette()
        # Устанавливаем фоновое изображение
        palette.setBrush(QPalette.ColorRole.Window, pixmap)
        # Применяем палитру к виджету
        self.setPalette(palette)
        # Устанавливаем автозаполнение фона
        self.setAutoFillBackground(True)

        return pixmap.size()
    
    def set_vbox_layout(self) -> QVBoxLayout:
        # Создаем вертикальный лэйаут для кнопок
        layout = QVBoxLayout(self)
        # Устанавливаем отступы между объектами в лэйауте
        layout.setSpacing(16)
        # Устанавливаем отступы вокруг лэйаута
        layout.setContentsMargins(20, 20, 20, 20)
        # Устанавливаем выравнивание по центру
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        return layout

    def set_central_label(self, image_path: str) -> QLabel:
        label = QLabel()
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        return label