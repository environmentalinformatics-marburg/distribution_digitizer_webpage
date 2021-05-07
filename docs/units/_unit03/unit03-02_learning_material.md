---
title: LM | Verortung im Raum
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

Für die Analyse und Darstellung von räumlichen Phänomenen müssen die Beschreibungen von Objekten im Raum räumlich verortet werden. Diesen Vorgang nennt man Georeferenzieren, Geolozieren, Verorten oder Geotaggen. Eine Georeferenzierung muss nicht mathematisch sein. Vielmehr ist sie Teil des räumlichen Modellierungsprozesses und die Auswahl der Konvention zur räumlichen Verortung wird deshalb von der individuellen Fragestellung bestimmt. Im Folgenden lernen Sie verschiedene Konventionen zur räumlichen Verortung kennen.


## Räumliche Verortung durch Namen und Adressen

Orte durch Benennung zu lokalisieren gehört zu den ältesten Kulturtechniken der Menschheit. Durch die Kombination von Namen und Ziffern ergibt sich beispielsweise die postalische Kodierung. In dieser Konvention ist *Deutschhaustrasse 10, 35032 Marburg, Deutschland* die Georeferenzierung für eines der Gebäude des Fachbereichs Geographie in Marburg. Sie ist ausreichend, um die Post zuverlässig zuzustellen und funktioniert ohne Mathematik, ohne geographische Koordinaten durch eine hierarchische Kette von Namenskodierung vom Gebäude bis zum Nationalstaat. Wenn sich die Kodierung ändert, beispielsweise durch die Umbenennung von Karl-Marx-Stadt in Chemnitz, bleibt der geographische Raumbezug dennoch erhalten. Voraussetzung für dieses System ist aber die Eineindeutigkeit der Beschreibung. Allein die Angabe eines Ortsnamens, z.B. London oder Neunkirchen, wäre zu wenig, da diese Namen vielfach auf der Erde vorkommen. Es braucht also ein übergeordnetes Zuordnungssystem, wie z.B. Landkreise oder Nationalstaaten. Noch besser ist eine möglichst allgemeingültiges Zuordnungssystem, weshalb die Thurn und Taxis Post 1853 in Deutschland Ortsnamen mit einem Zahlenschlüssel kodiert, der eine abstrakte, nachvollziehbare Identifikation der Raumposition dieser Orte möglich macht.

**Info**: Allen geographischen Informationen liegt eine eindeutige räumliche Zuordnung zugrunde.
{: .notice--info}


## Relative Verortung durch lineare Referenzierung

Eine lineare Referenzierung basiert auf eindimensionalen Lagebeziehungen. Entlang von Autobahnen wird dieses System verwendet und im Raum durch Kilometerangaben (auf kleinen blauen Schildern) abgebildet. Eine Pannen- oder Unfallstelle auf der Autobahn kann durch die Angabe *64,0 km, Fahrtrichtung Hamburg, rechte Fahrspur* verortet werden.

{% include gallery id="panel1"  caption= "Pannenort nördlich von Soltau." %}

Die Konvention funktioniert, weil die Kilometerangabe eindeutig ist. Nullpunkt ist der definierte Beginn der Autobahn und die Wegstrecke ist durch die Autobahn, also einer eindeutig definierten Strecke, vorgegeben. Das bedeutet im Umkehrschluss, dass eine solche, quantitative Referenzierung nur bei eindimensionalen Geoobjekten, also linearen Strukturen wie Straßen, Schienen, Rohr- oder Versorgungsleitungen, angewendet werden kann.

**Info**: Lineare Referenzen sind immer topologisch korrekt und können immer in geometrisch eindimensional messbaren Entfernungen angeben werden.
{: .notice--info}


## Geometrisch exakte maßstäbliche Raumabbildung

Die geometrisch exakte und maßstäbliche Raumabbildung ist eine zweidimensionale Erweiterung der linearen Referenzierung. Grundlage ist die von Carl Friedrich Gauß (1777 - 1855) entwickelte Vermessungsmethode, die eine Abbildung von Objekten relativ und in beliebiger Lage zueinander ermöglicht. Ein Beispiel für diese Form der Raumbeschreibung sind die Flurkarten, die als Teil der Kataster die Flurstücken und deren Eigentumsverhältnissen definieren.

{% include gallery id="panel2"  caption= "Historischer Katasterplan von Bukowsko, Galizien. Grafik: [przeslal Marek Silarski / Public domain via wikimedia.org](https://w.wiki/RRv)" %}

Während bei modernen Flurkarten und digitalen Katastern natürlich ein geographisches Referenzsystem hinterlegt ist, fehlt dieses in traditionellen Flurkarten. Die Karten dienen stattdessen ausschließlich der exakten Größenbeschreibung von baulichen Anlagen und Liegenschaften. Weitere tabellarische Informationen (z.B. Eigentumsverhältnisse, Lasten) werden im Liegenschaftsbuch vorgehalten und über eineindeutige Zahlenkombinationen mit den in der Karte dargestellten Flächen verbunden.

**Info**: Katasterpläne sind immer topologisch korrekt und bieten immer geometrisch zweidimensional maßstäblich messbare Entfernungen und Flächen.
{: .notice--info}


## Geographische Raumabbildung

