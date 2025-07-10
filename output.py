import os
from datetime import datetime as dt

from jinja2 import Environment, FileSystemLoader

import kanshi_data as kd


def output_html(meishiki, unsei):
    """
    HTMLファイルを出力する関数
    """
    env = Environment(loader=FileSystemLoader('html/', encoding='utf8'))
    template = env.get_template('template.html')

    wareki = kd.convert_to_wareki(meishiki.birthday)

    if meishiki.t_flag == 1:
        if os.name == 'nt':
            import locale
            locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
            birthday_str = meishiki.birthday.strftime(f'{wareki}%#m月%#d日 %#H時%#M分生')
        else:
            birthday_str = meishiki.birthday.strftime(f'{wareki}%-m月%-d日 %-H時%-M分生')
    else:
        if os.name == 'nt':
            import locale
            locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
            birthday_str = meishiki.birthday.strftime(f'{wareki}%#m月%#d日 -時-分生')
        else:
            birthday_str = meishiki.birthday.strftime(f'{wareki}%-m月%-d日 -時-分生')
    sex_str = '男命' if meishiki.sex == 0 else '女命'

    daiun = unsei.unsei["daiun"]
    nenun = unsei.unsei["nenun"]
    
    if meishiki.meishiki["tenkan"][3] != -1:

        content = {'birthday': birthday_str, 'sex': sex_str,
                   'tenkan1': kd.kan[meishiki.meishiki["tenkan"][0]], 'chishi1': kd.shi[meishiki.meishiki["chishi"][0]], 'zokan1': kd.kan[meishiki.meishiki["zokan"][0]], 'fortune1': kd.twelve_fortune[meishiki.meishiki["twelve_fortune"][0]], 'tsuhen_tenkan1': kd.tsuhen[meishiki.meishiki["tsuhen"][0]], 'tsuhen_zokan1': kd.tsuhen[meishiki.meishiki["tsuhen"][4]],
                   'tenkan2': kd.kan[meishiki.meishiki["tenkan"][1]], 'chishi2': kd.shi[meishiki.meishiki["chishi"][1]], 'zokan2': kd.kan[meishiki.meishiki["zokan"][1]], 'fortune2': kd.twelve_fortune[meishiki.meishiki["twelve_fortune"][1]], 'tsuhen_tenkan2': kd.tsuhen[meishiki.meishiki["tsuhen"][1]], 'tsuhen_zokan2': kd.tsuhen[meishiki.meishiki["tsuhen"][5]],
                   'tenkan3': kd.kan[meishiki.meishiki["tenkan"][2]], 'chishi3': kd.shi[meishiki.meishiki["chishi"][2]], 'zokan3': kd.kan[meishiki.meishiki["zokan"][2]], 'fortune3': kd.twelve_fortune[meishiki.meishiki["twelve_fortune"][2]], 'tsuhen_tenkan3': kd.tsuhen[meishiki.meishiki["tsuhen"][2]], 'tsuhen_zokan3': kd.tsuhen[meishiki.meishiki["tsuhen"][6]],
                   'tenkan4': kd.kan[meishiki.meishiki["tenkan"][3]], 'chishi4': kd.shi[meishiki.meishiki["chishi"][3]], 'zokan4': kd.kan[meishiki.meishiki["zokan"][3]], 'fortune4': kd.twelve_fortune[meishiki.meishiki["twelve_fortune"][3]], 'tsuhen_tenkan4': kd.tsuhen[meishiki.meishiki["tsuhen"][3]], 'tsuhen_zokan4': kd.tsuhen[meishiki.meishiki["tsuhen"][7]],
                   'choko': meishiki.meishiki["choko"], 'kubo': kd.shi[meishiki.meishiki["kubo"][0]] + kd.shi[meishiki.meishiki["kubo"][1]],
                   'moku': meishiki.meishiki["gogyo"][0], 'ka': meishiki.meishiki["gogyo"][1], 'do': meishiki.meishiki["gogyo"][2], 'gon': meishiki.meishiki["gogyo"][3], 'sui': meishiki.meishiki["gogyo"][4]}

    else:

        content = {'birthday': birthday_str, 'sex': sex_str,
                   'tenkan1': kd.kan[meishiki.meishiki["tenkan"][0]], 'chishi1': kd.shi[meishiki.meishiki["chishi"][0]], 'zokan1': kd.kan[meishiki.meishiki["zokan"][0]], 'fortune1': kd.twelve_fortune[meishiki.meishiki["twelve_fortune"][0]], 'tsuhen_tenkan1': kd.tsuhen[meishiki.meishiki["tsuhen"][0]], 'tsuhen_zokan1': kd.tsuhen[meishiki.meishiki["tsuhen"][4]],
                   'tenkan2': kd.kan[meishiki.meishiki["tenkan"][1]], 'chishi2': kd.shi[meishiki.meishiki["chishi"][1]], 'zokan2': kd.kan[meishiki.meishiki["zokan"][1]], 'fortune2': kd.twelve_fortune[meishiki.meishiki["twelve_fortune"][1]], 'tsuhen_tenkan2': kd.tsuhen[meishiki.meishiki["tsuhen"][1]], 'tsuhen_zokan2': kd.tsuhen[meishiki.meishiki["tsuhen"][5]],
                   'tenkan3': kd.kan[meishiki.meishiki["tenkan"][2]], 'chishi3': kd.shi[meishiki.meishiki["chishi"][2]], 'zokan3': kd.kan[meishiki.meishiki["zokan"][2]], 'fortune3': kd.twelve_fortune[meishiki.meishiki["twelve_fortune"][2]], 'tsuhen_tenkan3': kd.tsuhen[meishiki.meishiki["tsuhen"][2]], 'tsuhen_zokan3': kd.tsuhen[meishiki.meishiki["tsuhen"][6]],
                   'tenkan4': '-', 'chishi4': '-', 'zokan4': '-', 'fortune4': '-', 'tsuhen_tenkan4': '', 'tsuhen_zokan4': '',
                   'choko': meishiki.meishiki["choko"], 'kubo': kd.shi[meishiki.meishiki["kubo"][0]] + kd.shi[meishiki.meishiki["kubo"][1]],
                   'moku': meishiki.meishiki["gogyo"][0], 'ka': meishiki.meishiki["gogyo"][1], 'do': meishiki.meishiki["gogyo"][2], 'gon': meishiki.meishiki["gogyo"][3], 'sui': meishiki.meishiki["gogyo"][4]}

    p1 = '&nbsp;' + str(daiun[0][0]) if len(str(daiun[0][0])) == 1 else str(daiun[0][0])
    d_nen = {'p1': p1, 'p2': daiun[1][0], 'p3': daiun[2][0], 'p4': daiun[3][0], 'p5': daiun[4][0], 'p6': daiun[5][0], 'p7': daiun[6][0], 'p8': daiun[7][0], 'p9': daiun[8][0], 'p10': daiun[9][0], 'p11': daiun[10][0],
             'd_tsuhen1': kd.tsuhen[daiun[0][3]], 'd_kan1': kd.kan[daiun[0][1]], 'd_shi1': kd.shi[daiun[0][2]],
             'd_tsuhen2': kd.tsuhen[daiun[1][3]], 'd_kan2': kd.kan[daiun[1][1]], 'd_shi2': kd.shi[daiun[1][2]],
             'd_tsuhen3': kd.tsuhen[daiun[2][3]], 'd_kan3': kd.kan[daiun[2][1]], 'd_shi3': kd.shi[daiun[2][2]],
             'd_tsuhen4': kd.tsuhen[daiun[3][3]], 'd_kan4': kd.kan[daiun[3][1]], 'd_shi4': kd.shi[daiun[3][2]],
             'd_tsuhen5': kd.tsuhen[daiun[4][3]], 'd_kan5': kd.kan[daiun[4][1]], 'd_shi5': kd.shi[daiun[4][2]],
             'd_tsuhen6': kd.tsuhen[daiun[5][3]], 'd_kan6': kd.kan[daiun[5][1]], 'd_shi6': kd.shi[daiun[5][2]],
             'd_tsuhen7': kd.tsuhen[daiun[6][3]], 'd_kan7': kd.kan[daiun[6][1]], 'd_shi7': kd.shi[daiun[6][2]],
             'd_tsuhen8': kd.tsuhen[daiun[7][3]], 'd_kan8': kd.kan[daiun[7][1]], 'd_shi8': kd.shi[daiun[7][2]],
             'd_tsuhen9': kd.tsuhen[daiun[8][3]], 'd_kan9': kd.kan[daiun[8][1]], 'd_shi9': kd.shi[daiun[8][2]],
             'd_tsuhen10': kd.tsuhen[daiun[9][3]], 'd_kan10': kd.kan[daiun[9][1]], 'd_shi10': kd.shi[daiun[9][2]], }

    content.update(d_nen)

    age = dt.today().year - meishiki.birthday.year
    if age < nenun[0][0]:
        i = 0
    else:
        for i, n in enumerate(nenun):
            if age == n[0]:
                break
    n1 = '&nbsp;' + str(nenun[i][0]) if len(str(nenun[i][0])) == 1 else str(nenun[i][0])
    n2 = '&nbsp;' + str(nenun[i+1][0]) if len(str(nenun[i+1][0])) == 1 else str(nenun[i+1][0])
    n3 = '&nbsp;' + str(nenun[i+2][0]) if len(str(nenun[i+2][0])) == 1 else str(nenun[i+2][0])
    n4 = '&nbsp;' + str(nenun[i+3][0]) if len(str(nenun[i+3][0])) == 1 else str(nenun[i+3][0])
    n5 = '&nbsp;' + str(nenun[i+4][0]) if len(str(nenun[i+4][0])) == 1 else str(nenun[i+4][0])
    n6 = '&nbsp;' + str(nenun[i+5][0]) if len(str(nenun[i+5][0])) == 1 else str(nenun[i+5][0])
    n7 = '&nbsp;' + str(nenun[i+6][0]) if len(str(nenun[i+6][0])) == 1 else str(nenun[i+6][0])
    n8 = '&nbsp;' + str(nenun[i+7][0]) if len(str(nenun[i+7][0])) == 1 else str(nenun[i+7][0])
    n9 = '&nbsp;' + str(nenun[i+8][0]) if len(str(nenun[i+8][0])) == 1 else str(nenun[i+8][0])
    n10 = '&nbsp;' + str(nenun[i+9][0]) if len(str(nenun[i+9][0])) == 1 else str(nenun[i+9][0])
    n11 = '&nbsp;' + str(nenun[i+10][0]) if len(str(nenun[i+10][0])) == 1 else str(nenun[i+10][0])

    n_nen = {'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 'n6': n6, 'n7': n7, 'n8': n8, 'n9': n9, 'n10': n10, 'n11': n11,
             'n_tsuhen1': kd.tsuhen[nenun[i][3]], 'n_kan1': kd.kan[nenun[i][1]], 'n_shi1': kd.shi[nenun[i][2]],
             'n_tsuhen2': kd.tsuhen[nenun[i+1][3]], 'n_kan2': kd.kan[nenun[i+1][1]], 'n_shi2': kd.shi[nenun[i+1][2]],
             'n_tsuhen3': kd.tsuhen[nenun[i+2][3]], 'n_kan3': kd.kan[nenun[i+2][1]], 'n_shi3': kd.shi[nenun[i+2][2]],
             'n_tsuhen4': kd.tsuhen[nenun[i+3][3]], 'n_kan4': kd.kan[nenun[i+3][1]], 'n_shi4': kd.shi[nenun[i+3][2]],
             'n_tsuhen5': kd.tsuhen[nenun[i+4][3]], 'n_kan5': kd.kan[nenun[i+4][1]], 'n_shi5': kd.shi[nenun[i+4][2]],
             'n_tsuhen6': kd.tsuhen[nenun[i+5][3]], 'n_kan6': kd.kan[nenun[i+5][1]], 'n_shi6': kd.shi[nenun[i+5][2]],
             'n_tsuhen7': kd.tsuhen[nenun[i+6][3]], 'n_kan7': kd.kan[nenun[i+6][1]], 'n_shi7': kd.shi[nenun[i+6][2]],
             'n_tsuhen8': kd.tsuhen[nenun[i+7][3]], 'n_kan8': kd.kan[nenun[i+7][1]], 'n_shi8': kd.shi[nenun[i+7][2]],
             'n_tsuhen9': kd.tsuhen[nenun[i+8][3]], 'n_kan9': kd.kan[nenun[i+8][1]], 'n_shi9': kd.shi[nenun[i+8][2]],
             'n_tsuhen10': kd.tsuhen[nenun[i+9][3]], 'n_kan10': kd.kan[nenun[i+9][1]], 'n_shi10': kd.shi[nenun[i+9][2]], }

    content.update(n_nen)

    result = template.render(content)
    file_name = 'html/' + \
        meishiki.birthday.strftime('%Y_%m%d_%H%M_') + \
        str(meishiki.sex) + '.html'
    with open(file_name, 'w') as f:
        f.write(result)

    return file_name


