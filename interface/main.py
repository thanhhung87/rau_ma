import logging
import threading
import time

import keyboard
import pydirectinput
import PySimpleGUI as sg

import controller
import interface
from controller import SelectWindow
from controller import round as r
from controller.button import Button
from controller.filelog import OutputHandler, logger
from controller.global_variables import (
    bot_initialization,
    character_moves_event,
    config,
    global_event,
    path,
)

main_stop = False
main_start = False
appStarted = False
main_pause = False
main_status = False
button_pause = "Pause (Ctrl + Space)"
hotkey_combination_start = "ctrl+f9"
hotkey_combination_stop = "ctrl+q"
hotkey_combination_pause = "ctrl+space"
move_status = False
like_status = False


def on_hotkey_stop():
    global main_stop
    time.sleep(1)
    if main_stop is False:
        main_stop = True
        logger.debug("Stop thread main")


def on_hotkey_start():
    time.sleep(1)
    global main_start
    if main_start is False:
        main_start = True
        logger.debug("Start thread main")


def on_hotkey_pause():
    time.sleep(1)
    global main_pause
    if main_pause is False:
        main_pause = True
        logger.debug("Pause thread main")


def main():
    global main_status

    dota2 = SelectWindow("Dota 2")

    if dota2.hwnd:
        main_status = True
        global_event.sleep(1)
        dota2.move_window_to()
        global_event.sleep(1)
        logger.info(f"Tim thay cua so {dota2.app_name}")
        global_event.sleep(1)
        bot_initialization()
        n = 0
        while True:
            if global_event.check_event():
                # logger.info("Stop thread main")
                break
            n += 1
            # print("t dau auto lan: {}".format(n))
            logger.info("Bat dau auto lan: {}".format(n))
            if r.round_all(n) is False:
                break
            if Button.exit_game_round20() is False:
                break
            logger.info("Ket thuc auto lan {}".format(n))
            for t in range(10):
                if global_event.check_event():
                    break
                t = 10 - t
                # print("Dang cho 5s")
                logger.info(f"Dang cho bat auto lai sau {t}/10s")
                global_event.sleep(1)

    else:
        main_status = False
        logger.info("Khong tim thay cua so co ten {}".format(dota2.app_name))


class ThreadedApp:
    def __init__(self):
        self.t1 = None
        self.t_stop = None

    def run(self):
        global_event.app_start()
        character_moves_event.app_start()
        self.t1 = threading.Thread(target=main, args=(), daemon=True)
        self.t1.start()

    def stop(self):
        stop_app()
        # if self.t1 is not None:
        #     self.t1.join()
        # self.t1.join()

    @staticmethod
    def pause():
        global_event.app_pause()
        character_moves_event.app_pause()

    @staticmethod
    def resume():
        global_event.app_resume()
        character_moves_event.app_resume()


def stop_app():
    global_event.app_stop()
    character_moves_event.app_stop()


def main_window():
    global main_status, button_pause, main_stop, main_start, appStarted, main_pause
    sg.theme("SystemDefaultForReal")
    menu_def = [["Config", ["Auto", "Item", "Hero"]]]

    layout = [
        [sg.Menu(menu_def)],
        [
            sg.Output(
                key="-OUTPUT-",
                size=(50, 20),
                font=("Arial", 12),
                background_color="black",
                text_color="green",
            )
        ],
        [
            sg.Button("Start (Ctrl + F9)", key="-START-"),
            sg.Button("Stop (Ctrl + Q)", key="-STOP-", disabled=True),
            sg.Button(button_pause, key="-PAUSE-", disabled=True),
            sg.Button("Exit", key="Exit"),
        ],
    ]
    appStarted = False
    threaded_app = ThreadedApp()

    window = sg.Window(
        "Brodota-bot",
        layout,
        finalize=True,
        element_padding=(10, 10),
        auto_size_text=True,
        element_justification="center",
        auto_size_buttons=True,
        default_button_element_size=(12, 1),
    )
    log_output1 = OutputHandler(window)
    logger.addHandler(log_output1)
    logger.setLevel(logging.DEBUG)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-START-" or main_start is True:
            if appStarted is False:
                threaded_app.run()
                # if main_status is True:
                window["-START-"].update(disabled=True)
                window["-PAUSE-"].update(disabled=False)
                window["-STOP-"].update(disabled=False)
                appStarted = True
            main_start = False

        elif (event == "-STOP-") or (main_stop is True):
            if appStarted is True:
                threaded_app.stop()
                appStarted = False
                main_status = False
                window["-START-"].update(disabled=False)
                window["-STOP-"].update(disabled=True)
                window["-PAUSE-"].update(disabled=True)
            main_stop = False
        elif (event == "-PAUSE-") or (main_pause is True):
            if appStarted is True:
                if button_pause == "Pause (Ctrl + Space)":
                    button_pause = "Resume (Ctrl + Space)"
                    window["-PAUSE-"].update(button_pause)
                    threaded_app.pause()
                else:
                    button_pause = "Pause (Ctrl + Space)"
                    window["-PAUSE-"].update(button_pause)
                    threaded_app.resume()
            main_pause = False
        elif event == "Auto":
            # logger.info("Auto")
            interface.window_config_auto()

        elif event == "Emit":
            window["-OUTPUT-"].update(values[event] + "\n", append=True)
        elif main_status is True:
            window["-START-"].update(disabled=True)
            window["-PAUSE-"].update(disabled=False)
            window["-STOP-"].update(disabled=False)
            main_status = False
    window.close()


if __name__ == "__main__":
    keyboard.add_hotkey(hotkey_combination_stop, on_hotkey_stop)
    keyboard.add_hotkey(hotkey_combination_start, on_hotkey_start)
    keyboard.add_hotkey(hotkey_combination_pause, on_hotkey_pause)
    main_window()

    pass
