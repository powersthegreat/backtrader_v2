import sys

sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\storage')
import storage_1

storage = storage_1.Storage()
try:
    storage.move()
except TypeError as e:
    print("No new files to move to storage.")