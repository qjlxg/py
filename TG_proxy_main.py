# w1770946466 北慕白  https://github.com/w1770946466/Auto_proxy
# v2ray_collecto
# coding=utf-8
import base64
import requests
import re
import time
import os
import threading
from tqdm import tqdm
import random, string
import datetime
from time import sleep
import chardet

#试用机场链接
home_urls =(
'https://upm8kfu.nicecloud.win:8443',
'http://175.178.9.20',
'http://47.74.1.114:8089',
'http://nuxyun.v2rayflash.top',
'http://sub.kjdjakskl.cyou',
'http://xueyejiasu.com',
'https://0run.vip',
'https://25054128.xyz',
'https://57dea681-95e1-4f00-8807-302677474a89.38944.xyz',
'https://6xp5FU.tosslk.xyz',
'https://a.977344.xyz',
'https://a1.8jiasu.com',
'https://a1.allbluess.pro',
'https://apanel.tinnyrick.com',
'https://api.e986532.top',
'https://api.heima2u.com',
'https://api.shanhai.one',
'https://az.233235.xyz',
'https://az.757866.xyz',
'https://b1.mikasass.pro',
'https://c3.tolinkss.pro',
'https://cdn.yom666.net',
'https://cn.newbee.cyou',
'https://cn.newbee888.cc',
'https://cokecloud.me',
'https://dashuai.us',
'https://dobcloud.com',
'https://fast.sudatech.store',
'https://hn1r5k7322.bitmusttw.com',
'https://hongxingdl.com',
'https://hongxingdl.love',
'https://huojian.02000.net',
'https://jiasuba.xyz',
'https://lime1.xyz',
'https://link05.shanhai.me',
'https://link06.shanhai.me',
'https://littleqqq.co',
'https://mc.jiedianxielou.workers.dev',
'https://my.emovpns.top',
'https://MyEO9v.absslk.xyz',
'https://pavo.eu.org',
'https://portal.speedyyun.com',
'https://qingyun.zybs.eu.org',
'https://s1.byte11.com',
'https://saiboyun.org',
'https://shanhai.me',
'https://siris.eu.org',
'https://songguanting.eu.org',
'https://soulvpn.net',
'https://sub.372372.xyz',
'https://sub.cokecloud.world',
'https://sub1.pingboy.top',
'https://supz1.6128888.xyz',
'https://terfghtll.dashuai.us',
'https://v2lnk.net',
'https://vip.tinnyrick.com',
'https://vol.6128888.xyz',
'https://vpn.28.al',
'https://vvs.e54.site',
'https://www.ckckssl.top',
'https://www.duguletian.com',
'https://www.heima360.in',
'https://www.kuaidog006.top',
'https://www.kuaidog010.top',
'https://www.littleqqq.co',
'https://www.louwangzhiyu.xyz',
'https://www.mgnet.sbs',
'https://www.okanc.com',
'https://www.qf1.us',
'https://www.tiziwrops.com',
'https://www.xiahas.top',
'https://xc1.shishi1.buzz',
'https://xn--4gq62f.com',
'https://xueyejiasu.com',
'https://ykxqn.com',
'https://yV4iXJ.mcsslk.xyz',
'https://ywl.201593.xyz',
'https://www.mgjs.site',
'https://www.mgnet.vip',
'https://vip.baima360.com',
'https://18.mamamajd.site',
'http://51.255.173.39',
'https://5.44.251.106',
'http://47.101.67.199:6699',
'http://subxfxssr.xfxvpn.me',
'https://cokecloud.net',
'https://az2.233235.xyz',
'https://s.jiasu01.vip',
'https://sub.xueyejiasu.com',
'https://202504111330311.chibaba.ggff.net',
'http://202504081152261.chibaba.ggff.net',
'https://azyun.top',
'https://aq.louwangzhiyu.xyz',
'https://202503212313501.chibaba.ggff.net',
'https://xqsub.e54.site',
'https://www.vfast.life',
'https://link10.shanhai.one',
'https://mgnet.vip',
'https://w1.v2free.cc',
'https://nova.live',
'https://portal.passgfw.top',
'https://www.flybar4.cc',
'https://plu.socoo-best.xyz',
'https://a.112664.xyz',
'https://afun-waf.trafficmanager.net',
'https://feigou.zhunchuanpb.com',
'https://zhenxunkeai.top',
'https://dash2.moonriver.one',
'https://page.sulink.one',
'https://zhuye2.sulink.one',
'https://6.needss.one',
'https://needss.link',
'https://mgxiaowu.net',
'https://db01.in',
'https://hy-2.com',
'https://hy-2.sbs',
'https://abyssvpn.com',
'https://www.meigui168.net',
'https://s1.equinoxaa.com',
'https://www.f2ray.com',
'https://懒猫.com',
'https://www.z1z1.top',
'https://honven20.dgywzc.com',
'https://reurl.cc',
'https://cloud.speedypro.xyz',
'https://www.qlgq.top',
'https://www.v2ny.com',
'https://ikuuu.me',
'https://xn--iiq540h.com',
'https://jgjs02.com',
'https://xn--4gq62f52gdss.com',
'https://yuyan.online',
'https://board.jike99.xyz',
'https://dash.fscloud.cc',
'https://doucat.top',
'https://www.mojie.me',
'https://besnow.me',
'https://lksi.xyz',
'https://www.taishan.pro',
'https://zhu.suyun.bio',
'https://glados.space',
'https://tly.sh',
'https://sockboom.love',
'https://panel.keleofficial.com',
'https://daniu.e300daniu.top',
'https://klxq.djgskc.top',
'https://px.bt3.one',
'https://chy.fit',
'https://v3ssy.xyz',
'https://www.proxyvip.xyz',
'https://daxun.club',
'https://bcast.ink',
'https://b0chi.r-yu.me',
'https://cd520.xyz',
'https://www.aoxiangyun.top',
'https://www.mickey.business',
'https://sp.nfsq.me',
'https://cocolink.org',
'https://oukasou.xyz',
'https://www.aimacloud.info',
'https://user.xinna.co',
'https://nanmin.xyz',
'https://qiaoxbbq.com',
'https://mxwljsq.xyz',
'https://www.okvpn.cc',
'https://my.jetfast.dev',
'https://shandiandog.com',
'https://tagss04.pro',
'https://suo.yt',
'https://cdn.ednovas.org',
'https://qytvipaffcc04.qytvipaff.pro',
'https://fengwo.pro',
'https://love.52pokemon.cc',
'https://superbiu.com',
'https://ocloudvpn.com',
'https://mly01.miaolianyun.my',
'https://px.xinyo.me',
'https://airport.raloar.top',
'https://xunlian.site',
'https://www.cacapex.com',
'https://a.kpyun.live',
'https://main.cute-cloud.de',
'https://cloud.jisuba.me',
'https://yunduanjc.top',
'https://便宜机场.co',
'https://site01.stardad.lol',
'https://mogufan.com',
'https://changyouvpn.top',
@
'https://app.cloudog.me',
'https://invite6.cht.taipei',
'https://app.gomeow.cloud',
'https://guobaotegong.me',
'https://jjz2.31465.cfd',
'https://fil1.cloud.fil.firm.in.31465.cfd',
'https://172.104.33.229:7022',
'https://nexx.us.kg',
'https://a.0123456789.us.kg',
'https://a.opk.icu',
'https://569.2.passwallwall.life',
'https://aeda2.asa.lol',
'https://user.dafeiji.one',
'https://web2.dogssr.sbs',
'https://web2.52pokemon.cc',
'https://ni8.zxm.cc',
'https://www2345.养老机场.com',
'https://sub.ssrsub.com',
'https://mlshu.com',
'https://dash.bigcow.cc',
'https://www.fawncloud.one',
'https://廉价机场.com',
'https://cloud.speedyweb.xyz',
'https://z.luxury',
'https://askahh.com',
'https://powerwan.net',
'https://afun.la',
'https://xn--4gqp1u.com',
'https://web.nnpy.org',
'https://syyn.1.passwallwall.life',
'https://www11.henet.uk',
'https://ikuuu.pw',
'https://a.aik88.top',
'https://xn--wtq35pfyd55o.co',
'https://asa.lol',
'https://www.huaxia.cyou',
'https://newserver.t1i.top',
'https://ins.ins66.com',
'https://by.yunduanjc.top',
'https://pmy666.xyz',
'https://air.aptlive.org',
'https://naisicloud.xyz',
'https://qingyunti.cc',
'https://pfjc.im',
'https://w02.qytl2web01.cc',
'https://kaikaixinxin.me',
'https://kuailejc.xyz',
'https://dash.minizz.online',
'https://api114514.nuwaa.rest',
'https://yunlu.vip',
'https://vvcloud.us.kg',
'https://zouma.guanhua.xyz',
'https://kaolacloud.site',
'https://www.hj521.top',
'https://www.hj522.top',
'https://my.pianyi.info',
'https://zxc.noseisei.com',
'https://abc.noseisei.com',
'https://bailian.site',
'https://passwall.link',
'https://xyz.noseisei.com',
'https://b.yousu.cc',
'https://www.xbyun.live',
'https://app.legeth.cc',
'https://c.yousu.cc',
'https://vyy.idsduf.com',
'https://a.yousu.cc',
'https://www.smcow.com',
'https://thecom.today',
'https://xmfwww.cc',
'https://a123.buzz',
'https://aikx.me',
'https://zzz.youxuan.wiki',
'https://maple.icu',
'https://1.vyunyun.top',
'https://pkq.xlm.plus',
'https://ddddd.site',
'https://zqjc.org',
'https://www.aaaspeed.cc',
'https://xx-ai.io',
'https://zhenshihui.life',
'https://1run.vip',
'https://zhenshihui.shop',
'https://sq9xy6.cpminig.com',
'https://vpn.sudatech.store',
'https://app.cloudlion.me',
'https://user.susucloud.net',
'https://zhuiyun.top',
'https://gg.mqs.xyz',
'https://sulink.pro',
'https://arisaka.io',
'https://www.eyujichang.com',
'https://www.mangshe.org',
'https://db.shellnet.net',
'https://jisovpn.site',
'https://fpacecloud.com',
'https://niercloud.com',
'https://my.catfaka.com',
'https://www.xfxssr.com',
'https://b.xiaow.cc',
'https://www.chaoyue.shop',
'https://client.3i.lol',
'https://www.strongswans.net',
'https://wumaojichang.com',
'https://f.wwwq.net',
'https://www.dukadi.one',
'https://lanmaoyun.icu',
'https://waterwheel.buzz',
'https://ktmcloud.top',
'https://xianyuwangluo.top',
'https://syq.tw',
'https://cxk.lol',
'https://darkforest.cloud',
'https://sanxijichang.com',
'https://sidog.top',
'https://store.kakocloud.pro',
'https://gfw.best',
'https://www.genies.top',
'https://chiguayun.net',
'https://chiguayun.com',
'https://chiguayun.org',
'https://guanwang.me',
'https://liulangdiqiu.cc',
'https://qianggewangluo.com',
'https://nanbei.cloud',
'https://nanbei.buzz',
'https://www.1365365.xyz',
'https://bt3.one',
'https://tcity8.top',
'https://liangyuandian.club',
'https://shuimu.site',
'https://reborn.kaochang.ltd',
'https://fastestcloud.xyz',
'https://gd.kaxinzx.cc',
'https://kuaiqiangshou.xyz',
'https://neko.services',
'https://neko.yuriuni.com',
'https://vpn.gunyoung.top',
'https://my.legeth.com',
'https://dash.legeth.com',
'https://onefall.top',
'https://www.paopao.dog',
'https://app.birds.hk',
'https://www.1belt1road.vip',
'https://port.baozipu.cc',
'https://www.1655ss.com',
'https://usla.icola.top',
'https://22.lownet.xyz',
'https://suwayun.com',
'https://wayen.eu',
'https://mpddt.top',
'https://www.9yuan.top',
'https://jk-cloud.net',
'https://www.fooksun.xyz',
'https://jkcloud.net',
'https://www.flymetothemoon.work',
'https://ov2rayo.top',
'https://17yxyy.cc',
'https://54fxp.xyz',
'https://haoba.cloud',
'https://mianmd.ninja',
'https://www.gogocloud.cyou',
'https://planb.cat',
'https://v.cheerfun.dev',
'https://www.cantonx.com',
'https://air.yoyoss.xyz',
'https://www.v2ssr.top',
'https://91yun.buzz',
'https://portal.buddhajumpsoverthewall.com',
'https://network2.magic-in-china.com',
'https://kedouair.top',
'https://kaxin.cc',
'https://www.wkyun1688.com',
'https://ssr.giize.com',
'https://home.wkyuns.xyz',
'https://air.misakano.eu.org',
'https://yhcvpn.xyz',
'https://www.starlink9527.xyz',
'https://starlink.to',
'https://bajie.pw',
'https://bajie.info',
'https://marslink.org',
'https://www.marslink.cc',
'https://8rkt.xyz',
'https://58rocket.com',
'https://miaona.xyz',
'https://api.dashsp.top',
'https://miaona.co',
'https://miaona.org',
'https://latiao.club',
'https://58sd.net',
'https://latiao.us',
'https://glados.one',
'https://glados.network',
'https://bityun.org',
'https://sub.chbjpw.mobi',
'https://88catnet.com',
'https://www.99catnet.com',
'https://www.58mdss.com',
'https://mdss.cloud',
'https://huajic.link',
'https://w2.ddnsgo.xyz',
'https://2.flybar20.cc',
'https://dy3.yunhu1.xyz',
'https://ayucloud.services',
'https://bbs.cloudnetwork.pro',
'https://cainiao216.top',
'https://cainiao217.top',
'https://cainiao220.top',
'https://cainiao221.top',
'https://cainiao223.top',
'https://cainiao224.top',
'https://cloudfox.club',
'https://dash3.moonriver.one',
'https://dash4.moonriver.one',
'https://dash5.moonriver.one',
'https://dd.moonriver.cfd',
'https://dy.yh13.xyz',
'https://kugou.cloud',
'https://lianjia.me',
'https://lianjiajichang.com',
'https://lianjiasub.work',
'https://maoyun3.com',
'https://mcecloud.com',
'https://moonriver.one',
'https://s2.equinoxaa.com',
'https://s3.equinoxaa.com',
'https://subscribe2628.lanmaoyun.icu',
'https://sulian.life',
'https://tiedan.595418.xyz',
'https://uuvpn.cloud',
'https://www.cl001.site',
'https://www.diaomaojichang.top',
'https://www.ducklink.net',
'https://www.flybar13.cc',
'https://www.gscloud.icu',
'https://www.laoniu49.top',
'https://www.mbsurf.xyz',
'https://www.moonriver.sbs',
'https://www.tiedan168.net',
'https://sttlink.net',
'https://人人传承.com',
'https://一元中转.com',
'https://necloud.win',
'https://v2free.net',
'https://shopvpn.net',
'https://xingoogle.com',
'https://www.jwfree.us',
'http://ywl.201593.xyz',
'https://panel.nextnet.one',
'https://gotocdn.tencentagi.com',
'https://tlnnm.ntgdada.top',
'https://byijsq.com',
'https://jisu3.02000.net',
'https://yexiaowork.fmvp.al',
'https://202503021722111.chibaba.ggff.net',
'http://202504011048041.chibaba.ggff.net',
'https://xn--mes91t7ofgnw.com',
'http://yl.hq12.top/',
'https://cloud.jisuba.live',
'https://chuifengji.top',
'https://yihicloud.top',
'https://hssl8088.icu',
'https://xjyjc.top',
'http://wuxianjc.top',
'http://changyouVPN.top',
'http://kuailejc.xyz',
'https://1.dishuyun.top',
'https://baiyangxing.com',
'https://a03.qytvipaff.pro',
'https://xn--9kqx21a0sv.com',
'https://xn--4oq11ryli3rg.com',
'https://jp.taishan.pro',
'https://bbxy.xn--cesw6hd3s99f.com',
'https://flybit.vip',
'https://zongyunti.com',
'https://jiasu.la',
'https://dash.afun.la',
'https://affman.mellanox.fyi',
'https://www.xn--qprx60h.site',
'https://xn--4gq1dp1ix68g.xyz',
'https://www.redleaf.cloud',
'https://foxtiming.com',
'https://wuyouyun.sbs',
'https://hx666.02000.net',
'https://web3.52pokemon.cc',
'https://ofonet.net',
'https://air001.dianying.my',
'http://web.nnpy.org',
'https://snangua.com',
'https://c.xunle.de',
'http://suliannet.cn',
'https://ygl28a.235222.xyz',
'https://o274i.xffvps.eu.org',
'https://c6jxw.xffvps.eu.org',
'https://admin.linkerror.cc',
'http://x2b.eans.top',
'http://v.moon2046.com',
'http://panel.moon2046.com',
'http://47.122.132.169:23411',
'http://pay.xinghongpay.top',
'https://my.netv2.net',
'https://FdxjrlMBE8.mofangsub01.lol',
'https://service.mofangcloud.shop',
'https://netv2.net',
'https://uat-admin.drt-acs.org',
'https://xbb.cwhome.top',
'https://1st.760666.xyz',
'https://south.shuiyun.sbs',
'https://moes.lnaspiring.com',
'https://gogoyun.org',
'http://xb.718181.xyz',
'https://saiboyun.icu',
'http://bobapp.xuebispeed.com',
'https://api.nfspeed01.com',
'https://panel.nfspeed01.com',
'https://bobapp.nfspeed01.com',
'https://service.mf-api1.site',
'http://tt.yesiamai.com',
'http://deepquery.cn',
'https://go.yueyun.de',
'http://258936.xyz',
'http://www.258936.xyz',
'https://www.nmkjvpn.com',
'https://nmkjvpn.com',
'https://panel.fast8888.com',
'https://vpn.bpeaed.com',
'https://panel2.fast8888.com',
'https://airport.lat',
'https://tz1314.top',
'https://x.235222.xyz',
'https://xxx.xiaoshihoukepangle.sbs',
'https://hoo.caaa.tech',
'https://2501.xunle.de',
'https://www.baimao.us',
'https://jwlingjing.shop',
'https://154.17.15.126',
'https://us1.av8dcloud.top',
'https://vcros.net',
'https://v1-4-2.qwunessles.online',
'https://mvet.info',
'https://api.vetcross.work',
'https://vetcross.work',
'http://huojian2.xyz',
'http://www.huojian2.xyz',
'https://www.skyhomevpn.com',
'https://skyhomevpn.com',
'https://154.21.81.177',
'https://154.17.13.104',
'https://poqiang.site',
'https://www.xn--vl1a701a.xyz',
'https://abcd168.icu',
'https://www.abcd168.icu',
'https://4afcn.jp.313132.xyz',
'https://v02.520131.best',
'http://southsidelife.tryme3.xyz',
'https://api.xinghongapi.xyz',
'http://putao.i2345.org',
'http://putao.i2345.me',
'http://po1.6128888.xyz',
'http://po2.6128888.xyz',
'http://po3.6128888.xyz',
'http://fly.6128888.xyz',
'https://ddsfsdfsdf.tiktok.casa',
'http://apanel.allbatech.net',
'https://flybirdy.xyz',
'http://vpn.gangko.cn',
'https://dns.mytonxs.uk',
'https://gsmoney.uk',
'https://jisu2.02000.net',
'https://jisu4.02000.net',
'https://www.yywhale.com',
'https://v2.gpket.net',
'https://dy.lime5.xyz',
'https://01.conva.top',
'https://sub.nsxwo.com',
'https://xb.718181.xyz',
'https://suliannet.cn',
'https://111.xiyouji.tk',
'https://bobapp.xuebispeed.com',
'https://tt.yesiamai.com',
'https://deepquery.cn',
'https://258936.xyz',
'https://www.258936.xyz',
'https://wamn.icu',
'https://dy.yooyo.top',
'https://yang521.org',
'https://yang521.top',
'https://av8dcloud.top',
'https://dingyue.xjay.xyz',
'https://d58e3582afa99040e27b92b13c8f2280.boluoidc.com',
'https://huiguodingyue.yingmaox.cc',
'https://filashe.org',
'https://panel.moon2046.com',
'https://pay.xinghongpay.top',
'https://x2b.eans.top',
'https://v.moon2046.com',
'https://www.chinacmcc.xyz',
'https://xboard.ryuuz.cn',
'http://fast.thenight.icu',
'http://v02.520131.best',
'https://z.shipv.net',
'https://po2.6128888.xyz',
'https://po1.6128888.xyz',
'https://po3.6128888.xyz',
'https://fly.6128888.xyz',


)
#文件路径
update_path = "./sub/"
#所有的clash订阅链接
end_list_clash = []
#所有的v2ray订阅链接
end_list_v2ray = []
#所有的节点明文信息
end_bas64 = []
#获得格式化后的链接
new_list = []
#永久订阅
e_sub = ['']
#频道
urls =[]
#线程池
threads = []
#机场链接
plane_sub = ['']
#机场试用链接
try_sub = []
#获取频道订阅的个数
sub_n = -25
#试用节点明文
end_try = []

