import pygame as pg
from pygame.locals import *
from settings import *
from stage_data import *
from player import *
from stage import *

#ゲームクラス	
class Game():
	def __init__(self):
		pg.init()

		#クラスのインスタンス化
		self.stage = Stage(stage_data)
		self.player = Player(100, 200)
		#スプライトクラス設定してプレイヤーを追加
		self.playerSprite = pg.sprite.GroupSingle(self.player)

		#バックグラウンド画像の呼び出し、サイズ設定
		self.bg = pg.image.load('img/BG.png').convert()
		self.bg = pg.transform.scale(self.bg,(screen_width,screen_height))

	#溝に落ちた際に実行するメソッド
	def respawn(self):
		self.player = Player(100, 0)
		self.playerSprite.add(self.player)
	
	#メインループ処理
	def main(self):
		running = True
		while running:	
			for event in pg.event.get():
				if event.type == pg.QUIT:
					running = False
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_ESCAPE:
						running = False
			
			#画面の初期化
			SCREEN.fill((55,100,200))
			
			#背景を描画
			SCREEN.blit(self.bg,(0,0))
			#ステージの描画
			self.stage.draw()

			#プレイヤーが画面の端周辺に来た場合にバックグラウンド側を動かす処理
			if self.player.rect.x > RIGHT_EDGE and self.player.RIGHT:
				self.stage.scroll_front()
				#バックグラウンドが動いている時にプレイヤーが物体にぶつかると強制的に移動してしまうので、調整。
				if self.player.collisionX:
					self.player.rect.x -= 5
			#上記と同じ（左右反対の処理）
			elif self.player.rect.x < LEFT_EDGE and self.player.LEFT:
				self.stage.scroll_back()
				if self.player.collisionX:
					self.player.rect.x += 5
			
			#プレイヤーが溝に落っこちた時の処理
			if self.player.dead:
				self.respawn()
				self.player.dead = False

			#プレイヤーのメソッド呼び出し
			self.playerSprite.update(self.stage.tile_list)

			#クロック実行
			CLOCK.tick(FPS)
			pg.display.update()

		pg.quit()

#インスタンス化　→　実行
game = Game()
game.main()