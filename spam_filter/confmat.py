class BinaryConfusionMatrix():

    def __init__(self, pos_tag = "SPAM", neg_tag = "OK"):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
        self.TP = 0
        self.TN = 0
        self.FP = 0
        self.FN = 0


    def as_dict(self):
        eval = dict()
        eval["tp"] = self.TP
        eval["tn"] = self.TN
        eval["fp"] = self.FP
        eval["fn"] = self.FN
        return eval

    def update(self, truth, prediction):
        if (truth != self.neg_tag and truth != self.pos_tag) or \
        (prediction != self.neg_tag and prediction != self.pos_tag):
            raise ValueError
        
        if truth == self.pos_tag:
            if prediction == self.pos_tag:
                self.TP += 1
            else:
                self.FN += 1
        else:
            if prediction == self.pos_tag:
                self.FP += 1
            else:
                self.TN += 1

            
    def compute_from_dicts(self, truth_dict, pred_dict):
        for key in truth_dict.keys():
            self.update(truth_dict[key], pred_dict[key])
    