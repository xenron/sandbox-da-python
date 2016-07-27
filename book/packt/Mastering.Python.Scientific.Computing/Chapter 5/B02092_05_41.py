from scipy.io import netcdf
# file creation
f = netcdf.netcdf_file(’TestFile.nc’, ’w’)
f.history = ’Test netCDF File Creation’
f.createDimension(’age’, 12)
age = f.createVariable(’age’, ’i’, (’age’,))
age.units = ’Age of persons in Years’
age[:] = np.arange(12)
f.close()

#Now reading the file created  
f = netcdf.netcdf_file(’TestFile.nc’, ’r’)
print(f.history)
age = f.variables[’age’]
print(age.units)
print(age.shape)
print(age[-1])
f.close()