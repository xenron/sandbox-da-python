/* The code below shows how to use C-API provided by Python and NumPy */
/*
Author: Tanmay Dutta
Rev: 1.1
  Header Segment
*/

#include <Python.h>
#include <numpy/arrayobject.h>
#include <math.h>



/*
  Implementation of the actual C funtions
*/

static PyObject* square_func(PyObject* self, PyObject* args)
{
    double value;
    double answer;

    /*  parse the input, from python float to c double */
    if (!PyArg_ParseTuple(args, "d", &value))
        return NULL;
    /* if the above function returns -1, an appropriate Python exception will
     * have been set, and the function simply returns NULL
     */

    /* call cos from libm */
    answer = value*value;

    /*  construct the output from cos, from c double to python float */
    return Py_BuildValue("f", answer);
}

// Implemenation of square of numpy array

static PyObject* square_nparray_func(PyObject* self, PyObject* args)
{

  // variable declarations
    PyArrayObject *in_array;
    PyObject      *out_array;
    NpyIter *in_iter;
    NpyIter *out_iter;
    NpyIter_IterNextFunc *in_iternext;
    NpyIter_IterNextFunc *out_iternext;

    // Parse the argument tuple by specifying type "object" and putting the reference in in_array
    if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &in_array))
      {
	printf("Can not parse argument with format type O!. Probably passed object is not a python object ? ");
        return NULL;
      }
    // Construct the output from the new constructed input array 
    out_array = PyArray_NewLikeArray(in_array, NPY_ANYORDER, NULL, 0);
    // Test it and if the input is nothing then just return nothing. 
    if (out_array == NULL)
      {
	printf("failed while creating output array");
        return NULL;
      }
    //  Create the iterators 
    in_iter = NpyIter_New(in_array, NPY_ITER_READONLY, NPY_KEEPORDER,
                             NPY_NO_CASTING, NULL);

    //
    if (in_iter == NULL)
      // remove the ref and return null
      {
	printf("failed whilte creating the iterators for input array -- contact library developer ---");
        Py_XDECREF(out_array);
        return NULL;
      } 

    out_iter = NpyIter_New((PyArrayObject *)out_array, NPY_ITER_READWRITE,
                          NPY_KEEPORDER, NPY_NO_CASTING, NULL);

    if (out_iter == NULL) {
        NpyIter_Deallocate(in_iter);
        Py_XDECREF(out_array);
        return NULL;
	
    }

    in_iternext = NpyIter_GetIterNext(in_iter, NULL);
    out_iternext = NpyIter_GetIterNext(out_iter, NULL);
    if (in_iternext == NULL || out_iternext == NULL) {
        NpyIter_Deallocate(in_iter);
        NpyIter_Deallocate(out_iter);
        Py_XDECREF(out_array);
        return NULL;
	//        goto fail;
    }
    double ** in_dataptr = (double **) NpyIter_GetDataPtrArray(in_iter);
    double ** out_dataptr = (double **) NpyIter_GetDataPtrArray(out_iter);
    double val = 0 ;
    /*  iterate over the arrays */
    do {
      **out_dataptr =pow(**in_dataptr,2);
    } while(in_iternext(in_iter) && out_iternext(out_iter));

    /*  clean up and return the result */
    NpyIter_Deallocate(in_iter);
    NpyIter_Deallocate(out_iter);
    Py_INCREF(out_array);
    return out_array;

}



/*
  Method array structure definition
*/
static PyMethodDef Api_methods[] =
{
     {"py_square_func", square_func, METH_VARARGS, "evaluate the squares"},
     {"np_square",  square_nparray_func, METH_VARARGS,  "evaluates the square in numpy array"},
     {NULL, NULL, 0, NULL}
};


/*
  Initialization module
*/

PyMODINIT_FUNC
initnumpy_api_demo(void)
{
  (void)Py_InitModule3("numpy_api_demo", Api_methods,
		      "A demo to show Python and Numpy C-API");
   import_array();
}


