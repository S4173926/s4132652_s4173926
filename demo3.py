import pyhtml
import student_a_level_1
import student_a_level_2
import student_a_level_3

import student_b_level_1
import student_b_level_2
import student_b_level_3

pyhtml.need_debugging_help=True

#All pages that you want on the site need to be added as below
pyhtml.MyRequestHandler.pages["/"]      =student_a_level_1
pyhtml.MyRequestHandler.pages["/page2a"]=student_a_level_2 
pyhtml.MyRequestHandler.pages["/page3a"]=student_a_level_3 
pyhtml.MyRequestHandler.pages["/page1b"]=student_b_level_1 
pyhtml.MyRequestHandler.pages["/page2b"]=student_b_level_2 
pyhtml.MyRequestHandler.pages["/page3b"]=student_b_level_3
#Host the site!
pyhtml.host_site()