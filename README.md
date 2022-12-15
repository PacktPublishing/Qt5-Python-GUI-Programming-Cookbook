
### Get this product for $5

<i>Packt is having its biggest sale of the year. Get this eBook or any other book, video, or course that you like just for $5 each</i>


<b><p align='center'>[Buy now](https://packt.link/9781788831000)</p></b>


<b><p align='center'>[Buy similar titles for just $5](https://subscription.packtpub.com/search)</p></b>


# Qt5 Python GUI Programming Cookbook

<a href="https://www.packtpub.com/application-development/qt5-python-gui-programming-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781788831000 "><img src="https://d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/ppv4_main_book_cover/B09894_cover.png" alt="Qt5 Python GUI Programming Cookbook" height="256px" align="right"></a>

This is the code repository for [Qt5 Python GUI Programming Cookbook](https://www.packtpub.com/application-development/qt5-python-gui-programming-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781788831000 ), published by Packt.

**	Building responsive and powerful cross-platform applications with PyQt**

## What is this book about?
PyQt is one of the best cross-platform interface toolkits currently available; it's stable, mature, and completely native. If you want control over all aspects of UI elements, PyQt is what you need. This book will guide you through every concept necessary to create fully functional GUI applications using PyQt, with only a few lines of code.

This book covers the following exciting features:
Use basic Qt components, such as a radio button, combo box, and sliders 
Use QSpinBox and sliders to handle different signals generated on mouse clicks 
Work with different Qt layouts to meet user interface requirements 
Create custom widgets and set up customizations in your GUI 
Perform asynchronous I/O operations and thread handling in the Python GUI 
Employ network concepts, internet browsing, and Google Maps in UI 
Use graphics rendering and implement animation in your GUI 
Make your GUI application compatible with Android and iOS devices 

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1-788-83100-4) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoCalendar import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.calendarWidget.selectionChanged.connect
        (self.dispdate)
        self.show()
    def dispdate(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.
        selectedDate())
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
```

**Following is what you need for this book:**
If you’re an intermediate Python programmer wishing to enhance your coding skills by writing powerful GUIs in Python using PyQT, this is the book for you.

With the following software and hardware list you can run all code files present in the book (Chapter 1-13).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-8,10-12  | Python 3.5.0 | Windows, Mac OS X, and Linux (Any) |
| 1-8, 10-12 | PyQt5 version 5.6 | Windows, Mac OS X, and Linux (Any) |
| 9 | SQLite 3 | Windows, Mac OS X, and Linux (Any) |
| 9 | DB Browser for SQLite | Windows, Mac OS X, and Linux (Any) |
| 13 | QPython | Windows, Mac OS X, and Linux (Any) |
| 13 | Cython | Windows, Mac OS X, and Linux (Any) |
| 13 | Kivy | Windows, Mac OS X, and Linux (Any) |
| 13 | Oracle VM VirtualBox | Windows, Mac OS X, and Linux (Any) |
| 13 | Kivy Buildozer VM | Windows, Mac OS X, and Linux (Any) |
| 13 | XCode and libraries | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://www.packtpub.com/sites/default/files/downloads/Qt5PythonGUIProgrammingCookbook_ColorImages.pdf).

### Related products
* Computer Vision with OpenCV 3 and Qt5: Build visually appealing, multithreaded, cross-platform computer vision applications Paperback  – January 2, 2018  [[Packt]](https://www.amazon.com/Computer-Vision-OpenCV-multithreaded-cross-platform/dp/178847239X/ref=sr_1_1?ie=UTF8&qid=1532586055&sr=8-1&keywords=Computer+Vision+with+OpenCV+3+and+Qt5&dpID=51Z4u1hLAzL&preST=_SX218_BO1,204,203,200_QL40_&dpSrc=srch&utm_source=github&utm_medium=repository&utm_campaign=) [[Amazon]](https://www.amazon.com/dp/1-788-47239-X)

* Qt 5 Projects: Develop cross-platform applications with modern UIs using the powerful Qt framework Paperback  – February 23, 2018  [[Packt]](https://www.amazon.com/Qt-Projects-cross-platform-applications-framework/dp/1788293886/ref=sr_1_2_sspa?s=books&ie=UTF8&qid=1532586126&sr=1-2-spons&keywords=Qt+5+Projects&psc=1&utm_source=github&utm_medium=repository&utm_campaign=) [[Amazon]](https://www.amazon.com/dp/)

*  [[Packt]]() [[Amazon]](https://www.amazon.com/dp/)

*  [[Packt]]() [[Amazon]](https://www.amazon.com/dp/)

## Get to Know the Author
**BM Harwani**
is the founder and owner of Microchip Computer Education (MCE), based in Ajmer, India. He graduated with a BE in computer engineering from the University of Pune and also has a C level (masters diploma in computer technology) from DOEACC, Government of India. Having been involved in the teaching field for over 20 years, he has developed the art of explaining even the most complicated topics in a straightforward and easily understandable fashion. He is also a renowned speaker and the author of several books. To learn more, visit his blog, a site that helps programmers.

****
0

****
0

****
0

****
0

## Other books by the authors
[]()

[]()

[]()

[]()

[]()

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.


### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781788831000">https://packt.link/free-ebook/9781788831000 </a> </p>