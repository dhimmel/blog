Title: The history of publishing delays
Slug: history-of-delays
Date: 2016-01-20
Tags: publishing delays
Status: draft

**Copyright notice:** Unpublished work by Daniel Himmelstein, all rights reserved until this notice is removed.

## Acceptance delays

Green lines show the delay percentiles for each year and are spaced every 2.5<sup>th</sup>%. Quartiles are bold. The best-fit curve is shown as a gray band.

![Acceptance delays](https://raw.githubusercontent.com/dhimmel/delays/fe80fe4ee0eece86ff694bc973964a5651a4e18f/viz/acceptance-by-article.png)

Select your journal of interest to see historical acceptance delays. Individual articles are represented as red dots.

<img id="delay-img-accept" style="width:100%;">

<select id="select-accept" style="width:100%"></select>

## Publication delays

Time from acceptance to online publication

![Publication delays](https://raw.githubusercontent.com/dhimmel/delays/fe80fe4ee0eece86ff694bc973964a5651a4e18f/viz/publication-by-article.png)

<img id="delay-img-publish" style="width:100%;">

<select id="select-publish" style="width:100%"></select>


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

  var commit = "fe80fe4ee0eece86ff694bc973964a5651a4e18f";

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
