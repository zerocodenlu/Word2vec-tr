# Word2vec-tr
Word2veq in turkish

I trained the model based on wiki corpra on 2019.03.20:
https://dumps.wikimedia.org/trwiki/

After cleaning and preprocessing data, I used Gensim library to create Word2veq model: tr-word2veq-20190320
(You can download it via this link:
https://drive.google.com/file/d/1_J2Ix72Mo1PdS_FsDVUUM2ZtwLWvDvzG/view?usp=sharing).

The model trained on a 1764646 word types from a corpus of 77270207 raw words and 257016 sentences. It is 400 size vector for each word on 5 word window.

I created a jupeter notebook, so you can play arround the model. (the analogy function is collected from Satnford cs224 course material)



