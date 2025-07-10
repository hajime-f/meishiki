import sys
from datetime import datetime as dt

import kanshi_data as kd


class Unsei:
    """
    大運のクラス
    """

    def __init__(self, meishiki):

        self.meishiki = meishiki
        self.birthday = meishiki.birthday
        self.sex = meishiki.sex
        self.unsei = {}

    def is_junun_gyakuun(self, sex, y_kan):
        """
        ＜機能＞
        大運が順運か逆運かを判定する
        ＜入力＞
          - y_kan（int）：年柱天干の番号
          - self.sex（int）：性別の番号
        ＜出力＞
          - 順運（1）または逆運（0）の二値
        ＜異常検出＞
        取得できなかった場合はエラーメッセージを出力して強制終了する
        """

        if (((y_kan % 2) == 0) and (sex == 0)) or (((y_kan % 2) == 1) and (sex == 1)):
            return 1   # 年柱天干が陽干の男命 or 年柱天干が陰干の女命は、順運

        elif (((y_kan % 2) == 1) and (sex == 0)) or (((y_kan % 2) == 0) and (sex == 1)):
            return 0   # 年柱天干が陽干の女命 or 年柱天干が陰干の男命は、逆運

        else:
            print('大運の順逆を判定できませんでした。')
            sys.exit(1)

    def convert_year_ratio(self, birthday, jg):
        """
        ＜機能＞
        生年月日から前の節入日までの日数と、生年月日から次の節入日までの日数との比を、
        10年に占める割合に直す。
        例：8日：22日→3年：7年
        ＜入力＞
          - brithday（datetime）：生年月日
          - jg（1 or 0）：順運 or 逆運
        ＜出力＞
          - year_ratio_list（list）：10年に占める割合
        """
        p = self.meishiki.is_setsuiri(birthday, birthday.month)
        for i, s in enumerate(kd.setsuiri):
            if (s[0] == birthday.year) and (s[1] == birthday.month):
                if not p:
                    k = kd.setsuiri[i + 1]
                    previous_setsuiri = dt(year=s[0], month=s[1], day=s[2], hour=s[3], minute=s[4])
                    next_setsuiri = dt(year=k[0], month=k[1], day=k[2], hour=k[3], minute=k[4])
                else:
                    k = kd.setsuiri[i - 1]
                    previous_setsuiri = dt(year=k[0], month=k[1], day=k[2], hour=k[3], minute=k[4])
                    next_setsuiri = dt(year=s[0], month=s[1], day=s[2], hour=s[3], minute=s[4])
                break

        diff_previous = birthday - previous_setsuiri   # 生年月日から前の節入日までの日数
        diff_next = next_setsuiri - birthday           # 生年月日から次の節入日までの日数

        # ３日間を１年に置き換えるので、３除した値を丸める
        p_year = round((diff_previous.days + (diff_previous.seconds / 60 / 60 / 24)) / 3)
        n_year = round((diff_next.days + (diff_next.seconds / 60 / 60 / 24)) / 3)

        if (p_year == 0) and (jg == 0):
            p_year = 1
            n_year = 9
        elif (p_year == 0) and (jg == 1):
            pass
        elif (n_year == 0) and (jg == 0):
            pass
        elif (n_year == 0) and (jg == 1):
            p_year = 9
            n_year = 1
        else:
            pass
        year_ratio_list = [p_year, n_year]
        
        return year_ratio_list

    def find_kanshi_idx(self, kan, shi, p):
        """
        六十干支表から所定の干支のインデクスを返す
        """
        for idx, sk in enumerate(kd.sixty_kanshi):
            if (sk[0] == kan) and (sk[1] == shi):
                return idx + p

        print('干支が見つかりませんでした。')
        sys.exit(1)
    
    def append_daiun(self):
        """
        大運を命式に追加する
        """
        daiun = []
        meishiki = self.meishiki.meishiki

        # 順運か逆運か？
        jg = self.is_junun_gyakuun(self.meishiki.sex, meishiki["tenkan"][0])

        # 立運計算
        year_ratio_list = self.convert_year_ratio(self.birthday, jg)

        if jg:
            # 順運
            ry = year_ratio_list[1]  # 次の節入日が立運の起算日
            p = 1                    # 六十干支表を順にたどる
        else:
            # 逆運
            ry = year_ratio_list[0]  # 前の節入日が立運の起算日
            p = -1                   # 六十干支表を逆にたどる

        # 六十干支表の開始インデックスを得る
        idx = self.find_kanshi_idx(meishiki["tenkan"][1], meishiki["chishi"][1], p)

        for n in list(range(10, 140, 10)):

            if idx >= 60:
                idx = 0
            kan, shi = kd.sixty_kanshi[idx]
            tsuhen = kd.kan_tsuhen[meishiki["nikkan"]].index(kan)

            daiun.append([ry, kan, shi, tsuhen])

            ry += 10
            idx += p

        return daiun
            
    def append_nenun(self, daiun):
        """
        年運を命式に追加する
        """
        nenun = []
        idx = (self.meishiki.birthday.year - 3) % 60 - 1
        ry = daiun[0][0]

        meishiki = self.meishiki.meishiki

        for n in list(range(0, 120)):
            kan, shi = kd.sixty_kanshi[idx]
            tsuhen = kd.kan_tsuhen[meishiki["nikkan"]].index(kan)

            if n >= ry:
                nenun.append([n, kan, shi, tsuhen])

            idx += 1
            if idx >= 60:
                idx = 0

        return nenun

    def build_unsei(self):

        # 大運を得る
        daiun = self.append_daiun()
        
        # 年運を得る
        nenun = self.append_nenun(daiun)

        self.unsei.update({"daiun": daiun})
        self.unsei.update({"nenun": nenun})
