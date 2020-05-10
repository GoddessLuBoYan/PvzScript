# 0,2A 1 2 1 0 0,1E 1 2 0 0 1,30 1 2 0 0 0,2C 1 3 0 0 0,1E 1 3 0 0 1,30 1 3 0 0 0,2C 1 4 0 0 0,1E 1 4 0 0 1,30 1 4 0 0 0,2F 1 5 0 0 0,2C 2 2 0 0 0,1E 2 2 0 0 1,30 2 2 0 0 0,25 2 3 0 0 0,1E 2 3 0 0 1,30 2 3 0 0 0,2C 2 4 0 0 0,1E 2 4 0 0 1,30 2 4 0 0 0,2F 2 5 0 0 0,2F 3 1 0 0 0,10 3 1 0 0 0,10 3 2 0 0 0,2F 3 3 0 0 0,10 3 3 0 0 0,10 3 4 0 0 0,2F 3 5 0 0 0,10 3 5 0 0 0,10 3 6 0 0 0,29 3 7 0 0 0,10 3 7 0 1 0,1E 3 7 0 0 0,29 3 8 0 1 0,10 3 8 0 0 0,1E 3 8 0 1 0,2F 4 1 0 0 0,10 4 1 0 0 0,10 4 2 0 0 0,2F 4 3 0 0 0,10 4 3 0 0 0,10 4 4 0 0 0,2F 4 5 0 0 0,10 4 5 0 0 0,10 4 6 0 0 0,29 4 7 0 0 0,10 4 7 0 1 0,1E 4 7 0 0 0,29 4 8 0 1 0,10 4 8 0 1 0,1E 4 8 0 1 0,2C 5 2 0 0 0,1E 5 2 0 0 1,30 5 2 0 0 0,25 5 3 0 0 0,1E 5 3 0 0 1,30 5 3 0 0 0,2C 5 4 0 0 0,1E 5 4 0 0 1,30 5 4 0 0 0,2F 5 5 0 0 0,2A 6 2 1 0 0,1E 6 2 0 0 1,30 6 2 0 0 0,2C 6 3 0 0 0,1E 6 3 0 0 1,30 6 3 0 0 0,2C 6 4 0 0 0,1E 6 4 0 0 1,30 6 4 0 0 0,2F 6 5 0 0 0

import pvz
import pvz.logger as logger
from pvz.threads import running_in_thread

pvz.EnableLogger(True)
while not pvz.FindPvZ():
    print("等待找到游戏")
    pvz.Sleep(100)

pvz.BackgroundRunning(True)
print(f"当前场景: {pvz.GameUI()}")
pvz.SetZombies(zombies=["撑杆", "舞王", "冰车", "潜水", "海豚", "气球", "小丑", "橄榄", "白眼", "红眼", "蹦极"], mode="自然刷怪")

def 种垫材(y_pos = 9):
    pvz.Card("小喷菇", (1, y_pos))
    pvz.Card("阳光菇", (2, y_pos))
    pvz.Card("胆小菇", (5, y_pos))
    pvz.Card("花盆", (6, y_pos))

def 发炮(y_pos = 9):
    pvz.Pao((2, y_pos))
    pvz.Pao((5, y_pos))

def 铲垫材(y_pos = 9):
    pvz.Shovel((1, y_pos))
    pvz.Shovel((2, y_pos))
    pvz.Shovel((5, y_pos))
    pvz.Shovel((6, y_pos))

@running_in_thread
def 垫材线程():
    for wave in range(1, 21):
        pvz.Prejudge(150, wave)
        种垫材()

@running_in_thread
def 炮线程():
    刷新后等待时间 = 750 + 10 - 200 - 374
    for wave in range(1, 21):
        pvz.Prejudge(刷新后等待时间, wave)
        发炮()
        if wave in [9, 19, 20]:
            收尾(wave)
        if wave == 10:
            pvz.Delay(373 - 298)
            pvz.Card("荷叶", (3, 9))
            pvz.Card("毁灭菇", (3, 9))
            pvz.Card("咖啡豆", (3, 9))
        if wave == 20:
            pvz.Delay(373 - 298)
            pvz.Card("荷叶", (4, 9))
            pvz.Card("毁灭菇", (4, 9))
            pvz.Card("咖啡豆", (4, 9))

@running_in_thread
def 收尾(wave):
    global 红眼波次, 白眼波次
    if 红眼波次[wave - 1]:
        炮数 = 2
    elif 白眼波次[wave - 1]:
        炮数 = 1
    else:
        炮数 = 0
    if wave == 20 and 炮数 == 0:
        炮数 = 1
    for _ in range(炮数):
        pvz.Delay(760)
        种垫材()
        发炮()
    pass

@running_in_thread
def 临时伞():
    for i in [10, 20]:
        pvz.Prejudge(0, i)
        pvz.Card("荷叶", (3, 7))
        pvz.Card("保护伞", (3, 7))

@running_in_thread
def 冰消珊瑚():
    pvz.Prejudge(-150, 20)
    pvz.Card("寒冰菇", (1, 1))
    pvz.Card("咖啡豆", (1, 1))

@running_in_thread
def 炮消珊瑚():
    pvz.Prejudge(-130, 20)
    pvz.Pao((3, 7))

while True:
    while pvz.GameUI() != 2:
        pvz.Sleep(100)
    pvz.Sleep(1000)

    红眼波次 = pvz.GetZombieWaves(32)
    白眼波次 = pvz.GetZombieWaves(23)
    pvz.SelectCards(["小喷菇", "阳光菇", "胆小菇", "花盆", "三叶草", "保护伞", "毁灭菇", "南瓜", "咖啡豆", "荷叶"])

    炮线程()
    垫材线程()
    炮消珊瑚()
    pvz.StartNutsFixerThread([(3, 7), (4, 7), (3, 8), (4, 8)], "南瓜")
    pvz.StartAutoCollectThread()
