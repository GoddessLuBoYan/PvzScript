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
pvz.StartAutoCollectThread()

pvz.seeds.IMITATER_X = 470
pvz.seeds.IMITATER_Y = 470
pvz.seeds.simulate_manual_control = False

@running_in_thread
def PaoThread():
    pvz.Prejudge(200, 1)
    while pvz.GameUI() == 3:
        pvz.UpdatePaoList()
        pvz.Pao((2,7.7))
        pvz.Pao((5,7.7))
        pvz.Delay(700)


def LastPao(wave):
    global giga_waves
    has_giga = giga_waves[wave-1]
    if has_giga or wave == 20:
        pao_count = 3
    else:
        pao_count = 1
    y = 8.5 
    if wave == 20:
        y = 9
    pvz.Delay(200)
    for _ in range(pao_count):
        pvz.Delay(400)
        pvz.UpdatePaoList()
        pvz.Pao((2,y))
        pvz.Pao((5,y))

@running_in_thread
def FangShuaGuaiYanChi():
    last_wave = -1
    delay_time = 0
    while True:
        pvz.Delay(50)
        wave = pvz.CurrentWave()
        if wave != last_wave:
            last_wave = wave
            delay_time = 0
            continue
        if wave in [9,19] or wave < 1:
            continue
        if wave == 20:
            break
        delay_time += 50
        if delay_time >= 700:
            YanChiChuLi()
            delay_time -= 600

chuli_count = 0
def YanChiChuLi():
    # cards = ["樱桃炸弹", "窝瓜", "毁灭菇"]
    global chuli_count
    if chuli_count == 0:
        pvz.Card("樱桃炸弹", (2,9))
        pvz.Card("樱桃炸弹", (2,8)) #try
    elif chuli_count == 1:
        pvz.Card("窝瓜", (5,9))
        pvz.Card("窝瓜", (5,8)) #try
    elif chuli_count == 2:
        pvz.Card("睡莲", (3,9))
        pvz.Card("毁灭菇", (3,9))
        pvz.Card("咖啡豆", (3,9))
        pvz.Card("睡莲", (4,9)) #try
        pvz.Card("毁灭菇", (4,9))
        pvz.Card("咖啡豆", (4,9))
    chuli_count += 1
    if chuli_count >= 3:
        chuli_count = 0

@running_in_thread
def PaoXiaoShanHu():
    pvz.Prejudge(-125, 20)
    pvz.Pao((4,7))

@running_in_thread
def BingShaXiaoTou():
    pvz.Prejudge(150, 10)
    pvz.Card("寒冰菇", (1,7))
    pvz.Card("咖啡豆", (1,7))
    pvz.Prejudge(150, 20)
    pvz.Card("寒冰菇", (1,7))
    pvz.Card("咖啡豆", (1,7))

@running_in_thread
def BingXiaoShanHu():
    pvz.Prejudge(-200, 20)
    pvz.Card("寒冰菇", (1,7))
    pvz.Card("咖啡豆", (1,7))

@running_in_thread
def 临时伞():
    pvz.Prejudge(0,10)
    pvz.Card("睡莲", (3,8))
    pvz.Card("叶子保护伞", (3,8))
    pvz.Prejudge(0,20)
    pvz.Card("睡莲", (3,8))
    pvz.Card("叶子保护伞", (3,8))

n_pos = (3,9)
while True:
    pvz.Sleep(600)
    # 选卡并开始
    pvz.SelectCards(["高坚果", "咖啡豆", "叶子保护伞", "小喷菇", "寒冰菇", "窝瓜", "樱桃", "三叶草", "南瓜头", "睡莲"])
    giga_waves = pvz.utils.get_zombie_spawning_appear_waves(32)
    
    pvz.StartAutoCollectThread()
    pvz.StartNutsFixerThread([(3,7),(4,7)], "高坚果")
    # FangShuaGuaiYanChi()
    PaoThread()
    # BingShaXiaoTou()
    # PaoXiaoShanHu()
    BingXiaoShanHu()
    临时伞()


    while pvz.GameUI() != 2:
        pvz.Sleep(100)