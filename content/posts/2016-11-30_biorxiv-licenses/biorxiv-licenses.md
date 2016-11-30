Title: Licensing of bioRxiv preprints
Slug: biorxiv-licenses
Date: 2016-11-30
Tags: bioRxiv, preprints, licensing, Creative Commons, license, CC BY, publishing
Status: draft

[Medium Post](https://medium.com/@OmnesRes/so-i-went-ahead-and-grabbed-the-licensing-information-for-each-article-de0414b4ca3a) by Jordan Anaya of Omnes Res.

## Licenses over time

BioRxiv preprints don't appear to be getting more open over time. In fact, the proportion of CC BY licenses has been in decline since mid 2014.

<div id="date-figure"></div>

## Licenses by subject

Subjects with at least 100 preprints are shown. Bioinformatics appears to be the most open, whereas Cell Biology is the least open.
<div id="subject-figure"></div>

## Author scores

Each preprint received a score based on its license: 5 points for CC BY, 3 for CC BY-ND or CC BY-NC, 2 for CC BY-NC-ND, and 1 for all rights reserved. An authors score equals the sum of their preprints.

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
var commit = '2f1c2cd37ff234c173d6cde919d33776a5ca1753';


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
