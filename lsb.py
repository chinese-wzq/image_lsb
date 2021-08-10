# -*- coding: UTF-8 -*-
from PIL import Image
import sys,time,os,bitstring,math

print('图片藏文字与读取Demo    4.0ProPlus++MaxUltra \nby\tWZQ|帅in逼|13905069\n\n现仅支持藏文件！\n\n\n帮助：\n在控制台中使用"python lsb.py 原图片目录 编码后图片目录 待编码文件目录"进行编码\n使用"python lsb.py 待解码文件目录 解码后文件目录(不含文件扩展名)"进行解码\n\n')
#0 1 2 3 4 5 6 7 8 9
#用用留留 用 用留留用用
low_use=["0","1","4","5","8","9"]
low_unuse=["2","3","6","7"]
def image_code(sb:str,sbb:str,gwait:str):
    wait=[]
    #将文件后缀名存入
    tmp=[]
    for c in os.path.splitext(gwait)[1]:
        tmp.append(bin(ord(c)).replace('0b', '').zfill(7))
    if len(tmp)<10:
        while len(tmp)<10:
            tmp.append("0000000")
    wait=list(str(''.join(tmp)))
    sd=open(gwait,"rb")
    wait.extend(bitstring.BitStream(bytes=sd.read()).bin)
    for i in range(len(wait)):wait[i]=str(int(wait[i]))
    print("编码成功，正在生成图像......")
    file=Image.open(sb)
    loaded=file.load()
    count=0
    exit=False
    for i in range(file.size[0]):
        for ii in range(file.size[1]):
            fuck = list(loaded[i, ii])
            for iii in range(0, 3):
                g=list(str(fuck[iii]))
                if count > len(wait) - 1:
                    #多出来像素的处理
                    #查找最近的数字
                    a=10000
                    keep=""
                    for iiii in low_unuse:
                        if abs(int(iiii)-int(g[len(g)-1]))<a:
                            if int(fuck[iii])>=250 and int(iiii)<6:
                                keep=iiii
                                a=abs(int(iiii)-int(g[len(g)-1]))
                            elif int(fuck[iii])<250:
                                keep=iiii
                                a=abs(int(iiii)-int(g[len(g)-1]))
                    g[len(g)-1]=keep
                    exit=True
                else:
                    #需使用像素的处理
                    a=10000
                    keep=""
                    for iiii in low_use:
                        if abs(int(iiii)-int(g[len(g)-1]))<a and int(iiii)%2==int(wait[count])%2:
                            if int(fuck[iii])>=250 and int(iiii)<6:
                                keep=iiii
                                a=abs(int(iiii)-int(g[len(g)-1]))
                            elif int(fuck[iii])<250:
                                keep=iiii
                                a=abs(int(iiii)-int(g[len(g)-1]))
                    g[len(g)-1]=keep
                fuck[iii]=int("".join(g))
                count=count + 1
            loaded[i,ii]=tuple(fuck)
            if exit:break
        if exit:break
    print("图像生成成功，正在保存......")
    file.save(sbb)
    print("保存成功！正在关闭文件......")
    file.close()
    return sbb
def image_decode(sb:str,sbb:str):
    file=Image.open(sb)
    print("成功打开图片，正在读取......")
    loaded=file.load()
    tmp=[""]
    exit=False
    for i in range(file.size[0]):
        for ii in range(file.size[1]):
            for iii in range(0, 3):
                g=list(str(loaded[i,ii][iii]))
                if g[len(g)-1] in low_unuse:
                    print("读取完毕")
                    exit=True
                    break
                else:
                    if not len(tmp[len(tmp)-1])<7:
                        tmp.append("")
                    tmp[len(tmp)-1]=tmp[len(tmp)-1]+str(int(g[len(g)-1])%2)
            if exit:break
        if exit:break
    file.close()
    print("读取成功，已关闭原文件。正在分析文件扩展名......")
    text=tmp[0:10]
    main="".join(tmp[10:len(tmp)])
    main=main.zfill(math.ceil(len(main)/8)*8)
    for i in range(9,-1,-1):
        if int(text[i])==0:
            del text[i]
        else:
            break
    textt=""
    for i in range(len(text)):
        textt=textt+chr(int(text[i],2))
    print("分析成功，你的文件扩展名为："+textt+",保存的文件将会按此格式进行保存")
    print("正在保存文件.....")
    newfile=open(sbb+textt,"wb")
    newfile.write(bitstring.BitStream(bin=main).bytes)
    newfile.close()
    print("保存成功！感谢您的使用！")
    return 0
if len(sys.argv)==3:
    if image_decode(sys.argv[1],sys.argv[2]):
        print("解码成功！")
elif len(sys.argv)==4:
    image_code(sys.argv[1],sys.argv[2],sys.argv[3])
else:
    time.sleep(5)