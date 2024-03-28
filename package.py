#Package is nothing it is just a directory or folder which must contain a special fiel called __init__.py

#__init__.py can be empty, presence of this file in any directory shows that it contains a python package, so it can be importe the samw way as we do python module.
#so, how we import package .
#just as module.
#like import packagename.filename
#or from packagename.subpackagename.filename import function/class
#but above importing will be failed, becuase __init__.py file inside package should have list named as __all__
#so, what is it?
#it is taken to be the list of modules names that should be imported when from package import* is encountered.
#__al__=['dashboardfile','servicefile','productfile.'] #these all are vaailable inside that package 
#done 