# -*- coding: utf-8 -*-
import nltk

##语料库结构研究
phonetic = nltk.corpus.timit.phones('dr1-fvmh0/sa1')
phonetic

nltk.corpus.timit.word_times('dr1-fvmh0/sa1')

timitdict = nltk.corpus.timit.transcription_dict()
timitdict['greasy'] + timitdict['wash'] + timitdict['water']

phonetic[17:30]

nltk.corpus.timit.spkrinfo('dr1-fvmh0')

##语料库的生命周期
s1 = "00000010000000001000000"
s2 = "00000001000000010000000"
s3 = "00010000000000000001000"
nltk.windowdiff(s1, s1, 3)

nltk.windowdiff(s1, s2, 3)

nltk.windowdiff(s2, s3, 3)


##数据采集
import re
legal_pos = set(['n', 'v.t.', 'v.i.', 'adj', 'det'])
pattern = re.compile(r"'font-size:11.0pt'>([a-z.]+)<")

document = open("d:/data/dict.htm").read()
used_pos = set(re.findall(pattern, document))
illegal_pos = used_pos.difference(legal_pos)
print(list(illegal_pos))


from bs4 import BeautifulSoup

def lexical_data(html_file):
    SEP = '_ENTRY'
    html = open(html_file).read()
    html = re.sub(r'<p', SEP + '<p', html)
    text = BeautifulSoup(html,"lxml").get_text()
    text = ' '.join(text.split())
    for entry in text.split(SEP):
        if entry.count(' ') > 2:
            yield entry.split(' ', 3)
            
import csv
file=open("d:/data/dict1.csv", "w")
writer = csv.writer(file)
writer.writerows(lexical_data("d:/data/dict.htm"))   
file.close()
      


import csv
lexicon = csv.reader(open('d:/data/dict.csv'))
pairs = [(lexeme, defn) for (lexeme, _, _, defn) in lexicon]
lexemes, defns = zip(*pairs)
defn_words = set(w for defn in defns for w in defn.split())
sorted(defn_words.difference(lexemes))


idx = nltk.Index((defn_word, lexeme) 
                    for (lexeme, defn) in pairs
                     for defn_word in nltk.word_tokenize(defn) 
                     if len(defn_word) > 3) 
with open("dict.idx", "w") as idx_file:
        for word in sorted(idx):
            idx_words = ', '.join(idx[word])
            idx_line = "{}: {}".format(word, idx_words) 
            print(idx_line)


##使用XML
merchant_file = nltk.data.find('corpora/shakespeare/merchant.xml')
raw = open(merchant_file).read()
print(raw[:163])
print(raw[1789:2006])        

from xml.etree.ElementTree import ElementTree
merchant = ElementTree().parse(merchant_file)
merchant

merchant[0]

merchant[0].text

merchant.getchildren()


merchant[-2][0].text
merchant[-2][1]
merchant[-2][1][0].text
merchant[-2][1][54]
merchant[-2][1][54][0]
merchant[-2][1][54][0].text
merchant[-2][1][54][1]
merchant[-2][1][54][1].text


for i, act in enumerate(merchant.findall('ACT')):
     for j, scene in enumerate(act.findall('SCENE')):
         for k, speech in enumerate(scene.findall('SPEECH')):
             for line in speech.findall('LINE'):
                 if 'music' in str(line.text):
                     print("Act %d Scene %d Speech %d: %s" % (i+1, j+1, k+1, line.text))

from collections import Counter
speaker_seq = [s.text for s in merchant.findall('ACT/SCENE/SPEECH/SPEAKER')]
speaker_freq = Counter(speaker_seq)
top5 = speaker_freq.most_common(5)
top5                     
                     
from collections import defaultdict
abbreviate = defaultdict(lambda: 'OTH')
for speaker, _ in top5:
     abbreviate[speaker] = speaker[:4]

speaker_seq2 = [abbreviate[speaker] for speaker in speaker_seq]
cfd = nltk.ConditionalFreqDist(nltk.bigrams(speaker_seq2))
cfd.tabulate()                     


from nltk.corpus import toolbox
lexicon = toolbox.xml('rotokas.dic')

lexicon[3][0]
lexicon[3][0].tag
lexicon[3][0].text

[lexeme.text.lower() for lexeme in lexicon.findall('record/lx')]
 
import sys
from nltk.util import elementtree_indent
from xml.etree.ElementTree import ElementTree
elementtree_indent(lexicon)
tree = ElementTree(lexicon[3])
tree.write(sys.stdout, encoding='utf-8')


html = "<table>\n"
for entry in lexicon[70:80]:
    lx = entry.findtext('lx')
    ps = entry.findtext('ps')
    ge = entry.findtext('ge')
    html += "  <tr><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (lx, ps, ge)
html += "</table>"
print(html)


##使用Toolbox数据
from nltk.corpus import toolbox
lexicon = toolbox.xml('rotokas.dic')
sum(len(entry) for entry in lexicon) / len(lexicon)

from xml.etree.ElementTree import SubElement

def cv(s):
    s = s.lower()
    s = re.sub(r'[^a-z]',     r'_', s)
    s = re.sub(r'[aeiou]',    r'V', s)
    s = re.sub(r'[^V_]',      r'C', s)
    return (s)

def add_cv_field(entry):
    for field in entry:
        if field.tag == 'lx':
            cv_field = SubElement(entry, 'cv')
            cv_field.text = cv(field.text)
            
lexicon = toolbox.xml('rotokas.dic')
add_cv_field(lexicon[53])
print(nltk.toolbox.to_sfm_string(lexicon[53]))        


from collections import Counter
field_sequences = Counter(':'.join(field.tag for field in entry) for entry in lexicon)
field_sequences.most_common()    

grammar = nltk.CFG.fromstring('''
  S -> Head PS Glosses Comment Date Sem_Field Examples
  Head -> Lexeme Root
  Lexeme -> "lx"
  Root -> "rt" |
  PS -> "ps"
  Glosses -> Gloss Glosses |
  Gloss -> "ge" | "tkp" | "eng"
  Date -> "dt"
  Sem_Field -> "sf"
  Examples -> Example Ex_Pidgin Ex_English Examples |
  Example -> "ex"
  Ex_Pidgin -> "xp"
  Ex_English -> "xe"
  Comment -> "cmt" | "nt" |
  ''')

def validate_lexicon(grammar, lexicon, ignored_tags):
    rd_parser = nltk.RecursiveDescentParser(grammar)
    for entry in lexicon:
        marker_list = [field.tag for field in entry if field.tag not in ignored_tags]
        if list(rd_parser.parse(marker_list)):
            print("+", ':'.join(marker_list))
        else:
            print("-", ':'.join(marker_list))
            
lexicon = toolbox.xml('rotokas.dic')[10:20]
ignored_tags = ['arg', 'dcsv', 'pt', 'vx'] 
validate_lexicon(grammar, lexicon, ignored_tags)          


grammar = r"""
      lexfunc: {<lf>(<lv><ln|le>*)*}
      example: {<rf|xv><xn|xe>*}
      sense:   {<sn><ps><pn|gv|dv|gn|gp|dn|rn|ge|de|re>*<example>*<lexfunc>*}
      record:   {<lx><hm><sense>+<dt>}
    """  
    
from xml.etree.ElementTree import ElementTree
from nltk.toolbox import ToolboxData
db = ToolboxData()
db.open(nltk.data.find('corpora/toolbox/iu_mien_samp.db'))
lexicon = db.parse(grammar, encoding='utf8')
tree = ElementTree(lexicon)
with open("iu_mien_samp.xml", "wb") as output:
    tree.write(output)    