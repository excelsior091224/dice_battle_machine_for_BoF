import random, math, os, time
from datetime import datetime

# ダイスのクラス
class Dice:
    def __init__(self, dice_num, dice_size):
        # ダイスの数
        self.num = dice_num
        # ダイスの面数
        self.size = dice_size
    
    # ダイスを投げたときの処理
    def throw_dice(self):
        # ダイスの目を格納するリスト
        dice_roll = []
        # ダイスの数だけ繰り返すループ
        for i in range(self.num):
            # ダイスの面数からランダムな数（ダイスの出目）を変数numに代入
            num = random.randint(1, self.size)
            # ダイスの出目numをリストdice_rollに格納
            dice_roll.append(num)
        # ダイスの目が個数分入ったリストを返り値とする
        # 例：6面ダイス2個の場合：[1個目のダイスの目,2個目のダイスの目]
        return dice_roll

# ボクサーのクラス
class Boxer:
    def __init__(self, name, punch_power, speed, toughness, dice_12, dice_6):
        # ボクサーの名前
        self.name = name
        # HPの数
        self.hp = 40
        # パンチ力
        self.punch_power = punch_power
        # スピード
        self.speed = speed
        # タフネス
        self.toughness = toughness
        # 12面ダイス2個
        self.dice_12 = dice_12
        # 6面ダイス2個
        self.dice_6 = dice_6
        # 1ラウンドごとの攻勢に回った回数
        self.attack_num = 0
        print(self.name + '\n' + 'HP:' + str(self.hp) + '\n' + 'パンチ力:' + str(self.punch_power) + '\n' + 'スピード:' + str(self.speed) + '\n' + 'タフネス:' + str(self.toughness))

# 対戦ログを保存するフォルダを作成する関数
def make_folder():
    fight_log_dir = "fight_log"
    try:
        os.makedirs(fight_log_dir)
    except FileExistsError:
        pass
    return fight_log_dir

# 数値入力関数
# num_typeには入力する数値の種別を入れる
def decide_num(num_type):
    # 変数numが決定されるまでループ
    while True:
        # 1以上の数値を入力
        num = input('{}の値を入力してください（1以上の数字）:'.format(num_type))
        # 入力値を整数に変換
        try:
            num = int(num)
        # 数字以外の文字が入力された場合
        except ValueError:
            print("数字を入力してください")
        # 数字が入力された場合
        else:
            # 数字が0以下（0及び負の整数）の場合
            if num <= 0:
                print("1以上の数字を入力してください")
            # 1以上の数字が正常に入力された場合
            else:
                # "数値種別:数値"を表示
                print("{}:".format(num_type) + str(num))
                # numを返り値として終了
                return num

