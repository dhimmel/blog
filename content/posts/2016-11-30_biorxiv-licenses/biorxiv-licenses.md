Title: Licensing of bioRxiv preprints
Slug: biorxiv-licenses
Date: 2016-11-30
Tags: bioRxiv, preprints, licensing, Creative Commons, license, CC BY, publishing
Status: draft

Jordan Anaya of Omnes Res, creator of the PrePubMed search engine for biomedical preprints, recently compared _bioRxiv_ to _PeerJ Preprints_. We both agree that _PeerJ_ offers a better user experience with fantastic technology behind their preprint server. However, _bioRxiv_ has greater adoption in the biodata sciences.

In fact, since my last blog post on preprints at the beginning of 2016, _bioRxiv_ has grown by 140% from 2,785 to 6,918 preprints. The growth has been fueled largely by the efforts of [ASAPbio](http://asapbio.org/) and the growing recognition that [publishing delays](http://blog.dhimmel.com/history-of-delays/) are [interfering with science](https://doi.org/10.1038/530148a).

While _PeerJ_ requires that all preprints are published under a Creative Commons Attribution (CC BY) License, _bioRxiv_ allows authors to choose from five options: CC BY, CC BY-ND, CC BY-NC, CC BY-NC-ND, and all rights reserved (no license).

The purpose of Creative Commons licenses is to allow the reuse of content that would otherwise be prohibited by copyright. As a result, the open licensing of preprints is crucial for the growth of open access, the movement to make publicly-funded research articles available to and reusable by the public.

## License breakdown

Unfortunately, of the five options offered by _bioRxiv_, CC BY is the only [open license](http://opendefinition.org/licenses/), which requires that content "can be freely used, modified, and shared by anyone for any purpose." Therefore, with the help of Jordan Anaya, I looked into which licensing options authors were choosing for their _bioRxiv_ preprints. The breakdown shows that there's major room for improvement (see why license choices matter below).

Table goes here

### Licenses over time

Next, I looked to see whether _bioRxiv_ preprints were becoming more open over time. They weren't. In fact, the proportion of CC BY licenses has been in decline since mid 2014.

<div id="date-figure"></div>

### Licenses by subject

Next, I looked at the license breakdown by discipline. The figure below shows all subjects with at least 100 preprints. Bioinformatics appears to be the most open, whereas Cell Biology is the least open.

<div id="subject-figure"></div>

## Author leaderboard

Next, I assigned each preprint a score based on its license: 5 points for CC BY, 3 for CC BY-ND or CC BY-NC, 2 for CC BY-NC-ND, and 1 for all rights reserved. An author's score is the sum of their preprints.

Middle initials were removed to consolidate duplicate names for the same person. If you're worried that this analysis conflates multiple authors with the same name, start using [ORCID](http://orcid.org/ "Persistent digital identifiers for every researcher"). Luckily, with only 29,322 distinct author names, name collisions are yet to be a major problem.

<table id="authors" class="display" cellspacing="0" width="100%">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

Congratulations to [Mark Daly](https://www.broadinstitute.org/bios/mark-daly "Mark Daily at the Broad Institute") of the Broad Institute for leading both in terms of number of preprints and score. Also notable was Jesse Bloom of the Fred Hutchinson Cancer Research Center, who's posted 10 preprints, all under CC BY. Condolences to my advisor, [Casey Greene](http://www.greenelab.com/casey), whose unfortunate decision to post one of his XX bioRxiv preprints under all rights reserved kept him out of the top 10.

## Choosing between licenses

### All rights reserved

Archiving and dissemination

Diego https://www.eff.org/deeplinks/2016/02/stand-diego-support-open-access
Georgia State Case (Cambridge University Press et al. v. Patton et al.) 
https://en.wikipedia.org/wiki/Cambridge_University_Press_v._Patton
https://www.eff.org/deeplinks/2015/10/open-access-human-rights-issue

## Technology

https://github.com/dhimmel/biorxiv-licenses

[Medium Post](https://medium.com/@OmnesRes/so-i-went-ahead-and-grabbed-the-licensing-information-for-each-article-de0414b4ca3a) by Jordan Anaya of Omnes Res.

<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.12/css/jquery.dataTables.css">
<script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.js"></script>


<script src="//d3js.org/d3.v3.min.js"></script>
<script src="//vega.github.io/vega/vega.js"></script>
<script src="//vega.github.io/vega-lite/vega-lite.js"></script>
<script src="//vega.github.io/vega-editor/vendor/vega-embed.js" charset="utf-8"></script>

<style media="screen">
  .vega-actions a {
    margin-right: 5px;
  }
</style>

<script>
var base_url = 'https://raw.githubusercontent.com/dhimmel/biorxiv-licenses';
var commit = 'master';


$(document).ready(function () {
    $('#authors').dataTable({
        ajax: `${base_url}/${commit}/data/author-scores.json`,
        aoColumns: [
            {sWidth: '50%', sTitle: 'Author'},
            {sTitle: 'Preprints'},
            {sTitle: 'Score'}
        ],
        order: [[2, "desc"]],
        search: {regex: true}
    });
});

var actions = {export: true, source: false, editor: true};

var json_url = `${base_url}/${commit}/figure/license-vs-time/vega-lite-spec.json`;
var embedSpec = {mode: "vega-lite", url: json_url, renderer: 'svg', actions: actions};
vg.embed("#date-figure", embedSpec, function(error, result) {});

var json_url = `${base_url}/${commit}/figure/license-vs-subject/vega-lite-spec.json`;
var embedSpec = {mode: "vega-lite", url: json_url, renderer: 'svg', actions: actions};
vg.embed("#subject-figure", embedSpec, function(error, result) {});

</script>
