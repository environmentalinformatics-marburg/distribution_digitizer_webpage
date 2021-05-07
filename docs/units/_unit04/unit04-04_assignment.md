---
title: A04-1 | Hygrisches Klima
toc: true
header:
  image: /assets/images/04-splash.jpg
  image_description: "Unübersichtlich beschriebene Universitätstafel"
  caption: "Foto: Wikimedia Commons / CC0"
mathjax: true
---
<script type="text/javascript" async
	src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML">
</script>

<script type="text/x-mathjax-config">
   MathJax.Hub.Config({
     extensions: ["tex2jax.js"],
     jax: ["input/TeX", "output/HTML-CSS"],
     tex2jax: {
       inlineMath: [ ['$','$'], ["\\(","\\)"] ],
       displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
       processEscapes: true
     },
     "HTML-CSS": { availableFonts: ["TeX"] }
   });
</script>


Die Formel zur Berechnung der Evapotranspiration nach Haude wurde korrigiert!
{: .notice--danger}

Walter-Lieth-Diagramme sind trotz einiger Einschränkungen (Schneeniederschlag, Abschätzung der Evapotranspiration etc.) aufgrund der einfachen Datenverfügbarkeit und der leicht erfassbaren Aussage ein in Schulbüchern und Atlanten weit verbreitetes Darstellungsformat für die hydroklimatologische Charakterisierung eines Ortes. Sie zeigen durch die spezifische Darstellung aggregierter Temperatur- und Niederschlagsdaten auf einfache Art typische Jahresmuster von Niederschlag und Temperatur. Im Rahmen dieses Arbeitsblatts sollen Sie solche Klimadaten aufbereiten und das hygrische Klima mittels eines [Walter-Lieth-Diagramms](https://de.wikipedia.org/wiki/Klimadiagramm) und  einer Verdunstungsabschätzung nach Haude vergleichen und bewerten.

## Aufgabe 04-1-L1: Walter-Lieth-Diagramm

{% capture A04-1-L1 %}

Erstellen Sie bitte auf Basis der langjährigen mittleren monatlichen Lufttemperatur und der langjährigen mittleren monatlichen Niederschlagssumme für die DWD-Station Cölbe ein Walter-Lieth-Diagramm. Nutzen Sie hierfür den auf ILIAS verfügbaren [Datensatz](https://ilias.uni-marburg.de/ilias.php?ref_id=1880380&cmd=view&cmdClass=ilrepositorygui&cmdNode=tt&baseClass=ilrepositorygui) und orientieren Sie sich an der im Datensatz vorhandnen Zeitspanne. Bitte beachten Sie, dass Lücken in der Zeitserie nicht aufgefüllt oder anderweitig explizit berücksichtigt werden müssen.

Interpretieren Sie in maximal zwei Sätzen das Walter-Lieth-Diagramm.

Umfang: 1 Seite in Ihrer PDF-Datei.
{% endcapture %}

<div class="notice--success">
  <h4 class="no_toc">Aufgabenstellung 04-1-L1:</h4>
  {{ A04-1-L1 | markdownify }}
</div>

## Aufgabe 04-1-L2: Verdunstung nach Haude

{% capture A04-1-L2 %}

Berechnen Sie bitte die langjährige mittlere monatliche potentielle Evapotranspiration nach Haude für den in A04-1-L1 von Ihnen bereits aufbereiteten Datensatz (zur Berechnung siehe [Info Berechnung Haude](#info-verdunstung-nach-haude)). Erstellen Sie bitte anschließend ein Diagramm, dass die potentielle Evapotranspiration den langjährigen monatlichen Niederschlagssummen gegenüberstellt.

Interpretieren Sie mit maximal zwei Sätzen das Diagramm auf Basis der berechneten Evapotranspiration.

Umfang: 1 Seite in Ihrer PDF-Datei.
{% endcapture %}

<div class="notice--success">
  <h4 class="no_toc">Aufgabenstellung 04-1-L2:</h4>
  {{ A04-1-L2 | markdownify }}
</div>


## Aufgabe 04-1-L3: Walter-Lieth oder Haude?

{% capture A04-1-L3 %}

Vergleichen Sie die beiden erstellten Diagramme und diskutieren Sie Ihre Analyse mit maximal zwei Sätzen. Nennen und begründen Sie anschließend jeweils einen kritischen Aspekt, sowohl in der jeweiligen Darstellungs- als auch Berechnungsform mit insgesamt maximal vier Sätzen.

Umfang: 1 Seite in Ihrer PDF-Datei.
{% endcapture %}

<div class="notice--success">
  <h4 class="no_toc">Aufgabenstellung 04-1-L3:</h4>
  {{ A04-1-L3 | markdownify }}
</div>



{% capture haude %}
#### Info: Verdunstung nach Haude
Die Berechnung der Verdunstung nach Haude basiert auf der Formel:


$$ PET = k \cdot e  \cdot  (1 -  { F \over 100 }) [mm/d]$$ 



mit: $PET$ als die potentielle Evapotranspiration, $k$ als dem Haude-Faktor (siehe nachfolgende Tabelle), $e$ als dem Sättigungsdampfdruck um 14:00 Uhr in hPa und $F$ als der relativen Luftfeuchte in Prozent.

Der Sättigungsdampfdruck $e$ [hPa] kann nach der Magnus-Formel z.B. wie folgt berechnet werden:


$$ e = {6,11 \cdot   10} ^ {(7,48 ∗ T_{max}) \over (237 + T_{max})} [hPa]$$

mit: $T_{max}$ als der maximalen Lufttemperatur in Grad Celsius.

Im Rahmen dieser Aufgabe können Sie anstelle der Temperatur um 14:00 Uhr die mittlere maximale Lufttemperatur sowie anstelle der Luftfeuchte um 14:00 Uhr die mittlere Luftfeuchte verwenden. Die Haude-Faktoren sind in der nachfolgenden Tabelle nach [Hupfer et al. (2006)](https://www.springer.com/de/book/9783322967497) dargestellt:

|Monat      | Haude-Faktor|
|-----------|------|
| Januar    | 0,20 |
| Februar   | 0,20 |
| März      | 0,21 |
| April     | 0,29 |
| Mai       | 0,29 |
| Juni      | 0,28 |
| Juli      | 0,26 |
| August    | 0,25 |
| September | 0,23 |
| Oktober   | 0,22 |
| November  | 0,20 |
| Dezember  | 0,20 |
{% endcapture %}

<div class="notice--info">
  {{ haude | markdownify }}
</div>
