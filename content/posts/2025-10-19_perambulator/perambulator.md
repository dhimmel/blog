Title: Finding four corners when all the maps are wrong
Slug: perambulator
Date: 2025-10-19
Tags: gis, openstreetmap, osm, enfield, new hampshire, surveying, boundaries
Status: draft

The Four Corners is often thought of where Utah, Colorado, New Mexico, and Arizona collide.
But if are satisfied with a municipal as opposed to statal four corners, you likely can find a quadripoint much closer to home.

In my case, I'd been searching for the meeting point for four municipalities in New Hampshire  --- the towns of Hanover, Canaan, Enfield, and the City of Lebanon.

<!-- https://www.strava.com/activities/5798442786 -->
In 2021, my wife and I set out as newlyweds to find the monument and stand in four towns at once.
We searched the vicinity of where the maps showed the intersection, but found no markers or granite posts.

After four years of reeling in defeat from this failed mission, we set out again.
This time with a bigger expedition that included my partner in a [new venture](https://radoverlay.com/) and our respective offspring.
Parking at the Lakeview Cemetery in Enfield, then walking up the Class IV Old County Road, turning right off the path and up the slope towards the Tom Linnell Ridge trail.
Soon we found the prize.
<!-- https://www.strava.com/activities/15956675704 -->

![The quadripoint of Hanover, Canaan, Enfield, and Lebanon.]({attach}2025-09-27_hcel-four-corners.jpg)

The difference was that this time we were endowed with Page 93 of Kurt Gotthardt's [2010 report](https://www.enfieldnh.gov/media/7556) titled _A History of Enfield Town Lines: From 1761 to 2007_.
Herein the true GPS coordinates were revealed as 43°39′32.72″N 72°09′43.23″W (`43.659089,-72.162008`).

> the USGS topo maps stop showing the town lines after the 1996 series. You can view all of the USGS maps ever produced on [this website](https://www.usgs.gov/the-national-map-data-delivery/topographic-map-access-points). I use the Topoview feature, but have not tried the other options.

If you do not see a square symbol at the corner of where the town lines meet, then it's properly incorrect, and this error properly has been carried over to other maps as an incorrect corner.

<https://www.usgs.gov/index.php/faqs/why-dont-boundaries-us-topo-maps-match-and-why-are-some-missing>

TIGER census tracts have issue

Page 109-110 history

[A Manual on Municipal Boundaries: Perambulating Town Lines in New Hampshire](https://ftp.granit.unh.edu/submissions/MunicipalBounds/2014%20STATE%20GIS%20SUB%20COMMITTEE%20INFO/MANUAL%20ON%20Municipal%20Boundaries%20R&L%20Justified%20-WITH%20NO%20APPENDICES.pdf) by Robert G. Moynihan in 2003
<https://ftp.granit.unh.edu/submissions/MunicipalBounds/2014%20STATE%20GIS%20SUB%20COMMITTEE%20INFO/MANUAL%20ON%20Municipal%20Boundaries%20R&L%20Justified%20-WITH%20NO%20APPENDICES.pdf>

Page 11

> A statewide geographic information system (GIS), named Geographically Referenced Analysis and Information Transfer (GRANIT), has been developed to assist state and local officials make reasoned decisions relative to land use and natural resources issues.
>
> The current Political Boundary Layer of the state GIS was developed from existing United States Geological Survey (USGS) topographic maps with a scale of 1:24,000 (1 inch = 2000 feet). The expected positional accuracy of mapped features at this scale is in the +/- 40 to +/- 60 foot range. While the USGS maps are renowned for their reliability, it was known that some of the town lines on the maps might be incorrectly placed. In fact, a good example of this uncertainty occurs on the USGS “Peterborough North” quadrangle map which currently shows a part of the BenningtonGreenfield town line as 'indefinite boundary'. As the various individual maps were connected together (paneled) it was found that municipal boundaries did not always line up or match. Decisions were made to average the positions if the mismatch was small (less than 40 to 50 feet). Where the alignment of the town line from one map to another was significantly off, a new line segment was added to connect the two ends. This represents only an artificial “fix” and needs to be corrected. Obtaining more accurate positions of the monuments (during perambulations) will allow the system to be updated.

<https://www.openstreetmap.org/changeset/118449523>

<https://www.merrimackvalleylife.com/articles/on-the-hunt-for-boundary-markers/>

515 boundary point nodes in GRANIT as of 2014. <https://ftp.granit.unh.edu/submissions/MunicipalBounds/2014%20STATE%20GIS%20SUB%20COMMITTEE%20INFO/Presentations/R%20Moynihan%20Presentation%202004%20Perambulation%20of%20Town%20Lines%20in%20New%20Hampshire.pdf>
