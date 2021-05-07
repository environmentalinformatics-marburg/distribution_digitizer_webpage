---
title: LM | Modellierung und Abbildung von Räumen
toc: true
header:
  image: /assets/images/02-splash.jpg
  image_description: "Blick ins Lahntal mit Grünlandwirtschaft, Baustelle für Stromtrassen und Regenbogen."
  caption: "Foto: T. Nauss / CC0"
---


{% include video id="LgwetO8etR4" provider="youtube" %}

## Raum und räumliche Prozesse
Im Beispiel von John Snows Karte der Cholerafälle haben Sie bereits den Zusammenhang von Raum (London, Soho) und räumlichen Prozessen (Cholera-Ausbruch) kennengelernt. Seine Erkenntnis war: *Je näher ein Wohnhaus an der Wasserpumpe in 43 Broadwick Street liegt, umso mehr Todesopfer wurden in dem Wohnhaus verzeichnet*. Wenn wir das verallgemeinert ausdrücken wollen, können wir den *1. Hauptsatz der Geographie*  von Waldo Tobler heranziehen: “Everything is related to everything else, but near things are more related than distant things” ([Tobler, 1970](https://www.tandfonline.com/doi/abs/10.2307/143141)).

Mit diesem Satz schuf Tobler eine Grundlage für die Analyse, Modellierung und Simulation räumlicher Prozesse, die auf distanzbasierten Prozessen und Zusammenhängen beruhen.

**Info**: Tobler benötigte für sein Simulationsmodell der Bevölkerungsentwicklung in Detroit eine Lösung für die seinerzeit sehr limitierten Computerressourcen. Dazu teilte er die Stadt in eine Gitterstruktur und machte mit seinem 1. Hauptsatz die Not zur Tugend indem er so zu belegen trachtete, dass die in einem über die Stadt gelegten Gitter modellierte Bevölkerungsentwicklung immer nur von den direkten Nachbarzellen und nie von der Entwicklung anderer Zellen oder der ganzen Stadt abhing. Gültigkeit besitzt der Satz auch z.B. für die Ausprägung von Wissensdomänen in Wikipedia, wie Hecht und Moxley (2009) in ihrem spannenden Artikel *[Terabytes of Tobler: Evaluating the First Law in a Massive, Domain-Neutral Representation of World Knowledge](https://link.springer.com/chapter/10.1007/978-3-642-03832-7_6)* zeigen. Hingegen gilt er z.B. für Artenreichtum [(Bjorholm et al. 2008, BMC Ecol)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2424035/) und zahlreiche andere, räumliche Phänomene und Prozesse **nicht**.
{: .notice--primary}

Toblers Satz ist nicht die einzige Möglichkeit Raum zu beschreiben. Im Gegenteil, der Satz zielt sehr stark auf räumlich-funktionale Beziehungen ab. Wie Raum noch beschrieben und verstanden werden kann, erfahren Sie im Video.

{% include video id="mELVmkhvG9Y" provider="youtube" %}

## Abbildung von Raum
Die Wahrnehmung und Interpretation der realen Welt erfordert eine Abstraktionsleistung, mit anderen Worten eine zielgerichtete Vereinfachung. Hierfür benötigen wir, sowohl im Alltag als auch in der Wissenschaft, geeignete Strategien. Bei der Abstraktion schaffen wir im ersten Schritt unser eigenes, konstruiertes *Modell* der Welt. Wir definieren einen Raumausschnitt und eine Perspektive auf diesen Ausschnitt, die manche Phänomene in den Vordergrund treten, andere wegfallen lässt. Unser Modell ist deshalb immer nur eine Sichtweise von vielen auf die Welt. Ob und inwieweit unser Raummodell der Wirklichkeit entspricht, lässt sich deshalb auch nur aus dem gewählten Blickwinkel oder dem zuvor definierten Zweck bewerten. Für eine wissenschaftliche Modellierung des Raums ist es deshalb entscheidend, die Zielstellung des Modells zu definieren und transparent zu kommunizieren.

**Beispiel**: Wir können eine Landschaft wie das Lahntal, aus Wäldern, Ackerflächen, Wiesen und kleineren Orten, z.B. unter dem Gesichtspunkt *"Tourismus"* modellieren und damit die landschaftliche Diversität, Ausblicke, Sehenswürdigkeiten etc. in den Fokus nehmen. Die gleiche Landschaft können wir auch unter dem Gesichtspunkt *"Agrarproduktion"* mit Fokus auf landwirtschaftliche Produkte modellieren. Oder wir nehmen den Aspekt *"Gewässerschutz"* auf und betrachten die räumlichen Verhältnisse zwischen der Landnutzung (z.B. Ackerflächen, Waldflächen...) und der Lahn hinsichtlich z.B. des Prozesses der Nährstoffeinträge.
Alle drei Blickwinkel könnte man wiederum zu einer abstrakten Kategorie der *"Ökosystemleistung"* zusammenfassen und die Multifunktionalität von Landschaften in den Vordergrund unseres Modells stellen. Wenn Sie dieses Beispiel interessiert, schauen Sie mal in [Manning et al. Redefining ecosystem multifunctionality. Nat Ecol Evol 2, 427–436 (2018).](https://doi.org/10.1038/s41559-017-0461-7)
{: .notice--info}

Wie der Prozess der Modellierung (Abstraktion) abläuft, zeigen wir Ihnen im Video - natürlich mit einem Modell.

{% include video id="UH66r4cUyfM" provider="youtube" %}

## Abgrenzung von Raum

Um Räume zu Modellieren benötigen wir noch eine geeignete Vorgehensweise. Generell kann Raum bzw. können darin enthaltene Objekte oder Phänomene als

* diskrete Geoobjekte oder
* kontinuierliche Räume oder Felder

abgebildet werden.

Ein diskretes Geoobjekt ist alles, was klar räumlich abgrenzbar und zählbar ist. Ein Feld ist kontinuierlich und verändert sich in Raum und Zeit. In der digitalen Praxis, z.B. in geographischen Informationssystemen müssen aber auch die kontinuierlichen Felder in räumlich abgegrenzte Objekte zerlegt werden, z.B. als Rasterobjekte. Im Unterschied zu tatsächlich diskreten Objekten füllen die so zerlegten Kontinua den Raum aber lückenlos und überschneidungsfrei aus.

Beispiele für ein Kontinuum sind das Relief oder die Lufttemperatur. Beispiele für diskrete Objekte sind ein Haus oder ein Baum. Ein Berggipfel ist schon weniger eindeutig, je nachdem ob man die höchste Spitze als Gipfel, oder die Region um diese Spitze herum als Gipfel bezeichnet. Letzteres erfordert eine Abgrenzung oft entlang einer Höhenlinie.

**Info**: Die Modellierung in der Geographie ist durch die raum-zeitlichen Zusammenhänge ein komplexer Vorgang. Die Modellierung hilft uns die Welt durch Reduktion verständlicher zu machen, sie wird interpretier-, prognostizier- und gestaltbar. Diese Eigenschaften verleihen der Modellierung und den Modellen, traditionell  auch in der Geographie und den geographischen Bildungskontexten, eine besondere Bedeutung, sind doch Globen, Karten, Stadtmodelle, Klimamodelle etc. reduzierte Abbildungen der Welt. Eine Vertiefung dieser theoretischen Grundlage und das daraus abgeleitete Kompetenzmodell zur Modellierung in der Geographie kann hier nachgelesen werden: [Ammoneit R, Reudenbach C, Turek A, Nauß T, Peter C (2020) Geographische Modellierkompetenz – Modellierung von Raum konzeptualisieren. gwu 1: 19–29](https://austriaca.at/0xc1aa5576_0x003b1ef9.pdf).
{: .notice--primary}

Wie wir Räume mit Ihren Kontinua erfassen und sinnvoll abgrenzen können und wie uns das bei der Komplexitätsreduktion hilft, erfahren Sie im Video.

{% include video id="NgoNpI9hmJY" provider="youtube" %}




<!--
Vorlesung:

Trotz dieser elementaren Einschränkung werden Repräsentationen des Raumes zwingend für das Verständnis von Prozessen und Zusammenhängen für gemeinsame Planung und Interaktion etc. benötigt. Oft sind unterschiedliche oder variable Repräsentationen notwendig, um die Realität ausreichend zielführend abzubilden.

Wer geographische Fachkompetenz erwerben will, muss die genannten Aspekte berücksichtigen. Wissenschaftstheoretisch kann Geographie durchaus als ein Methodenverbund, dessen Ziel es ist raum-zeitliche Zusammenhänge nachvollziehbar und reproduzierbar zu konstruieren, begriffen werden.

Wie setzen wir in der Geographie am einfachsten und effizientesten die Abstraktion unserer Weltsicht um? Zunächst erfordert eine Raumbeschreibung die Festlegung eines Ausschnitts und eines Zwecks der beobachteten Welt. Nur dann kann in zielführender Weise vereinfacht (abstrahiert) werden. Hierzu wird üblicherweise die geographische Repräsentation von Raum durch eindeutige Raumobjekte mit beliebigen Merkmalsausprägungen (E-Kirche: gotischer Baustil, Sandsteinbau, Touristenattraktion…,) oder kontinuierliche Merkmalsausprägungen im Raum (Luftdruck, Temperatur, Bevölkerung, ...) beschrieben.

<html>
<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Fr%C3%A4nkische-Schweiz-westliche-Kante-16-05-2005.jpeg/640px-Fr%C3%A4nkische-Schweiz-westliche-Kante-16-05-2005.jpeg?uselang=de" title="View from the west of the Fränkische Schweiz. In the center of the photo you can see the escarpment outlier // Walberla// "><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Fr%C3%A4nkische-Schweiz-westliche-Kante-16-05-2005.jpeg/640px-Fr%C3%A4nkische-Schweiz-westliche-Kante-16-05-2005.jpeg?uselang=de" width="50%"  alt="Fränkische Schweiz Westrand"></a>
</html>

*Abbildung 01-03: Blick auf die Fränkische Schweiz von Westen. In der Bildmitte ist der Zeugenberg Walberla zu sehen (Arnold 2005)*


Beginnen wir mit einem geographischen Begriff von Raum, der uns aus dem Alltagswissen vertraut ist. So kennen viele die Region der Fränkischen Schweiz. Wir assoziieren mit solchen *Raumentitäten* eine mehr oder weniger diffuse, gleichwohl abgegrenzte Raumausdehnung (Region) oder die Vorstellung einer Landschaft (vgl. Abb. 01-03). Derart als Entitäten empfundenen Räumen werden häufig auch Attribute wie kulinarische, kulturelle oder freizeitorientierte Aspekte zugeordnet. So ist die Fränkische Schweiz sowohl für ihre Weine und lokalen Biere als auch beispielsweise für ihre Osterbrunnen (vgl. Abb. 01-04) oder ihr touristisches Potenzial bekannt.

Ein weiteres sehr eingängiges Beispiel für solche räumlichen Übergänge stellt das Relief dar (vgl. Abb. 01-05), denn die Erdoberfläche weist eine quasi-kontinuierlich unterschiedliche Höhe auf. Die räumliche Verbreitung dieser Merkmalsausprägung variiert kontinuierlich. Versucht man vor diesem Hintergrund eine räumliche Abgrenzung der Fränkischen Schweiz so mögen nicht nur die religiösen oder kulinarischen Vorlieben der Bevölkerung, sondern auch z.B. die morphologischen oder edaphischen Eigenschaften der Erdoberfläche die sie bevölkern inhomogen im Raum verteilt sein. Die Karte der Fränkischen Schweiz (vgl. Abb. 01-06) versucht dies durch ein radiales Verblassen der Farben im Randbereich zu symbolisieren, allerdings ohne zu verdeutlichen wie es zu dieser Abgrenzung kommt.

</html>
 <a href="http://minibsc.gis-ma.org/GISBScL1/de/image/eierbrunnen.jpg" title="Marketplace of  Ebermannstadt with the decorated Well of Mary. This is an example of the typical Easter decoration in this region (Behrendes 2010).">  <img src="http://minibsc.gis-ma.org/GISBScL1/de/image/eierbrunnen.jpg" width="50%"  alt="Easter Decoration Ebermannstadt">  </a>
 </html>

*Abbildung 01-04: Der Marktplatz von Ebermannstadt mit dem geschmückten Marienbrunnen und Osterbäumen. Beispielhaft für den typischen Osterschmuck der fränkischen Schweiz *

<html>
<a  href="https://www.flickr.com/photos/environmentalinformatics-marburg/13921790904" title="01-05-dem-fraenkische-schweiz by Environmental Informatics Marburg, on Flickr"><img src="https://farm8.staticflickr.com/7226/13921790904_b0919259f8_n.jpg" width="50%" alt="01-05-dem-fraenkische-schweiz"></a>
</html>

Abbildung 01-05: Digitales Geländemodell der Fränkischen Schweiz und angrenzender Regionen. Datengrundlage SRTM Daten 90 Meter räumliche Auflösung (GIS.MA 2009)

<html>
 <a href="http://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Fraenkische_Schweiz.png/800px-Fraenkische_Schweiz.png" title="Map of the Fränkische Schweiz ">  <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Fraenkische_Schweiz.png/800px-Fraenkische_Schweiz.png" width="50%"  alt="Map of Frankonian Switzerland">  </a>
 </html>


*Abbildung 01-06: Karte der Fränkischen Schweiz (Mikmaq 2009)*
-->
