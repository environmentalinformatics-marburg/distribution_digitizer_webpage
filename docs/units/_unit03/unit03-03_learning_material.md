---
title: LM | Geodaten und Geoobjekte
toc: true

header:
  image: /assets/images/03-splash.jpg
  image_description: "Cutout from  Measured carbon dioxide concentrations in Vancouver"
  caption: "Bild: [flickr](https://flic.kr/p/RNxn74) / CC-BY-2.0"

panel1:  
  - url: https://www.flickr.com/photos/environmentalinformatics-marburg/13981635311
    image_path: https://live.staticflickr.com/7325/13981635311_ae1b12e0cf_b.jpg
    title: "Screenshot von OpenStreeMap mit einem roten Kreis der einen fiktiven Pannenort auf einer Autobahn identifziert."
    alt: "Screenshot von OpenStreeMap mit einem roten Kreis der einen fiktiven Pannenort auf einer Autobahn identifziert."

panel2:  
  - url: https://w.wiki/RRv
    image_path: https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Bukowsko_-_mapa_katastralna_%281906%29.jpg/1280px-Bukowsko_-_mapa_katastralna_%281906%29.jpg
    title: "Historischer Katasterplan von Bukowsko, Galizien. Grafik: przeslal Marek Silarski / Public domain via wikimedia.org"
    alt: "Katasterplan von Bukowsko, 1906, Galizien."

panel3:  
  - url: https://w.wiki/RS6
    image_path: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Geographic_coordinates_sphere.svg/487px-Geographic_coordinates_sphere.svg.png
    title: "Geographische Koordinaten auf einer idealisierten Erdkugel. Grafik: E^(nix) / CC BY-SA via wikimedia.org"
    alt: "Durch Winkel abgebildete, geographische Koordinaten auf einer Kugel."
---

Sind Objekte im Raum eingemessen, können sie zusammen mit Ihren Merkmalsausprägungen als geographische Daten gespeichert werden. Der Begriff Objekt ist sehr weit gefasst. Es kann sich um einen individuellen Baum oder ein individuelles Haus handeln, die z.B. von Hand eingemessen sind, oder aber um ganze Landschaften, die z.B. durch Satellitenmessungen erfasst wurden. Gleiches gilt für Merkmalsausprägungen. Es können sowohl unmittelbare Eigenschaften der Objekte sein, z.B. die Baumart oder die Wandfarbe des Hauses, oder durch sie erfasste Eigenschaften, wie z.B. die Lufttemperatur, die durch das Objekt "Klimastation" gemessen wird oder die Reflexion der Landoberfläche, die durch den Satellitensensor erfasst wird.

## Geodaten

Geographische Daten oder Geodaten repräsentieren Informationen durch räumlich fixierte, maschinenlesbare Konstrukte aus Zeichen, Bildern oder Funktionen. Die zentrale Fragestellung lautet: Was ist spezifisch geographisch an einer bestimmten Information? Ein Beispiel:

*Die Lufttemperatur an der Klimastation in Cölbe, Landkreis Marburg-Biedenkopf betrug am 23.05.2020 um 10:40 MESZ 14°C. Die Koordinaten lauten 50,839° Nord, 8,779° Ost, die Höhe ist 478 m.*

Die Aussage verbindet Raum (Koordinaten und Höhe) mit Zeit (Datum und Zeitangabe) und der Eigenschaft der Lufttemperatur. Zusätzlich sind weitere Eigenschaften vorhanden: Klimastation, Cölbe, Landkreis Marburg-Biedenkopf. Aus dieser Aussage kann folgendes geographisches Datum gebildet werden:

```
50.839 N; 8.779 E; 187 ü. MSL; 10:40 MESZ; Cölbe; 14°C
```

Die Station könnten darüber hinaus noch mit der Stations-ID des Deutschen Wetterdienstes *869* eindeutig beschrieben werden (z.B. welche Sensoren, welcher Untergrund, zeitliche Entwicklung der Bebauung im Umfeld).

Geographische Daten verbinden somit räumlich eindeutig verortete Objekte mit mindestens einer Merkmalsausprägung. Merkmalsausprägungen können beliebiger Natur sein (z.B. physikalische Messgrößen, soziologische Aspekte, Adressen, statistische Kennzahlen, individuelle Bewertungen).

## Geoobjekte

