# -*- coding: UTF-8 -*-
from PIL import Image
import sys,time
print('图片藏文字与读取Demo\nby\t吴宗权\n\n仅支持纯英文，不支持字符的编码！\n\n\n帮助：\n在控制台中使用"python lsb.py 原图片目录 编码后图片目录 编码内容"进行编码\n使用"python lsb.py 编码后文件目录"进行解码')
def image_code(sb:str,sbb:str,gwait:str):
    tmp = []
    for c in gwait:
        tmp.append(bin(ord(c)).replace('0b', ''))
    wait = list(str(''.join(tmp)))
    print("编码成功，正在生成图像......")
    file = Image.open(sb)
    loaded = file.load()
    count = 0
    for i in range(file.size[0]):
        for ii in range(file.size[1]):
            fuck = list(loaded[i, ii])
            for iii in range(0, 3):
                if count > len(wait) - 1:
                    g = list(str(fuck[iii]))
                    g[len(g) - 1] = "0"
                    fuck[iii] = int("".join(g))
                else:
                    g = list(str(fuck[iii]))
                    g[len(g) - 1] = wait[count]
                    fuck[iii] = int("".join(g))
                count = count + 1
            loaded[i, ii]=tuple(fuck)
    print("图像生成成功，正在保存......")
    file.save(sbb)
    print("保存成功！正在关闭文件......")
    file.close()
    return sbb
def image_decode(sb:str):
    file=Image.open(sb)
    print("成功打开图片，正在读取......")
    loaded=file.load()
    tmp=[""]
    for i in range(file.size[0]):
        for ii in range(file.size[1]):
            for iii in range(0, 3):
                g=list(str(loaded[i,ii][iii]))
                if not len(tmp[len(tmp)-1])<7:
                    tmp.append("")
                tmp[len(tmp) - 1]=tmp[len(tmp)-1]+g[len(g)-1]
    print("读取成功，正在分析......")
    for i in range(len(tmp)-1,-1,-1):
        if int(tmp[i])==0:
            del tmp[i]
        else:
            break
    for i in range(len(tmp)):
        tmp[i]=chr(int(tmp[i],2))
    strla="".join(tmp)
    print("分析成功，正在关闭文件.....")
    file.close()
    return strla
if len(sys.argv)==2:
    print(image_decode(sys.argv[1]))
elif len(sys.argv)==4:
    image_code(sys.argv[1], sys.argv[2],sys.argv[3])
else:
    time.sleep(5)