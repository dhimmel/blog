Title: On author versus numeric citation styles
Slug: cite-styles
Date: 2018-03-20
Tags: bibliography, references, citations, works cited, journals, Manubot, eLife, PeerJ, Thinklab
Status: draft

Should citations in scholarly writing appear as author-year snippets, like ([Pantcheva, 2018](http://site.uit.no/english/writing-style/citationstyles/ "Citation styles: Vancouver and Harvard systems"); [Zelle, 2015](http://docs.citationstyles.org/en/1.0.1/primer.html "Primer — An Introduction to CSL: v1.0.1")), or numbers, like [[1](https://www.nottingham.ac.uk/studyingeffectively/writing/referencing/styles.aspx "Studying Effectively: Referencing styles. University of Nottingham"),[2](https://library.wur.nl/infoboard/7_citing/citation_styles.html "Author-date or numeric style. Wageningen University & Research")]?
Let's refer to these two methods as _author-style_ and _numeric-style_.
You may have also heard them referred to as the [Harvard](https://en.wikipedia.org/wiki/Parenthetical_referencing) and [Vancouver](https://en.wikipedia.org/wiki/Vancouver_system) referencing systems.

## Author-style

Here's an example of author-style from our recent Sci-Hub Coverage Study published in _eLife_.
First, see how citations appear in the main text:

![Sci-Hub Coverage Study in eLife: author-style citations]({attach}scihub-cites-author.png)

Notice how studies with 3 or more authors use "et al." rather than listing every single author.
Also note how the letter `a` was appended to `Van Noorden, 2013` to denote that this is the first of the two Van Noorden articles from 2013 that we cited.

With author-style, references (items in the bibliography) are sorted alphabetically by first-author's surname:

![Sci-Hub Coverage Study in eLife: author-style refences]({attach}scihub-refs-author.png){width="70%"}

## Numeric-style

Here's the same paragraph as above, but using numeric-style, which is the default for Manubot – the tool we used to write [the manuscript](https://greenelab.github.io/scihub-manuscript/):

![Sci-Hub Coverage Study via Manubot: numeric-style citations]({attach}scihub-cites-numeric.png)

When using numeric-style citations, references are numbered according to the order they were cited.
As such, the references section (bibliography) is a numbered list:

![Sci-Hub Coverage Study via Manubot: numeric-style references]({attach}scihub-refs-numeric.png)

## Usage in PubMed Central

In general, each journal (or even publisher) has a preferred citation style that's applied to all of their articles.
However, I couldn't find much information on the overall prevalence of the two styles.
Hence, I turned to the PubMed Central (PMC) Open Access (OA) [Subset](https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/), which as of March 4, 2018 contained fulltexts for 1,875,131 articles in a standardized machine-readable format (JATS XML).
This corpus is fantastic for text & data mining.
Note it could be ever better, but due to licensing issues, 61% of the 4.8 million articles in PMC are excluded from its OA Subset:
please help by only publishing in [libre OA](https://goo.gl/S8uKk5 "DOAJ Search for CC BY Journals") journals!

Anyways, 1,602,392 articles included citations and references ([source code](https://gitlab.com/dhimmel/pmc-citation-styles)).
I crafted a _heuristic_ (a bunch of rules / handmade algorithm) to classify the citation style of an article as numeric, author, or unknown.
While there's no guarantee the algorithm correctly classifies every citation/article, I fed it a collection of [test cases](https://gitlab.com/dhimmel/pmc-citation-styles/blob/afbcbe68479f54d2e77a2352340809e0fc1e9e56/utils/test_utils.py#L80-110) (enforced via [continuous integration](https://doi.org/10.1038/550143a "Collaborative software development made easy")) to ensure it's not too misbehaved.

Overall, 86.0% of articles used numeric-style and 12.2% used author-style (the algorithm could not resolve 1.8% of articles, classifying them as unknown).
Here's the popularity of each citation style by year of publication (absolute counts on the left, normalized proportions on the right):

![Popularity of citation styles by year](https://glcdn.githack.com/dhimmel/pmc-citation-styles/raw/694ebea384372d87e68b4582087a10233de945b5/figure/years-mutlipanel.svg)

We see that each year more articles were added to the PMC OA Subset than the year before, with a total of 255,736 articles added from 2017.
However, the relative popularity of author- versus numeric-style citations has remained relatively constant.

What about the proliferation of unknown-style articles from 2008–2012?
These are almost all from the [_Acta Crystallographica_](https://en.wikipedia.org/wiki/Acta_Crystallographica) series of journals, which hyperlinks citations using the ▶ symbol.
See [`PMC3793688`](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3793688/ "De Silva et al. 2013. Acta Crystallographica Section E: Structure Reports. DOI: 10.1107/S1600536813018643") for example.
Manual inspection reveals that _Acta Crystallographica_ references are actually author-style.

Here are some easter eggs:

+ In 2003 and 2004, _PLOS Biology_ published 283 articles using author-style citations before switching to numeric-style, which remains the PLOS style to this day.
+ The article with the most references at 3,112 is [World checklist of hornworts and liverworts](https://doi.org/10.3897/phytokeys.59.6261) in the journal _PhytoKeys_ (`PMC4758082`), which used author-style for its 12,274 in-text citations.
+ The article with the second-most references at 2,857 is [QCD and strongly coupled gauge theories](https://doi.org/10.1140/epjc/s10052-014-2981-5) from _The European Physical Journal C_ (`PMC4413533`), which uses numeric-style to render its 3,679 in-text citations.

## The worst case

Below, I'll go over the pros and cons of author- versus numeric-style.
But first, I want to introduce the Project Rephetio manuscript that will help exhibit the _worst-case_ performance of the two styles.

Project Rephetio was the final act of my PhD, and we took a [radically open](http://git.dhimmel.com/rephetio-manuscript/#realtime-open-science-thinklab) approach for this study.
First, we used the (now defunct) website Thinklab to post our proposal and publicly discuss the project while it was underway.
All code was posted immediately to GitHub under an open license.
Data was also uploaded to GitHub, or if too large, to Figshare.
In the end, the project encompassed 86 Thinklab discussions, 41 [GitHub](https://git.io/v5zvX) repositories (23 of which we archived on [Zenodo](https://goo.gl/FMiqHq)), 9 [Figshare](https://doi.org/ccq3) records, and several prepublication manuscripts (i.e. via Manubot, Thinklab, and bioRxiv).

The Project Rephetio manuscript was [eventually published](http://doi.org/10.7554/eLife.26726) in the journal _eLife_ with a total of 394 citations to 241 references.
I was the first author of 93 of the references, which took a full three pages of bibliography in [_eLife_'s PDF]({attach}elife-26726-v2.pdf) (_eLife_ uses author-style):

![Project Rephetio eLife PDF: all references to Himmelstein first-author works](elife-26726-v2-himmelstein-refs.png)

Only one of these "self-citations" was to a traditional scholarly output — the [predecessor study](https://doi.org/10.1371/journal.pcbi.1004259 "Himmelstein & Baranzini. 2015. Heterogeneous Network Edge Prediction: A Data Integration Approach to Prioritize Disease-Associated Genes. PLOS Computational Biology") to Project Rephetio.
The remaining 92 references were to non-traditional outputs generated during the course of the study:
62 Thinklab discussions/documents, 24 Zenodo records, 5 Figshare records, and 1 preprint.

As scientific communication grows beyond immutable journal articles in the coming decades, we can expect to see more and more studies like Project Rephetio, which will have a large number of references to non-journal outputs, such as code, data, and discussion forums.
Today's worst-case bibliographies will be tomorrow's average cases.

## Which style is best?

Benefits Author style:

1. You can recognize a study by just looking at the text of a citation.

Anti: fields bigger, non-traditional outputs

2. The first author is more visibly credited.
3. Identify outdated studies

4. Citations and references can be prepared independently, without the assistance of a typesetting program, assuming there are no author-year collisions.

Benefits of numeric-style:

1. Space savings
2. Less distracting
3. Easier lookup of a citation in the references
4. Can cite works that don't have authors

The days where author-style made sense for scholarly manuscripts has passed.

Average number of authors per biomedical publication [now exceeding](https://10.15200/winn.141832.26907 "Robert Aboukhalil · 2014 · The rising trend in authorship · Winnower") five, referring to papers by just their first author et al. will often overlook the majority of contributions.

![Project Rephetio via Thinklab: numeric-style citations](rephetio-cites-numeric.png)

![Project Rephetio via eLife Lens: author-style citations](rephetio-cites-author.png)


# The Worst Case

https://gitlab.com/dhimmel/pmc-citation-styles/blob/master/07.rephetio-stats.ipynb
https://elifesciences.org/articles/26726#references
93 self references where I'm first author.
62 Thinklab, 24 Zenodo, 5 Figshare, the bioRxiv preprint for the study, and one peer-reviewed study this study builds off of.

We were just shy of breaking single-letter-suffix disambiguation, getting to `2015z` for Himmelstein works from 2015 and `2016w` for Himmelstein works from 2016.

These 93 references took up three pages of the [PDF](({attach}elife-26726-v2.pdf))'s bibliography:


The 394 author-style citations consumed a total of 8,542 characters, excluding the surrounding parentheses and multi-citation separators.
That's an average of 21.7 characters versus 2.6 characters average for the same manuscript using numeric-style.


