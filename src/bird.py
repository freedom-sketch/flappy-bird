from typing import List
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtGui import QPixmap

from src.config import (BIRD_GRAVITY, BIRD_FLAP_POWER, BIRD_ROTATION_UP, 
                        BIRD_ROTATION_DOWN, BIRD_ROTATION_SPEED, BIRD_ANIM_SPEED
)

class Bird(QGraphicsPixmapItem):
    def __init__(self) -> None:
        super().__init__()
        self.sprites: List[QPixmap] = [
            QPixmap("assets/sprites/redbird-downflap.png"),
            QPixmap("assets/sprites/redbird-midflap.png"),
            QPixmap("assets/sprites/redbird-upflap.png")
        ]
        self.current_frame: int = 1
        self.setPixmap(self.sprites[self.current_frame])
        
        self.setTransformOriginPoint(self.boundingRect().center())
        
        self.velocity: float = 0.0
        self.anim_counter: int = 0

    def flap(self) -> None:
        self.velocity = BIRD_FLAP_POWER

    def update_state(self) -> None:
        self.velocity += BIRD_GRAVITY
        self.setY(self.y() + self.velocity)
        
        if self.velocity < 0:
            self.setRotation(BIRD_ROTATION_UP)
        else:
            rotation: float = min(self.rotation() + BIRD_ROTATION_SPEED, BIRD_ROTATION_DOWN)
            self.setRotation(rotation)

        self.anim_counter += 1
        if self.anim_counter % BIRD_ANIM_SPEED == 0:
            self.current_frame = (self.current_frame + 1) % 3
            self.setPixmap(self.sprites[self.current_frame])