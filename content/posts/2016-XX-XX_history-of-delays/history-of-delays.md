Title: The history of publishing delays
Slug: history-of-delays
Date: 2016-02-10
Tags: publishing delays
Status: draft

**Notice:** Unpublished work by Daniel Himmelstein, all rights reserved until this notice is removed. Please do not share this page until its publication.

***

Last July, I [released a summary](http://blog.dhimmel.com/plos-and-publishing-delays/#journals_wrapper) of the recent publishing delays at 3,475 journals. The post attracted lots of attention via [Twitter](https://twitter.com/dhimmel/status/615624280026394625) and [*Nature News*](https://doi.org/10.1038/523131f), primarily because scientists are frustrated with the sluggish pace of publishing.

However, a major question remained. Are publication delays getting better or worse? Kendall Powell, writing a feature for *Nature News* released in tandem with this post, contacted me. Her investigation had uncovered a widespread belief that delays were worsening with time. But she wanted data, and the existing data was highly [concentrated](http://wp.me/p4Ir7n-5Y) or [anecdotal](https://doi.org/10.1096/fj.12-0901ufm).

So I set out to uncover the history of publishing delays. Using PubMed, I extracted

+ **acceptance delays**—days from receival to acceptance—for 3,238,646 articles since 1965
+ **publishing delays**—days from acceptance to online publication—for 2,661,145 articles since 1997

through the end of 2015.

## Acceptance delays

The time between submission and acceptance encapsulates editorial decision, peer review, and revision. Below, we visualize 51 years of acceptance delays. Each year, the green lines indicate delay percentiles, spaced every 2.5 points with quartiles bolded. The gray band displays a curve fitted for all articles over time.

![Acceptance delay versus year accepted](https://raw.githubusercontent.com/dhimmel/delays/75fef346ac44acea6ae6f7536d1ab584758b9518/viz/acceptance-by-article.png "51 years of acceptance delays")

The number of journals reporting acceptance delays prior to 1981 [is in](https://github.com/dhimmel/delays/blob/19506467197da6a487aec51fe92a212d78ccae0f/data/year-summaries.tsv) the single digits, so drawing conclusions on those early years would be premature. However since 1981, the median acceptance delay has teetered around the 100 day mark. So on a per article level, acceptance delays don't appear to be worsening. If anything, long delays are becoming less frequent as evidenced by the downward sloping third quartile line and best-fit curve since 1988.

Interested in a specific journal? Use the selection box below to explore its acceptance delay history. Red dots represent individual articles.

<img id="delay-img-accept" style="width:100%;">

<select id="select-accept" style="width:100%"></select>

## Publication delays

Online publication [began in the '90s](https://doi.org/10.3998/3336451.0003.212) and quickly became standard. Nowadays, since print rarely precedes online access, an article's online debut is its effective date of publication. Conveniently in PubMed, precise dates are considerably more available for online compared to print publication.

The time between acceptance and online publication encapsulates typesetting, proofing, and occasionally press releasing. The plot below shows the history of online publication delays since 2000, the first year with a double-digit number of journals.

![Publication delay versus year published](https://raw.githubusercontent.com/dhimmel/delays/75fef346ac44acea6ae6f7536d1ab584758b9518/viz/publication-by-article.png "16 years of online publication delays")

Publication delays have approximately been cut in half since the early 2000s. Progress hit a plateau in 2009 with the median delay stabilizing around 25 days. However, the longest delays steadily decreased up until 2014.

These findings illustrate the transformative power of the digital age: publication speed doubled and now greater transparency will bring scrutiny to the stragglers, who will hopefully pick up their pace. Use the selection box below to view the publication delay history of a specific journal.

<img id="delay-img-publish" style="width:100%;">

<select id="select-publish" style="width:100%"></select>

## Journal trends

The last decade witnessed the rise of the megajournal. By [rapidly publishing a large quantity](https://doi.org/10.7717/peerj.981) of articles, megajournals could be driving article-level delay trends. So what about journal-level delay trends? If you select a random journal, are you more likely to see increasing or decreasing delays?

For each journal, we regressed article delay versus date. The resulting slope indicates the average number of days a journal's delays increased per year. The distributions of these slopes are shown below. Dashes indicate quartiles and crosses indicate means.

![Journal-level delay trends](https://raw.githubusercontent.com/dhimmel/delays/19506467197da6a487aec51fe92a212d78ccae0f/viz/slope-distributions.png)

69% percent of journals experienced decreasing publication delays. However in terms of acceptance delays, journals are roughly split between quickening and slowing. The positive skew of the acceptance distribution suggests that the slowing journals have slowed more than the quickening journals have quickened, although this effect is minor.

## Limitations

+ Only includes published articles, rejections may be different
+ Non-selection bias
+ Errant data
+ Receival is initial submission or revised submission
+ provisional PDF

<script src="https://code.jquery.com/jquery-2.1.4.min.js" type="text/javascript"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.1/js/select2.min.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.1/css/select2.min.css" rel="stylesheet" />

<script type="text/javascript">

  function update_image(type) {
    var nlm_id = jQuery('#select-' + type).val();
    console.log('update_image', type, nlm_id );
    var url = "https://raw.githubusercontent.com/dhimmel/delays/" + commit + "/viz/journal/" + type + '/' + nlm_id + '.png';
    jQuery('#delay-img-' + type).attr('src', url);
  }

  function initialize_select(data, type) {
    console.log('initialize_select', data, type )
    jQuery('#select-' + type).select2({
      data: data,
      placeholder: "Select a journal"
    });
    //jQuery('#select-' + type).val('0001027');
    update_image(type);
  }

  var commit = "75fef346ac44acea6ae6f7536d1ab584758b9518";

  // accept
  var url = "https://raw.githubusercontent.com/dhimmel/delays/" + commit  + "/webapp/select2-accept" + ".json";
  jQuery.getJSON( url, callback=function( data ) {
    initialize_select(data, 'accept');
    });
  jQuery('#select-accept').on("select2:select", function(e) {
    update_image('accept');
    });

  // publish
  var url = "https://raw.githubusercontent.com/dhimmel/delays/" + commit  + "/webapp/select2-publish" + ".json";
  jQuery.getJSON( url, callback=function( data ) {
    initialize_select(data, 'publish');
    });
  jQuery('#select-publish').on("select2:select", function(e) {
    update_image('publish');
    });

</script>
