# Keylogger em Python
Este é um keylogger simples em Python que utiliza uma biblioteca pynput para capturar as teclas pressionadas pelo usuário e salvar em um arquivo de log.

## Como funciona
O programa utiliza a função "on_press" da biblioteca pynput para capturar as teclas pressionadas pelo usuário e a função "logging.info" da biblioteca logging para salvar em um arquivo de log.

O local onde o arquivo de log será salvo pode ser definido na variável "log_dir" e o formato dos logs pode ser definido na função "basicConfig".

O programa fica esperando até que o usuário pressione alguma tecla. Quando isso acontece, uma tecla é registrada no arquivo de log e o programa volta a aguardar a próxima tecla.

## Como usar

- Instale uma biblioteca pynput:
pip install pynput

- Abra o arquivo "keylogger.py" em um editor de texto e defina o local onde os logs serão salvos na variável "log_dir".

- Execute o programa:
python keylogger.py

- Para interromper o programa, pressione "CTRL+C".

## Obs
Os logs das teclas pressionadas serão salvos no arquivo de log definido na variável "log_dir".
