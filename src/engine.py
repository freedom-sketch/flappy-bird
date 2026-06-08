from typing import List, Optional
from PySide6.QtCore import QObject, QTimer, QRectF, Qt
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
import random

from src.bird import Bird
from src.pipe import Pipe
from src.mainwindow import MainWindow
from src.config import *

class GameEngine(QObject):
    def __init__(self, view: MainWindow) -> None:
        super().__init__()
        self.view: MainWindow = view
        self.scene = view.scene
        self.state: str = "MENU"
        
        self.timer: QTimer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(FPS_INTERVAL)
        
        self.pipes: List[Pipe] = []
        self.frames: int = 0
        
        self.bird: Optional[Bird] = None
        
        self.score: int = 0
        self.score_items: List[QGraphicsPixmapItem] = []
        
        self.init_environment()
        self.show_menu()

    def init_environment(self) -> None:
        # Фон масштабируем под окно
        bg_pixmap = QPixmap("assets/sprites/background-day.png").scaled(
            WINDOW_WIDTH, WINDOW_HEIGHT, Qt.AspectRatioMode.IgnoreAspectRatio
        )
        self.bg: QGraphicsPixmapItem = QGraphicsPixmapItem(bg_pixmap)
        self.bg.setZValue(Z_BG)
        self.scene.addItem(self.bg)

        base_pixmap = QPixmap("assets/sprites/base.png").scaled(
            WINDOW_WIDTH, int(WINDOW_HEIGHT - BASE_Y), Qt.AspectRatioMode.IgnoreAspectRatio
        )
        self.base: QGraphicsPixmapItem = QGraphicsPixmapItem(base_pixmap)
        self.base.setPos(0.0, BASE_Y)
        self.base.setZValue(Z_BASE)
        self.scene.addItem(self.base)
        
        self.message: QGraphicsPixmapItem = QGraphicsPixmapItem(QPixmap("assets/sprites/message.png"))
        self.gameover_msg: QGraphicsPixmapItem = QGraphicsPixmapItem(QPixmap("assets/sprites/gameover.png"))
        self.message.setZValue(Z_UI)
        self.gameover_msg.setZValue(Z_UI)
        
        self.scene.addItem(self.message)
        self.scene.addItem(self.gameover_msg)
        
        self.center_item(self.message)
        self.center_item(self.gameover_msg)

    def center_item(self, item: QGraphicsPixmapItem) -> None:
        rect: QRectF = item.boundingRect()
        item.setPos((WINDOW_WIDTH - rect.width()) / 2.0, (WINDOW_HEIGHT - rect.height()) / 2.0)

    def clear_score(self) -> None:
        for item in self.score_items:
            self.scene.removeItem(item)
        self.score_items.clear()

    def update_score_display(self) -> None:
        self.clear_score()
        score_str: str = str(self.score)
        
        total_width: float = 0.0
        temp_pixmaps: List[QPixmap] = []
        
        for char in score_str:
            pix: QPixmap = QPixmap(f"assets/sprites/{char}.png")
            temp_pixmaps.append(pix)
            total_width += pix.width()
            
        current_x: float = (WINDOW_WIDTH - total_width) / 2.0
        
        for pix in temp_pixmaps:
            item: QGraphicsPixmapItem = QGraphicsPixmapItem(pix)
            item.setZValue(Z_SCORE)
            item.setPos(current_x, SCORE_Y)
            self.scene.addItem(item)
            self.score_items.append(item)
            current_x += pix.width()

    def show_menu(self) -> None:
        self.state = "MENU"
        self.message.setVisible(True)
        self.gameover_msg.setVisible(False)
        self.clear_pipes()
        self.clear_score()
        
        if self.bird is not None:
            self.scene.removeItem(self.bird)
            self.bird = None

    def start_game(self) -> None:
        self.state = "PLAYING"
        self.message.setVisible(False)
        
        self.score = 0
        self.update_score_display()
        
        self.bird = Bird()
        self.bird.setZValue(Z_BIRD)
        self.bird.setPos(BIRD_START_X, BIRD_START_Y) 
        
        self.scene.addItem(self.bird)
        self.bird.flap()
        self.frames = 0

    def game_over(self) -> None:
        self.state = "GAMEOVER"
        self.gameover_msg.setVisible(True)

    def handle_input(self) -> None:
        if self.state == "MENU":
            self.start_game()
        elif self.state == "PLAYING":
            if self.bird is not None:
                self.bird.flap()
        elif self.state == "GAMEOVER":
            self.show_menu()

    def clear_pipes(self) -> None:
        for pipe in self.pipes:
            self.scene.removeItem(pipe)
        self.pipes.clear()

    def spawn_pipe(self) -> None:
        center: int = random.randint(PIPE_MIN_CENTER, PIPE_MAX_CENTER)
        
        top_pipe: Pipe = Pipe(PIPE_SPAWN_X, float(center - PIPE_GAP // 2 - PIPE_SPRITE_HEIGHT), is_top=True)
        bottom_pipe: Pipe = Pipe(PIPE_SPAWN_X, float(center + PIPE_GAP // 2), is_top=False)
        
        self.scene.addItem(top_pipe)
        self.scene.addItem(bottom_pipe)
        self.pipes.extend([top_pipe, bottom_pipe])

    def game_loop(self) -> None:
        if self.state != "PLAYING" or self.bird is None:
            return
            
        self.bird.update_state()
        self.frames += 1
        
        if self.frames % PIPE_SPAWN_INTERVAL == 0:
            self.spawn_pipe()
            
        bird_rect: QRectF = self.bird.sceneBoundingRect()
        
        if bird_rect.top() <= 0.0 or bird_rect.bottom() >= self.base.y():
            self.game_over()
            return
            
        for pipe in self.pipes[:]:
            pipe.update_pos()
            
            if not pipe.passed and bird_rect.left() > pipe.sceneBoundingRect().right():
                pipe.passed = True
                if pipe.is_top:
                    self.score += 1
                    self.update_score_display()

            if pipe.is_offscreen():
                self.scene.removeItem(pipe)
                self.pipes.remove(pipe)
            
            if pipe.sceneBoundingRect().intersects(bird_rect.adjusted(HITBOX_MARGIN, HITBOX_MARGIN, -HITBOX_MARGIN, -HITBOX_MARGIN)):
                self.game_over()