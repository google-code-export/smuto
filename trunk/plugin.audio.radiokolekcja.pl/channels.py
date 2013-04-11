CHANNELS = list()

class Channel(object):
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

        CHANNELS.append(self)


Channel(1, 'Radio Eska Rock', 'http://lodz.radio.pionier.net.pl:8000/pl/eskarock.mp3')
Channel(2, 'Roxy FM', 'http://szczecin.radio.pionier.net.pl:8000/pl/roxyfm.ogg')
