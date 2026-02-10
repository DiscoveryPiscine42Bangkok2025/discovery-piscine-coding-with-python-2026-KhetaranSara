import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(keyword, text)
    if len(matches) > 0:
        print(len(matches))
    else:
        print("none")
else:
    print("none")