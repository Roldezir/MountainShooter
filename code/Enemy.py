#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from enum import verify

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = 1

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.name=='Enemy3':
            # Verifica se atinge o topo
            if self.rect.top <= 0:
                self.direction = 1  # Muda a direção para baixo
            elif self.rect.bottom >= WIN_HEIGHT:
                self.direction = -1  # Muda a direção para cima

            # Move o inimigo
            if self.direction == 1:
                # Desce duas vezes mais rápido
                self.rect.centery += ENTITY_SPEED[self.name] * 2
            else:
                # Move normalmente para cima
                self.rect.centery -= ENTITY_SPEED[self.name]

























    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
