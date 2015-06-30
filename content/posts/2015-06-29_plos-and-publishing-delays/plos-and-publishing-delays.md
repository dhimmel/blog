Title: Publication delays at PLOS and 3,475 other journals
Slug: plos-and-publishing-delays
Date: 2015-06-29
Tags: publishing, PLOS, journals, open access, acceptance time, publication time, PLOS Computational Biology, PubMed, scraping

On April 22, 2015 my research was formally accepted to *PLOS Computational Biology*. 68 days later the article has yet to be published. My [current project](https://dx.doi.org/10.15363/thinklab.4) builds on the [forthcoming study](https://dx.doi.org/10.1101/011569) and would benefit from its publication. Frustrated, I decided to investigate whether such delays are commonplace at PLOS.

## Publication and acceptance delays at PLOS

I started by retrieving all PubMed records for the 7 PLOS journals. For each journal, I randomly selected 1000 articles and scraped the PLOS website for receival, acceptance, and publication timestamps. Using this scraped data, I plotted publishing delays over time.

![PLOS publication times from website scraping](https://raw.githubusercontent.com/dhimmel/plostime/39ff289cae08c81bce6aed499e8df391a05b2107/figure/scraped-plos-publication-times.png "Scraped PLOS publication times")

I am not alone! Starting in 2011, publications delays at *PLOS Computational Biology* began regularly breaching 80 days. *PLOS Genetics*, *Pathogens*, and *Neglected Tropical Diseases* experienced similar publishing delay explosions in 2011, although appear to have recently improved. These extreme temporal fluctuations suggest that delays are not an innate and immutable characteristic of publishing, but instead dependent on operational efficiency and organizational well-being.

The two oldest and most established PLOS journals, *Biology* and *Medicine*, followed a different pattern: long delays in their early years followed by stability at 40 days since 2009. The dearth of *PLOS Biology* records prior to 2009, resulted from broken DOI redirects. Before my scraper finished its duties, PLOS [fixed the issue](https://twitter.com/dhimmel/status/613842560360951808) resulting in the few visible *Biology* articles of that period.

The scraped data is nice because it comes directly from the source, but is time intensive and limited to a single webpage layout. Therefore, I also extracted timestamps from PubMed. Below I show publication (solid lines) and acceptance (dotted lines) times from this larger dataset.

![PLOS acceptance and publication times from PubMed](https://raw.githubusercontent.com/dhimmel/plostime/39ff289cae08c81bce6aed499e8df391a05b2107/figure/plos-stages.png "PLOS acceptance  times (dotted line) and publication times (solid line)")

With more articles, fine-grained temporal trends emerge. The findings are consistent with the scraped data. *PLOS Computational Biology* appears to have made some recent improvement, but still is over 50 days from acceptance to publication.

Regarding acceptance time, *PLOS Medicine* is an outlier, teetering around the 200 day mark. This finding is in line with my single experience with *PLOS Medicine*, which consisted of poor communication and delays.

*PLOS One* has historically fared well compared to other PLOS journals both in acceptance and publication times. However, delays at *PLOS One* have been relentlessly trending upwards. The focus on technical validity rather than article impact at *PLOS One* likely contributes to quicker review and revision periods.

## Publication and acceptance delays for PLOS alternatives

Next, I decided to compile recent delay information for as many journals as possible. I instructed my PubMed querier to retrieve records for all 1,572,538 publications since 2014. Of these articles, 667,773 had timestamps. PubMed data is not perfect. For example, 9,945 articles had anachronistic timestamps and were omitted.

I looked at delays for open access journals in my field. Below, publication time distributions are shown for 16 journals.

![Publishing time per journal](https://raw.githubusercontent.com/dhimmel/plostime/39ff289cae08c81bce6aed499e8df391a05b2107/figure/publication-days-violinplot.png)

As luck would have it, *PLOS Computational Biology* has the highest median publication time. Since all PLOS journals use the same editorial and typesetting system, the poor performance across the PLOS family is unsurprising.

*eLife* is quickest with a majority of articles published within 3 days after acceptance. The comparison is skewed because *eLife* allows [early access](http://elifesciences.org/content/early/recent) to a pre-formatted article PDF. However, early access provides many of the benefits of publication such as visibility and citability.

Next, I looked at acceptance times for the same 16 journals.

![Acceptance time per journal](https://raw.githubusercontent.com/dhimmel/plostime/39ff289cae08c81bce6aed499e8df391a05b2107/figure/acceptance-days-violinplot.png)

*PeerJ* is a clear winner with a median time of 74 days. The variation between journals for acceptance time is less drastic than for publication time: peer review sets a lower limit on the time needed for acceptance.

## Publication and acceptance times for all journals

The table below shows the median days till acceptance and publication for 3,482 journals. A journal may be omitted if it is not indexed by PubMed or had no timestamped articles since 2014.

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

Acceptance and publication times are not the only factor to consider when selecting a journal. Traditionally, the impact factor -- average citations for articles published in the two preceding years -- has been a primary criteria. However, any single metric is insufficient to make an informed decision on where to submit. A host of other journal attributes matter such as readership, aesthetics, communication, friendliness, flexibility, features, and web nativity.

I propose a journal review service. Like yelp for scientific publishing except that author reviews will be [CC-BY](https://creativecommons.org/licenses/by/4.0/). I see three main benefits:

1. Transparency -- past author experiences with a journal are a treasure trove in need of a display case
1. Search -- even finding all journals that publish research in your field is difficult. A search feature would support filters and rankings based on user preferences.
3. Progress -- journals can improve based on their feedback. If not, they will perish.

Let us know in the comments if any services already exist to fulfill this role.

## In conclusion

My goal in performing this extensive evaluation of PLOS publishing times was to bring light to an area of publishing that needed it. PLOS led the open access revolution and still has its unique advantages. Hopefully, public feedback will allow PLOS to improve in the areas where it struggles.

Check out the [GitHub repository](https://github.com/dhimmel/plostime) for source code, datasets, and figures.

<link rel="stylesheet" type="text/css" href="//cdn.datatables.net/1.10.7/css/jquery.dataTables.min.css">
<script type="text/javascript" src="//code.jquery.com/jquery-2.1.4.min.js"></script>
<script type="text/javascript" src="//cdn.datatables.net/1.10.7/js/jquery.dataTables.min.js"></script>

<script>
$(document).ready(function() {
    $('#journals').dataTable( {
      "ajax": '//raw.githubusercontent.com/dhimmel/plostime/39ff289cae08c81bce6aed499e8df391a05b2107/data/journal-times.json',
      aoColumns: [
        { sWidth: '50%', sTitle: 'Journal' },
        { bVisible: false},
        { sTitle: 'Articles' },
        { sTitle: 'Acceptance'},
        { sTitle: 'Publication' } ],
      "order": [[ 2, "desc" ]],
      "search": { "regex": true }
}
    );
} );
</script>
