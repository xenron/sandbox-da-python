# -*- coding: utf-8 -*-

# 1. 《Python自然语言分析》第11章课后习题：1,4

# 1. In Example 11-2 the new field appeared at the bottom of the entry. Modify this
# program so that it inserts the new subelement right after the lx field. (Hint: create
# the new cv field using Element('cv'), assign a text value to it, then use the
# insert() method of the parent element.)

# 在例11-2 中新字段出现在条目底部。修改这个程序使它就在lx 字段后面插入新的子
# 元素。（提示：使用Element('cv')创建新的cv 字段，分配给它一个文本值，然后使用
# 父元素的insert()方法。）

import re
import nltk
from nltk.etree.ElementTree import SubElement
from nltk.corpus import toolbox

def cv(s):
    s = s.lower()
    s = re.sub(r'[^a-z]', r'_', s)
    s = re.sub(r'[aeiou]', r'V', s)
    s = re.sub(r'[^V_]', r'C', s)
    return (s)
def add_cv_field(entry):
    for field in entry:
        if field.tag == 'lx':
            cv_field = SubElement(entry, 'cv')
            cv_field.text = cv(field.text)
lexicon = toolbox.xml('rotokas.dic')
add_cv_field(lexicon[53])

print nltk.to_sfm_string(lexicon[53])

# \lx kaeviro
# \ps V
# \pt A
# \ge lift off
# \ge take off
# \tkp go antap
# \sc MOTION
# \vx 1
# \nt used to describe action of plane
# \dt 03/Jun/2005
# \ex Pita kaeviroroe kepa kekesia oa vuripierevo kiuvu.
# \xp Pita i go antap na lukim haus win i bagarapim.
# \xe Peter went to look at the house that the wind destroyed.
# \cv CVVCVCV

# 4. Write a program to find any parts-of-speech (ps field) that occurred less than 10
# times. Perhaps these are typing mistakes?

# 写一个程序，找出所有出现少于10 次的词性（ps 字段）。或许有打字错误？



