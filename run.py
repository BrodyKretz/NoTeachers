import webbrowser
from pynput.keyboard import Key, Listener

url = 'https://docs.google.com/'

def show(key):
    if key == Key.tab:
        webbrowser.open_new_tab(url)
        webbrowser.open_new(url)

    if key != Key.tab:
        print("")

    # by pressing 'delete' button
    # you can terminate the loop
    if key == Key.delete:
        return False


# Collect all event until released
with Listener(on_press=show) as listener:
    listener.join()

    webbrowser.open_new_tab(url)
    webbrowser.open_new(url)
