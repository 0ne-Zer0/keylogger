# Keylogger em Python
Este é um keylogger simples em Python que utiliza uma biblioteca pynput para capturar as teclas pressionadas pelo usuário e salvar em um arquivo de log.

## Como funciona
O programa utiliza a função __"on_press"__ da biblioteca pynput para capturar as teclas pressionadas pelo usuário e a função __"logging.info"__ da biblioteca logging para salvar em um arquivo de log.

O local onde o arquivo de log será salvo pode ser definido na variável __"log_dir"__ e o formato dos logs pode ser definido na função __"basicConfig"__.

O programa fica esperando até que o usuário pressione alguma tecla. Quando isso acontece, uma tecla é registrada no arquivo de log e o programa volta a aguardar a próxima tecla.

## Como usar

- Instale uma biblioteca pynput:
pip install pynput

- Abra o arquivo __"keylogger.py"__ em um editor de texto e defina o local onde os logs serão salvos na variável __"log_dir"__.

- Execute o programa:
_python keylogger.py_

- Para interromper o programa, pressione __"CTRL+C"__.

## Obs
Os logs das teclas pressionadas serão salvos no arquivo de log definido na variável __"log_dir"__.
