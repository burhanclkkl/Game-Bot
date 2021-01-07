# Green Stable SS' M

import discord
from discord.ext.commands import Bot
import datetime
import time
import random
import requests
from bs4 import BeautifulSoup

TOKEN = "<DISCORD TOKEN>"   # Token

client = discord.Client()
bot = Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(str(bot.user) + " Bot Hazır!") # Bot Ready Info

# Döviz Verileri 
r = requests.get('https://www.doviz.com/' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("span",  attrs={"class":["value"," valueIncreased"," valueDecreased"]})
y = source.find_all("span",  attrs={"class":"name"})

list = []
list1 = []

for i in x:
    list.append(i.text)
for i in y:
    list1.append(i.text)
metin =  "\n" +list1[0] +" : "+  list[0] +"\n" + list1[1] +" : "+ list[1] +"\n"+ list1[2]  +" : "+ list[2] +"\n" + list1[3]  +" : "+ list[3]+"\n"+ list1[4]  +" : "+  list[4]+"\n"+list1[5]  +" : "+  list[5] +"\n"+list1[6]  +" : "+  list[6]+"\n"+ list1[7]  +" : "+  list[7] 

# Süper Lig Verileri
r = requests.get('https://www.mackolik.com/puan-durumu/t%C3%BCrkiye-s%C3%BCper-lig/482ofyysbdbeoxauk19yg7tdt' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("span", attrs={"class":"p0c-competition-tables__team-name p0c-competition-tables__team-name--full"})

list = []
list1 = []

for i in x:
    list.append(i.text)
for siralama in range(1,20):
    list1.append(str(siralama))    

superlig =  "\n" +list1[0] +" : "+  list[0] +"\n" + list1[1] +" : "+ list[1] +"\n"+ list1[2]  +" : "+ list[2] +"\n" + list1[3]  +" : "+ list[3]+"\n"+ list1[4]  +" : "+  list[4]+"\n"+list1[5]  +" : "+  list[5] +"\n"+list1[6]  +" : "+  list[6]+"\n"+ list1[7]  +" : "+  list[7] + "\n" +list1[8] +" : "+  list[8] +"\n" + list1[9] +" : "+ list[9] +"\n"+ list1[10]  +" : "+ list[10] +"\n" + list1[11]  +" : "+ list[11]+"\n"+ list1[12]  +" : "+  list[12]+"\n"+list1[13]  +" : "+  list[13] +"\n"+list1[14]  +" : "+  list[14]

# Piremier Ligi Verileri
r = requests.get('https://www.mackolik.com/puan-durumu/ingiltere-premier-lig/2kwbbcootiqqgmrzs6o5inle5' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("span", attrs={"class":"p0c-competition-tables__team-name p0c-competition-tables__team-name--full"})

list = []
list1 = []

for i in x:
    list.append(i.text)
for siralama in range(1,20):
    list1.append(str(siralama))

premier =  "\n" +list1[0] +" : "+  list[0] +"\n" + list1[1] +" : "+ list[1] +"\n"+ list1[2]  +" : "+ list[2] +"\n" + list1[3]  +" : "+ list[3]+"\n"+ list1[4]  +" : "+  list[4]+"\n"+list1[5]  +" : "+  list[5] +"\n"+list1[6]  +" : "+  list[6]+"\n"+ list1[7]  +" : "+  list[7] + "\n" +list1[8] +" : "+  list[8] +"\n" + list1[9] +" : "+ list[9] +"\n"+ list1[10]  +" : "+ list[10] +"\n" + list1[11]  +" : "+ list[11]+"\n"+ list1[12]  +" : "+  list[12]+"\n"+list1[13]  +" : "+  list[13] +"\n"+list1[14]  +" : "+  list[14]

# Bundesliga Ligi Verileri
r = requests.get('https://www.mackolik.com/puan-durumu/almanya-bundesliga/6by3h89i2eykc341oz7lv1ddd' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("span", attrs={"class":"p0c-competition-tables__team-name p0c-competition-tables__team-name--full"})

list = []
list1 = []

for i in x:
    list.append(i.text)
for siralama in range(1,20):
    list1.append(str(siralama))

bundesliga =  "\n" +list1[0] +" : "+  list[0] +"\n" + list1[1] +" : "+ list[1] +"\n"+ list1[2]  +" : "+ list[2] +"\n" + list1[3]  +" : "+ list[3]+"\n"+ list1[4]  +" : "+  list[4]+"\n"+list1[5]  +" : "+  list[5] +"\n"+list1[6]  +" : "+  list[6]+"\n"+ list1[7]  +" : "+  list[7] + "\n" +list1[8] +" : "+  list[8] +"\n" + list1[9] +" : "+ list[9] +"\n"+ list1[10]  +" : "+ list[10] +"\n" + list1[11]  +" : "+ list[11]+"\n"+ list1[12]  +" : "+  list[12]+"\n"+list1[13]  +" : "+  list[13] +"\n"+list1[14]  +" : "+  list[14]

# ING BSL (Basketbol) Verileri
r = requests.get('https://www.mackolik.com/puan-durumu/almanya-bundesliga/6by3h89i2eykc341oz7lv1ddd' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("span", attrs={"class":"p0c-competition-tables__team-name p0c-competition-tables__team-name--full"})

list = []
list1 = []

for i in x:
    list.append(i.text)
for siralama in range(1,20):
    list1.append(str(siralama))

ing_bsl =  "\n" +list1[0] +" : "+  list[0] +"\n" + list1[1] +" : "+ list[1] +"\n"+ list1[2]  +" : "+ list[2] +"\n" + list1[3]  +" : "+ list[3]+"\n"+ list1[4]  +" : "+  list[4]+"\n"+list1[5]  +" : "+  list[5] +"\n"+list1[6]  +" : "+  list[6]+"\n"+ list1[7]  +" : "+  list[7] + "\n" +list1[8] +" : "+  list[8] +"\n" + list1[9] +" : "+ list[9] +"\n"+ list1[10]  +" : "+ list[10] +"\n" + list1[11]  +" : "+ list[11]+"\n"+ list1[12]  +" : "+  list[12]+"\n"+list1[13]  +" : "+  list[13] +"\n"+list1[14]  +" : "+  list[14]

# NBA Doğu (Basketbol) Verileri

r = requests.get('https://www.mackolik.com/basketbol/puan-durumu/usa-nba/2019-2020/e2w9iicoifx689pzi5jqw7j4a' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("span", attrs={"class":"p0c-competition-tables__team-name"})

list = []
list1 = []

for i in x:
    list.append(i.text)
for siralama in range(1,16):
    list1.append(str(siralama))

nba_east =  "\n" + list1[0] + " : " +  list[0] +"\n" + list1[1] +" : "+ list[1] +"\n"+ list1[2]  +" : "+ list[2] +"\n" + list1[3]  +" : "+ list[3]+"\n"+ list1[4]  +" : "+  list[4]+"\n"+list1[5]  +" : "+  list[5] +"\n"+list1[6]  +" : "+  list[6]+"\n"+ list1[7]  +" : "+  list[7] + "\n" +list1[8] +" : "+  list[8] +"\n" + list1[9] +" : "+ list[9] +"\n"+ list1[10]  +" : "+ list[10] +"\n" + list1[11]  +" : "+ list[11]+"\n"+ list1[12]  +" : "+  list[12]+"\n"+list1[13]  +" : "+  list[13] +"\n"+list1[14]  +" : "+  list[14]

# NBA Batı (Basketbol) Verileri

r = requests.get('https://www.mackolik.com/basketbol/puan-durumu/usa-nba/2019-2020/e2w9iicoifx689pzi5jqw7j4a' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("span", attrs={"class":"p0c-competition-tables__team-name"})

siralama1 = 0  
siralama = 0

for i in x :
    siralama += 1 
    if siralama >= 15:
        siralama1 += 1
        list1.append(str(siralama))  

nba_west =  "\n" + list1[0] + " : " +  list[0] +"\n" + list1[1] +" : "+ list[1] +"\n"+ list1[2]  +" : "+ list[2] +"\n" + list1[3]  +" : "+ list[3]+"\n"+ list1[4]  +" : "+  list[4]+"\n"+list1[5]  +" : "+  list[5] +"\n"+list1[6]  +" : "+  list[6]+"\n"+ list1[7]  +" : "+  list[7] + "\n" +list1[8] +" : "+  list[8] +"\n" + list1[9] +" : "+ list[9] +"\n"+ list1[10]  +" : "+ list[10] +"\n" + list1[11]  +" : "+ list[11]+"\n"+ list1[12]  +" : "+  list[12]+"\n"+list1[13]  +" : "+  list[13] +"\n"+list1[14]  +" : "+  list[14]

# IP Adresi Öğrenme

r = requests.get('https://www.atakdomain.com/ip-sorgulama' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("div", attrs={"class":"ip-show div-center"})

list = []

for i in x :
    list.append(i.text)
ip_learn = "\n" +list[0] 

# Vikipedi Rastgele Başlık

r = requests.get('https://tr.wikipedia.org/wiki/%C3%96zel:Rastgele' )
source = BeautifulSoup(r.content,"html.parser")
x = source.find_all("h1", attrs={"id":"firstHeading"})

list = []

for i in x:
    list.append(i.text)

vikipedi =  "\n" +list[0] 

# Argo Kelime Bildirimi
argo_list = ["piç", "amk","orospu"]

# Hava Durumu

steam = requests.get('https://www.mgm.gov.tr/tahmin/turkiye.aspx?g=1#sfB')
soup = BeautifulSoup(steam.content,"html.parser")

info_hava_1= soup.find('p', attrs={"class":"tiktik_guncelleme"})
info_hava_2 =  soup.find('p', attrs={"class":"tiktik_dikkat"})


@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    
    
    # Yardım Embed 
    if message.content == '!yardim':
        
        embed = discord.Embed(title=f"Merhaba , {message.author.name}",timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Spor : ", value="""⚽ Süper Lig : !superlig
                                                ⚽ Bundesliga Ligi : !bundesligalig
                                                ⚽ Piremier Lig : !premierlig
                                                🏀 ING BSL : !ing_bsl
                                                🏀 NBA Doğu : !nba_east
                                                🏀 NBA Batı : !nba_west                                
                                                """, inline=False)
        embed.add_field(name="Steam : ", value="""🕹️🎮 Ücretsiz Yeni Ve Popüler Oyunlar : !game_populer
                                                🕹️🎮 Steam Oyunları Ücretsiz Çok Satanlar : !game_free_cok
                                                🕹️🎮 Steam Oyunları Çok Satanlar : !game_cok
                                                🕹️🎮 Steam Oyunları Özel Fırsatlar : !game_ozel
                                                """, inline=False)
        embed.add_field(name="💵 Döviz : ", value="!doviz", inline=False)
        embed.add_field(name="League of Legends Oyun Geçmişi", value="!lol-<BÖLGE>-<NICK>", inline=False)
        embed.add_field(name="☀️ Hava Durumu :", value="!hava_durumu", inline=False)
        embed.add_field(name="Profiller : ", value="!github-<USERNAME>", inline=False)
        embed.add_field(name="Sunucu Bilgileri : ", value="!info", inline=False)
        embed.add_field(name="IP Adresiniz:", value="!ip_adresim", inline=False)
        embed.add_field(name="Şans Oyunu:", value="Yazı Tura : !yazi-tura \nZar Oyunu : !zar-at", inline=False)
        embed.add_field(name="Vikipedi Rastgele Konu:", value="!vikipedi", inline=False)
        embed.add_field(name="Kurallar : ", value="!rules", inline=False)
        embed.add_field(name="Yardım : ", value="!yardim", inline=False)
        file = discord.File("img/pp.png", filename="pp.png")
        embed.set_thumbnail(url="attachment://pp.png")
        embed.set_footer(text="Creator : Green Stable SS'M 👋") 
        await message.channel.send(file=file,embed=embed)
        
    # Kurallar Embed
    if message.content == '!rules':       
        
        embed = discord.Embed(title=f"Merhaba , {message.author.name}",timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        embed.add_field(name="Genel Kurallar : ", value="""  1- Küfür argo kelimeler yasak! (Mute veya süreli ban).
                                                        2- Dil din ırk ayrımı yapmak yasaktır (Direkt ban).
                                                        3- Yaşı küçük üyelerle dalga geçmek ayrımcılık yapmak yasak
                                                        4- Rol istemek yetki istemek yasak.
                                                        5- Dini tartışma yapmak yasak.
                                                        """, inline=False)
        
        embed.add_field(name="❗️⚠️", value="""   6- Tartışmak tartışma yaratmak veya tartışmaya dahil olmak yasak.
                                                        7- Admin ve yetkili üyelerine saygısızlık yapmak yasak.
                                                        8- 18+ paylaşımlar paylaşmak yasak cinsel içerikli kan intihar söylemli paylaşımlar yasaktır!
                                                        9- Reklam yapmak yasak özelden reklam yapanları bildirmenizi rica ediyoruz!
                                                        10- Küfür edip çıkmak ardından gene girmek yasak eğer girerse sınırsız ban atılır.
                                                        11- Özelden kız üyelerimize asılmak cinsel içerikli konuşmak yasak Direkt ban! 
                                                         
                                                        @everyone
                                                        """, inline=False)                                                
        file = discord.File("img/pp.png", filename="pp.png")
        embed.set_thumbnail(url="attachment://pp.png")
        embed.set_footer(text=" Creator : Green Stable SS'M 👋") 
        await message.channel.send(file=file,embed=embed)
    
    # Sunucu Hakkında Bilgi Embed
    if message.content == '!info':
        
        embed = discord.Embed(title=f"{message.guild.name}", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server Kuruluşu : ", value=f"{message.guild.created_at}", inline=False)
        embed.add_field(name="Server Sahibi", value=f"{message.guild.owner}", inline=False)
        embed.add_field(name="Server Bölgesi", value=f"{message.guild.region}", inline=False)
        embed.add_field(name="Server ID", value=f"{message.guild.id}", inline=False)
        file = discord.File("img/pp.png", filename="pp.png")
        embed.set_thumbnail(url="attachment://pp.png")
        
        await message.channel.send(file=file,embed=embed)
    
    # Github Profil Paylaşımı Embed
    if '!github-' in message.content:
        
        profile = str(message.content).replace("!github-", "")      
        r = requests.get('https://github.com/'+ profile +"/" )
        source = BeautifulSoup(r.content,"html.parser")
        
        pp = source.find_all("a", attrs={"itemprop":"image"})
        name = source.find_all("span", attrs={"class":"p-name vcard-fullname d-block overflow-hidden"})
        bio = source.find_all("div", attrs={"class":"p-note user-profile-bio mb-3 js-user-profile-bio f4"})
        fllw = source.find_all("span", attrs={"class":"text-bold text-gray-dark"})
        
        for i in pp :
            pp_ = i.get('href')

        for i in name:
            name_ = i.text
        
        for i in bio:
            bio_ = i.text
            
        if bio_ == "":
            bio_ = " Profil Bio Boş ... " 
        
        if name_ == "":
            name_ = " İsim Boş ... "
        
        list_follow = []
        
        for i in fllw:
            list_follow.append(i.text) 
            
        metin_fllw = "Takipçi Sayısı : "+ list_follow[0] + " \nTakip Edilen Sayısı : "+ list_follow[1] +" \nYıldız Sayısı : "+  list_follow[2] 

        embed=discord.Embed(title="GitHub Profili : " + message.author.name, timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        embed.set_thumbnail(url=pp_)
        embed.add_field(name="İsim : ", value=str(name_), inline=False)
        embed.add_field(name="Profile Bio : ", value=str(bio_), inline=False)
        embed.add_field(name="Daha Fazlası : ", value=metin_fllw, inline=False)
        embed.add_field(name="Link : ", value='https://github.com/'+ profile +"/", inline=False)
        embed.set_footer(text="Creator : Green Stable SS'M 👋")
        await message.channel.send(embed=embed)

    # Yazı - Tura
    if message.content == '!yazi-tura':  
        
        await message.channel.send("Para Atılıyor ...")
        
        time.sleep(5)
        
        x = random.randint(0,1)
        
        if x ==1:
            yazi_tura = "Yazi Kazandı"
        else:
            yazi_tura = "Tura Kazandı"
    
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/coin.gif", filename="coin.gif")
        embed.set_thumbnail(url="attachment://coin.gif")
        embed.add_field(name="Çıkan Sonuç : ", value=yazi_tura, inline=False)
        embed.set_footer(text=" Creator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)

    # Zar Oyunu
    if message.content == '!zar-at': 
        
        await message.channel.send("Zar Atılıyor ...")
        
        time.sleep(5)
        
        x = random.randint(1,6)
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/zar.png", filename="zar.png")
        embed.set_thumbnail(url="attachment://zar.png")
        embed.add_field(name="Çıkan Sonuç : ", value= x, inline=False)
        embed.set_footer(text=" Creator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)
        
    # IP Adresi Öğrenme
    if message.content == '!ip_adresim': 
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/ip.png", filename="ip.png")
        embed.set_thumbnail(url="attachment://ip.png")
        embed.add_field(name="IP Adresiniz : ", value=ip_learn, inline=False)
        embed.set_footer(text="Creator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)
        
    # Vikipedi Random Başlık
    if message.content == '!vikipedi': 
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/vikipedi.jpg", filename="vikipedi.jpg")
        embed.set_thumbnail(url="attachment://vikipedi.jpg")
        embed.add_field(name="Vikipedi Rastegele Başlık : ", value=vikipedi, inline=False)
        embed.set_footer(text="Wikipedia Sitesinden Rastgele Başlık Önerir. \nCreator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)
    
    # Argo Kelime Kullanımı Uyarısı
    for i in argo_list:
        
        kelime = str(i)
        
        if kelime in str(message.content).lower():
            
            embed = discord.Embed(title="Yanlış Kelime Kullanımı !!",timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
            file = discord.File("img/pp.png", filename="pp.png")
            embed.add_field(name="Yanlış Kelime Kullanan Kişi", value=f"{message.author.name}⛔✋", inline=False)
            embed.set_thumbnail(url="attachment://pp.png")
            await message.channel.send(file=file,embed=embed)
            
    # Döviz Embed
    if message.content == '!doviz':  
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=0x06db14)       
        file = discord.File("img/world.gif", filename="world.gif")
        embed.set_thumbnail(url="attachment://world.gif")
        embed.add_field(name="Döviz Kuru :", value=metin, inline=False)
        embed.add_field(name="Not :", value=" Anlık Değer Farkları Gerçekleşebilir ..", inline=False)
        embed.set_footer(text=" Creator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)
            
    # Süper Lig 
    if message.content == '!superlig':  
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/logo.jpg", filename="logo.jpg")
        embed.set_thumbnail(url="attachment://logo.jpg")
        embed.add_field(name="Güncel Fikstür Piremier Lig\n", value=superlig, inline=False)
        embed.set_footer(text=" İlk 15 Takım Görüntülenmektedir. \nCreator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)        
        
    # Premier Lig 
    if message.content == '!premierlig':  
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/logo.jpg", filename="logo.jpg")
        embed.set_thumbnail(url="attachment://logo.jpg")
        embed.add_field(name="Güncel Fikstür Süper Lig\n", value=premier, inline=False)
        embed.set_footer(text=" İlk 15 Takım Görüntülenmektedir. \nCreator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)
            
     # Bundesliga Ligi
    if message.content == '!bundesligalig': 
         
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/bundesliga.png", filename="bundesliga.png")
        embed.set_thumbnail(url="attachment://bundesliga.png")
        embed.add_field(name="Güncel Fikstür Bundesliga Lig\n", value=bundesliga, inline=False)
        embed.set_footer(text=" İlk 15 Takım Görüntülenmektedir. \nCreator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)         
      
    # ING BSL 
    if message.content == '!ing_bsl':  
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/ing.png", filename="ing.png")
        embed.set_thumbnail(url="attachment://ing.png")
        embed.add_field(name="Güncel Fikstür Bundesliga Lig\n", value=ing_bsl, inline=False)
        embed.set_footer(text=" İlk 15 Takım Görüntülenmektedir. \nCreator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)
   
    # NBA EAST
    if message.content == '!nba_east': 
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/nba.jpg", filename="nba.jpg")
        embed.set_thumbnail(url="attachment://nba.jpg")
        embed.add_field(name="Güncel Fikstür NBA Doğu\n", value=nba_east, inline=False)
        embed.set_footer(text=" İlk 15 Takım Görüntülenmektedir. \nCreator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)
   
    # NBA WEST   
    if message.content == '!nba_west':  
        
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        file = discord.File("img/nba.jpg", filename="nba.jpg")
        embed.set_thumbnail(url="attachment://nba.jpg")
        embed.add_field(name="Güncel Fikstür NBA Doğu\n", value=nba_west, inline=False)
        embed.set_footer(text=" İlk 15 Takım Görüntülenmektedir. \nCreator : Green Stable SS'M 👋")
        await message.channel.send(file=file,embed=embed)
        
    # Günlük Hava Durumu
    if message.content == '!hava_durumu': 
        
        await message.channel.send("https://www.mgm.gov.tr/FTPDATA/analiz/harita/png/haritatahmingun1.png")
        embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
        embed.add_field(name="Not : ", value=info_hava_1, inline=False)
        embed.add_field(name="Not : ", value=info_hava_2, inline=False)
        embed.set_footer(text="Creator : Green Stable SS'M 👋")
        await message.channel.send(embed=embed)

    # Ücretsiz Yeni Ve Popüler Oyunlar
    if message.content == '!game_populer':
        
        # Steam Oyunları Ücretsiz Yeni Ve Popüler Oyunlar

        steam = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/?l=turkish#p=0&tab=NewReleases')
        soup = BeautifulSoup(steam.content,"html.parser")
        
        game_img = soup.find_all('img', attrs={"class":"tab_item_cap_img"})
        game_name = soup.find_all("div", attrs={"class":"tab_item_name"})
        game_price = soup.find_all("div", attrs={"class":"discount_final_price"})
        game_link = soup.find_all('a', attrs={"class": ["tab_item","app_impression_tracked"," __web-inspector-hide-shortcut__"]})
        
        img_games = []
        name_games = []
        price_games = []
        link_games = []
        
        i = 0    
        for link in game_img:
            i +=1
            img_games.append(link.get('src'))
            if i == 10:
                break
        i = 0
        for link in game_name:
            i +=1
            name_games.append(link.text)
            if i == 10:
                break
        i = 0    
        for link in game_price:
            i +=1
            price_games.append(link.text)
            if i == 10:
                break
        i = 0    
        for link in game_link:
            i +=1
            link_games.append(link.get('href'))
            if i == 10:
                break
            
        s = 0
       
        await message.channel.send("Oyunlar Listeleniyor ...")
        time.sleep(5)
        
        for i in range(0,5):
            
            s += 1
            
            oyun_fotografi = img_games[i]   
            oyun_ismi = name_games[i]
            oyun_fiyati = price_games[i]
            oyun_linki = link_games[i]
            
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url=oyun_fotografi)
            embed.add_field(name= str(s) +") " +oyun_ismi, value="\nFiyat : " +oyun_fiyati + "\nOyun Linki : "+ oyun_linki , inline=False)
            embed.set_footer(text="Creator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)   
                    
    # Steam Oyunları Ücretsiz Çok Satanlar
    if message.content == '!game_free_cok':  
        
        # Steam Oyunları Ücretsiz Çok Satanlar
            
        steam = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/?l=turkish#p=0&tab=TopSellers')
        soup = BeautifulSoup(steam.content,"html.parser")
        
        game_img = soup.find_all('img', attrs={"class":"tab_item_cap_img"})
        game_name = soup.find_all("div", attrs={"class":"tab_item_name"})
        game_price = soup.find_all("div", attrs={"class":"discount_final_price"})
        game_link = soup.find_all('a', attrs={"class": ["tab_item","app_impression_tracked"," __web-inspector-hide-shortcut__"]})
        
        img_games = []
        name_games = []
        price_games = []
        link_games = []
        
        i = 0    
        for link in game_img:
            i +=1
            img_games.append(link.get('src'))
            if i == 10:
                break
        i = 0
        for link in game_name:
            i +=1
            name_games.append(link.text)
            if i == 10:
                break
        i = 0    
        for link in game_price:
            i +=1
            price_games.append(link.text)
            if i == 10:
                break
        i = 0    
        for link in game_link:
            i +=1
            link_games.append(link.get('href'))
            if i == 10:
                break
        s = 0
        
        await message.channel.send("Oyunlar Listeleniyor ...")
        time.sleep(5)
        
        for i in range(0,5):
            
            s += 1
            
            oyun_fotografi = img_games[i]   
            oyun_ismi = name_games[i]
            oyun_fiyati = price_games[i]
            oyun_linki = link_games[i]
            
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url=oyun_fotografi)
            embed.add_field(name= str(s) +") " +oyun_ismi, value="\nFiyat : " +oyun_fiyati + "\nOyun Linki : "+ oyun_linki , inline=False)
            embed.set_footer(text="Creator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)   
            
    # Steam Oyunları Çok Satanlar
    if message.content == '!game_cok':
        
        # Steam Oyunları Çok Satanlar
            
        steam = requests.get('https://store.steampowered.com/search/?filter=topsellers')
        soup = BeautifulSoup(steam.content,"html.parser")
        
        game_img = soup.find_all('img', attrs={"class":"tab_item_cap_img"})
        game_name = soup.find_all("div", attrs={"class":"tab_item_name"})
        game_price = soup.find_all("div", attrs={"class":"discount_final_price"})
        game_link = soup.find_all('a', attrs={"class": ["tab_item","app_impression_tracked"," __web-inspector-hide-shortcut__"]})
        
        img_games = []
        name_games = []
        price_games = []
        link_games = []
        
        i = 0    
        for link in game_img:
            i +=1
            img_games.append(link.get('src'))
            if i == 10:
                break
        i = 0
        for link in game_name:
            i +=1
            name_games.append(link.text)
            if i == 10:
                break
        i = 0    
        for link in game_price:
            i +=1
            price_games.append(link.text)
            if i == 10:
                break
        i = 0    
        for link in game_link:
            i +=1
            link_games.append(link.get('href'))
            if i == 10:
                break
        s = 0
        
        await message.channel.send("Oyunlar Listeleniyor ...")
        time.sleep(5)
        
        for i in range(0,5):
            
            s += 1
            
            oyun_fotografi = img_games[i]   
            oyun_ismi = name_games[i]
            oyun_fiyati = price_games[i]
            oyun_linki = link_games[i]
            
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url=oyun_fotografi)
            embed.add_field(name= str(s) +") " +oyun_ismi, value="\nFiyat : " +oyun_fiyati + "\nOyun Linki : "+ oyun_linki , inline=False)
            embed.set_footer(text="Creator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)     
     
    # Steam Oyunları Özel Fırsatlar
    if message.content == '!game_ozel':
        
        # Steam Oyunları Özel Fırsatlar
        
        steam = requests.get('https://store.steampowered.com/specials#tab=TopSellers')
        soup = BeautifulSoup(steam.content,"html.parser")
        
        game_img = soup.find_all('img', attrs={"class":"tab_item_cap_img"})
        game_name = soup.find_all("div", attrs={"class":"tab_item_name"})
        game_price = soup.find_all("div", attrs={"class":"discount_final_price"})
        game_link = soup.find_all('a', attrs={"class": ["tab_item","app_impression_tracked"," __web-inspector-hide-shortcut__"]})
        
        img_games = []
        name_games = []
        price_games = []
        link_games = []
        
        i = 0    
        for link in game_img:
            i +=1
            img_games.append(link.get('src'))
            if i == 10:
                break
        i = 0
        for link in game_name:
            i +=1
            name_games.append(link.text)
            if i == 10:
                break
        i = 0    
        for link in game_price:
            i +=1
            price_games.append(link.text)
            if i == 10:
                break
        i = 0    
        for link in game_link:
            i +=1
            link_games.append(link.get('href'))
            if i == 10:
                break
        s = 0
        
        await message.channel.send("Oyunlar Listeleniyor ...")
        time.sleep(5)
        
        for i in range(0,5):
            
            s += 1
            
            oyun_fotografi = img_games[i]   
            oyun_ismi = name_games[i]
            oyun_fiyati = price_games[i]
            oyun_linki = link_games[i]
            
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url=oyun_fotografi)
            embed.add_field(name= str(s) +") " +oyun_ismi, value="\nFiyat : " +oyun_fiyati + "\nOyun Linki : "+ oyun_linki , inline=False)
            embed.set_footer(text="Creator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)                                               
        
    # League of Legends Game History TR
    if '!lol-tr-' in message.content:
            
            profile = str(message.content).replace("!lol-tr-", "")      
            steam = requests.get('https://www.lolskill.net/summoner/TR/' +profile + '/matches')
            soup = BeautifulSoup(steam.content,"html.parser")
             
            mac_cha = soup.find_all('div' , {"class" : "kda tip text-center"})
            mac_cha_name = soup.find_all('div' , {"class" : "kda tip text-center"})
            mac_turu = soup.find_all('p' , {"class" : "text queue"})   
            mac_kda = soup.find_all('p' , {"class" : "value"})
  
            list = []
            list1= []      
            list3= []    
            list4= []
            
            for i in mac_kda:   
                list.append(i.text)
                
            for i in mac_turu:
                list1.append(i.text)
            
            for i in mac_cha:
                list3.append(i.get("data-champion-image"))
            
            for i in mac_cha_name:
                list4.append(i.get("data-champion-name"))     
            
            
            game_1 = "\nKarakter : " + list4[0] + "\nMaç Türü : " + list1[0] + "\nMaç Sonucu : " + list[0] +"\nKDA : " + list[1] + "\nOyun Süresi : " + list[2] 
            game_2 = "\n\nKarakter : " + list4[1] +"\nMaç Türü : " + list1[1] + "\nMaç Sonucu : " + list[3] +"\nKDA : " + list[4] + "\nOyun Süresi : " + list[5]
            game_3 = "\n\nKarakter : " + list4[2] +"\nMaç Türü : " + list1[2] + "\nMaç Sonucu : " + list[6] +"\nKDA : " + list[7] + "\nOyun Süresi : " + list[8]
            game_4 = "\n\nKarakter : " + list4[3] +"\nMaç Türü : " + list1[3] + "\nMaç Sonucu : " + list[9] +"\nKDA : " + list[10] + "\nOyun Süresi : " + list[11]
            game_5 = "\n\nKarakter : " + list4[4] +"\nMaç Türü : " + list1[4] + "\nMaç Sonucu : " + list[12] +"\nKDA : " + list[13] + "\nOyun Süresi : " + list[14]


            await message.channel.send("Maç Sonuçları Listeleniyor ...")
            time.sleep(5)    

            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[0])
            embed.add_field(name=profile + " Oyuncusunun Maç Sonucu : ", value=game_1, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)                                 

            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[1])
            embed.add_field(name= profile + " Oyuncusunun Maç Sonucu : ", value=game_2, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)
            
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[2])
            embed.add_field(name= profile + " Oyuncusunun Maç Sonucu : ", value=game_3, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)
                      
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[3])
            embed.add_field(name= profile + " Oyuncusunun Maç Sonucu : ", value=game_4, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)
                       
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[4])
            embed.add_field(name= profile + " Oyuncusunun Maç Sonucu : ", value=game_5, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)

    # League of Legends Game History EUROPE WEST
    if '!lol-west-' in message.content:
            
            profile = str(message.content).replace("!lol-tr-", "")      
            steam = requests.get('https://www.lolskill.net/summoner/WEST/' +profile + '/matches')
            soup = BeautifulSoup(steam.content,"html.parser")
             
            mac_cha = soup.find_all('div' , {"class" : "kda tip text-center"})
            mac_cha_name = soup.find_all('div' , {"class" : "kda tip text-center"})
            mac_turu = soup.find_all('p' , {"class" : "text queue"})   
            mac_kda = soup.find_all('p' , {"class" : "value"})
  
            list = []
            list1= []      
            list3= []    
            list4= []
            
            for i in mac_kda:   
                list.append(i.text)
                
            for i in mac_turu:
                list1.append(i.text)
            
            for i in mac_cha:
                list3.append(i.get("data-champion-image"))
            
            for i in mac_cha_name:
                list4.append(i.get("data-champion-name"))     
            
            
            game_1 = "\nKarakter : " + list4[0] + "\nMaç Türü : " + list1[0] + "\nMaç Sonucu : " + list[0] +"\nKDA : " + list[1] + "\nOyun Süresi : " + list[2] 
            game_2 = "\n\nKarakter : " + list4[1] +"\nMaç Türü : " + list1[1] + "\nMaç Sonucu : " + list[3] +"\nKDA : " + list[4] + "\nOyun Süresi : " + list[5]
            game_3 = "\n\nKarakter : " + list4[2] +"\nMaç Türü : " + list1[2] + "\nMaç Sonucu : " + list[6] +"\nKDA : " + list[7] + "\nOyun Süresi : " + list[8]
            game_4 = "\n\nKarakter : " + list4[3] +"\nMaç Türü : " + list1[3] + "\nMaç Sonucu : " + list[9] +"\nKDA : " + list[10] + "\nOyun Süresi : " + list[11]
            game_5 = "\n\nKarakter : " + list4[4] +"\nMaç Türü : " + list1[4] + "\nMaç Sonucu : " + list[12] +"\nKDA : " + list[13] + "\nOyun Süresi : " + list[14]


            await message.channel.send("Maç Sonuçları Listeleniyor ...")
            time.sleep(5)    

            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[0])
            embed.add_field(name=profile + " Oyuncusunun Maç Sonucu : ", value=game_1, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)                                 

            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[1])
            embed.add_field(name= profile + " Oyuncusunun Maç Sonucu : ", value=game_2, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)
            
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[2])
            embed.add_field(name= profile + " Oyuncusunun Maç Sonucu : ", value=game_3, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)
                      
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[3])
            embed.add_field(name= profile + " Oyuncusunun Maç Sonucu : ", value=game_4, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)
                       
            embed=discord.Embed(title="GAME BOT'", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())   
            embed.set_thumbnail(url="https:"+ list3[4])
            embed.add_field(name= profile + " Oyuncusunun Maç Sonucu : ", value=game_5, inline=False)
            embed.set_footer(text="Oynanan Son 5 Maç Listeleniştir \nCreator : Green Stable SS'M 👋")
            await message.channel.send(embed=embed)
                        
bot.run(TOKEN)           
            

