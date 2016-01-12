Title: The history of publishing delays
Slug: history-of-delays
Date: 2016-02-10
Tags: publishing delays
Status: draft

**Notice:** Unpublished work by Daniel Himmelstein, all rights reserved until this notice is removed. Please do not share this page until its publication.

***

Last July, I [released a summary](http://blog.dhimmel.com/plos-and-publishing-delays/#journals_wrapper) of the recent publishing delays at 3,475 journals. The post attracted lots of attention via [Twitter](https://twitter.com/dhimmel/status/615624280026394625) and [*Nature News*](https://doi.org/10.1038/523131f), primarily because scientists are frustrated with the sluggish pace of publishing.

However, a major question remained. Are publication delays getting better or worse? Kendall Powell, writing a feature article for *Nature News* released in tandem with this post, contacted me. Her investigation had uncovered a widespread belief that delays were worsening with time. But she wanted data, and the existing data was highly [concentrated](http://wp.me/p4Ir7n-5Y) or [anecdotal](https://doi.org/10.1096/fj.12-0901ufm).

So I set out to uncover the history of publishing delays. Using PubMed, I extracted:

+ **acceptance delays**—days from receival to acceptance—for 3,238,646 articles since 1965
+ **publishing delays**—days from acceptance to online publication—for 2,661,145 articles since 1997

## Acceptance delays

Green lines show the delay percentiles for each year and are spaced every 2.5<sup>th</sup>%. Quartiles are bold. The best-fit curve is shown as a gray band.

![Acceptance delays](https://raw.githubusercontent.com/dhimmel/delays/75fef346ac44acea6ae6f7536d1ab584758b9518/viz/acceptance-by-article.png)

Select your journal of interest to see historical acceptance delays. Individual articles are represented as red dots.

<img id="delay-img-accept" style="width:100%;">

<select id="select-accept" style="width:100%"></select>

## Publication delays

Time from acceptance to online publication

![Publication delays](https://raw.githubusercontent.com/dhimmel/delays/75fef346ac44acea6ae6f7536d1ab584758b9518/viz/publication-by-article.png)

<img id="delay-img-publish" style="width:100%;">

<select id="select-publish" style="width:100%"></select>

## Journal trends

![Change in delays over time](https://raw.githubusercontent.com/dhimmel/delays/19506467197da6a487aec51fe92a212d78ccae0f/viz/slope-distributions.png)

## Limitations

+ Only includes published articles, rejections may be different
+ Journal reported
+ Data quality

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
