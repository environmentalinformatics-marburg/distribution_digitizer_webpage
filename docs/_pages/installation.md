---
title: Installation
header:
  image: "/assets/images/teaserimages/world_temp.png"
  caption: '[Environmental Informatics Marburg](https://www.uni-marburg.de/en/fb19/disciplines/physisch/environmentalinformatics)'
permalink: /installation.html
sidebar:
---

<span style="color:red">
The download and installation guide for the software comes in here
</span>


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

