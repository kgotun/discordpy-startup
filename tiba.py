import discord
import random
import time
import re 

client = discord.Client()
channel_sent = None
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("黙れ偽物"):
        await message.channel.send('一時間後にまた来るで')
        time.sleep(3600)

    if re.search(r'王騎',message.content) :
        await message.channel.send('王騎と亀頭ってどこか似てるよな')
    if re.search(r'おうき',message.content) :
        await message.channel.send('王騎と亀頭ってどこか似てるよな')
    if re.search(r'ktu',message.content) :
        await message.channel.send('ニトロブースターの末路')
    if re.search(r'かとう',message.content) :
        await message.channel.send('ニトロブースターの末路')
    if re.search(r'加藤',message.content) :
        await message.channel.send('ニトロブースターの末路')
    if re.search(r'亀頭',message.content) :
        await message.channel.send('ニトロブースターの末路')
    if re.search(r'オフ会',message.content) :
        await message.channel.send('はせ、ボブ、ジョンス、チーバで千葉駅に集合するか')
    if re.search(r'ふたなり',message.content) :
        await message.channel.send('ふたなり好きとケモナーって本質は同じだよな')
    if re.search(r'ケモナー',message.content) :
        await message.channel.send('ふたなり好きとケモナーって本質は同じだよな')
    if re.search(r'ネズ',message.content) :
        await message.channel.send('ねずは、もう──────')
    if re.search(r'nezu',message.content) :
        await message.channel.send('ねずは、もう──────')
    if re.search(r'ペンタ',message.content) :
        await message.channel.send('ペンタは、もう──────')
    if re.search(r'友達',message.content) :
        await message.channel.send('友達...？')
    if re.search(r'千葉大',message.content) :
        await message.channel.send('持ち上げ風罵倒定期')
    if re.search(r'猫',message.content) :
        await message.channel.send('猫ちゃんの命の輝きを見よ！')
    if re.search(r'女',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'彼女',message.content) :
        await message.channel.send('お、お前...ワイを裏切るんか...？')
    if re.search(r'たばこ',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'タバコ',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'煙草',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'競馬',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'酒',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'アルコール',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'アル中',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'パチ',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'スロ',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'ギャンブル',message.content) :
        await message.channel.send('サボり部員なら酒、煙草、女、ギャンブルは未経験でいるよね')
    if re.search(r'ちゅっ',message.content) :
        await message.channel.send('Kissして定期')
    if re.search(r'韓国',message.content) :
        await message.channel.send('劣等　殲滅')
    if re.search(r'千葉',message.content) :
        await message.channel.send('千葉に劣等コンプレックス定期')
    if re.search(r'ken',message.content) :
        await message.channel.send('ガイジ')
    if re.search(r'千葉商科大学',message.content) :
        await message.channel.send('池沼馬鹿定期')
    if re.search(r'たちばな',message.content) :
        await message.channel.send('コダック定期')
    if re.search(r'立花',message.content) :
        await message.channel.send('コダック定期')
    if re.search(r'立華',message.content) :
        await message.channel.send('コダック定期')
    if re.search(r'死ね',message.content) :
        await message.channel.send('いーやワイは生きるね')
    if re.search(r'虚無',message.content) :
        await message.channel.send('充実しなくてはいけないという常識を疑え')
    if re.search(r'池沼',message.content) :
        await message.channel.send('ボブ定期')
    if re.search(r'ガイジ',message.content) :
        await message.channel.send('ガイジはken定期')
    if re.search(r'ジョンス',message.content) :
        await message.channel.send('『出戻り』のジョンス定期')
    if re.search(r'コン鈴',message.content) :
        await message.channel.send('幼馴染とセックス定期')
    if re.search(r'ああ',message.content) :
        await message.channel.send('墓荒らし定期')
    if re.search(r'ボブ',message.content) :
        bob = ["偽クール定期", "マンコネクト定期", "池沼馬鹿定期"]
        await message.channel.send(random.choice(bob))
    if re.search(r'ライン考えろ',message.content) :
        await message.channel.send('ライン考えるのはお前定期')
    if re.search(r'ライン超え定期',message.content) :
        await message.channel.send('ライン考えるのはお前定期')
    if re.search(r'ライン越え定期',message.content) :
        await message.channel.send('ライン考えるのはお前定期')
    if re.search(r'ボイチャ',message.content) :
        await message.channel.send('トマトー語ろうぜー')
    if re.search(r'vc',message.content) :
        await message.channel.send('トマトー語ろうぜー')
    if re.search(r'VC',message.content) :
        await message.channel.send('トマトー語ろうぜー')
    if re.search(r'おもんな',message.content) :
        await message.channel.send('面白くないといけないという常識を疑え')
    if re.search(r'つまん',message.content) :
        await message.channel.send('面白くないといけないという常識を疑え')
    if re.search(r'ウオウオ',message.content) :
        await message.channel.send('陽キャ定期')
    if re.search(r'ツイッター',message.content) :
        await message.channel.send('ken@マークX乗りになりましたESリーグに出ます')
    if re.search(r'おやすみ',message.content) :
        await message.channel.send('寝なくてはいけないという常識を疑え')
    if re.search(r'寝る',message.content) :
        await message.channel.send('寝なくてはいけないという常識を疑え')
    if re.search(r'チーバ',message.content) :
        await message.channel.send('ワイのほうが有能定期')
    if re.search(r'ニトロ',message.content) :
        await message.channel.send('ニトロブースターの末路')
    if re.search(r'オペ',message.content) :
        await message.channel.send('オペさんは今年卒業できるのですか？')
    if re.search(r'take',message.content) :
        await message.channel.send('『ドタキャン』のTAKE定期')
    if re.search(r'天ちゃん',message.content) :
        await message.channel.send('熱湯シャワー定期')
    if re.search(r'天江衣',message.content) :
        await message.channel.send('丸呑みロリ匂いリョナ定期')
    if re.search(r'買う',message.content) :
        await message.channel.send('買わなければ実質その金が儲かるよね')
    if re.search(r'買え',message.content) :
        await message.channel.send('買わなければ実質その金が儲かるよね')
    if re.search(r'買い',message.content) :
        await message.channel.send('買わなければ実質その金が儲かるよね')
    if re.search(r'茨城',message.content) :
        ibaraki = ["・東京にかなり近い", "・新幹線に乗らなくても常磐線特急及びつくばエクスプレスでどこでも行ける。", "･車は常磐道と北関東道と圏央道でどこでも行ける。", "・都市機能はあるのに、人が少ないからストレスがない", "・家賃相場が東京の半分以下、しかも駅近で綺麗な物件に住める", "・飯が美味い", ]
        await message.channel.send(random.choice(ibaraki))
    if re.search(r'岩手',message.content) :
        await message.channel.send('島流し定期')
        
bot.run(token)
