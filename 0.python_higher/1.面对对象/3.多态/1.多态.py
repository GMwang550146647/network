"""
由于python的鸭子类型，所以多态显得不太重要了
"""


class AudoFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename
        self.play()


class MP3File(AudoFile):
    ext = 'mp3'

    def play(self):
        print("Playing {} as mp3".format(self.filename))


class WavFile(AudoFile):
    ext = 'wav'

    def play(self):
        print("Playing {} as wav".format(self.filename))


class OggFile(AudoFile):
    ext = 'ogg'

    def play(self):
        print("Playing {} as ogg".format(self.filename))


if __name__ == '__main__':
    ogg = OggFile("myfile.ogg")
    mp3 = MP3File("myfile.mp3")
    wav = WavFile("myfile.wav")
    ddd = WavFile("myfile.mp3")
