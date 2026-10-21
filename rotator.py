# Made and developed by gneval9 Software
# 27-09-2026
import os
import sys
import time

os.system("clear")

print("Controles:")
print("""
flechas -> rotar objeto
awsd    -> mover objeto
i-o     -> zoom
z       -> alternar perspectiva
t       -> alternar punto
r       -> resetear posición

q       -> cerrar programa
""")

print("Introduzca la ruta (relativa) del archivo a cargar \n")
ruta = str(input(">> "))
#ruta = "../FD3DE_space_game/Modelos/nave.fd3de"

escala = 1
rot_velocity = 4
perspectiva = True
punto = True

import fd3de
import framedirect
import keyboard

obj = None
screen_x, screen_y = framedirect.resolution()

ejes_3d_load = [[0,0,0, 1,2,3],[10,0,0],[0,10,0],[0,0,10]]
ejes_3d = fd3de.spawn(ejes_3d_load)

fd3de.move("x", -500, ejes_3d)
fd3de.move("y", 300, ejes_3d)


def load():
	global obj
	try:
		obj_load = fd3de.load(ruta)
		obj = fd3de.spawn(obj_load)
	except:
		pass

def render():
	global obj
	
	if punto == True and obj["position"][0] == 0 and obj["position"][1] == 0 and obj["position"][2] == 0:
		framedirect.draw_circle(screen_x // 2, screen_y // 2, 5, framedirect.RED)
	else:
		pass
	

	fd3de.render(obj, fd3de.WHITE, escala, perspectiva)
	fd3de.render(ejes_3d, fd3de.GREEN, 6, False)
	
	fd3de.update()
	
	fd3de.clear_object(obj, escala, perspectiva)
	fd3de.render(ejes_3d, fd3de.BLACK, 6, False)
	
	framedirect.draw_circle(screen_x // 2, screen_y // 2, 5, framedirect.BLACK)


def reload():
	global obj
	rotation = obj["rotation"]
	pos = obj["position"]	

	load()

	fd3de.rotate("x", rotation[0], obj)
	fd3de.rotate("y", rotation[1], obj)
	fd3de.rotate("z", rotation[2], obj)
	
	fd3de.move("x", pos[0], obj)
	fd3de.move("y", pos[1], obj)
	fd3de.move("z", pos[2], obj)





load()

while True:
	if keyboard.is_pressed("right"):
		fd3de.rotate("y", -rot_velocity, obj)
		fd3de.rotate("y", rot_velocity, ejes_3d)	

	if keyboard.is_pressed("left"):
		fd3de.rotate("y", rot_velocity, obj)
		fd3de.rotate("y", -rot_velocity, ejes_3d)

	if keyboard.is_pressed("up"):
		fd3de.rotate("x", rot_velocity, obj)
		fd3de.rotate("x", -rot_velocity, ejes_3d)


	if keyboard.is_pressed("down"):
		fd3de.rotate("x", -rot_velocity, obj)
		fd3de.rotate("x", rot_velocity, ejes_3d)




	if keyboard.is_pressed("d"):
		fd3de.move("x", 5, obj)

	if keyboard.is_pressed("a"):
		fd3de.move("x", -5, obj)

	if keyboard.is_pressed("w"):
		fd3de.move("y", 5, obj)

	if keyboard.is_pressed("s"):
		fd3de.move("y", -5, obj)




	if keyboard.is_pressed("z"):
		perspectiva = not perspectiva
		time.sleep(0.1)


	if keyboard.is_pressed("r"):
		fd3de.move("x", -obj["position"][0], obj)
		fd3de.move("y", -obj["position"][1], obj)
		fd3de.move("z", -obj["position"][2], obj)


	if keyboard.is_pressed("t"):
		punto = not punto
		time.sleep(0.1)

	if keyboard.is_pressed("q"):
		sys.exit()
	


	if keyboard.is_pressed("o") and escala < 8:
		escala += 0.2

	elif keyboard.is_pressed("i") and escala > 0.3:
		escala -= 0.2


	reload()
	render()


