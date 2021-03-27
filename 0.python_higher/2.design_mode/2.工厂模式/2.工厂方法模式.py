from abc import ABCMeta, abstractmethod

'''1.1.Abstract Creator'''


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


'''1.2.Concreate Creator'''


class PersonSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


'''2.1.Abstract Creator'''


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


'''2.2.Concrete Creator'''


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = input("Which Profile you'd want to create:\t")
    profile = eval(profile_type.lower())()
    print("Creating Profile ..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