#获取群组聊天中的HTTP链接
def get_channel_http(url):
    headers = {
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://t.me/s/oneclickvpnkeys',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.post(
        url, headers=headers)
    #print(response.text)
    pattren = re.compile(r'"https+:[^\s]*"')
    url_lst = pattren.findall(response.text)
    #print('获取到',len(url_lst),'个网址')
    #print(url_lst)
    return url_lst


#对bs64解密
def jiemi_base64(data):  # 解密base64
    # 对 Base64 编码后的字符串进行解码，得到字节字符串
    decoded_bytes = base64.b64decode(data)
    # 使用 chardet 库自动检测字节字符串的编码格式
    encoding = chardet.detect(decoded_bytes)['encoding']
    # 将字节字符串转换为字符串
    decoded_str = decoded_bytes.decode(encoding)
    return decoded_str

#判读是否为订阅链接
def get_content(url):
    #print('【获取频道',url,'】')
    url_lst = get_channel_http(url)
    #print(url_lst)
    #对链接进行格式化
    for i in url_lst:
        result = i.replace("\\", "").replace('"', "")
        if result not in new_list:
            if "t" not in result[8]:
                if "p" not in result[-2]:
                    new_list.append(result)
    #print(new_list)
    #print("共获得", len(new_list), "条链接")
    #获取单个订阅链接进行判断
    i = 1
    try:
        new_list_down = new_list[sub_n::]
    except:
        new_list_down = new_list[len(new_list) * 2 // 3::]
    #print("共获得", len(new_list_down), "条链接")
    #print('【判断链接是否为订阅链接】')
    for o in new_list_down:
        try:
            res = requests.get(o)
            #判断是否为clash
            try:
                skuid = re.findall('proxies:', res.text)[0]
                if skuid == "proxies:":
                    #print(i, ".这是个clash订阅", o)
                    end_list_clash.append(o)
            except:
                #判断是否为v2
                try:
                    #解密base64
                    peoxy = jiemi_base64(res.text)
                    #print(i, ".这是个v2ray订阅", o)
                    end_list_v2ray.append(o)
                    end_bas64.extend(peoxy.splitlines())
                    
                #均不是则非订阅链接
                except:
                    #print(i, ".非订阅链接")
                    pass
        except:
            #print("第", i, "个链接获取失败跳过！")
            pass
        i += 1
    return end_bas64

#写入文件
def write_document():
    if e_sub == [] or try_sub == []:
        print("订阅为空请检查！")
    else:
        #永久订阅
        random.shuffle(e_sub)
        for e in e_sub:
            try:
                res = requests.get(e)
                proxys=jiemi_base64(res.text)
                end_bas64.extend(proxys.splitlines())
            except:
                print(e,"永久订阅出现错误❌跳过")
        print('永久订阅更新完毕')
        #试用订阅
        random.shuffle(try_sub)
        for t in try_sub:
            try:
                res = requests.get(t)
                proxys=jiemi_base64(res.text)
                end_try.extend(proxys.splitlines())
            except Exception as er:
                print(t,"试用订阅出现错误❌跳过",er)
        print('试用订阅更新完毕',try_sub)
        #永久订阅去重
        end_bas64_A = list(set(end_bas64))
        print("去重完毕！！去除",len(end_bas64) - len(end_bas64_A),"个重复节点")
        #永久订阅去除多余换行符
        bas64 = '\n'.join(end_bas64_A).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #试用去除多余换行符
        bas64_try = '\n'.join(end_try).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #获取时间，给文档命名用
        t = time.localtime()
        date = time.strftime('%y%m', t)
        date_day = time.strftime('%y%m%d', t)
        #创建文件路径
        try:
            os.mkdir(f'{update_path}{date}')
        except FileExistsError:
            pass
        txt_dir = update_path + date + '/' + date_day + '.txt'
        #写入时间订阅
        file = open(txt_dir, 'w', encoding='utf-8')
        file.write(bas64)
        file.close()       
        
        #减少获取的个数
        r = 1
        length = len(end_bas64_A)  # 总长
        m = 8  # 切分成多少份
        step = int(length / m) + 1  # 每份的长度
        for i in range(0, length, step):
            print("起",i,"始",i+step)
            zhengli = '\n'.join(end_bas64_A[i: i + step]).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
            #将获得的节点变成base64加密，为了长期订阅
            obj = base64.b64encode(zhengli.encode())
            plaintext_result = obj.decode()
            #写入长期订阅
            file_L = open("Long_term_subscription"+str(r), 'w', encoding='utf-8')
            file_L.write(plaintext_result)
            r += 1
        #写入总长期订阅
        obj = base64.b64encode(bas64.encode())
        plaintext_result = obj.decode()
        file_L = open("Long_term_subscription_num", 'w', encoding='utf-8')
        file_L.write(plaintext_result)
        #写入试用订阅
        obj_try = base64.b64encode(bas64_try.encode())
        plaintext_result_try = obj_try.decode()
        file_L_try = open("Long_term_subscription_try", 'w', encoding='utf-8')
        file_L_try.write(plaintext_result_try)
        #写入README
        with open("README.md", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        now_time = datetime.datetime.now()
        TimeDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for index in range(len(lines)):
            try:
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription_num`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription1`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription2`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription3`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription4`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription5`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription6`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription7`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription8`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length-step*7}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription3.yaml`\n': # 目标行内容
                    lines.pop(index+4)
                    lines.pop(index+4)
                    lines.insert(index+4, f'Updata：`{TimeDate}`\n')
                    lines.insert(index+4, f'### Try the number of high-speed subscriptions: `{len(try_sub)}`\n')
                if lines[index] == '>Trial subscription：\n': # 目标行内容
                    lines.pop(index)
                    lines.pop(index)
                """
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
                """
            except:
                #print("写入READ出错")
                pass
        #写入试用订阅
        for index in range(len(lines)):
            try:
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        #lines.insert(index+n-1, f'\n>')
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
            except:
                print("写入试用出错")
        
        with open("README.md", 'w', encoding='utf-8') as f:
            data = ''.join(lines)
            f.write(data)
        print("合并完成✅")
        try:
            numbers =sum(1 for _ in open(txt_dir))
            print("共获取到",numbers,"节点")
        except:
            print("出现错误！")
        
    return

#获取clash订阅
def get_yaml():
    print("开始获取clsah订阅")
    urls = []
    n = 1
    for i in urls:
        response = requests.get(i)
        #print(response.text)
        file_L = open("Long_term_subscription" + str(n) +".yaml", 'w', encoding='utf-8')
        file_L.write(response.text)
        file_L.close()
        n += 1
    print("clash订阅获取完成！")

#获取机场试用订阅
def get_sub_url():
    V2B_REG_REL_URL = '/api/v1/passport/auth/register'
    times = 1
    for current_url in home_urls:
        i = 0
        while i < times:
            header = {
                'Referer': current_url,
                'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            form_data = {
                'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))+'@gmail.com',
                'password': 'autosub_v2b',
                'invite_code': '',
                'email_code': ''
            }
            if current_url == 'https://xn--4gqu8thxjfje.com' or current_url == 'https://seeworld.pro'  or current_url == 'https://www.jwckk.top'or current_url == 'https://vvtestatiantian.top':
                try:
                    fan_res = requests.post(
                        f'{current_url}/api/v1/passport/auth/register', data=form_data, headers=header)
                    auth_data = fan_res.json()["data"]["auth_data"]
                    #print(auth_data)
                    fan_header = {
                        'Origin': current_url,
                        'Authorization': ''.join(auth_data),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Connection': 'keep-alive',
                        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                        'Referer': current_url,
                    }
                    fan_data = {
                        'period': 'onetime_price',
                        'plan_id': '1',
                    }
                    fan_res_n = requests.post(
                        f'{current_url}/api/v1/user/order/save', headers=fan_header, data=fan_data)
                    #print(fan_res_n.json()["data"])
                    fan_data_n = {
                        'trade_no':fan_res_n.json()["data"],
                        #'method': '1',
                    }
                    fan_res_pay = requests.post(
                        f'{current_url}/api/v1/user/order/checkout', data=fan_data_n, headers=fan_header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={fan_res.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as result:
                    print(result)
                    break
            else:
                try:
                    response = requests.post(
                        current_url+V2B_REG_REL_URL, data=form_data, headers=header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as e:
                    print("获取订阅失败",e)
            i += 1

            
  
def get_kkzui():
    # ========== 抓取 kkzui.com 的节点 ==========
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://kkzui.com/jd?orderby=modified",headers=headers)
        article_url = re.search(r'<h2 class="item-heading"><a href="(https://kkzui.com/(.*?)\.html)"',res.text).groups()[0]
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'<p><strong>这是v2订阅地址</strong>：(.*?)</p>',res.text).groups()[0]
        print(sub_url)
        e_sub.append(sub_url)
        print("获取kkzui.com完成！")
    except:
        print("获取kkzui.com失败！")
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://www.cfmem.com/search/label/free",headers=headers)
        article_url = re.search(r"https?://www\.cfmem\.com/\d{4}/\d{2}/\S+v2rayclash-vpn.html",res.text).group()
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'>v2ray订阅链接&#65306;(.*?)</span>',res.text).groups()[0]
        print(sub_url)
        try_sub.append(sub_url)
        e_sub.append(sub_url)
    except Exception as e:
        print(e)
        
    
if __name__ == '__main__':
    print("========== 开始获取机场订阅链接 ==========")
    get_sub_url()
    print("========== 开始获取kkzui.com订阅链接 ==========")
    get_kkzui()
    print("========== 开始获取频道订阅链接 ==========")
    for url in urls:
        #print(url, "开始获取......")
        thread = threading.Thread(target=get_content,args = (url,))
        thread.start()
        threads.append(thread)
        #resp = get_content(get_channel_http(url))
        #print(url, "获取完毕！！")
    #等待线程结束
    for t in tqdm(threads):
        t.join()
    print("========== 准备写入订阅 ==========")
    res = write_document()
    clash_sub = get_yaml()
    print("========== 写入完成任务结束 ==========")
