# -*- coding: utf-8 -*-

import urllib
st = u'小姐,不凶'
st = st.encode('gb2312')
print st
s = urllib.quote(st)
print s  # %D0%A1%BD%E3%2C%B2%BB%D0%D7
# %D0%A1%BD%E3%A3%AC%B2%BB%D0%D7





