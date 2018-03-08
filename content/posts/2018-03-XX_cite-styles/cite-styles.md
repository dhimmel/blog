Title: On author versus numeric citation styles
Slug: cite-styles
Date: 2018-03-20
Tags: bibliography, references, citations, works cited, journals, Manubot, eLife, PeerJ, Thinklab
Status: draft

Should citations in scholarly writing appear as author-year snippets, like ([Pantcheva, 2018](http://site.uit.no/english/writing-style/citationstyles/ "Citation styles: Vancouver and Harvard systems"); [Zelle, 2015](http://docs.citationstyles.org/en/1.0.1/primer.html "Primer — An Introduction to CSL: v1.0.1")), or numbers, like [[1](),[2]()]?
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
please consider only publishing in libre OA journals!

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

## When to use what


PLOS, BMC-series journals, Nature journals



There are two main ways to organize reference lists and citations in scholarly writing.


Numbered references or alphabetical

Textual citation, Parenthetical citation

Downside of texual (in-line citations)

## Popularity
