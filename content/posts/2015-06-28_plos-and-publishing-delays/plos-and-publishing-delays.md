Title: Publication delays at PLOS
Slug: plos-and-publishing-delays
Date: 2015-06-22
Tags: publishing, PLOS, journals, open access


On April 22, 2015 [my research](https://dx.doi.org/10.1101/011569) was formally accepted to *PLOS Computational Biology*. 68 days later the article has yet to published. My [current project](https://dx.doi.org/10.15363/thinklab.4) builds on the forthcoming study and would benefit from its publication. Frustrated, I decided to investigate whether such delays are commonplace at PLOS.

## Publication and acceptance delays at PLOS

I started by retrieving all pubmed records for the 7 PLOS journals. For each journal, I randomly selected 1000 articles and scraped the PLOS website for receival, acceptance, and publication timestamps. Using this scraped data, I plotted publishing delays over time.

![PLOS publication times from website scraping](https://raw.githubusercontent.com/dhimmel/plostime/3e4d95f83b67a57fc9a3d8efc504729cf4f1c130/figure/scraped-plos-publication-times.png "Scraped PLOS publication times")

I am not alone! Starting in 2011, publications delays at *PLOS Comp Bio* began regularly breaching 80 days. *PLOS Genetics*, *Pathogens*, and *Neglected Tropical Diseases* experienced similar publishing delay explosions in 2011, although appear to recently improved. These marked temporal fluctuations suggest that delays are not an innate and immutable characteristic of publishing, but instead dependent on operational efficiency and organizational well-being.

The two oldest and most established PLOS journals, *Biology* and *Medicine*, followed a different pattern: long delays in their early years followed by stability at 40 days since 2009. The dearth of *PLOS Biology* records prior to 2009, resulted from broken DOI redirects. Before my scraper finished its duties, PLOS [fixed the issue](https://twitter.com/dhimmel/status/613842560360951808) resulting in the few visible Biology articles of that period.

The scraped data is nice because it comes directly from the source, but is time intensive and limited to a single webpage layout. Therefore, I also extracted timestamps from pubmed. Below I show publication (solid lines) and acceptance (dotted lines) times from this larger dataset.

![PLOS acceptance and publication times from pubmed](https://raw.githubusercontent.com/dhimmel/plostime/3e4d95f83b67a57fc9a3d8efc504729cf4f1c130/figure/plos-stages.png "PLOS acceptance  times (dotted line) and publication times (solid line)")

With more articles, fine-grained temporal trends emerge. The findings are consistent with the scraped data. *PLOS Comp Bio* appears to have made some recent improvement, but still is over 50 days from acceptance to publication.

Regarding acceptance time, *PLOS Medicine* is an outlier, teetering around the 200 day mark. This finding is in line with my single experience with *PLOS Medicine*, which consisted of poor communication and delays.

*PLOS One* has historically fared well compared to other PLOS journals both in acceptance and publication times. However, delays at *PLOS One* have been relentlessly trending upwards. The focus on technical validity rather than article impact at *PLOS One* likely contributes to quicker review and revision periods.

## Publication and acceptance delays for PLOS alternatives

Next, I decided to compile recent delay information for as many journals as possible. I instructed my pubmed querier to retrieve records for all 1,572,538 publications since 2014. Of these articles, 667,773 had timestamps. Pubmed data is not perfect. For example, 9,945 articles had anachronistic timestamps and were omitted.

I looked at delays for open access journals in my field. Below, publication time distributions are shown for 15 journals.

![Publishing time per journal](https://raw.githubusercontent.com/dhimmel/plostime/3e4d95f83b67a57fc9a3d8efc504729cf4f1c130/figure/publication-days-violinplot.png)

As luck would have it, *PLOS Computational Biology* has the highest median publication time. Since all PLOS journals use the same editorial and typesetting system, the poor performance across the PLOS family is unsurprising.

*eLife* is quickest with a majority of articles published within 3 days after acceptance. The comparison is skewed because *eLife* allows [early access](http://elifesciences.org/content/early/recent) to a pre-formatted article PDF. However, early access provides many of the benefits of publication such as visibility and citability.

Next, I looked at acceptance times for the same 15 journals.

![Acceptance time per journal](https://raw.githubusercontent.com/dhimmel/plostime/3e4d95f83b67a57fc9a3d8efc504729cf4f1c130/figure/acceptance-days-violinplot.png)

*PeerJ* is a clear winner with a median time of 74 days. The variation between journals for acceptance time is less drastic than for publication time: peer review sets a lower limit on the time needed for acceptance.

## Publication and acceptance times for all journals

The table below shows the median days till acceptance and publication for all journals. Journals whose article timestamps were missing from pubmed are not included.

<table id="journals" class="display" cellspacing="0" width="100%">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

## Calling for a journal review service


<link rel="stylesheet" type="text/css" href="//cdn.datatables.net/1.10.7/css/jquery.dataTables.min.css">
<script type="text/javascript" src="//code.jquery.com/jquery-2.1.4.min.js"></script>
<script type="text/javascript" src="//cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready(function() {
    $('#journals').dataTable( {
      "ajax": '//raw.githubusercontent.com/dhimmel/plostime/b81933192a54d2d5432f83fe1bf7d76ac749eb5e/data/journal-times.json',
      aoColumns: [
        { sWidth: '50%', sTitle: 'Journal' },
        { bVisible: false},
        { sTitle: 'Articles' },
        { sTitle: 'Acceptance'},
        { sTitle: 'Publication' } ],
      "order": [[ 2, "desc" ]]}
    );
} );
</script>
