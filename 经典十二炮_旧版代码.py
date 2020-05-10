import pvz

pvz.EnableLogger(True)
while not pvz.FindPvZ():
    print("等待找到游戏")
    pvz.Sleep(100)

pvz.BackgroundRunning(True)
# pvz.GotoEndless()
print(f"当前场景: {pvz.GameUI()}")
pvz.QuickPass()
# pvz.StartAutoCollectThread()
n_pos = (3,9)
while True:
    pvz.Sleep(600)
    # 选卡并开始
    pvz.SelectCards(["毁灭菇", "咖啡豆", "小喷菇", "阳光菇", "胆小菇", "花盆", "樱桃", "三叶草", "南瓜头", "睡莲"])
    giga_waves = pvz.utils.get_zombie_spawning_appear_waves(32)
    
    pvz.StartAutoCollectThread()
    pvz.StartNutsFixerThread([(1,1),(2,1),(5,1),(6,1)], "南瓜头")
    # 前9波
    # pvz.Prejudge(-130, 1)
    for i in range(1, 10):
        pvz.Prejudge(-100, i)
        pvz.UpdatePaoList()
        pvz.Pao((2,9))
        pvz.Pao((5,9))
        # pvz.Delay(600)

    print("第9波收尾")
    if giga_waves[8]:
        for i in range(2):
            pvz.Delay(600)
            pvz.UpdatePaoList()
            pvz.Pao((2,9))
            pvz.Pao((5,9))

    else:
        pvz.Delay(600)
        pvz.UpdatePaoList()
        pvz.Pao((2,9))
        pvz.Pao((5,9))

    # 第10波
    pvz.Prejudge(-50, 10)
    pvz.UpdatePaoList()
    pvz.Pao((2,9))
    pvz.Pao((5,9))
    # pvz.Delay(250)
    # pvz.Card("樱桃", (2,9))
    if n_pos == (3,9):
        n_pos = (4,9)
    else:
        n_pos = (3,9)
    pvz.Card("睡莲", n_pos)
    pvz.Card("毁灭菇", n_pos)
    pvz.Card("咖啡豆", n_pos)
    pvz.Delay(200)
    pvz.Card("三叶草", (1,7))
    # pvz.Prejudge(-130, 11)


    # 第11-19波
    for i in range(11, 20):
        pvz.Prejudge(-100, i)
        pvz.UpdatePaoList()
        pvz.Pao((2,9))
        pvz.Pao((5,9))
        # pvz.Delay(600)


    print("第19波收尾")
    if giga_waves[18]:
        for i in range(2):
            pvz.Delay(600)
            pvz.UpdatePaoList()
            pvz.Pao((2,9))
            pvz.Pao((5,9))


    else:
        pvz.Delay(600)
        pvz.UpdatePaoList()
        pvz.Pao((2,9))
        pvz.Pao((5,9))


    pvz.Prejudge(-150, 20)
    pvz.UpdatePaoList()
    pvz.Pao((4,7))
    pvz.Delay(100)
    pvz.Pao((2,9))
    pvz.Pao((5,9))
    if giga_waves[19]:
        for i in range(2):
            pvz.Delay(600)
            pvz.UpdatePaoList()
            pvz.Pao((2,9))
            pvz.Pao((5,9))
        pvz.Delay(600)
        pvz.UpdatePaoList()
        pvz.Pao((2,8))
        pvz.Pao((5,8))

    else:
        pvz.Delay(600)
        pvz.UpdatePaoList()
        pvz.Pao((2,9))
        pvz.Pao((5,9))

    while pvz.GameUI() != 2:
        pvz.Sleep(100)