import pygame as pg

#画面サイズの設定
screen_width = 1200
screen_height = 600
#1マスのサイズを設定
tile_size = 50
#画面サイズを１マスのサイズで割った数を取得
ROWS = int(screen_width / tile_size) #24
COLUMNS = int(screen_height / tile_size) #12
#プレイヤーのサイズ
PLAYER_SIZE = 50
 
#画面のサイズ指定
SCREEN = pg.display.set_mode((screen_width, screen_height))
#タイトルの設定
pg.display.set_caption('Platform')	
#時間の設定
CLOCK = pg.time.Clock()
FPS = 60

#画面の左右の端を設定（この範囲を超えるとバックグラウンドが動く（プレイヤーは止まる））
RIGHT_EDGE = screen_width - int(screen_width / 5)
LEFT_EDGE = int(screen_width / 5)
