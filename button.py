import pyautogui
import time

class bt_infor():
    def __init__(self,para_name):
         self.name= para_name
         self.img = "data\\image\\"+para_name+".png"
Back=bt_infor("Back")
Disconnect=bt_infor("Disconnect")
LeaveGame=bt_infor("LeaveGame")


def click(bt_infor):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                bt_infor.img, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            time.sleep(1)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            time.sleep(0.2)
            pyautogui.moveTo(200,200)
            # pyautogui.moveTo(0, 0)
            # print("I can see it")
            break
        except pyautogui.ImageNotFoundException:
            i = i+1
            if i > 120:
                break
            print("Đang tìm hình ảnh button {} so lan {}".format(bt_infor.name,i))
            time.sleep(0.5)
def exit_game():
    click(Back)

    click(Disconnect)

    click(LeaveGame)






bt_CreateCustomLobby = r"data\image\CreateCustomLobby.png"
bt_ServerLocaltion = r"data\image\ServerLocaltion.png"
bt_ServerLocaltion_Singapore = r"data\image\ServerLocaltion_Singapore.png"
bt_CreatePassLobby = r"data\image\CreatePassLobby.png"
bt_CreateGame = r"data\image\CreateGame.png"
bt_StartGame = r"data\image\StartGame.png"
bt_Accept = r"data\image\Accept.png"
bt_Confirm = r"data\image\Confirm.png"
bt_Challenge = r"data\image\Challenge.png"
bt_SelectCharacter = r"data\image\SelectCharacter.png"
bt_Prepare = r"data\image\Prepare.png"
bt_ProceedToRound2 = r"data\image\ProceedToRound2.png"
bt_Roll = r"data\image\Roll.png"

bt_ProceedToRound3 = r"data\image\ProceedToRound3.png"
bt_ProceedToRound4 = r"data\image\ProceedToRound4.png"
bt_ProceedToRound5 = r"data\image\ProceedToRound5.png"
bt_ProceedToRound6 = r"data\image\ProceedToRound6.png"
bt_ProceedToRound7 = r"data\image\ProceedToRound7.png"
bt_ProceedToRound8 = r"data\image\ProceedToRound8.png"
bt_ProceedToRound9 = r"data\image\ProceedToRound9.png"
bt_ProceedToRound10 = r"data\image\ProceedToRound10.png"
bt_ProceedToRound11 = r"data\image\ProceedToRound11.png"
bt_ProceedToRound12 = r"data\image\ProceedToRound12.png"
bt_ProceedToRound13 = r"data\image\ProceedToRound13.png"
bt_ProceedToRound14 = r"data\image\ProceedToRound14.png"
bt_ProceedToRound15 = r"data\image\ProceedToRound15.png"
bt_ProceedToRound16 = r"data\image\ProceedToRound16.png"
bt_ProceedToRound17 = r"data\image\ProceedToRound17.png"
bt_ProceedToRound18 = r"data\image\ProceedToRound18.png"
bt_ProceedToRound19 = r"data\image\ProceedToRound19.png"
bt_ProceedToRound20 = r"data\image\ProceedToRound20.png"
bt_Resurrect=r"data\image\Resurrect.png"