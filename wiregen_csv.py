import csv
import os


datas = []
string = ''
for filename in os.listdir('/root/wireclient'):
        if filename.endswith('.conf'):
          with open(os.path.join('/root/wireclient', filename)) as f:
            contents = f.readlines();
            contentStr = '\n'.join([line.strip() + string for line in contents])
            datas.append(['L1_hongkong1','NORMAL','HongKong','https://w7.pngwing.com/pngs/586/727/png-transparent-hk-hong-kong-sar-china-flag-icon.png',contentStr,'red', 1 ])
            print(contentStr)

header = ['WIRE_name','WIRE_type','WIRE_country','WIRE_COUNTRY_FLAG_IMG_URL','WIRE_content','OVPN_theme_color','WIRE_level']


with open('wire.csv','w', encoding='UTF8') as f:

        writer = csv.writer(f)

        writer.writerow(header)


        for data in datas:
          writer.writerow(data)

f.close()
