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
# pvz.StartAutoCollectThread()

@running_in_thread
def PaoThread():
    wave = 0
    while wave < 20:
        wave += 1
        logger.info(f"本波次为: {wave}")
        try:
            pvz.Prejudge(-130,wave)
        except Exception as e:
            logger.warning(e)
        pvz.UpdatePaoList()
        pvz.Pao((2,9))
        pvz.Pao((5,9))
        if wave in [1,3,5,6,8,10,12,14,15,17,19,20]:
            pvz.Delay(115)
            pvz.Pao((2,7.35))
            pvz.Pao((5,7.35))
        else:
            pvz.Delay(350)
            pvz.Pao((2,3))
            pvz.Pao((5,3))
        if wave in [9,19,20]:
            LastPao(wave)
        pvz.Delay(wait_countdown_cs)
        countdown = pvz.WaveCountdown() 
        logger.info(f"距离下一波刷新还有{countdown}cs")
        if countdown > 300 and wave not in [9,19,20]:
            YanChiChuLi()

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
        pvz.Card("窝瓜", (2,9))
        pvz.Card("窝瓜", (2,8)) #try
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



n_pos = (3,9)
while True:
    pvz.Sleep(600)
    # 选卡并开始
    pvz.SelectCards(["毁灭菇", "咖啡豆", "小喷菇", "阳光菇", "寒冰菇", "窝瓜", "樱桃", "三叶草", "南瓜头", "睡莲"])
    giga_waves = pvz.utils.get_zombie_spawning_appear_waves(32)
    
    pvz.StartAutoCollectThread()
    # FangShuaGuaiYanChi()
    PaoThread()
    BingShaXiaoTou()
    PaoXiaoShanHu()


    while pvz.GameUI() != 2:
        pvz.Sleep(100)