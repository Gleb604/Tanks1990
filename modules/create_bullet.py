import pygame
import modules.settings as m_settings
import modules.explosion as m_explosion
import modules.data_base as m_data
import modules.create_sound as m_sound
import random
import time

pygame.init()

class Bullet(m_settings.Settings):
    def __init__(self, width1 = 6, height1 = 8, x1 = 0, y1 = 0, name_file1 = None, direction = None, type_bullet = None, speed = 2):
        m_settings.Settings.__init__(self, width = width1, height = height1, x = x1, y = y1, name_file = name_file1)
        self.load_image()
        self.STOP = False
        self.EXPLOSION = False
        self.DIRECTION = direction
        self.TYPE_BULLET = type_bullet
        self.SPEED = speed
        if self.DIRECTION == None:
            self.DIRECTION = "UP"
        self.rotate_image_bullet()

    def rotate_image_bullet(self):
        if self.DIRECTION == "L":
            self.IMAGE = pygame.transform.rotate(self.IMAGE, 90)
        elif self.DIRECTION == "R":
            self.IMAGE = pygame.transform.rotate(self.IMAGE, -90)
        elif self.DIRECTION == "DW":
            self.IMAGE = pygame.transform.rotate(self.IMAGE, 180)

        
    def move_bullet(self, hero, bullet, list_bullet):
        # move UP
        if self.DIRECTION == "UP":
            if self.Y > 0 and self.STOP == False:
                self.Y = self.Y - self.SPEED
            if self.Y <= 0:
                # if len(list_bullet) != 0:
                if bullet in list_bullet:
                    # index = list_bullet.index(bullet)
                    list_bullet.remove(bullet)
                    # del list_bullet[index]
        # move DOWN
        if self.DIRECTION == "DW":
            if self.Y <= 576 and self.STOP == False:
                self.Y = self.Y + self.SPEED
            if self.Y >= 576:
                # if len(list_bullet) != 0:
                if bullet in list_bullet:
                    # index = list_bullet(bullet)
                    # del list_bullet[index]
                    list_bullet.remove(bullet)
        # move LEFT
        if self.DIRECTION == "L":
            if self.X > 0 and self.X + self.WIDTH > 0 and self.STOP == False:
                self.X = self.X - self.SPEED
            if self.X <= 0:
                # if len(list_bullet) != 0:
                if bullet in list_bullet:
                    # index = list_bullet.index(bullet)
                    # del list_bullet[index]
                    list_bullet.remove(bullet)
        # move RIGHT
        if self.DIRECTION == "R":
            if self.X < 576 and self.X + self.WIDTH < 576 and self.STOP == False:
                self.X = self.X + self.SPEED
            if self.X + self.WIDTH >= 574:
                # if len(list_bullet) != 0:
                if bullet in list_bullet:
                    # index = list_bullet.index(bullet)
                    # del list_bullet[index]
                    list_bullet.remove(bullet)
        #
        self.collid_brick_U_D(hero, bullet, list_bullet)
    # 
    def collid_brick_U_D(self, hero, bullet, list_bullet):
        def collide_vertical(brick):
            list_red_brick = ["1.png", "2.png", "3.png", "4.png", "5.png"]
            for red in list_red_brick:
                if brick.NAME_FILE == f"images/textures/red_brick/{red}":
                    self.STOP = True
                    explosion = m_explosion.Explosion(x1 = bullet.X - 4, y1 = bullet.Y - 4)
                    m_data.list_explosion.append(explosion)
                    m_data.list_bricks.remove(brick)
                    sound = m_sound.Sound_track(name_file= "sound/explosion_red_brick.mp3")
                    m_data.list_sound.append(sound)
                    if bullet in list_bullet:
                        list_bullet.remove(bullet)
                    self.STOP = False
            if brick.NAME_FILE == "images/textures/white_brick.png":
                self.STOP = True
                explosion = m_explosion.Explosion(x1 = bullet.X - 4, y1 = bullet.Y - 4)
                m_data.list_explosion.append(explosion)
                sound = m_sound.Sound_track(name_file= "sound/shoot_white_block.mp3")
                # m_data.list_sound.append(sound)
                m_data.list_sound_1.append(sound)
                if bullet in list_bullet:
                    list_bullet.remove(bullet)
                self.STOP = False
            if brick.TYPE_OBJECT != None and bullet.TYPE_BULLET != brick.TYPE_OBJECT:
                self.STOP = True
                explosion = m_explosion.Explosion(x1 = brick.X, y1 = brick.Y, width1= 32, height1= 32)
                m_data.list_explosion.append(explosion)
                sound = m_sound.Sound_track(name_file= "sound/explosion_tank.mp3")
                m_data.list_sound.append(sound)
                if brick.TYPE_OBJECT == 'hero':
                    brick.SOUND_MOVE.stop()
                    brick.SOUND_STOP.stop()
                if brick in m_data.list_bricks:
                    m_data.list_bricks.remove(brick)
                if bullet in list_bullet:
                    list_bullet.remove(bullet)
                self.STOP = False

        #
        for brick in m_data.list_bricks:
            # collide move up dw
            if self.X + 3 >= brick.X and self.X + 3 <= brick.X + brick.WIDTH:
                if self.DIRECTION == "UP":
                    if self.Y <= brick.Y + brick.HEIGHT and self.Y > brick.Y:
                        collide_vertical(brick)
                if self.DIRECTION == "DW":
                    if self.Y + self.HEIGHT >= brick.Y and self.Y + self.HEIGHT < brick.Y + brick.HEIGHT:
                        collide_vertical(brick)
            # collide move left right
            if self.Y + 4 > brick.Y and self.Y + 4 < brick.Y + brick.HEIGHT:
                if self.DIRECTION == "L":
                    if self.X + self.WIDTH > brick.X + brick.WIDTH and self.X < brick.X + brick.WIDTH:
                        collide_vertical(brick) 
                # collide move right
                if self.DIRECTION == "R":
                    if self.X < brick.X and self.X + self.WIDTH > brick.X:
                        collide_vertical(brick) 

    
bullet = Bullet(name_file1= "images/bullet/bullet.png") 