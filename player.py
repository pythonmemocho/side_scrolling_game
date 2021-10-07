import pygame as pg
from pygame.locals import *
from settings import *
from stage import *

#プレイヤークラス
class Player(pg.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		#画像の設定
		image = pg.image.load("img\player.png").convert_alpha()
		image = pg.transform.scale(image,(PLAYER_SIZE,PLAYER_SIZE))
		self.right_image = image
		#元の画像が左向きなので画像を180度Y軸に反転させる
		self.left_image = pg.transform.flip(image,True,False)
		self.image = self.right_image
		#画像からrectサイズを取得
		self.rect = self.image.get_rect()
		#位置の設定
		self.rect.x = x
		self.rect.y = y
		#画像の高さと幅の取得
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		#y軸方向の速度設定、とりあえず0にしておく
		self.vel_y = 0
		#jumpしているかのフラグ
		self.jumped = False
		#地面についているかのフラグ
		self.on_ground = True
		#空中にいる状態かのフラグ
		self.in_the_air = False
		#死亡したかのフラグ
		self.dead = False
		#向きの設定
		self.direction = 0
		self.RIGHT = False
		self.LEFT  = False
		#動きの幅（量）設定(始めは0で設定）
		self.dx = 0
		self.dy = 0

	#操作のメソッド
	def key_con(self,data):
		#x軸、y軸の移動幅 初期化
		self.dx = 0
		self.dy = 0							

		#キー操作関数
		key = pg.key.get_pressed()
		#右移動キー
		if key[K_RIGHT]:
			self.RIGHT,self.LEFT = True, False
			self.direction = 0
			self.dx += 5
		if not key[K_RIGHT]:
			self.RIGHT = False
		
		#左移動キー
		if key[K_LEFT]:
			self.RIGHT,self.LEFT = False, True
			self.direction = 1
			self.dx -= 5
		if not key[K_LEFT]:
			self.LEFT = False

		#jumpキーを押した時、ジャンプするかフラグで判断。条件に当てはまればジャンプ実行
		if key[K_SPACE] and self.jumped == False and self.on_ground == True and self.in_the_air == False:
			self.jumped = True
			self.vel_y = -20
			self.on_ground = False
		#jumpのキーを放した（false）ら、jumpフラグをfalseに戻す
		if not key[K_SPACE]:
			self.jumped = False

		#重力の追加（後に設定するメソッドで）
		self.add_gravity()

		#X軸当たり判定TRUEならdxを0にする
		if self.collisionX(data):
			self.dx = 0
		self.collisionY(data)

		#プレイヤーが画面端に来た場合の処理
		if self.rect.x > RIGHT_EDGE and self.RIGHT:
			self.dx = 0
		if self.rect.x <= 0 and self.LEFT:
			self.dx = 0
		if self.rect.x >= screen_width:
			self.dx = 0

		#プレイヤーの位置に移動速度を足す
		self.rect.x += self.dx
		self.rect.y += self.dy

		#プレイヤーが地面のギャップに落ちた時の処理
		if self.rect.top >= screen_height:
			self.dead = True
			self.kill()

	#X軸方向の当たり判定
	def collisionX(self,data):
		for tile in data:
			if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
				return True

	#Y軸方向の当たり判定			
	def collisionY(self,data):
		for tile in data:
			if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
				if self.vel_y < 0:
					self.dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
	
				elif self.vel_y >= 0:
					self.dy = tile[1].top - self.rect.bottom
					self.vel_y = 0
					self.on_ground = True
					self.in_the_air = False	

	#重力の設定メソッド
	def add_gravity(self):
		#重力設定、y軸速度を加速してdyにプラスする
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		self.dy += self.vel_y

		#y軸速度が0でなければ、フラグをtrueにする。
		# 接触判定で地面と接触している時はy軸速度を0にするので、y軸速度が0でないということは、空中にいるということです。
		if self.vel_y != 0:
			self.in_the_air = True
	
	#描画用メソッド
	def draw(self):
		#プレイヤーをスクリーンに描画(directioonの 0 か 1 で左右を判定)
		if self.direction == 0:
			self.image = self.right_image
		if self.direction == 1:
			self.image = self.left_image
		SCREEN.blit(self.image,(self.rect.x,self.rect.y))	

	#updateメソッドに処理をまとめる
	def update(self,data):
		self.key_con(data)
		self.draw()