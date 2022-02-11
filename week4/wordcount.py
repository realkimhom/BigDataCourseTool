from mrjob.job import MRJob
import re
from mrjob.step import MRStep

# \w match a-z A-Z 0-9
# \D mathch a-z A-Z
WORD_RE = re.compile(r"[\D']+")


class wordcount(MRJob):

    def mapper(self, _, line):
        for sentence in WORD_RE.findall(line):
            words = sentence.split(sep=', ')
            for word in words:
                yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)



if __name__ == '__main__':
    wordcount.run()
