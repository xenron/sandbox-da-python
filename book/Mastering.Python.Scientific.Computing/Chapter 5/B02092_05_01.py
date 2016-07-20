import numpy as np
x2d = np.array( ((100,200,300), (111,222,333), (123,456,789)) )
x2d.shape # Output:(3L, 3L)
x2d.dtype # Output:dtype('int32')
x2d.size # Output:9
x2d.itemsize # Output:4
x2d.ndim # Output:2
x2d.data # Output:<read-write buffer for 0x00000000031B9990, size 36, offset 0 at 0x0000000001CE19D0>
