from mrjob.job import MRJob

class MRmyjob(MRJob):
    def mapper(self,_,line):
        data = line.split(", ")
        if len(data)>=2:
            age = data[0].strip()
            workclass = data[1].strip()
            # if len(workclass) >1:
            yield workclass, age

    def reducer(self,work_class,list_of_values):
        # 这里求的不是个数，是全部的和
        a =[int(i) for i in list_of_values]
        sum_a = sum(a)
        average_a = float(sum_a)/len(a)
        yield work_class, average_a

if __name__ == '__main__':
    MRmyjob.run()