#!/usr/bin/env python3

import random
print("Content-Type: text/html")
print("")

no=random.randint(1,6)

print("""
<html>
<head><title>Dice</title></head>
<body>
<h1>{num}</h1>

</body>
</html>
""".format(num=no))
