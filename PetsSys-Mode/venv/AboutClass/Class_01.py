

class Student(object):

    def __init__(self,name='xiaomi',age=12):
        self.name=name
        self.age=age

    def is_studying(self,course_name):
        print("%s is studying %s"%(self.name,course_name))

    def watch_mv(self):
        if self.age>18:
            print('%s is watching 喜洋洋'%self.name)
        else:
            print('%s is watching 漫威'%self.name)



xiaowang=Student('xiaowang',18)

xiaowang.is_studying("art")

xiaowang.watch_mv()