Geoobjekte sind Repräsentationen real existierender Objekte in unserem Modell, z.B. in unserer analogen oder digitalen Karte.
Sie sind durch folgende Eigenschaften definiert:
* Geometrie = Wo liegt es und wie wird es abgebildet? Die Geometrie ist die räumliche Dimension des Geoobjekts. Sie ergibt sich aus der geographischen Lage und der Dimensionalität der Abbildung. Die Lage ist durch geographische oder kartographische Koordinaten bestimmt. Dabei kann es sich um einen Ort (z.B. Haus), oder eine Reihe von Orten (z.B. Verlauf einer Straße) handeln. Die Dimensionalität bestimmt, ob ein Geoobjekte als Punkt, Strecke oder Fläche dargestellt wird. Die Darstellung kann dabei vom Maßstab abhängig sein.
* Topologie = Wie liegt es zu einem anderen Objekt? Die Topologie definiert Beziehungen zwischen Geoobjekten. Die Topologie ergibt sich oft direkt aus der Geometrie der Objekte, z.B. wenn zwei Ackerflächen nebeneinander liegen. Sie muss aber explizit angegeben werden, z.B. wenn sich zwei Straßen im Raum kreuzen und definiert werden muss, ob es sich um eine Kreuzung oder um eine Über-/Unterführung handelt.
* Attribute = Welche Eigenschaften hat es? Die Attribute sind die semantische Dimension des Geoobjekts. Sie charakterisieren weitere Eigenschaften, z.B. den Ortsnamen oder andere Merkmalsausprägungen wie z.B. das Klima in einem Wald. In Attributen können auch zeitliche Veränderungen z.B. von Lufttemperaturen angegeben werden, die nicht mit räumlichen Veränderungen einhergehen, wie es z.B. beim Landnutzungswandel der Fall ist.

Geoobjekte können real existierende, diskrete Objekte (z.B. Baum, Haus, Fluss) oder kontinuierliche Felder (z.B. Klima) beschreiben. Während Geoobjekte in analog gezeichneten Karten immer durch Vektoren dargestellt werden, stehen in der digitalen Verarbeitung grundsätzlich zwei Datenmodelle zur Verfügung: Vektoren und Raster.

### Vektordatenmodell

In einem kartesischen Koordinatensystem können aus den Grundelementen Punkt, Richtung und Strecke beliebig komplexe räumliche Strukturen zur Modellierung von Geoobjekten aufgebaut werden:
* Punkt: Ein Punkt wird durch die Angabe seiner Koordinaten definiert. Die Punktvektoren werden als Knoten bezeichnet.
* Linie: Eine Linie wird durch zwei Knoten im Koordinatensystem referenziert, die durch eine Linie verbunden werden. Die Linienverbindungen werden als Kante bezeichnet.
* Polygon: Ein Polygon beschreibt eine durch mindestens drei Knoten und zwei Kanten definierte Fläche. Polygone werden als Maschen bezeichnet. Wichtig ist, dass im digitalen Datensatz die Schließung der Fläche explizit definiert ist. Sonst ist z.B. ein augenscheinlich geschlossenes Dreieck nur für den menschlichen Betrachter, nicht aber für den Computer geschlossen.

Merkmalsausprägung werden in Attributtabellen gespeichert, die mit den geometrischen Informationen der Vektoren verbunden sind. Über die Attributtabelle können beliebig viele Merkmale mit einem Vektor verknüpft werden.

<html><a href="https://www.flickr.com/photos/environmentalinformatics-marburg/13973697615" title="02-8 by Environmental Informatics Marburg, on Flickr"><img src="https://farm6.staticflickr.com/5224/13973697615_88db5c67e1.jpg" width="500" height="352" alt="02-8"></a></html>

*Abbildung 02-08:Graphische und numerische Darstellung der drei Grundobjekte (Punkt, Linie, Fläche) eines Vektordatenmodells mit Hilfe eines kartesischen Koordinatensystems (GIS.MA 2009)*

### Rasterdatenmodell

In Rastermodellen werden homogene Merkmalsausprägungen als Zahlenwerte in überschneidungsfreien Gitterzellen abgebildet. Im Unterschied zu den Vektormodellen, kann immer nur ein Merkmal in einem Raster gespeichert werden. Mehrere Merkmale müssen einzeln in mehreren Rasterebenen gespeichert werden.

<html><a href="https://www.flickr.com/photos/environmentalinformatics-marburg/13993690753" title="02-9 by Environmental Informatics Marburg, on Flickr"><img src="https://farm8.staticflickr.com/7369/13993690753_173e09e3fb.jpg" width="500" height="494" alt="02-9"></a></html>
