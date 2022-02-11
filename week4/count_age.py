from mrjob.job import MRJob
import re
from mrjob.step import MRStep

# \w match a-z A-Z 0-9
# \D mathch a-z A-Z
# WORD_RE = re.compile(r"[\D']+")


class wordcount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        words = line.split(sep=', ')
        yield words[0],1


    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    wordcount.run()