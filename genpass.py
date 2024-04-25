import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923", ":skull:"]
    return random.choice(emodji)


def flip_coin():
    coin = ["HEADS", "TAILS"]
    return random.choice(coin)

def gifsend():
    gifs = ["https://tenor.com/view/nobody-asked-6million-years-who-asked-fartic-gif-20339864", "https://tenor.com/view/thank-you-for-your-opinion-trash-can-trash-bin-garbage-gif-13363889255931521681", "https://tenor.com/view/who-asked-who-asked-meme-ok-and-mfs-who-use-who-asked-as-an-insult-yeah-i-use-who-asked-gif-26768500", "https://tenor.com/view/dont-care-didnt-ask-didnt-ask-invisible-meme-discord-invisible-image-gif-25053275", "https://tenor.com/view/who-asked-me-trying-to-find-who-asked-spongebob-spunch-bob-gif-22526294", "https://tenor.com/view/nerd-who-asked-gif-26495564", "https://tenor.com/view/spin-record-cat-gif-21749933", "https://tenor.com/view/yuh-uh-meme-funny-nuh-uh-gif-4499945910302690705", "https://tenor.com/view/nuh-uh-beocord-no-lol-gif-24435520", "https://tenor.com/view/social-credit-social-credit-score-credit-score-score-china-gif-23125701", "https://media.discordapp.net/attachments/1212456869138931784/1216484253668212866/image0.gif?ex=6625783f&is=6613033f&hm=cacd429ecc9f8844cd291a7de8a70a0dfac7ef3927be5da5cfe449672affab39&", "https://imgur.com/NQinKJB", "https://media.discordapp.net/attachments/897214984310911046/928732650401849384/mucha.gif?ex=662aafae&is=66183aae&hm=39aa3bf0e575bc0613a8b9640dc06133432f8dde1bb621c9c7fb46a853ae1339&", "https://tenor.com/view/spongebob-spongebob-cry-gif-20104177", "https://tenor.com/view/chips-potato-chips-spinning-gif-27138427"]
    return random.choice(gifs)