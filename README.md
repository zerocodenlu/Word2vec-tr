# Word2vec-tr
Word2veq in turkish

This is the updated model of this :https://github.com/akoksal

So, I trained the model based on wiki corpra on 2019.03.20:
https://dumps.wikimedia.org/trwiki/

After cleaning and preprocessing data, I used Gensim library to create Word2veq model: tr-word2veq-20190320
(You can access this model from my Google Drive).

The model trained on a 386351035 raw words (355290602 effective words). It is 400 size vector for each word on 5 word window.

I created a jupeter notebook, so you can play arround the model. (the analogy function is collected from Satnford cs224 course material)



