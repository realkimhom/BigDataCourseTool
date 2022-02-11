
from mrjob.job import MRJob

class MRmyjob(MRJob):
    def mapper(self,_,line):
        data = line.split(", ")
        if len(data)>=2:
            age = data[0].strip()
            yield None, age

    def reducer(self,_,list_of_values):
        # 这里求的不是个数，是全部的和
        a =[int(i) for i in list_of_values]
        sum_a = sum(a)
        lenght_a = len(a)
        yield "average:", float(sum_a)/lenght_a

if __name__ == '__main__':
    MRmyjob.run()