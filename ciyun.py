import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud


# 1.读入txt文本数据
# 
text = open(r'test.txt', "r", encoding='utf-8').read()
cut_text = jieba.cut(text)
result = " ".join(cut_text)
wc = WordCloud(
    font_path = 'C:/Windows/Font/simfang.ttf',
    background_color='white',
    width=500,
    height=350,
    max_font_size=50,
    min_font_size=10,
    mode='RGBA'
)
wc.generate(result)
wc.to_file(r"wordcloud.png")
plt.figure("jay")
plt.imshow(wc)
plt.axis("off")
plt.show()