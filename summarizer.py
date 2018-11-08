from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def summarizer(url, SENTENCES_COUNT=2):
   LANGUAGE = "english"
   # SENTENCES_COUNT = 1
   # url =  "https://sea.pcmag.com/smartphones/17424/apple-iphone-x"
   parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

   # text = ' '.join(text.split())
   # parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
   stemmer = Stemmer(LANGUAGE)

   summarizer = Summarizer(stemmer)
   summarizer.stop_words = get_stop_words(LANGUAGE)

   sentences = []
   for sentence in summarizer(parser.document, SENTENCES_COUNT):
      print(sentence)
      sentences.append(str(sentence))
   return sentences

# print(get_summarize("https://sea.pcmag.com/smartphones/17424/apple-iphone-x"))