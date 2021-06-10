---
title: FAQ
header:
  image: "/assets/images/teaserimages/world_temp.png"
  caption: '[Environmental Informatics Marburg](https://www.uni-marburg.de/en/fb19/disciplines/physisch/environmentalinformatics){:target="_blank"}'
permalink: /faq.html
sidebar:
toc: true
---

## Why does the pixel classification program detects dark squares too and is that good?

For some values of Guassian and Kernel Filter, the dark squares might retain through the filter because of high pixel intensity values. The goal of the pixel classification program is to detect all the legend elements in the map as much as possible. If the program detects dark squares, then its good.

## How do I check whether I have georeferenced correctly in QGIS?

Once you have georeferenced, the map should automatically appear as a layer on the top of Open Street Map(OSM). If not either your layer or project CRS or SRS is wrong. (It should be 102025).

## Error in reading template_matching.py?

This is because either the working directory or the python path is wrong. Check the working directory at the DD Shiny application interface and download the new version of software through github. The new version of software automatically sets the working directory and finds the new python path.

## Error in locating app.R?
 
This is because the working directory is wrong in start_dd_app.R. Follow the steps to change the path in new version of software or manually set the working directory in the R Studios through,

Session -> Set Working Directory -> To the Source File Location.

## Error in running use_python() function?

If this is the case, then install reticulate through install.packages(“reticulate”). Execute this command in start_dd_app.R console.

## Do I have to change any program?

Do not modify the program. In case if you face errors, then follow the tutorial and above FAQs to solve the errors in start_dd_app.R.

## Can I use R Cloud to execute the whole software?

No, R Cloud memory gets easily exhausted when the inputs are TIF/TIFF files (because of the large memory consumption). R Studio (offline) is highly recommended.

## Your questions are not listed here?

Feel free to e-mail your query to Venkates@students.uni-marburg.de along with the screenshots!.
