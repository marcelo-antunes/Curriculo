import numpy as np
from wordcloud import WordCloud

text = "resiliência ética aprendizado maturidade diversidade respeito comprometimento coragem foco"

x, y = np.ogrid[:600, :600]
mask = (x - 300) ** 2 + (y - 300) ** 2 > 300 ** 2
mask = 255 * mask.astype(int)

wc = WordCloud(mode="RGBA", background_color="rgba(0,0,0,0)", colormap="tab20", repeat=True, mask=mask)
wc.generate(text)
wc.to_file('./img/words.png')