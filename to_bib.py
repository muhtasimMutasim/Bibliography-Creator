import csv
import sys

            
#Look up set Defualt
class BookRecord:
    #def __init__(self, author, title, publisher, publication_city, publiction_date, isbn):
    def __init__(self, **kwargs): #kwargs is a dictionary and you can take in key words
        self.isbn = kwargs.setdefault('id', None)
        #self.author = kwargs.setdefault('author')
        self.author = kwargs.setdefault('author', None)
        self.title = kwargs.setdefault('title', None)
        self.publisher = kwargs.setdefault('pub', None)
        self.city = kwargs.setdefault('place', None)
        self.date = kwargs.setdefault('year', None)
        self.language = kwargs.setdefault('lang', None)

    def fullName(self):
        all_names = []
        names = self.author.split(";")
        #print(names)
        for name in names:
            #return name
            #pass
            name = name.lstrip().split(" ")
            #return '{1} by {0}'.format((name[-1],name[:-1]), )#.lstrip()))
            self.author = '{0};'.format((name[-1],name[:-1])) #, self.title)
            self.author = self.author.replace("'", "", 10).replace("[", "", 10).replace("]", "", 10)
            all_names.append(self.author)
        self.author = all_names
        return self.author
    
    def title_Name(self):
        titlesWithAuthor = []
        #self.__str__ =
        #for names in self.author:
        title_name = '{0} by {1}'.format(self.title, self.author)
        title_name = title_name.replace("[", "", 10).replace("]", "", 10).replace("(", "", 10).replace(")","", 10)
        title_name = title_name.replace("[", "", 10).replace("'", "", 10).replace(";,", ";", 10)
        #title_name = title_name.replace("]\"('", "", 7)
        titlesWithAuthor.append(title_name)
        self.__str__ = titlesWithAuthor
        return(self.__str__)
        #print(title_name)
        #'{0} by {1}'.format(title, fullN)

    def bib(self):
        for author in self.author:    
            author = author.replace("[", "", 10).replace("]", "", 10).replace("(", "", 10).replace(")","", 10)
            author = author.replace("[", "", 10).replace("'", "", 10).replace(";,", ";", 10)
        bibligoraphy = "{0}. {1}. {2}: {3}. {4}".format(author, self.title, self.publisher, self.city, self.date)
        bibligoraphy = bibligoraphy.replace("[", "", 10).replace("]", "", 10).replace("(", "", 10).replace(")","", 10)
        bibligoraphy = bibligoraphy.replace("..",".", 10).replace(";.", ".", 10)
        return(bibligoraphy)
        
class BookList(list):
    def __init__(self, *args):
        #pass
        for row in args:
            br = BookRecord(**row)
            #self.append(br.title_Name())
            self.append(br.fullName())
            #br.title_Name()
            br.bib()
            
def main():
    #file = "C:/Users\mmuht\Desktop/INST326/Class Data/books.csv"
    PracticeFile ="C:/Users\mmuht\Desktop/INST326/Class Data/PracticeData.csv"
    with open(PracticeFile, "r") as f:
        raw = csv.DictReader(f)
        bl = BookList(*raw)
        bl.bib()

        
if __name__ == '__main__':
    main()
