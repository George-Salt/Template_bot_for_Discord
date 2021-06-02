import discord
import random

client = discord.Client()

greetings = ["привет", "hello", "hi", "ку", "здарова", "здравствуй", "прив", "bonjour", "бонжур", "здравствуйте"]

kak = ["как поживаешь?","как поживаешь", "как тебе здесь", "как тебе сервер", "как тебе здесь?", "как тебе сервер?", "как дела?", "как дела", "как твои дела?", "как ваши дела?"]

ny = ["ну", "эй", "эй, бот", "бот", "ботяра", "ну, бот"]

otveti = ["Отлично!", "Все хорошо!", "Здорово!", "Все замечательно!", "Превосходно!"]

spisok_grustnih_otvetov = ["плохо", "ужасно", "очень плохо", "все плохо", "не очень", "(", ":(", "плохо!", "ужасно!", "очень плохо!", "все плохо!", "не очень!", "фигово", "фигово!"]

spisok_veselih_otvetov = ["та норм", "неподражаемо", "удовлетворительно", "хорошо", "норм", "нормально", "не плохо", "все хорошо", "отлично", "здорово", "превосходно", "восхитительно", "классно","офигенно", "прикольно", "супер", ":D", ")", "замечательно"]

imya = ["как тебя зовут?", "как тебя звать?", "как твое имя?", "можешь сказать свое имя?", "как тебя зовут", "как тебя звать", "как вас зовут", "как вас звать", "как вас зовут?", "как вас звать?", "как твое имя", "можешь сказать свое имя", "можете сказать свое имя", "можете сказать свое имя?"]

zan = ["Я читаю сообщения на нашем сервере", "Я смотрю видео на YouTube", "Я играю в Euro Truck Simulator 2", "Я разговариваю по Skype", "Я клею модель самолета", "Я играю в баскетбол с ботом по имени MEE6"]

chem = ["чем занимаешься?", "что делаешь?", "чем ты занят?", "чем занимаешься", "что делаешь", "чем ты занят"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    soobshenie = message.content

    if soobshenie.lower() in greetings:
        await message.channel.send(f' {message.author.mention} Привет!')

    if soobshenie.lower() in kak:
        otvet = random.randint(0,4)
        await message.channel.send(f' {message.author.mention} ' + otveti[otvet] + " Как у вас дела?")

    if soobshenie.lower() in spisok_veselih_otvetov:
        await message.channel.send(f' {message.author.mention} Очень рад за вас!')
        
    if soobshenie.lower() in spisok_grustnih_otvetov:
        await message.channel.send(f' {message.author.mention} Очень жаль!')
    
    if soobshenie.lower() in ny:
        await message.channel.send(f' {message.author.mention} Что?')

    if soobshenie.lower() in imya:
        await message.channel.send(f' {message.author.mention} Моё имя Salt Bot. Меня создал @George Salt#3733')

    if soobshenie.lower() in chem:
        otvet = random.randint(0,5)
        await message.channel.send(f' {message.author.mention} ' + zan[otvet])



client.run('NzQ4MTgzMDgwODcwODcxMTEy.X0Ztyw.aGMNdC_kE6XCxUBTsyVP9wkSqzA')
