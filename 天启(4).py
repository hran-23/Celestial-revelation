def 天启():
    import os
    import random
    try:
        os.makedirs('用户')
    except:
        print('已检测到用户')

    xs={'0':'颠起来','1':'天启预报','2':'从红月开始','3':'道诡异仙',
        '4':'蛊真人','5':'明克街13号','6':'我真不是邪神走狗','7':'大奉打更人',
        '8':'诡秘之主','9':'诡舍','10':'烂柯棋缘','11':'地球上线'}

    xs1={'1':'我想挨一顿毒打，两顿也行',
         '2':'再美好的东西，也有丑陋的本质。便如爱情，也不过是刻在了基因里的繁衍；便如养育，也只是内心深处的母性本能在作祟；又如友情，只是来源于对庞大族群的不安全感；而所谓的善良也好，怜悯也罢，其实也只是因为内心深处的恐惧，造成了自我对这种现象的畏惧，因而生出的抵抗情绪而已。',
         '3':'何为坐忘道？堕其肢体，黜遁聪智，离形去知，同于大通，此谓坐忘！坐者，动也。忘者，念也。非坐则止其役，非忘则息其思。役不止，则神静。思不息，则心宁！',
         '4':'杨间仙友非我所杀，乃是遮天完美合谋致死，给我投票送巨阳真传',
         '5':'妓女养大的秩序之神',
         '6':'我只是一个普通书店的老板，我的书店中，充满着各种温馨治愈的故事，当你心情不好的时候，可以随时来我的书店，喝上一杯热茶，看看书，放松心情，世上没有过不去的事。',
         '7':'我这一生，不问前尘，不求来世，只轰轰烈烈，快意恩仇，败尽各族英杰，傲笑六道神魔！',
         '8':'我们是一群时刻对抗着危险和疯狂的可怜虫，但我们更是守护者 ',
         '9':'',
         '10':'',
         '11':''
         }

    编码={'1':'utf-8','2':'utf-8','3':'utf-8','4':'utf-8','5':'utf-8','6':'ANSI',
        '7':'utf-8','8':'utf-8','9':'utf-8','10':'utf-8','11':'utf-8'}

    用户='用户\\'
    书库='书屋\\'

    while 1==1:
        zh=input('请与历史激起共鸣（无法共鸣请输入’我已归来‘进行联系):')
        if zh=='我已归来':
            while 1==1:
                try:
                    zh=input('请构塑您的身份')
                    r=open(用户+zh+'.txt','x')
                    r.close()
                except:
                    print('您的尊名沾染了某些禁忌')
                    continue
                with open(用户+zh+'.txt','w') as zc:
                    mm=input('建立您在此位面的锚')
                    zc.write(mm)
                    print()
                break
        try:
            with open(用户+zh+'.txt','r') as zh1:
                zh1r=zh1.read()
            while 1==1:
                mm=input('尊敬的'+zh+',请与您的锚建立联系:')
                print()
                if mm==zh1r:
                    print(zh+',只要您不放弃自己的崇高，世界的大门会向您打开')
                    print('')
                    break
                else:
                    print('失去锚点之人终会被黑暗吞噬')
                    print()
            break
        except:
            print()
            print('门没有记录您的过去')
            print()

    while 1==1:
        for w in xs:
            print(w+'.'+xs[w])
        xs0=input('您的脚印遍布世界，今日您想去往哪里：')
        print('')

        if xs0 not in xs.keys():
            print('这段历史似乎没被记录')
            print()
            continue
        break

    if xs0=='0':#颠起来
        for w in xs:
            print(xs[w])
        w=int(w)
        while 1==1:
            w1=str(random.randint(1,w))
            with open(书库+xs[w1]+'.txt','rt',errors='ignore',encoding=编码[w1]) as l:
                n0=0
                for i in l:
                    i=i.lstrip()
                    if i=='':
                        continue
                    n0+=1
            n1=random.randint(1,n0)
            with open(书库+xs[w1]+'.txt','rt',errors='ignore',encoding=编码[w1]) as l:
                n0=0
                for i in l:
                    i=i.lstrip()
                    if i=='':
                        continue
                    n0+=1
                    if n0==n1:
                        TL=input(i)
                        break
            if TL!='':
                break



    else:#正常
        try:
            with open(用户+zh+xs[xs0]+'cd.txt', 'r') as file:
                content = file.read()
        except:
            with open(用户+zh+xs[xs0]+'cd.txt', 'w') as file:
                content='0'
                file.write('0')
        while 1==1:
            try:
                c=int(input('''回溯您的过往，或者您想从“空屋”开始
                特殊数字：
                -1：回到上次布局的终点（上次读到'''+str(content)+'''行）
                -2：寻找历史的节点
                >>>'''))
                break
            except:
                print('''
        门无法识别你的语言
        ''')

        print('')
        if c==-1:
            c=int(content)



        if c==-2:
            n=1==1
            while n:
                l=open(书库+xs[xs0]+'.txt','rt',errors='ignore',encoding=编码[xs0])
                查找=input('宿命展现出的曾经：')
                print('')
                d={}
                b=0
                b1=0
                for w in l.readlines():
                    w=w.lstrip()
                    if w=='':
                        continue
                    b1+=1
                    if w.find(查找)!=-1:
                        b+=1
                        d[str(b)]=b1
                        print(b,w)
                l.close()
                print('您寻找的“果”是哪一个（若还没有人种下这个“因”，请输入永恒')
                查找=input()
                print('')
                if 查找=='永恒':
                    continue
                c=d[查找]
                n=1==2

        print(xs1[xs0])
        print()

        l=open(书库+xs[xs0]+'.txt','rt',errors='ignore',encoding=编码[xs0])
        b=0
        print('''Enter：下一行
        其他+Enter：关闭程序并保存
        ''')
        for w in l.readlines():
            w=w.lstrip()
            if w=='':
                continue
            b+=1
            if b>=c:
                a=input(str(b)+' '+w)

                if not a=='': 
                    with open(用户+zh+xs[xs0]+'cd.txt', 'w') as file:
                        file.write(str(b))
                    break
        l.close()
        print('\n'*100)
天启()
