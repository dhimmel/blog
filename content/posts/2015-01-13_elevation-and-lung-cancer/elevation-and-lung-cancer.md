Title: Elevation, Oxygen, and Cancer of the Lung
Slug: elevation-and-lung-cancer
Date: 2015-01-13
Tags: altitude, cancer, counties, elevation, epidemiology, incidence, lung cancer, oncology, oxygen, statistics

For the past two years, [Kamen Simeonov](http://www.ksimeonov.com/ "Kamen Simeonov Homepage") and I have been working on a project codenamed _The Lung_. Today is _PeerJ Publication Day_ and the results of our research are now online:

> Simeonov KP, Himmelstein DS (2015) **Lung cancer incidence decreases with elevation: evidence for oxygen as an inhaled carcinogen**. _PeerJ_ 2:e705 [doi:10.7717/peerj.705](http://dx.doi.org/10.7717/peerj.705 "Lung cancer incidence decreases with elevation")
> <div data-badge-popover="right" data-badge-type="large-bar" data-doi="10.7717/peerj.705" data-hide-no-mentions="true" class="altmetric-embed"></div>

## Findings

In this study, we investigated whether cancer rates varied with altitude. Our primary focus was lung cancer, since the lung comes into direct contact with inhaled air and the level of atmospheric oxygen decreases with elevation. The same reactivity of oxygen that makes it an ideal input for respiration also risks causing cellular damage and mutation. Therefore, we evaluated whether inhaled oxygen is a human carcinogen by investigating the association between cancer and elevation. We analyzed ~250 counties in the Western United States, where the mountainous terrain results in varying elevations and high quality county data is available.

We found that lung cancer decreased dramatically with rising elevation. This trend did not extend to breast, colorectal, or prostate cancer supporting our hypothesis that the elevation-dependent carcinogen is inhaled. The association between lung cancer and elevation remained after accounting for potential confounding factors, such as smoking, pollution, and obesity. Additionally, other environmental variables that could protect against lung cancer, such as UVB exposure (an indicator of sunlight-induced vitamin D synthesis), were unable to replace the effect of elevation.

To convey the magnitude of the observed association, we imagine a hypothetical situation where the entire United States elevates to the level of the highest US county (San Juan, Colorado at 3,473 meters / 11,395 feet). Were all other factors to remain constant, we estimate 65,496 fewer new cases of lung cancer would arise per year. For comparison, 224,210 new cases of lung cancer [arose](http://dx.doi.org/10.3322/caac.21208 "Cancer statistics, 2014") in the United States last year.

While we don't recommend anyone relocate just yet and the risk for nonsmokers is low, experimental confirmation of oxygen-driven tumorgenesis could lead to new insights that yield better lung cancer preventions and treatment. Learn more about our findings in the [press release](http://eurekalert.org/e/64Wk "Press Release: Can inhaled oxygen cause cancer?") or see *SciShow's* [video summary](https://youtu.be/HrIrB9reWwQ?t=89s):

<iframe width="604" height="340" src="https://www.youtube.com/embed/HrIrB9reWwQ?start=89&#038;feature=oembed" frameborder="0" allowfullscreen></iframe>

## Visualization

Interact with this scatterplot to explore the relationship between elevation and lung cancer. The bivariate plot shows unadjusted lung cancer incidence decreasing with county elevation. The partial regression plot shows the relationship while accounting for additional factors, such as smoking and education. Accounting for the additional factors sharpened the association. Vector (pdf) versions of the manuscript figures are [available from the project's repository](https://github.com/dhimmel/elevcan/tree/master/manual/figures/vectors "Project GitHub -- Vector Images"). 

<iframe src="http://dipper.ucsf.edu:3838/elevcan" style="border: none; width: 100%; height: 645px">Shiny Visualization</iframe>


<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
