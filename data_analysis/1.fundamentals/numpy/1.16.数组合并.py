import numpy as np
arr=np.arange(20).reshape(4,5)
result=np.concatenate([arr,arr,arr],axis=1)
print(result)
result=np.concatenate([arr,arr,arr],axis=0)
print(result)