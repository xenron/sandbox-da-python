import numpy as np
rectype= np.dtype({'names':['mintemp', 'maxtemp', 'avgtemp', 'city'], 'formats':['i4','i4', 'f4', 'a30']})
a = np.array([(10, 44, 25.2, 'Indore'),(10, 42, 25.2, 'Mumbai'), (2, 48, 30, 'Delhi')],dtype=rectype)
print a[0]
print a[’mintemp’]
print a[’maxtemp’]
print a[’aavgtemp’]
print a['city']