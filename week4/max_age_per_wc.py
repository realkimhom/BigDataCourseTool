from mrjob.job import MRJob
import re
from mrjob.step import MRStep



class wordcount(MRJob):

    # def steps(self):
    #     return [
    #         MRStep(mapper=self.mapper,
    #                reducer=self.reducer_1),
    #         MRStep(reducer = self.reducer_2)
    #
    #     ]
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_1)

        ]

    def mapper(self, _, line):
        data = line.split(sep=', ')
        if len(data)>=2:
            age = data[0].strip()
            work_class = data[1].strip()
            # if len(workclass) >1:
            yield (work_class, age),1

    def reducer_1(self, work_class_and_age, frequency):
        yield work_class_and_age[0],(sum(frequency),work_class_and_age[1])


    def reducer_2(self,class_name,frequency_and_age):
        age_frequency = [(int(x[1]),x[0]) for x in frequency_and_age]
        age_frequency = sorted(age_frequency,key=lambda x:x[0],reverse=True)
        yield class_name,age_frequency[0]


if __name__ == '__main__':
    wordcount.run()