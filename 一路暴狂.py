# 阵型字符串: 
# 0 0,10 4 1 0 0 0,10 4 2 0 0 0,2F 4 3 0 2 0,10 4 3 0 0 0,10 4 4 0 1 0,2F 4 5 0 0 0,10 4 5 0 0 0,10 4 6 0 0 0,2F 4 7 0 2 0,10 4 7 0 0 0,10 4 8 0 0 0,2F 5 1 0 2 0,2F 5 3 0 0 0,2F 5 5 0 2 0,2F 6 1 0 0 0,2F 6 3 0 1 0,2F 6 5 0 1 0

import pvz
import pvz.logger as logger
from pvz.threads import running_in_thread

pvz.EnableLogger(True)
while not pvz.FindPvZ():
    print("等待找到游戏")
    pvz.Sleep(100)

pvz.BackgroundRunning(True)
# pvz.GotoEndless()
print(f"当前场景: {pvz.GameUI()}")
pvz.QuickPass()
pvz.JumpLevel(1009)
pvz.SetZombies(zombies=["撑杆", "舞王", "冰车", "海豚", "气球", "矿工", "小丑", "扶梯", "白眼", "红眼"], mode="自然刷怪")
# pvz.StartAutoCollectThread()

pvz.seeds.IMITATER_X = 470
pvz.seeds.IMITATER_Y = 470
pvz.seeds.simulate_manual_control = False

@running_in_thread
def 预判炮炸():
    for wave in [1,2,3,4,5,7,8,9,10,11,12,13,14,16,17,18,19,20]:
        if wave in [10,20]:
            pvz.Prejudge(-80, wave)
        else:
            pvz.Prejudge(-130, wave)
        pvz.UpdatePaoList()
        pvz.Pao((2,9))
        pvz.Pao((5,9))
        pvz.Delay(110)
        pvz.Pao((5,8))
        if wave in [9,19,20]:
            收尾(wave)
        if wave == 10:
            # pvz.Delay(374-110-110)
            pvz.Card("窝瓜", (2,9))
            # pvz.Card("辣椒", (6,9))

@running_in_thread
def 预判核炸():
    for wave in [6,15]:
        pvz.Prejudge(0,wave)
        for pos in [(3,9), (4,9)]:
            pvz.Card("睡莲", pos)
            pvz.Card("毁灭菇", pos)
            pvz.Card("咖啡豆", pos)
        pvz.Delay(198+110)
        pvz.Card("樱桃炸弹", (5, 8))


@running_in_thread
def 收尾(wave):
    global giga_waves
    has_giga = giga_waves[wave-1]
    if has_giga:
        pvz.Delay(600)
        pvz.UpdatePaoList()
        pvz.Pao((2,9))
        pvz.Pao((5,9))
        pvz.Delay(110)
        pvz.Pao((5,8))
    y = 8.5 
    if wave == 20:
        y = 9
    pvz.Delay(600)
    pvz.UpdatePaoList()
    pvz.Pao((2,y))
    pvz.Pao((5,y))

@running_in_thread
def 炮消珊瑚():
    pvz.Prejudge(-125, 20)
    pvz.Pao((4,7))

@running_in_thread
def 冰杀小偷():
    pvz.Prejudge(150, 10)
    pvz.Card("寒冰菇", (1,7))
    pvz.Card("咖啡豆", (1,7))
    pvz.Prejudge(150, 20)
    pvz.Card("寒冰菇", (1,7))
    pvz.Card("咖啡豆", (1,7))

@running_in_thread
def 冰消珊瑚():
    pvz.Prejudge(-200, 20)
    pvz.Card("寒冰菇", (1,7))
    pvz.Card("咖啡豆", (1,7))

@running_in_thread
def 临时伞():
    for wave in [10, 20]:
        pvz.Prejudge(0,wave)
        pvz.Card("叶子保护伞", (2,7))
        pvz.Delay(600)
        pvz.Shovel((2,7))

while True:
    pvz.Sleep(600)
    # 选卡并开始
    pvz.SelectCards(["毁灭菇", "咖啡豆", "叶子保护伞", "辣椒", "寒冰菇", "窝瓜", "樱桃", "三叶草", "南瓜头", "睡莲"])
    giga_waves = pvz.utils.get_zombie_spawning_appear_waves(32)
    
    # pvz.StartAutoCollectThread()
    pvz.StartNutsFixerThread([(1,1),(2,1),(1,5),(1,6),(1,7)], "南瓜头")
    临时伞()
    炮消珊瑚()
    预判炮炸()
    预判核炸()


    while pvz.GameUI() != 2:
        pvz.Sleep(100)