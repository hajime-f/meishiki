import datetime
import re
import sys
import unicodedata

# 各年号の元年を定義
era_dict = {
    "昭和": 1926,
    "平成": 1989,
    "令和": 2019,
}


def date_converter(text):

    # 正規化
    normalized_text = unicodedata.normalize("NFKC", text)

    # 西暦の場合を処理
    if normalized_text[0:2] == '西暦':

        # 年月日を抽出
        pattern = r"西暦(?P<year>[0-9]{{4}})年(?P<month>[0-9]{{1,2}})月(?P<day>[0-9]{{1,2}})日".format(
            eraList="|".join("西暦"))
        date = re.search(pattern, normalized_text)

        # 抽出できなかったら終わり
        if date is None:
            sys.exit(1)

        # date型に変換して返す
        return datetime.date(int(date.group("year")), int(date.group("month")), int(date.group("day")))

    # 和暦の場合を処理

    # 年月日を抽出
    pattern = r"(?P<era>{eraList})(?P<year>[0-9]{{1,2}}|元)年(?P<month>[0-9]{{1,2}})月(?P<day>[0-9]{{1,2}})日".format(
        eraList="|".join(era_dict.keys()))
    date = re.search(pattern, normalized_text)

    # 抽出できなかったら終わり
    if date is None:
        sys.exit(1)

    # 年を変換
    for era, start_year in era_dict.items():
        if date.group("era") == era:
            if date.group("year") == "元":
                year = start_year
                break
            else:
                year = start_year + int(date.group("year")) - 1
                break

    # date型に変換して返す
    return datetime.date(year, int(date.group("month")), int(date.group("day")))


def time_converter(date, time_text):

    d = date.strftime("%Y-%m-%d")
    if time_text == '':
        return datetime.datetime.strptime(d, '%Y-%m-%d'), False
    else:
        birthday = datetime.datetime.strptime(
            d + ' ' + time_text, '%Y-%m-%d %H時%M分')

        # サマータイムを考慮する
        if datetime.datetime(year=1948, month=5, day=2) <= birthday <= datetime.datetime(year=1948, month=9, day=11) or datetime.datetime(year=1949, month=4, day=3) <= birthday <= datetime.datetime(year=1949, month=9, day=10) or datetime.datetime(year=1950, month=5, day=7) <= birthday <= datetime.datetime(year=1950, month=9, day=9) or datetime.datetime(year=1951, month=5, day=6) <= birthday <= datetime.datetime(year=1951, month=9, day=8):
            birthday = datetime.datetime(year=birthday.year, month=birthday.month, day=birthday.day,
                                         hour=birthday.hour - 1, minute=birthday.minute)

        return birthday, True