def match(FIGHT_LOG_DIR,max_round,red_boxer,blue_boxer):
    fight_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    match_title = '{}_{}_VS_{}'.format(fight_datetime, red_boxer.name, blue_boxer.name)
    log_title = FIGHT_LOG_DIR + '/' + match_title
    log_text = ''
    log_text += match_title + '\n'
    print_text = ''
    max_round = max_round
    current_round = 1
    current_turn = 1
    print_text = '試合開始!\n'
    print(print_text)
    log_text += print_text + '\n'
    while current_round <= max_round or red_boxer.hp <= 0 or blue_boxer.hp <= 0:
        input('いずれかのキーを押すと試合が進行します:')
        red_dice_12 = red_boxer.dice_12.throw_dice()
        blue_dice_12 = blue_boxer.dice_12.throw_dice()
        red_dice_12_sum = sum(red_dice_12) + red_boxer.speed
        blue_dice_12_sum = sum(blue_dice_12) + blue_boxer.speed

        print_text = str(current_round) + "ラウンド" + str(current_turn) + "ターン目\n"
        print(print_text)
        log_text += print_text + '\n'

        print_text = '赤コーナー:{}:{}:{} VS 青コーナー:{}:{}:{}\n'.format(red_boxer.name, str(red_dice_12),str(red_dice_12_sum),blue_boxer.name,str(blue_dice_12),str(blue_dice_12_sum))
        print(print_text)
        log_text += print_text + '\n'
        
        if red_dice_12_sum > blue_dice_12_sum:
            red_boxer.attack_num += 1
            print_text = '赤コーナー・{}選手の攻撃\n'.format(red_boxer.name)
            print(print_text)
            log_text += print_text + '\n'

            red_dice_6 = red_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(red_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            if red_dice_6[0] == 1:
                if red_dice_6[1] >= 1 and red_dice_6[1] <= 3:
                    red_punch_type = 'ジャブ'
                elif red_dice_6[1] >= 4 and red_dice_6[1] <= 6:
                    red_punch_type = 'ジャブの連打'
            elif red_dice_6[0] == 2:
                if red_dice_6[1] >= 1 and red_dice_6[1] <= 3:
                    red_punch_type = '左ボディブロー'
                elif red_dice_6[1] >= 4 and red_dice_6[1] <= 6:
                    red_punch_type = '右ボディブロー'
            elif red_dice_6[0] == 3:
                if red_dice_6[1] >= 1 and red_dice_6[1] <= 3:
                    red_punch_type = '左ストレート'
                elif red_dice_6[1] >= 4 and red_dice_6[1] <= 6:
                    red_punch_type = '右ストレート'
            elif red_dice_6[0] == 4:
                if red_dice_6[1] >= 1 and red_dice_6[1] <= 3:
                    red_punch_type = '左フック'
                elif red_dice_6[1] >= 4 and red_dice_6[1] <= 6:
                    red_punch_type = '右フック'
            elif red_dice_6[0] == 5:
                if red_dice_6[1] >= 1 and red_dice_6[1] <= 3:
                    red_punch_type = '左アッパーカット'
                elif red_dice_6[1] >= 4 and red_dice_6[1] <= 6:
                    red_punch_type = '右アッパーカット'
            elif red_dice_6[0] == 6:
                if red_dice_6[1] >= 1 and red_dice_6[1] <= 3:
                    red_punch_type = 'カウンターパンチ'
                elif red_dice_6[1] >= 4 and red_dice_6[1] <= 6:
                    red_punch_type = '必殺技'
            red_attack_num = sum(red_dice_6) + red_boxer.punch_power - blue_boxer.toughness
            print_text = '赤コーナー・{}選手の{}!\n'.format(red_boxer.name,red_punch_type)
            print(print_text)
            log_text += print_text + '\n'

            if red_attack_num < 1:
                print_text = 'しかし、防御された!\n'
                print(print_text)
                log_text += print_text + '\n'
            elif red_punch_type == 'ジャブ':
                blue_boxer.hp -= red_attack_num
                print_text = '青コーナー・{}選手に{}のダメージ。体力{}\n'.format(blue_boxer.name,str(red_attack_num),str(blue_boxer.hp))
                print(print_text)
                log_text += print_text + '\n'
                if blue_boxer.hp <= 0:
                    blue_boxer.hp = 1
                    print_text = 'ジャブのため持ちこたえる。体力{}\n'.format(blue_boxer.hp)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_attack_num >= 7:
                        print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        if blue_boxer.toughness == 1:
                            blue_boxer.toughness = 1
                            if blue_boxer.speed <= 1:
                                blue_boxer.speed = 1
                            else:
                                blue_boxer.speed -= 1
                        else:
                            blue_boxer.toughness -= 1
                        blue_dice_6 = blue_boxer.dice_6.throw_dice()
                        print_text = '{}\n'.format(blue_dice_6)
                        print(print_text)
                        log_text += print_text + '\n'
                        if sum(blue_dice_6) <= 3:
                            print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                            print(print_text)
                            log_text += print_text + '\n'
                            print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                            print(print_text)
                            log_text += print_text + '\n'
                            with open(log_title, mode='w', encoding='utf-8') as f:
                                f.write(log_text)
                            input('キーを押したら終了します')
                            break
                        elif sum(blue_dice_6) >= 4 and sum(blue_dice_6) <= 6:
                            print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,)
                            print(print_text)
                            log_text += print_text + '\n'
                            blue_boxer.hp += 1
                            print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                        elif sum(blue_dice_6) >= 7:
                            print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                            blue_boxer.hp += 2
                            print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                elif 15 <= blue_boxer.hp <= 40 and red_attack_num >= 16:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if blue_boxer.toughness == 1:
                        blue_boxer.toughness = 1
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                        else:
                            blue_boxer.speed -= 1
                    else:
                        blue_boxer.toughness -= 1
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) == 2:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 3 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,)
                        print(print_text)
                        log_text += print_text + '\n'
                        if blue_boxer.hp <= 39:
                            blue_boxer.hp += 1
                            print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        if blue_boxer.hp <= 38:
                            blue_boxer.hp += 2
                            print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                        elif blue_boxer.hp == 39:
                            blue_boxer.hp += 1
                            print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                elif blue_boxer.hp >= 10 and blue_boxer.hp <= 14 and red_attack_num >= 13:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    if blue_boxer.toughness == 1:
                        blue_boxer.toughness = 1
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                        else:
                            blue_boxer.speed -= 1
                    else:
                        blue_boxer.toughness -= 1
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) == 2:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 3 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 1
                        print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 2
                        print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp >= 1 and blue_boxer.hp <= 9 and red_attack_num >= 7:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if blue_boxer.toughness == 1:
                        blue_boxer.toughness = 1
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                        else:
                            blue_boxer.speed -= 1
                    else:
                        blue_boxer.toughness -= 1
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) <= 3:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 4 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 1
                        print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 2
                        print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
            elif red_punch_type == '必殺技':
                blue_boxer.hp -= red_attack_num
                print_text = '青コーナー・{}選手に{}のダメージ。体力{}\n'.format(blue_boxer.name,str(red_attack_num),str(blue_boxer.hp))
                print(print_text)
                log_text += print_text + '\n'
                print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                print(print_text)
                log_text += print_text + '\n'
                if blue_boxer.toughness == 2:
                    blue_boxer.toughness = 1
                    if blue_boxer.speed <= 1:
                        blue_boxer.speed = 1
                    else:
                        blue_boxer.speed -= (2 - blue_boxer.toughness)
                elif blue_boxer.toughness <= 1:
                    blue_boxer.toughness = 1
                    if blue_boxer.speed <= 2:
                        blue_boxer.speed = 1
                    else:
                        blue_boxer.speed -= 2
                else:
                    blue_boxer.toughness -= 2
                if blue_boxer.hp >= 15:
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) == 2:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 3 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        if blue_boxer.hp <= 39:
                            blue_boxer.hp += 1
                            print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        if blue_boxer.hp <= 38:
                            blue_boxer.hp += 2
                            print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                        elif blue_boxer.hp == 39:
                            blue_boxer.hp += 1
                            print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                elif blue_boxer.hp >= 10 and blue_boxer.hp <= 14:
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) == 2:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 3 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 1
                        print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 2
                        print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp >= 1 and blue_boxer.hp <= 9:
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) <= 3:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 4 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 1
                        print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 2
                        print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp >= -3 and blue_boxer.hp <= 0:
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) <= 4:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 5 and sum(blue_dice_6) <= 6:
                        blue_boxer.hp = 1
                        print_text = '青コーナー・{}選手立ち上がる。体力{}に回復\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        blue_boxer.hp = 2
                        print_text = '青コーナー・{}選手立ち上がる。体力{}に回復\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp >= -4 and blue_boxer.hp <= 0:
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        break
                    elif sum(blue_dice_6) == 7:
                        blue_boxer.hp = 1
                        print_text = '青コーナー・{}選手立ち上がる。体力{}に回復\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 8:
                        blue_boxer.hp = 2
                        print_text = '青コーナー・{}選手立ち上がる。体力{}に回復\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp <= -5:
                    print_text = '青コーナー・{}選手TKO!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    print_text = '赤コーナー・{}選手のTKO勝利!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title, mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break
            else:
                blue_boxer.hp -= red_attack_num
                print_text = '青コーナー・{}選手に{}のダメージ。体力{}\n'.format(blue_boxer.name,str(red_attack_num),str(blue_boxer.hp))
                print(print_text)
                log_text += print_text + '\n'
                if blue_boxer.hp >= 15 and red_attack_num >= 16:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if blue_boxer.toughness == 1:
                        blue_boxer.toughness = 1
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                        else:
                            blue_boxer.speed -= 1
                    else:
                        blue_boxer.toughness -= 1
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) == 2:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 3 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,)
                        print(print_text)
                        log_text += print_text + '\n'
                        if blue_boxer.hp <= 39:
                            blue_boxer.hp += 1
                            print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        if blue_boxer.hp <= 38:
                            blue_boxer.hp += 2
                            print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                        elif blue_boxer.hp == 39:
                            blue_boxer.hp += 1
                            print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                elif blue_boxer.hp >= 10 and blue_boxer.hp <= 14 and red_attack_num >= 13:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    if blue_boxer.toughness == 1:
                        blue_boxer.toughness = 1
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                        else:
                            blue_boxer.speed -= 1
                    else:
                        blue_boxer.toughness -= 1
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) == 2:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 3 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 1
                        print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 2
                        print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp >= 1 and blue_boxer.hp <= 9 and red_attack_num >= 7:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if blue_boxer.toughness == 1:
                        blue_boxer.toughness = 1
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                        else:
                            blue_boxer.speed -= 1
                    else:
                        blue_boxer.toughness -= 1
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) <= 3:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 4 and sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 1
                        print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        print_text = '青コーナー・{}選手立ち上がる。\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        blue_boxer.hp += 2
                        print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp >= -3 and blue_boxer.hp <= 0:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if blue_boxer.toughness == 1:
                        blue_boxer.toughness = 1
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                        else:
                            blue_boxer.speed -= 1
                    else:
                        blue_boxer.toughness -= 1
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) <= 4:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) >= 5 and sum(blue_dice_6) <= 6:
                        blue_boxer.hp = 1
                        print_text = '青コーナー・{}選手立ち上がる。体力{}に回復\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 7:
                        blue_boxer.hp = 2
                        print_text = '青コーナー・{}選手立ち上がる。体力{}に回復\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp >= -4 and blue_boxer.hp < -3:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if blue_boxer.toughness == 1:
                        blue_boxer.toughness = 1
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                        else:
                            blue_boxer.speed -= 1
                    else:
                        blue_boxer.toughness -= 1
                    blue_dice_6 = blue_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(blue_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(blue_dice_6) <= 6:
                        print_text = '青コーナー・{}選手KO!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '赤コーナー・{}選手のKO勝利!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(blue_dice_6) == 7:
                        blue_boxer.hp = 1
                        print_text = '青コーナー・{}選手立ち上がる。体力{}に回復\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(blue_dice_6) >= 8:
                        blue_boxer.hp = 2
                        print_text = '青コーナー・{}選手立ち上がる。体力{}に回復\n'.format(blue_boxer.name,blue_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif blue_boxer.hp <= -5:
                    print_text = '青コーナー・{}選手ダウン!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    blue_boxer.toughness -= 1
                    print_text = '青コーナー・{}選手TKO!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    print_text = '赤コーナー・{}選手のTKO勝利!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title, mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break

        elif blue_dice_12_sum > red_dice_12_sum:
            blue_boxer.attack_num += 1
            print_text = '青コーナー・{}選手の攻撃\n'.format(blue_boxer.name)
            print(print_text)
            log_text += print_text + '\n'

            blue_dice_6 = blue_boxer.dice_6.throw_dice()
            print_text = '{}\n'.format(blue_dice_6)
            print(print_text)
            log_text += print_text + '\n'
            if blue_dice_6[0] == 1:
                if blue_dice_6[1] >= 1 and blue_dice_6[1] <= 3:
                    blue_punch_type = 'ジャブ'
                elif blue_dice_6[1] >= 4 and blue_dice_6[1] <= 6:
                    blue_punch_type = 'ジャブの連打'
            elif blue_dice_6[0] == 2:
                if blue_dice_6[1] >= 1 and blue_dice_6[1] <= 3:
                    blue_punch_type = '左ボディブロー'
                elif blue_dice_6[1] >= 4 and blue_dice_6[1] <= 6:
                    blue_punch_type = '右ボディブロー'
            elif blue_dice_6[0] == 3:
                if blue_dice_6[1] >= 1 and blue_dice_6[1] <= 3:
                    blue_punch_type = '左ストレート'
                elif blue_dice_6[1] >= 4 and blue_dice_6[1] <= 6:
                    blue_punch_type = '右ストレート'
            elif blue_dice_6[0] == 4:
                if blue_dice_6[1] >= 1 and blue_dice_6[1] <= 3:
                    blue_punch_type = '左フック'
                elif blue_dice_6[1] >= 4 and blue_dice_6[1] <= 6:
                    blue_punch_type = '右フック'
            elif blue_dice_6[0] == 5:
                if blue_dice_6[1] >= 1 and blue_dice_6[1] <= 3:
                    blue_punch_type = '左アッパーカット'
                elif blue_dice_6[1] >= 4 and blue_dice_6[1] <= 6:
                    blue_punch_type = '右アッパーカット'
            elif blue_dice_6[0] == 6:
                if blue_dice_6[1] >= 1 and blue_dice_6[1] <= 3:
                    blue_punch_type = 'カウンターパンチ'
                elif blue_dice_6[1] >= 4 and blue_dice_6[1] <= 6:
                    blue_punch_type = '必殺技'
            blue_attack_num = sum(blue_dice_6) + blue_boxer.punch_power - red_boxer.toughness
            print_text = '青コーナー・{}選手の{}!\n'.format(blue_boxer.name,blue_punch_type)
            print(print_text)
            log_text += print_text + '\n'
            if blue_attack_num < 1:
                print_text = 'しかし、防御された!\n'.format(blue_boxer.name,blue_punch_type)
                print(print_text)
                log_text += print_text + '\n'
            elif blue_punch_type == 'ジャブ':
                red_boxer.hp -= blue_attack_num
                print_text = '赤コーナー・{}選手に{}のダメージ。体力{}\n'.format(red_boxer.name,str(blue_attack_num),str(red_boxer.hp))
                print(print_text)
                log_text += print_text + '\n'
                if red_boxer.hp <= 0:
                    red_boxer.hp = 1
                    print_text = 'ジャブのため持ちこたえる。体力{}\n'.format(red_boxer.hp)
                    print(print_text)
                    log_text += print_text + '\n'
                    if blue_attack_num >= 7:
                        print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        if red_boxer.toughness == 1:
                            red_boxer.toughness = 1
                            if red_boxer.speed <= 1:
                                red_boxer.speed = 1
                            else:
                                red_boxer.speed -= 1
                        else:
                            red_boxer.toughness -= 1
                        red_dice_6 = red_boxer.dice_6.throw_dice()
                        print_text = '{}\n'.format(red_dice_6)
                        print(print_text)
                        log_text += print_text + '\n'
                        if sum(red_dice_6) <= 3:
                            print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                            print(print_text)
                            log_text += print_text + '\n'
                            print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                            print(print_text)
                            log_text += print_text + '\n'
                            with open(log_title, mode='w', encoding='utf-8') as f:
                                f.write(log_text)
                            input('キーを押したら終了します')
                            break
                        elif sum(red_dice_6) >= 4 and sum(red_dice_6) <= 6:
                            print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name,)
                            print(print_text)
                            log_text += print_text + '\n'
                            red_boxer.hp += 1
                            print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                        elif sum(red_dice_6) >= 7:
                            print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                            red_boxer.hp += 2
                            print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                elif 15 <= red_boxer.hp <= 40 and blue_attack_num >= 16:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(red_dice_6) == 2:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 3 and sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name,)
                        print(print_text)
                        log_text += print_text + '\n'
                        if red_boxer.hp <= 39:
                            red_boxer.hp += 1
                            print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        if red_boxer.hp <= 38:
                            red_boxer.hp += 2
                            print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                        elif red_boxer.hp == 39:
                            red_boxer.hp += 1
                            print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                elif red_boxer.hp >= 10 and red_boxer.hp <= 14 and blue_attack_num >= 13:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(red_dice_6) == 2:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 3 and sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 1
                        print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 2
                        print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp >= 1 and red_boxer.hp <= 9 and blue_attack_num >= 7:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    log_text += print_text + '\n'
                    if sum(red_dice_6) <= 3:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 4 and sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 1
                        print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 2
                        print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
            elif blue_punch_type == '必殺技':
                red_boxer.hp -= blue_attack_num
                print_text = '赤コーナー・{}選手に{}のダメージ。体力{}\n'.format(red_boxer.name,str(blue_attack_num),str(red_boxer.hp))
                print(print_text)
                log_text += print_text + '\n'
                print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                print(print_text)
                log_text += print_text + '\n'
                if red_boxer.toughness == 2:
                    red_boxer.toughness = 1
                    if red_boxer.speed <= 1:
                        red_boxer.speed = 1
                    else:
                        red_boxer.speed -= (2 - red_boxer.toughness)
                elif red_boxer.toughness <= 1:
                    red_boxer.toughness = 1
                    if red_boxer.speed <= 2:
                        red_boxer.speed = 1
                    else:
                        red_boxer.speed -= 2
                else:
                    red_boxer.toughness -= 2
                if red_boxer.hp >= 15:
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) == 2:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 3 and sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        if red_boxer.hp <= 39:
                            red_boxer.hp += 1
                            print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        if red_boxer.hp <= 38:
                            red_boxer.hp += 2
                            print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                        elif red_boxer.hp == 39:
                            red_boxer.hp += 1
                            print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                elif red_boxer.hp >= 10 and red_boxer.hp <= 14:
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) == 2:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 3 and sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 1
                        print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 2
                        print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp >= 1 and red_boxer.hp <= 9:
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) <= 3:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 4 and sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 1
                        print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 2
                        print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp >= -3 and red_boxer.hp <= 0:
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) <= 4:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 5 and sum(red_dice_6) <= 6:
                        red_boxer.hp = 1
                        print_text = '赤コーナー・{}選手立ち上がる。体力{}に回復\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        red_boxer.hp = 2
                        print_text = '赤コーナー・{}選手立ち上がる。体力{}に回復\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp >= -4 and red_boxer.hp < -3:
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) == 7:
                        red_boxer.hp = 1
                        print_text = '赤コーナー・{}選手立ち上がる。体力{}に回復\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 8:
                        red_boxer.hp = 2
                        print_text = '赤コーナー・{}選手立ち上がる。体力{}に回復\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp <= -5:
                    print_text = '赤コーナー・{}選手TKO!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    print_text = '青コーナー・{}選手のTKO勝利!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title, mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break
            else:
                red_boxer.hp -= blue_attack_num
                print_text = '赤コーナー・{}選手に{}のダメージ。体力{}\n'.format(red_boxer.name,str(blue_attack_num),str(red_boxer.hp))
                print(print_text)
                log_text += print_text + '\n'
                if red_boxer.hp >= 15 and blue_attack_num >= 16:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) == 2:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 3 and sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        if red_boxer.hp <= 39:
                            red_boxer.hp += 1
                            print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name,)
                        print(print_text)
                        log_text += print_text + '\n'
                        if red_boxer.hp <= 38:
                            red_boxer.hp += 2
                            print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                        elif red_boxer.hp == 39:
                            red_boxer.hp += 1
                            print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                            print(print_text)
                            log_text += print_text + '\n'
                elif red_boxer.hp >= 10 and red_boxer.hp <= 14 and blue_attack_num >= 13:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) == 2:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 3 and sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 1
                        print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 2
                        print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp >= 1 and red_boxer.hp <= 9 and blue_attack_num >= 7:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) <= 3:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 4 and sum(blue_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 1
                        print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        print_text = '赤コーナー・{}選手立ち上がる。\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        red_boxer.hp += 2
                        print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp >= -3 and red_boxer.hp <= 0:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) <= 4:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) >= 5 and sum(red_dice_6) <= 6:
                        red_boxer.hp = 1
                        print_text = '赤コーナー・{}選手立ち上がる。体力{}に回復\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 7:
                        red_boxer.hp = 2
                        print_text = '赤コーナー・{}選手立ち上がる。体力{}に回復\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp >= -4 and red_boxer.hp < -3:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    red_dice_6 = red_boxer.dice_6.throw_dice()
                    print_text = '{}\n'.format(red_dice_6)
                    print(print_text)
                    if sum(red_dice_6) <= 6:
                        print_text = '赤コーナー・{}選手KO!\n'.format(red_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        print_text = '青コーナー・{}選手のKO勝利!\n'.format(blue_boxer.name)
                        print(print_text)
                        log_text += print_text + '\n'
                        with open(log_title, mode='w', encoding='utf-8') as f:
                            f.write(log_text)
                        input('キーを押したら終了します')
                        break
                    elif sum(red_dice_6) == 7:
                        red_boxer.hp = 1
                        print_text = '赤コーナー・{}選手立ち上がる。体力{}に回復\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                    elif sum(red_dice_6) >= 8:
                        red_boxer.hp = 2
                        print_text = '赤コーナー・{}選手立ち上がる。体力{}に回復\n'.format(red_boxer.name,red_boxer.hp)
                        print(print_text)
                        log_text += print_text + '\n'
                elif red_boxer.hp <= -5:
                    print_text = '赤コーナー・{}選手ダウン!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    if red_boxer.toughness == 1:
                        red_boxer.toughness = 1
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                        else:
                            red_boxer.speed -= 1
                    else:
                        red_boxer.toughness -= 1
                    print_text = '赤コーナー・{}選手TKO!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    print_text = '赤コーナー・{}選手のTKO勝利!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title, mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break

        else:
            print_text = '両者クリンチ。\n'
            print(print_text)
            log_text += print_text + '\n'
            if red_boxer.hp <= 38:
                red_boxer.hp += 2
                print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
            elif red_boxer.hp == 39:
                red_boxer.hp += 1
                print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
            if blue_boxer.hp <= 38:
                blue_boxer.hp += 2
                print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
            elif blue_boxer.hp == 39:
                blue_boxer.hp += 1
                print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                print(print_text)
                log_text += print_text + '\n'
                    
        if current_turn == 3:
            print_text = '第{}ラウンド終了。\n'.format(str(current_round))
            print(print_text)
            log_text += print_text + '\n'
            current_turn = 1
            current_round += 1

            if current_round > max_round:
                print_text = '全ラウンド終了。\n'
                print(print_text)
                print_text = '赤コーナー:{}選手\nHP:{}\nパンチ力:{}\nスピード:{}\nタフネス:{}\n'.format(red_boxer.name,red_boxer.hp,red_boxer.punch_power,red_boxer.speed,red_boxer.toughness)
                print(print_text)
                log_text += print_text + '\n'
                print_text = '青コーナー:{}選手\nHP:{}\nパンチ力:{}\nスピード:{}\nタフネス:{}\n'.format(blue_boxer.name,blue_boxer.hp,blue_boxer.punch_power,blue_boxer.speed,blue_boxer.toughness)
                print(print_text)
                log_text += print_text + '\n'

                if red_boxer.hp > blue_boxer.hp:
                    print_text = '判定により、勝者・赤コーナー・{}選手!\n'.format(red_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title, mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break
                elif blue_boxer.hp > red_boxer.hp:
                    print_text = '判定により、勝者・青コーナー・{}選手!\n'.format(blue_boxer.name)
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title, mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break
                else:
                    print_text = '判定によりこの試合引き分け。\n'
                    print(print_text)
                    log_text += print_text + '\n'
                    with open(log_title, mode='w', encoding='utf-8') as f:
                        f.write(log_text)
                    input('キーを押したら終了します')
                    break
            else:
                print_text = 'インターバルに入ります。\n'
                print(print_text)
                log_text += print_text + '\n'
                if red_boxer.hp <= 38:
                    red_boxer.hp += 2
                    print_text = '赤コーナー・{}選手、体力2回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                    print(print_text)
                    log_text += print_text + '\n'
                elif red_boxer.hp == 39:
                    red_boxer.hp += 1
                    print_text = '赤コーナー・{}選手、体力1回復して{}。\n'.format(red_boxer.name,red_boxer.hp)
                    print(print_text)
                    log_text += print_text + '\n'
                if blue_boxer.hp <= 38:
                    blue_boxer.hp += 2
                    print_text = '青コーナー・{}選手、体力2回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                    print(print_text)
                    log_text += print_text + '\n'
                elif blue_boxer.hp == 39:
                    blue_boxer.hp += 1
                    print_text = '青コーナー・{}選手、体力1回復して{}。\n'.format(blue_boxer.name,blue_boxer.hp)
                    print(print_text)
                    log_text += print_text + '\n'
                if red_boxer.attack_num > blue_boxer.attack_num:
                    if red_boxer.attack_num == 3:
                        if red_boxer.speed <= 2:
                            red_boxer.speed = 1
                            print_text = '赤コーナー・{}選手、攻め疲れのためスピード減って{}に。\n'.format(red_boxer.name,red_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                        else:
                            red_boxer.speed -= 2
                            print_text = '赤コーナー・{}選手、攻め疲れのためスピード2減って{}に。\n'.format(red_boxer.name,red_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                    elif red_boxer.attack_num >= 1 and red_boxer.attack_num < 3:
                        if red_boxer.speed <= 1:
                            red_boxer.speed = 1
                            print_text = '赤コーナー・{}選手、攻め疲れのためスピード減って{}に。\n'.format(red_boxer.name,red_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                        else:
                            red_boxer.speed -= 1
                            print_text = '赤コーナー・{}選手、攻め疲れのためスピード1減って{}に。\n'.format(red_boxer.name,red_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                elif blue_boxer.attack_num > red_boxer.attack_num:
                    if blue_boxer.attack_num == 3:
                        if blue_boxer.speed <= 2:
                            blue_boxer.speed = 1
                            print_text = '青コーナー・{}選手、攻め疲れのためスピード減って{}に。\n'.format(blue_boxer.name,blue_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                        else:
                            blue_boxer.speed -= 2
                            print_text = '青コーナー・{}選手、攻め疲れのためスピード2減って{}に。\n'.format(blue_boxer.name,blue_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                    elif blue_boxer.attack_num >= 1 and blue_boxer.attack_num < 3:
                        if blue_boxer.speed <= 1:
                            blue_boxer.speed = 1
                            print_text = '青コーナー・{}選手、攻め疲れのためスピード減って{}に。\n'.format(blue_boxer.name,blue_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                        else:
                            blue_boxer.speed -= 1
                            print_text = '青コーナー・{}選手、攻め疲れのためスピード1減って{}に。\n'.format(blue_boxer.name,blue_boxer.speed)
                            print(print_text)
                            log_text += print_text + '\n'
                red_boxer.attack_num = 0
                blue_boxer.attack_num = 0
                print_text = '赤コーナー:{}選手\nHP:{}\nパンチ力:{}\nスピード:{}\nタフネス:{}\n'.format(red_boxer.name,red_boxer.hp,red_boxer.punch_power,red_boxer.speed,red_boxer.toughness)
                print(print_text)
                log_text += print_text + '\n'
                print_text = '青コーナー:{}選手\nHP:{}\nパンチ力:{}\nスピード:{}\nタフネス:{}\n'.format(blue_boxer.name,blue_boxer.hp,blue_boxer.punch_power,blue_boxer.speed,blue_boxer.toughness)
                print(print_text)
                log_text += print_text + '\n'
        else:
            current_turn += 1

# 対戦ログ保存フォルダ作成
FIGHT_LOG_DIR = make_folder()

# 12面ダイス2個を作成
dice_12 = Dice(2,12)
# 6面ダイス2個を作成
dice_6 = Dice(2,6)

# 赤コーナーのボクサー作成プロセス
print('赤コーナーのボクサーを作成します')
# 名前設定
red_name = input('名前を入力してください:')
# パンチ力設定
red_punch_power = decide_num('パンチ力')
# スピード設定
red_speed = decide_num('スピード')
# タフネス設定
red_toughness = decide_num('タフネス')
print('')
# ボクサー作成
red_boxer = Boxer(red_name, red_punch_power, red_speed, red_toughness, dice_12, dice_6)
print('')

# 青コーナーのボクサー作成プロセス
print('青コーナーのボクサーを作成します')
# 名前設定
blue_name = input('名前を入力してください:')
# パンチ力設定
blue_punch_power = decide_num('パンチ力')
# スピード設定
blue_speed = decide_num('スピード')
# タフネス設定
blue_toughness = decide_num('タフネス')
print('')
# ボクサー作成
blue_boxer = Boxer(blue_name, blue_punch_power, blue_speed, blue_toughness, dice_12, dice_6)
print('')

# 最大ラウンド数
max_round = decide_num('試合の最大ラウンド数')

match(FIGHT_LOG_DIR,max_round,red_boxer,blue_boxer)