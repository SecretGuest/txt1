# import re
# s='(kkkk(fl)alsk'
# ret=re.search('(?<=\()[^\)]+',s)
# print(ret.group())

import re
s='(kk(kk(fl)alsk'
ret=re.search('(?<=\()[^\)]+',s)
print(ret.group())


