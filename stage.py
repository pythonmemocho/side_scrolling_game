import pygame as pg
from pygame import *
from settings import *
from player import *

class Stage():
	def __init__(self, data):
		#空のリストを用意
		self.tile_list = []
		#4枚のタイルが1つになった画像を呼び出します
		self.sprite_sheet = pg.image.load("img/tiles.png").convert_alpha()
		
		#のちに用意するstageの番号1を地面とし、リストに位置とサイズ情報を格納していく
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 0:
					self.img = self.get_image(self.sprite_sheet,0,0,tile_size,tile_size)				
					self.img_rect = self.tile_info(self.img,col_count,row_count)
					tile = (self.img, self.img_rect)
					self.tile_list.append(tile)
				if tile == 1:
					self.img = self.get_image(self.sprite_sheet,51,0,tile_size,tile_size)
					self.img_rect = self.tile_info(self.img,col_count,row_count)
					tile = (self.img, self.img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					self.img = self.get_image(self.sprite_sheet,0,51,tile_size,tile_size)
					self.img_rect = self.tile_info(self.img,col_count,row_count)
					tile = (self.img, self.img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					self.img = self.get_image(self.sprite_sheet,51,51,tile_size,tile_size)				
					self.img_rect = self.tile_info(self.img,col_count,row_count)
					tile = (self.img, self.img_rect)
					self.tile_list.append(tile)	
				col_count += 1
			row_count += 1
	
	#先に呼び出した画像から情報を取得するメソッド		
	def tile_info(self,image,col_count,row_count):
		rect = image.get_rect()
		rect.x = col_count * tile_size
		rect.y = row_count * tile_size
		return rect

	#4つのタイルの画像から1つ取得するメソッド（x、yで取得する画像の開始位置を指定）
	def get_image(self,sheet, x, y, width, height):
			image = pg.Surface((width, height))
			image.blit(sheet, (0, 0), (x, y, width, height))
			return image

	#描画用メソッド（tile[0]に画像,tile[1]に描画位置が格納されている）
	def draw(self):
		for tile in self.tile_list:
			SCREEN.blit(tile[0],tile[1])
	
	#プレイヤーの位置が端に近づいたら実行するメソッド。タイルのxを足したり、引いたりして描画位置を調節する
	def scroll_front(self):	
		for tile in self.tile_list:
			tile[1].x -= 5
	def scroll_back(self):	
		for tile in self.tile_list:
			tile[1].x += 5
