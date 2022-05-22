from tinvest_robot_perevalov.news_fetcher import _init_sentiment_analyzer
    
def test_init_sentiment_analyzer():
    sentiment_analyzer = _init_sentiment_analyzer()
    assert 'negative' == sentiment_analyzer.predict_sentiment("Very bad news")
    assert 'positive' == sentiment_analyzer.predict_sentiment("The best news ever")
