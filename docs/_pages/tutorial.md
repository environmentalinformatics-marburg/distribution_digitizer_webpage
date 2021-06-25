---
title: Tutorial
header:
  image: "/assets/images/teaserimages/digitizer_teaser.jpg"
  caption: '[Environmental Informatics Marburg](https://www.uni-marburg.de/en/fb19/disciplines/physisch/environmentalinformatics){:target="_blank"}'
permalink: /tutorial.html
sidebar:
toc: true
---



In the app, which should look like this

![Digitizer Interface]({{site.baseurl}}/assets/images/shiny/DD_user_interface.png)
<figcaption> The Digitizer user interface.
</figcaption>

you first need to set your working directory for executing the commonds of the Digitizer application.



## Working Directory

Sets the working directory in the Digitizer application.

Paste the path to your working directory in the field "Working Git Directory". You can find this path in the R Console as it is printed out by default when starting the app.

Make sure that you
* do NOT include in the path
  * quotation marks
  * empty spaces
  * special characters,
* use / and not \ to separate folders, and
* that your path ends with /  








## Map clipping: Object detection: Prerequisites

* Clear the input, output, and templates/map directories (= delete the files in there).
* Copy the input files to data/input and templates to the data/templates/maps.
* In case if the maps are notcropped, crop template maps and savethem underthe data/templates/mapdirectory.
* Ensure that the output directory is empty


## Map clipping: Object detection: Execution

* Check the working directory of the DD-R Shiny application again
* press "Start the template matching" for doing the object detection
* Checkthe data/output folder for the results. Also try different threshold values.
* The expected results in the output folder are (in this case) all cropped maps from the images in the input directory.
* Delete all the unwantedor noise images manually.


## Pixel classification

* Try some values for the filters and "start the pixel classification", which will use the output from the previous object detection step.
* The Gaussianfilter recommended value is 9 and the kernel filter recommended value is 5, feel free to try with the other values.
* The desired output is maps, which have the occurrence points marked in blue in your output folder. These files will then be used for geo-referencing.


## Georeferencing

* Get theopen street map data and the geo-referencer plugin.-The raster files are the output files of pixel classification stored under data/output/pixel_c folder.
* Your layer and your QGIS project should have the same CRS, namely EPSG (or ESRI): 102025.
* Know the structure of GCP data, e.g.:It mainly has four columnswith coordinates,The first two columns contain the coordinates of the input image (=image space), the next two columns contain the coordinated in some CRS referringto the real world (=geographical space)




# Move to extra page: 


# Theoretical background

## Object detection

Below you can find a tutorial for getting started with detecting maps on pages of scanned books, which is the first step before automatically detecing points (=occurrence records) on these maps afterwards.

{% include pdf pdf="Tutorial_template_matching.pdf" %}

## Template matching

{% include pdf pdf="template_matching.pdf" %}

## Object Detection (Additional Tutorial)
Additional slides of Object Detection and Execution Tutorial.

{% include pdf pdf="Object_Detection_Additional.pdf" %}

## Pixel Classification and Georeferencing
Pixel classification  and Geo-referencing overview and tasks.

{% include pdf pdf="DigitizeIT Software_final pixel classification.pdf" %}

## Pixel Classification Tutorial
Lecture slides on Pixel Classification.

{% include pdf pdf="Pixel_Classification.pdf" %}

## Geo-referencing Tutorial
Lecture slides on Geo-referencing.

{% include pdf pdf="Geo_referencing.pdf" %}





<!--
## Digitizer Tutorial

Follow this Tutorial Step-by-Step:

{% include pdf pdf="DigitizeIT_Tutorial.pdf" %}

<br>

-->




