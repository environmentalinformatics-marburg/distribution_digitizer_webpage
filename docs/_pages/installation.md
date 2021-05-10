---
title: Installation
header:
  image: "/assets/images/teaserimages/world_temp.png"
  caption: '[Environmental Informatics Marburg](https://www.uni-marburg.de/en/fb19/disciplines/physisch/environmentalinformatics){:target="_blank"}'
permalink: /installation.html
sidebar:
toc: true
---




## Download the Digitizer

The following environments should be installed on your computer for starting the distribution digitizer app locally on your personal computer:

 - [R](https://cran.r-project.org/){:target="_blank"} 
 - [RStudio](https://www.rstudio.com/products/rstudio/download/){:target="_blank"}
 - For installing the R shiny package, start RStudio, connect to the internet, and run:
 
```markdown
install.packages("shiny")
```


## Start the Digitizer
Open RStudio and execute:
```markdown
shiny::runGist("https://gist.github.com/sforteva/138af2ea533c2d1c3d1631b5d2d41e86")
```

Now you should see the dialog box "DD User interface" if everything went fine.



