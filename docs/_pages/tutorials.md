---
title: Tutorials
id: Units
header:
  image: "/assets/images/00-unit-splash.jpg"
  caption: 'Photo: [**Environmental Informatics Marburg**](https://www.flickr.com/environmentalinformatics-marburg/)'

permalink: /tutorials.html
sidebar:
  nav: "units"
---

## Where you can download test pictures of a book 
You can download pictures from the Pakistan books [here](http://digitizer.umweltinformatik-marburg.de:4000/distributionDigitizer/data.html)
locally.
The pictures are saved special in .png format and you can use them later in the DD-App.

## How to start DD-App locally on your personal computer:

### Requirements
R, RStudio and Shiny-Library. This tree environments must be installed on your computer. 
If you have not done that, please follow these steps:
 - To install R on Windows follow this [link](https://cran.r-project.org/bin/windows/base/) 
 - To install R on Linux follow this [link](https://cran.r-project.org/doc/manuals/R-admin.html) 
 - Download and install RStudio [hier](https://www.rstudio.com/products/rstudio/download/)
 - If you still haven’t installed the Shiny package, start the RStudio, connect to the internet, and run:
 
```markdown
install.packages("shiny")
```

### Start the Application
Open the RStudio and write this:
```markdown
shiny::runGist("https://gist.github.com/sforteva/138af2ea533c2d1c3d1631b5d2d41e86")
```
If everything is ok, you would see the dialog box "DD Userinterface".

### Which options do you see on this window now 

At the top left, with the help of the "Browse" button, you can select a picture from a local folder. 
If you have selected a picture, with the mouse you can select and save an area in the image 

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
