#Iteration
# Paython-da "class" iterable olmadigi ucun, dongu yaratmaq ucun __iter__ ve __next__ funksiyalarini yaratmaliyiq

class Course():
    def __init__(self,course_list):
        self.course_list = course_list # Course Listimiz
        self.index = -1 # Index
        
    def __iter__(self):
        return self # iter funksiyasini cagiririq

    def __next__(self): # next funksiyasini çağiririq.
        self.index += 1
        if (self.index < len(self.course_list)):
            return self.course_list[self.index]
        else:
            self.index = -1
            raise StopIteration

element = Course(["Puython","Java","C#","Js"]) # Object'imizi yaradiriq.
 
for i in element:
    print(i)


 