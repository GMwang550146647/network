"""
由于python的鸭子类型，所以多态显得不太重要了
"""


class AudoFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename
        # self.play()


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


class MyClass():
    def play(self):
        print("This is my class do whatever I want!")


if __name__ == '__main__':
    # 1.多态！ 他们都继承自一个类！所以相同类型的变量就能装一起！
    ogg = OggFile("myfile.ogg")
    mp3 = MP3File("myfile.mp3")
    wav = WavFile("myfile.wav")
    movies = [ogg, mp3, wav]
    for moviei in movies:
        moviei.play()

    #2.鸭子类型！ 不要求继承自一个类，只需要他们有同一个属性或者方法就行了！
    mc=MyClass()
    movies.append(mc)
    for moviei in movies:
        moviei.play()
