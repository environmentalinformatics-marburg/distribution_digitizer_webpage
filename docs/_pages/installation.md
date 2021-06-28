---
title: Installation
header:
  image: "/assets/images/teaserimages/world_temp.png"
  caption: '[Environmental Informatics Marburg](https://www.uni-marburg.de/en/fb19/disciplines/physisch/environmentalinformatics){:target="_blank"}'
permalink: /installation.html
sidebar:
toc: true
---




### Download

Download the required files from the Github repository:

[Github Link](https://github.com/environmentalinformatics-marburg/distribution_digitizer_students.git)

Download the repository as zip file on your local disk by pressing the green button "code" and then extract the zip file for working with the contained folder.

One convenient method is to save the file in the D\: Drive if you use Windows.

In any case, make sure you know the path to this directory. You need to enter it in the DD application ("Working git directory").


### Prerequisites

* RStudio (available for free download [here](https://www.rstudio.com/products/rstudio/download/))

Make sure that you have the latest version installed.


* R Packages "shiny" and "reticulate"

Install them with 
```R
install.packages(c("shiny", "reticulate"))
```
While installing "reticulate", if prompted for the additional installation of "miniconda" hit "yes" for obtaining a local Python installation.

* The Digitizer makes use of additional functions from several R packages and Pyhon moduls. Installing all theses depencencies might take a while.



### Set your working directory

The working directory is the path to the folder with your downloaded files.

This path must be set to the folder containing for being able to execute the shiny app.
By default, "app.R" lies at the root of this repository. 

In RStudio, the path to the working directory can be set automatically with
```R
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
```

or manually with a path of your choice:

```R
setwd("D:/distribution_digitizer_students-main/") # uncomment this line for setting the working directory manually.
```


### Start the Digitizer

Open the file "start_dd_app.R" with RStudio and run the whole code, either by selecting the whole code and hitting control + enter or by pressing the button "Run App".

Now you should see the dialog box "DD User interface" if everything went fine:

![Digitizer Interface]({{site.baseurl}}/assets/images/shiny/DD_user_interface.png)
<figcaption> The Digitizer user interface.
</figcaption>







### Explanation of the contained files and folders in the downloaded repository


#### Files
* app.R: the source code of the shiny application.
* config.txt: still needed?
* start_dd_app.R: Open and execute with RStudio for starting the app.
* README.md: Additional information

#### Folders
* data
  * input: Your scanned book pages go in here.
  * output: output for all modules (map cropping, pixel classification, georeferencing).
  * templates: Template files created with the Digitizer for map cropping and detecting legend elements on maps. Also Ground Control Points for georeferencing go in here.
* src: The source code of the application.
* www: Layout for the application. 






