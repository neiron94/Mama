import os
import utils
import confmat

def quality_score(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + 10 * fp + fn)


def compute_quality_for_corpus(corpus_dir):
    truth_path = os.path.join(corpus_dir, "!truth.txt")
    predict_path = os.path.join(corpus_dir, "!prediction.txt")

    truth_dict = utils.read_classification_from_file(truth_path)
    predict_dict = utils.read_classification_from_file(predict_path)

    cm = confmat.BinaryConfusionMatrix()
    cm.compute_from_dicts(truth_dict, predict_dict)
    
    quality = quality_score(cm.TP, cm.TN, cm.FP, cm.FN)

    return quality
