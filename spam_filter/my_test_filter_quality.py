import simplefilters
import quality
import os

filter = simplefilters.RandomFilter()

train_corpus = "spam-data-12-s75-h25/1"
test_corpus = "spam-data-12-s75-h25/2"

filter.train(train_corpus)
filter.test(test_corpus)

q = quality.compute_quality_for_corpus(test_corpus)
print(q)

path_to_pred = os.path.join(test_corpus, "!prediction.txt")
os.remove(path_to_pred)
