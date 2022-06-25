import os, sys
try:
    __import__("sparrow").tlisensi()
except Exception as e:
    exit(str(e))