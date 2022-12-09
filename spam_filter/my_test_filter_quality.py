import filter
import quality
import os

filter = filter.MyFilter()



train_corpus = "spam-data-12-s75-h25/1"
test_corpus = "spam-data-12-s75-h25/2"



filter.train(train_corpus)
filter.test(test_corpus)

print("\n\n\nQUALITY IS ", end="") #DEBUG
q = quality.compute_quality_for_corpus(test_corpus)
print("{:.2f}".format(q))

path_to_pred = os.path.join(test_corpus, "!prediction.txt")
os.remove(path_to_pred)
