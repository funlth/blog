# coding:utf-8
from textblob import TextBlob

def analyze_sentiment(comment_text):
    '''
    使用 TextBlob 库将评论文本进行情感分析
    返回一个字典，包括极性和主观性分数
    '''
    blob = TextBlob(comment_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    result = {'polarity': polarity, 'subjectivity': subjectivity}
    return result