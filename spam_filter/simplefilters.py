import basefilter
import random


class NaiveFilter(basefilter.BaseFilter):
    
    def test_one_mail(self, text):
        return "OK"


class ParanoidFilter(basefilter.BaseFilter):
    
    def test_one_mail(self, text):
        return "SPAM"


class RandomFilter(basefilter.BaseFilter):
    
    def test_one_mail(self, text):
        rand = random.randint(0, 1)
        return "SPAM" if rand else "OK"
