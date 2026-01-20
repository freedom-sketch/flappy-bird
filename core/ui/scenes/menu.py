from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPalette
from infra.config import Config

class Menu(QWidget):
    def __init__(self, config: Config) -> None:
        super().__init__()

        # Инициализация размеров и фона
        self.w = config.application.width
        self.h = config.application.height

        # Устанавливаем фиксированный размер виджета
        self.setFixedSize(self.w, self.h)

        # Устанавливаем фон меню
        if config.application.menu_background_path:
            pixmap = QPixmap(config.application.menu_background_path)
            # Настраиваем палитру для фона
            palette = self.palette()
            # Устанавливаем фоновое изображение
            palette.setBrush(QPalette.ColorRole.Window, pixmap)
            # Применяем палитру к виджету
            self.setPalette(palette)
            # Устанавливаем автозаполнение фона
            self.setAutoFillBackground(True)
        else:
            self.setStyleSheet("background-color: white;")

        # Создаем вертикальный лэйаут для кнопок
        layout = QVBoxLayout(self)
        # Устанавливаем отступы между объектами в лэйауте
        layout.setSpacing(16)
        # Устанавливаем отступы вокруг лэйаута
        layout.setContentsMargins(20, 20, 20, 20)
        # Устанавливаем выравнивание по центру
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        for text in ["Старт", "Выход"]:
            btn = QPushButton(text)
            btn.setFixedSize(220, 60)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    background: #2a82da;
                    color: white;
                    border-radius: 10px;
                }
                QPushButton:hover { background: #3a92ea; }
            """)
            layout.addWidget(btn)