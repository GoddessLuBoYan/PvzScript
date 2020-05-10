# 阵型字符串: 

# 0,2A 1 1 1 0 0,1E 1 1 0 2 0,29 1 2 0 0 0,1E 1 2 0 1 1,30 1 2 0 0 0,2C 1 3 0 0 0,1E 1 3 0 0 1,30 1 3 0 0 0,25 2 1 0 1 0,1E 2 1 0 2 0,2A 2 2 1 0 0,1E 2 2 0 0 1,30 2 2 0 0 0,29 2 3 0 0 0,1E 2 3 0 2 1,30 2 3 0 0 0,2C 2 4 0 0 0,1E 2 4 0 0 1,30 2 4 0 0 0,2A 2 5 1 0 0,2F 3 1 0 0 0,10 3 1 0 0 0,10 3 2 0 0 0,2F 3 3 0 0 0,10 3 3 0 0 0,10 3 4 0 0 0,2B 3 5 0 0 0,1E 3 5 0 0 0,2A 3 6 1 0 0,10 3 6 0 0 0,1E 3 6 0 0 0,2F 4 1 0 0 0,10 4 1 0 0 0,10 4 2 0 0 0,2F 4 3 0 0 0,10 4 3 0 0 0,10 4 4 0 0 0,E 4 5 0 0 0,10 4 5 0 0 0,1E 4 5 0 0 0,2A 4 6 1 0 0,10 4 6 0 0 0,1E 4 6 0 0 0,25 5 1 0 1 0,1E 5 1 0 2 0,2A 5 2 1 0 0,1E 5 2 0 0 1,30 5 2 0 0 0,29 5 3 0 2 0,1E 5 3 0 0 1,30 5 3 0 0 0,2C 5 4 0 0 0,1E 5 4 0 0 1,30 5 4 0 0 0,2A 5 5 1 0 0,2A 6 1 1 0 0,1E 6 1 0 0 0,29 6 2 0 2 0,1E 6 2 0 1 1,30 6 2 0 0 0,2C 6 3 0 0 0,1E 6 3 0 2 1,30 6 3 0 0 0
import pvz
import pvz.logger as logger
import sys
from pvz.threads import running_in_thread

pvz.EnableLogger(True)
while not pvz.FindPvZ():
    print("等待找到游戏")
    pvz.Sleep(100)

pvz.BackgroundRunning(True)
# pvz.GotoEndless()
print(f"当前场景: {pvz.GameUI()}")
# pvz.QuickPass()
# pvz.JumpLevel(1009)
pvz.SetZombies(zombies=["撑杆", "舞王", "冰车", "普通", "读报", "矿工", "小丑", "橄榄", "白眼", "红眼", "蹦极"], mode="自然刷怪")
# pvz.StartAutoCollectThread()

# pvz.seeds.IMITATER_X = 470
# pvz.seeds.IMITATER_Y = 470
# pvz.seeds.simulate_manual_control = False

def PP():
    pvz.UpdatePaoList()
    pvz.Pao((2,8))
    pvz.Pao((5,8))
    return "PP"

def I():
    pvz.Coffee()
    return "I"

def N():
    for pos in [(3,8), (3,9), (4,8), (4,9)]:
        pvz.Card("睡莲", pos)
        pvz.Card("核弹", pos)
        pvz.Card("咖啡豆", pos)
    return "N"

def c6u():
    # i_delay = 373+100-298+109 ice3
    i_delay = 373+200
    pp_delay = 1750 - i_delay
    while True:
        yield I()
        pvz.Delay(pp_delay)
        yield PP()
        pvz.Delay(i_delay)
        yield I()
        pvz.Delay(pp_delay)
        yield PP()
        pvz.Delay(700)
        yield N()
        pvz.Delay(1050)
        yield PP()
        pvz.Delay(i_delay)

@running_in_thread
def 收尾():
    curr_wave = pvz.CurrentWave()
    if giga_waves[curr_wave - 1]:
        pao_time = 2
    elif garg_waves[curr_wave - 1]:
        pao_time = 1
    else:
        pao_time = 0
    y_pos = 7.5
    for _ in range(pao_time):
        pvz.Delay(1750)
        pvz.UpdatePaoList()
        pvz.Pao((2, y_pos))
        pvz.Pao((5, y_pos))
        y_pos -= 0.5


@running_in_thread
def 冰杀小偷():
    pvz.Prejudge(150, 10)
    pvz.Coffee()
    pvz.Prejudge(150, 20)
    pvz.Coffee()

@running_in_thread
def one_loop(first_wave, last_wave):
    pvz.Prejudge(110, first_wave)
    cor = c6u()
    while True:
        step = next(cor)
        wave = pvz.CurrentWave()
        if wave >= last_wave and (step == "N" or step == "PP"):
            收尾()
            break

def main():
    global giga_waves, garg_waves
    while True:
        while pvz.GameUI() != 2:
            pvz.Sleep(100)
        pvz.Sleep(600)
        # 选卡并开始
        pvz.SelectCards(["睡莲", "南瓜", "寒冰菇", "模仿寒冰菇", "咖啡豆", "核弹", "窝瓜", "三叶草", "小喷菇", "阳光菇"])
        giga_waves = pvz.utils.get_zombie_spawning_appear_waves(32)
        garg_waves = pvz.utils.get_zombie_spawning_appear_waves(23)
        
        pvz.StartAutoCollectThread()
        pvz.StartAutoFillIceThread(spots=[(4,5)])
        pvz.StartNutsFixerThread([(3,5),(3,6),(4,5),(4,6),(1,1),(2,1),(5,1),(6,1)], "南瓜头")

        one_loop(1, 9)
        one_loop(10, 19)
        one_loop(20, 20)

        

    sys.exit(0)

if __name__ == '__main__':
    main()