Title: Finding four corners when all the maps are wrong
Slug: perambulator
Date: 2025-10-19
Tags: gis, openstreetmap, osm, enfield, new hampshire, surveying, boundaries
Status: draft

The Four Corners is often thought of where Utah, Colorado, New Mexico, and Arizona collide.
But if are satisfied with a municipal as opposed to statal four corners, you likely can find a quadripoint much closer to home.

In my case, I'd been searching for the meeting point for four municipalities in New Hampshire — the towns of Hanover, Canaan, Enfield, and the City of Lebanon.

<!-- https://www.strava.com/activities/5798442786 -->
In 2021, my wife and I set out as newlyweds to find the monument and stand in four towns at once.
We searched the vicinity of where the maps showed the intersection, but found no markers or granite posts.

After four years of reeling in defeat from this failed mission, we set out again.
This time with a bigger expedition that included my partner in a [new venture](https://radoverlay.com/) and our respective offspring.
Parking at the Lakeview Cemetery in Enfield, then walking up the Class IV Old County Road, turning right off the path and up the slope towards the Tom Linnell Ridge trail.
Soon we found the prize.
<!-- https://www.strava.com/activities/15956675704 -->

![The quadripoint of Hanover, Canaan, Enfield, and Lebanon.]({attach}2025-09-27_hcel-four-corners.jpg)

The difference was that this time we were endued with Page 93 of Kurt Gotthardt's [2010 report](https://www.enfieldnh.gov/media/7556) titled _A History of Enfield Town Lines: From 1761 to 2007_.
Herein the true GPS coordinates were revealed as 43°39′32.72″N 72°09′43.23″W (`43.659089,-72.162008`).

Gotthardt dedicated his report to "to all of those who walked the Town Lines before me".
Walking the lines refers to _perambulation_.
New Hampshire law requires that towns perform this act with regularity:

> The lines between the towns in this state shall be perambulated, and the marks and bounds renewed, once in every 7 years forever, by the selectmen of the towns, or by such persons as they shall in writing appoint for that purpose.

Despite the statute, only 15 of 110 towns [surveyed](https://ftp.granit.unh.edu/submissions/MunicipalBounds/2014%20STATE%20GIS%20SUB%20COMMITTEE%20INFO/Articles/NHMunicipal%20Assoc%20Perambulation%20Data%20Report%202010.pdf "NHMA Perambulation Survey: Total-Sample Data Summary. 2010-07-28") in 2010 had comprehensively walked their lines.
And a 2017 [bill](https://legiscan.com/NH/bill/SB171/2017, "New Hampshire Senate Bill 171") sought to repeal the duty altogether,
passing the Senate with a voice vote before the House deemed the matter "inexpedient to legislate".

Gotthardt has participated in XX perambulations of Enfield, first in XXXX and most recently in XXXX.
<!-- quick bio of Gotthardt, how he became interested in this, his perambulation partner, etc -->
In the case of my search for the HCEL corner, Gotthardt's GPS coordinates for the marker proved critical as well as the report's online availability and indexing by search engines.

In my earlier attempt to locate the quadripoint, I had gone to the location where maps showed the intersection.
However, it turns out the maps were wrong to the tune of 500 feet.
I asked Gotthardt how this could be, to which he provided a detailed historical account:

> The problem with the maps showing Enfield/Lebanon town line is that they are all based on a 1927 USGS topo map that showed the town lines on it, but the map makers were not sure where all of the true corners were located.
> For example, the Enfield/Lebanon town line is a straight line per both Charters that created those towns, but if you put a straight edge on that line as shown on any USGS topo map it will show a bend in the line as it crosses Mascoma Lake.
> They also needed to have the Cannan town line meet the Enfield/Lebanon/Hanover town lines,
> so they "adjusted" the lines to all meet.
>
> Unfortunately this error has carried forward to today's maps.
> Some USGS topo maps that show town lines will actually state on the map next to the line "approximate location".
> If you look closely at the USGS topo maps, you will see a small square located along some town lines where they cross a road,
> those are locations where the map makers located a town line monument at some point in time,
> they too are carried forward onto any future USGS topo maps.
> Some of those monuments are still there, others have been lost or are missing.
> The USGS topo maps are the best reference maps for topo features, but political boundaries are not topo features.

Here is the 1996 USGS Topo map, with <span style="text-decoration-line: underline; text-decoration-color: #8210C4;">purple markup</span> to show town names and the true location of the four corners.

![The 1996 USGS Topo map showing the Hanover, Canaan, Enfield, and Lebanon border from the NH_Enfield_329548_1996_24000_geo. Markup in purple]({attach}usgs-topo-map-1996-hcel-four-corners-with-markup-reduced.png)

I started to wonder whether all maps were wrong?
I found the HCEL quadripoint was misplaced on OpenStreetMap, Google Maps, Apple Maps, NH GRANIT, [TIGER](https://tigerweb.geo.census.gov/tigerweb/) census tracts, the 2024 DeLorme Atlas & Gazetteer, Lebanon's [MapGeo](https://lebanonnh.mapgeo.io/), and Hanover's [AxisGIS](https://www.axisgis.com/HanoverNH/) (some layers correct).

GRANIT is New Hampshire's statewide geographic information system.
Robert Moynihan expounds on how political boundaries were added to GRANIT in a 2003 report titled [A Manual on Municipal Boundaries: Perambulating Town Lines in New Hampshire](https://ftp.granit.unh.edu/submissions/MunicipalBounds/2014%20STATE%20GIS%20SUB%20COMMITTEE%20INFO/MANUAL%20ON%20Municipal%20Boundaries%20R&L%20Justified%20-WITH%20NO%20APPENDICES.pdf "A Manual on Municipal Boundaries: Perambulating Town Lines in New Hampshire. By UNH Professor Robert Moynihan. 2003-09. Page 11"):

> The current Political Boundary Layer of the state GIS was developed from existing United States Geological Survey (USGS) topographic maps with a scale of 1:24,000 (1 inch = 2000 feet). The expected positional accuracy of mapped features at this scale is in the ± 40 to ± 60 foot range. While the USGS maps are renowned for their reliability, it was known that some of the town lines on the maps might be incorrectly placed. In fact, a good example of this uncertainty occurs on the USGS “Peterborough North” quadrangle map which currently shows a part of the Bennington–Greenfield town line as 'indefinite boundary'. As the various individual maps were connected together (paneled) it was found that municipal boundaries did not always line up or match. Decisions were made to average the positions if the mismatch was small (less than 40 to 50 feet). Where the alignment of the town line from one map to another was significantly off, a new line segment was added to connect the two ends. This represents only an artificial “fix” and needs to be corrected. Obtaining more accurate positions of the monuments (during perambulations) will allow the system to be updated.

In my correspondence with Gotthardt, I asked him how prevalent misplaced corners are.
His response:

> The USGS topo maps stop showing the town lines after the 1996 series. … If you do not see a square symbol at the corner of where the town lines meet, then it's probably incorrect, and this error probably has been carried over to other maps as an incorrect corner.

So we have now established that:

1. many political boundary corners in the USGS topo maps were approximates and hence may deviate considerably from the actual monument location.
2. most maps derive their town boundaries from USGS topo maps.
3. parambulation is the official mechanism to locate the true boundaries, which can then be updated on maps.

Hence a concerted effort is now needed to establish the location of all town corners in New Hampshire by means of parambulation.
And once enshrined in parambulation reports, the coordinates shall be used to refine the location of political boundaries on maps and in geographic information systems.

I decided to do my part by updating OpenStreetMap.
I describe OpenSteetMap as the _one map to rule them all_,
since it is the only mature platform that meets all critical criteria:
global, broad, crowd-sourced, and reusable under an open license.
Make an edit on OpenSteetMap and in due time you will likely see it appear in the wild,
as many maps are based on OpenSteetMap data.
Make an edit to a map other than OpenSteetMap and prepare for your effort to be lost to the sands of time or the silos of exclusivity.

The unit of change in OpenStreetMaps is called a _changeset_, which a bundle of edits (like a commit in Git parlance).
My edits consisted of 3 changesets: [172589326](https://osmcha.org/changesets/172589326) to move the boundary stone close to the parambulated coordinates in the iD editor, [173198750](https://www.openstreetmap.org/changeset/173198750) to make the boundary stone to exactly the parambulated coordinates in the JOSM editor, and [173652662](https://osmcha.org/changesets/173652662) to update the metadata on the boundary stone to note the discrepancy with the TIGER/USGS location.

At the time of writing, the OpenStreetMap [node](https://www.openstreetmap.org/node/9012708145) for the quadripoint has the following metadata tags:

```txt
boundary: marker
historic: boundary_stone
height: 0.9652
material: granite
inscription: E C H L
name: Enfield/Lebanon/Hanover/Canaan Granite Post
note: Located at 43.659089, -72.162008 according to https://www.enfieldnh.gov/media/7556#page=93. Note that the USGS map location is approximate and incorrect and this incorrect location was adopted by GRANIT and many other maps.
```

<!-- double check inscription -->
In the end, I moved the location of boundary by XX feet (XX meters), which increased the size of the Enfield by XX% (from XX to XX square miles).

If you're looking to visit another Enfield boundary by foot, the Enfield/Plainfield/Grantham Corner ([node](https://www.openstreetmap.org/node/13230460968), coordinates XX) is a worthy of exploration.
I was drawn to this boundary, since it also had an approximate USGS location and I like to survey with my own eyes before editing OpenStreetMap.
Located in the Upper Valley Land Trust's [Snow Mountain Conservation Area](https://uvlt.org/conservation-areas/snow-mountain/),
you can visit two nearby towers, only one of which still operates.
Don't miss the ponds in the vicinity, one which empties to the north into Stony Brook and then the Mascoma River and second that gives rise to Great Brook to the south before emptying into the Connecticut River.
What different trajectories for water bodies that are within 500 feet of each other!
<!-- https://www.strava.com/activities/16130218018 -->

![The pond in the Snow Mountain Conservation Area that drains into Stony Brook with the operating cellular tower in the background]({attach}2025-10-13_snow-mountain-pond.jpg)

***

> The other point regarding using the granite post as the true corner point for the 4 towns is the other rule of surveying regarding what takes precedence when a new or re-survey is done, and this is called "rules of construction" which dictates which "deed" (or charter) description to use when determining where a corner is located. See [this article](https://www.washingtonsurveyor.com/blog/priority-of-calls-aka-rules-of-construction-what-they-are-and-why-they-matter) for a good description. So even though the original charter stated compass bearings and distances, when the first surveyors put a stake in the ground and called it the corner and everybody accepted it as the corner, it became the "true" corner regardless of what the written description stated.

What percent did this resize enfield?
<https://osmcha.org/changesets/118449523>

<https://www.usgs.gov/index.php/faqs/why-dont-boundaries-us-topo-maps-match-and-why-are-some-missing>

TIGER census tracts have issue

Page 109-110 history

<https://www.openstreetmap.org/changeset/118449523>

<https://www.merrimackvalleylife.com/articles/on-the-hunt-for-boundary-markers/>

515 boundary point nodes in GRANIT as of 2014. <https://ftp.granit.unh.edu/submissions/MunicipalBounds/2014%20STATE%20GIS%20SUB%20COMMITTEE%20INFO/Presentations/R%20Moynihan%20Presentation%202004%20Perambulation%20of%20Town%20Lines%20in%20New%20Hampshire.pdf>

<https://www.nhpr.org/nh-news/2015-05-23/why-new-hampshire-towns-are-supposed-to-walk-their-boundaries-even-in-the-gps-age>
<https://www.citizenscount.org/news/town-line-perambulation-law>

360 Years of Perambulation
New Hampshire Town and City, November/December 2010
By Christopher J. Porter
<https://ftp.granit.unh.edu/submissions/MunicipalBounds/2014%20STATE%20GIS%20SUB%20COMMITTEE%20INFO/Articles/360%20Years%20of%20Perambulation%20%20NH%20Cities%20and%20Town%20Magazine%20Article%20Nov-Dec%202010.pdf>

<https://www.enfieldnh.gov/media/12106>

1827 law

> The rules of surveying state that the corners as monumented when the original survey was conducted are the true corners
...
As a side note regarding the location of town lines, the line is a straight line from "corner to corner", you are not locating a true town line if you only look at the line from one reference monument to another reference monument. These reference monuments were placed for convenience only.

The other point regarding using the granite post as the true corner point for the 4 towns is the other rule of surveying regarding what takes precedence when a new or re-survey is done, and this is called "rules of construction" which dictates which "deed" (or charter) description to use when determining where a corner is located. See the article below for a good description. So even though the original charter stated compass bearings and distances, when the first surveyors put a stake in the ground and called it the corner and everybody accepted it as the corner, it became the "true" corner regardless of what the written description stated.
<https://www.washingtonsurveyor.com/blog/priority-of-calls-aka-rules-of-construction-what-they-are-and-why-they-matter>
