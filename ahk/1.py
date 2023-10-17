# pip install ahk
# pip install "ahk[binary]"

from ahk import AHK

ahk = AHK()

ahk.mouse_move(x=100, y=100, speed=100, blocking=True)      # blocking=True - пока мышка не дойдет до конечной
                                                            #  точки, программа дальше выполнятся не будет
print('stop')
print(ahk.mouse_position)

for window in ahk.list_windows():
    print(window.title)

    # Some more attributes
    print(window.text)           # window text -- or .get_text()
    print(window.get_position()) # (x, y, width, height)
    print(window.id)             # the ahk_id of the window
    print(window.pid)            # process ID -- or .get_pid()
    print(window.process_path)   # or .get_process_path()
