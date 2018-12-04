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

output = '''Python for finance by 'Yan, Yuxing;'
Learn to program with Minecraft® : transform your world with the power of Python by 'Richardson, Craig;'
Foundations of Python network programming : the comprehensive guide to building network applications with Python by 'Rhodes, Brandon;', 'Goerzen, John;'
Internet programming with Python by 'Watters, Aaron;', 'Rossum, Guido, Van;', 'Ahlstrom, James, C;'
Python natural language processing : explore NLP with machine learning and deep learning techniques by 'Thanaki, Jalaj;'
An introduction to programming using Python by 'Schneider, David, I;'
Mastering Object-oriented Python by 'Lott, Steven, F, ;'
Django 1.1 testing and debugging : building rigorously tested and bug-free Django applications by 'Tracey, Karen, Marie;'
OpenCV Computer Vision with Python by 'Howse, Joseph;'
Python tools for Visual Studio : leverage the power of the Visual Studio IDE to develop better and more efficient Python projects by 'Sabia, Martino;', 'Wang, Cathy;'
The Python language reference manual : for Python version 3.2 by 'Rossum, Guido, Van;', 'Drake, Fred, L;'
Python Scripting for ArcGIS. by 'Zandbergen, Paul, A;'
Python testing beginner's guide by 'Arbuckle, Daniel;'
Parallel programming with Python : develop efficient parallel systems using the robust Python environment by 'Palach, Jan;'
Foundations of agile Python development by 'Younker, Jeff;'
Help your kids with computer coding : a unique step-by-step visual guide, from binary code to building games by 'Vorderman, Carol;', 'Woodcock, Jon;', 'McManus, Sean;', 'Steele, Craig;', 'Quigley, Claire;', 'McCafferty, Daniel;'
Python data analysis : learn how to apply powerful data analysis techniques with popular open source Python modules by 'Idris, Ivan;'
Python for software design : how to think like a computer scientist by 'Downey, Allen;'
Python for bioinformatics by 'Bassi, Sebastian;'
Program arcade games : with Python and Pygame by 'Craven, Paul, Vincent;'
Learning OpenCV 3 computer vision with Python : unleash the power of computer vision with Python using OpenCV by 'Minichino, Joe;', 'Howse, Joseph;'
Python and Tkinter programming by 'Grayson, John, E;'
Python Web programming by 'Holden, Steve;', 'Beazley, David, M;'
Foundations of Python network programming by 'Rhodes, Brandon;', 'Goerzen, John;'
Deep learning for natural language processing : creating neural networks with Python by 'Goyal, Palash;', 'Pandey, Sumit;', 'Jain, Karan;'
Python : the complete reference by 'Brown, Martin, C;'
Python for kids for dummies by 'Scott, Brendan;'
Pro Android Python with SL4A by 'Ferrill, Paul;'
Mastering Python Forensics. by 'Spreitzenbarth, Dr., Michael;', 'Uhrmann, Dr., Johann;'
Blender 2.49 scripting : extend the power and flexibility of Blender with the help of Python, a high-level, easy-to-learn scripting language by 'Anders, Michel;'
Programming with Python by 'Padmanabhan, Tattamangalam, R;'
Python forensics : a workbench for inventing and sharing digital forensic technology by 'Hosmer, Chet;'
Learning robotics using Python : design, simulate, program, and prototype an autonomous mobile robot using ROS, OpenCV, PCL, and Python by 'Joseph, Lentin;'
The practice of computing using Python by 'Punch, W, F;', 'Enbody, Richard, J;'
Programming with Python by 'Altom, Tim;', 'Chapman, Mitch;'
Python for Unix and Linux system administration by 'Gift, Noah;', 'Jones, Jeremy;'
Discovering computer science : interdisciplinary problems, principles, and Python programming by 'Havill, Jessen;'
High performance Python by 'Gorelick, Micha;', 'Ozsvald, Ian;'
Python testing cookbook : over 70 simple but incredibly effective recipes for taking control of automated testing using powerful Python testing tools by 'Turnquist, Greg, Lee;'
Head first programming : a learner's guide to programming using the Python language by 'Barry, Paul;', 'Griffiths, David;'
Text processing in Python by 'Mertz, David;'
Python for experimental psychologists by 'Dalmaijer, Edwin, S;'
Object-oriented programming in Python by 'Goldwasser, Michael, H;', 'Letscher, David;'
Applied natural language processing with Python : implementing machine learning and deep learning algorithms for natural language processing by 'Beysolow, Taweh;'
Practical data science cookbook : 89 hands-on recipes to help you complete real-world data science projects in R and Python by 'Ojeda, Tony;', 'Murphy, Sean, Patrick;', 'Bengfort, Benjamin;', 'Dasgupta, Abhijit;'
>>>  '''