Sollen Objekte in Raumabbildungen nicht nur relativ exakt zueinander, sondern auch absolut auf der Erde verortet werden, müssen die Objekte in einem mit der Erde verbundenen Koordinatensystem verortet werden. Wenn wir für die Erde in erster Näherung eine Kugelgestalt annehmen, dann können beliebige Punkte an ihrer Oberfläche durch zwei Winkel bestimmt werden: Der Zenit beschreibt die geographische Breite, der Azimut die geographische Länge. Eine geographische Breite von 0° beschreibt Orte entlang des Äquators. Nördliche Breiten werden durch positive Gradangaben oder durch die Bezeichnung "Nord", südliche Breiten durch negative Gradangabe oder die Bezeichnung "Süd" beschrieben. Eine geographische Länge von 0° beschreibt Orte entlang des Längenkreises, der durch die Londoner Sternwarte Greenwich verläuft. Diesen Längengrad bezeichnet man als Hauptmeridian. Östliche Breiten werden durch positive Gradangaben oder die Bezeichnung "Ost", westliche Breiten durch negative Gradangaben oder die Bezeichnung "West" beschrieben.

{% include gallery id="panel3"  caption= "Geographische Koordinaten auf einer idealisierten Erdkugel. Grafik: [E^(nix) / CC BY-SA via wikimedia.org](https://w.wiki/RS6)" %}

Die Erde ist keine Kugel. Sie kann durch einen Geoid beschrieben werden, das durch das Schwerefeld der Erde bestimmt wird und Fläche gleichen Schwerepotentials darstellt. Eine dieser Schwerepotentialflächen ist durch die mittlere Höhe der Weltmeere dargestellt. Diese setzt sich natürlich unter den Kontinenten fort. Der Geoid weist im Vergleich zu kugelförmigen Körpern viele Abweichungen im Zehnermeterbereich auf. Deshalb ist es für Vermessungsaufgaben einfacher, die Erdgestalt über einen Ellipsoid anzunähern. Das dafür nötige *geodätische Bezugssystem* besteht aus dem geodätischen Datum und dem Referenzrahmen:

* Geodätisches Datum: Anstelle des Geoids wird die Erdform durch einen Ellipsoid beschrieben, der ggf. lokal angepasst und als Referenzellipsoid bezeichnet wird. Die Lage und Ausrichtung des Referenzellipsoid wird im Schwerefeld der Erde eindeutig verortet und durch ein geodätisches Datum eindeutig beschrieben.
* Referenzrahmen: Das durch das geodätische Datum aufgespannte Koordinatensystem wird an der Erdoberfläche über die Koordinaten von sogenannten Festpunkten in einen Referenzrahmen eingehängt. Im Minimalfall ist ein Festpunkt notwendig. Bei hochgenauen Vermessungen muss ferner die Abweichung zwischen der Lotrichtung, die durch das Schwerefeld der Erde bestimmt ist und der Normalen auf den Referenzellipsoid berücksichtigt werden.

**Info**: Da es viele Referenzellipsoide und Referenzrahmen gibt muss das jeweils verwendete, geodätische Bezugssystem zwingend bekannt sein. Die gleichen Koordinaten beschreiben bei falscher geodätischer Zuordnung sonst Orte, die um mehrere Zehnerkilometer auseinander liegen können.
{: .notice--info}

{% include video id="ZPSSlinFmMA" provider="youtube" %}


## Geodätische Raumabbildung

Mit Hilfe von geographischen Raumabbildungen können Objekte absolut auf der Erde verortet werden. Die Abbildung von Räumen basiert aber häufig auf zweidimensionalen Medien - sowohl in der Aufnahme durch z.B. Luft- oder Satellitenbilder, als auch in der Darstellung z.B. in gedruckten oder digitalen Karten. Die dreidimensionale geographische Raumabbildung muss also in eine zweidimensionale, verebnete Projektionen der Erdoberfläche überführt werden. Dieser Vorgang wird häufig kartographische oder geodätische Projektion bzw. Abbildung genannt. Die mathematische Transformationsvorschrift wird als Kartennetzentwurf oder (Karten-)Projektionssystem bezeichnet. Für eine Kartenprojektion benötigt man analog zur geographischen Raumabbildung geodätisches Bezugssystem zur Abbildung der Erde und zusätzlich eine Transformationsvorschrift, die die geographischen Koordinaten (Länge und Breite) in ein kartesisches Koordinatensystem (Rechtswert und Hochwert) überführt. Zusammen ergibt sich so aus geodätischem Bezugssystem (Geodätisches Datum und Referenzrahmen) und Projektionssystem das eindeutige *Koordinatenreferenzsystems*.

**Info**: Um die Vielzahl an Koordinatenreferenzsystems eineindeutig zu beschreiben, hat die European Petroleum Survey Group Geodesy ein eindeutiges Nummernsystem entwickelt, das jedes Koordinatensystem mit einem nummerischen EPSG-Code beschreibt. Eine Übersicht findet sich z.B. auf der [Spatial Reference](https://spatialreference.org/) Webseite.
{: .notice--info}

Geodätische und kartographische Abbildung wird oft synonym verwendet. Die kartographsiche Abbildung beschreibt strenggenommen aber nur solche Projektionen, die unmittelbar geometrisch für die ganze Erde oder zumindest die Erdhalbkugel konstruiert werden können. Damit ist sie nur für kleinmaßstäbige Abbildungen geeignet. Geodätische Abbildungen bezeichnen demgegenüber die weitgehend verzerrungsfreien, großmaßstäbigen Darstellungen, die getrennt für schmalen Streifen auf der Erde berechnet werden.

{% include video id="RS8SJGUcQyU" provider="youtube" %}
