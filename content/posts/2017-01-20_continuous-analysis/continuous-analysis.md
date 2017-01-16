Title: University software licenses prevent reproducible science
Slug: continuous-analysis
Date: 2017-01-20
Tags: software, licensing, continuous analysis, reproducibility, Universities
Status: draft

Today is an exciting day for reproducibility in computational sciences. Continuous analysis awakens with its [publication](https://doi.org/10.1101/056473 "Brett Beaulieu-Jones & Casey Greene (2017) Reproducible Computational Workflows with Continuous Analysis. Nature Biotechnology") in _Nature Biotechnology_. **Continuous analysis** is a method for automatically re-executing a study whenever its source code is updated. Any changes resulting from the update are tracked and visible.

Once properly configured, continuous analysis makes a computational study fully reproducible at every state throughout its history. It works by combining two technologies. First, **continuous integration** monitors the source data and code for changes. If a change is detected, the study is re-executed by a CI service such as [Travis CI](https://travis-ci.com/), [CircleCI](https://circleci.com/), or [Drone](http://try.drone.io/). Second, to ensure the same computational environment is always available, **Docker** is used. [Docker](https://www.docker.com/) allows you to containerize a custom software environment, so anyone can run your analysis at any future time.

## The Problem

In order for continuous analysis to enable reproducibility, the Docker image for a study must be publicly available. [Docker Hub](https://hub.docker.com/) provides a convenient home for Docker images. However, for full reproducibility, images and containers should also be deposited to a persistent archive, such as figshare or Zenodo, under an open license, so they remain available in perpetuity.

When you make a Docker image publicly available, you _distribute_ the containerized software. Accordingly, the right to redistribute software is a precondition for using it in reproducible computational workflows powered by continuous analysis. Unfortunately, copyright and licensing agreements often restrict distribution. The [solution](http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/ "Jake VanderPlas (2014) The Whys and Hows of Licensing Scientific Code. AstroBetter") is releasing software under a permissive open source license to allow redistribution and integration with other codebases.

The current situation is dire. Many academics are unaware that copyright prevents distribution and reuse of their code, even after they've posted it online and published a corresponding study. However, this post will focus on a different barrier to reproducibility: <font style="font-variant: small-caps">Licensing offices at universities that fully comprehend legal restrictions on software reuse and explicitly choose to prevent redistribution.</font>

In these instances, universities require users of publicly funded software to enter into a licensing agreement. Copyright is no longer the primary obstacle to reuse, and fair use is no longer an alibi. Instead users are contractually bound to a custom license agreement. And few researchers have the legal background to appreciate the consequences. They simply register on a website, click agree, and subsequently overlook the legal baggage they've now taken on to perform their research. I'll focus on two cases, but you're encouraged to comment on others.

## CIBERSORT of Stanford University

[CIBERSORT](https://cibersort.stanford.edu/ "CIBERSORT HomePage at Stanford") is an R program for analyzing gene expression data. Since its 2015 [publication](https://doi.org/10.1038/nmeth.3337 "Aaron Newman et al. (2015) Robust enumeration of cell subsets from tissue expression profiles. Nature Methods") in _Nature Methods_, it's been cited 71 times. The CIBERSORT program is made available, after registration and upon special request, under a [Stanford Non-commercial Software License Agreement](https://gist.github.com/dhimmel/58dcd9b512e669f20a65ddf73997b733 "GitHub Gist of the CIBERSORT License"). The title suggests this a standard license for Stanford, but Google doesn't pull up any other instances of its use. Here are some of the specifics:

> RECIPIENT shall not distribute the Program or transfer it to any other person or organization without prior written permission from STANFORD.

Hence, workflows using CIBERSORT are ineligible for reproducibility through continuous analysis as users are forbidden from distributing a Docker image. How about reimplementing the algorithm in Python, so you can get on with your containerization? With unlicensed software this would be a good option as copyright doesn't cover ideas. However, if you've agreed to the CIBERSORT license, reimplementing the algorithm is no longer an option:

> RECIPIENT shall not reverse engineer, reverse assemble, reverse compile, decompile, disassemble, or otherwise attempt to create the source code for the Program. RECIPIENT acknowledges that any programs created based on the Program will be considered a derivative of the Program and owned by STANFORD.

One of the most exciting aspects of continuous analysis is that whenever you change a piece of source code, you're automatically shown the consequences. But not CIBERSORT as the:

> RECIPIENT shall NOT make modifications to the Program.

This is a major impediment as you're not allowed to enhance the software or even make bugfixes. So hypothetically, if CIBERSORT hardcoded its ν-SVM to only evaluate three regularization strengths, you wouldn't be allowed to add additional values to improve model fitting. And finally, don't try to do anything valuable with this publicly funded software:

> RECIPIENT shall not use the Program for commercial advantage, or in the course of for-profit activities.

So not only is the CIBERSORT license terrible for reproducibility, it's profoundly antiscientific. Yet, who funded the work? Three NIH Grants. One DOD grant. And several philanthropic foundations and charities including Doris Duke, Damon Runyon, B&J Cardon, Ludwig, and Thomas + Stacey Siebel.

## GSEA of the Broad Institute

Gene Set Enrichment Analysis (GSEA) is a Java program produced at the Broad Institute to help make biological sense out of a list of genes. The software was originally described in a [2005 _PNAS_ paper](https://doi.org/10.1073/pnas.0506580102 "Aravind Subramanian et al. (2005) Gene set enrichment analysis: A knowledge-based approach for interpreting genome-wide expression profiles. Proceedings of the National Academy of Sciences") and later in a [2007 _Bioinformatics_ paper](https://doi.org/10.1093/bioinformatics/btm369 "Aravind Subramanian et al. (2007) GSEA-P: a desktop application for Gene Set Enrichment Analysis. Bioinformatics"). The program has been updated over time, most recently in October 2016. Together the two publications have amassed nearly 11 thousand citations.

The [GSEA website](http://software.broadinstitute.org/gsea/index.jsp "GSEA HomePage at the Broad Institute") deceptively states:

> Please register to download the GSEA software … Registration is free. Its only purpose is to help us track usage for reports to our funding agencies.

In reality, [registration](http://software.broadinstitute.org/gsea/register.jsp?next=index.jsp "GSEA/MSigDB Registration and License Agreement") requires agreeing to the [Massachusetts Institute of Technology Single User License Agreement for Internal Research Purposes Only](https://gist.github.com/dhimmel/04bfed6f618686ef53e050ba1191d917 "GitHub Gist of the GSEA/MSigDB License Agreement"). Despite its generic title, this is a highly customized license that does not appear to be used anywhere else.

Accompanying the software is a database of gene sets called MSigDB, which is covered by the same license. In 2016, this license forced me to [remove MSigDB](https://doi.org/10.15363/thinklab.d108#3 "Daniel Himmelstein (2016) MSigDB licensing: Removing MSigDB from the Rephetio project. Thinklab") from an integrative resource I was creating. This incident, along with others, was covered in the _Nature_ story titled [legal confusion threatens to slow data science](https://doi.org/10.1038/536016a "Simon Oxenham (2016) Legal confusion threatens to slow data science. Nature"). Here we'll focus instead on how MIT's license prevents reproducible research using the GSEA software.

First, users are forbidden from sharing any Docker images containing GSEA: 

> In no event shall LICENSEE sublicense or distribute, in whole or in part, the PROGRAM, modifications, [or] BUG FIXES

Nevertheless without sharing the Docker image, a researcher could still benefit from continuous analysis. While not ideal for reproducibility, a private Docker image or encrypted GSEA binary could be used in continuous integration to enable automatic re-execution and diffing of changes. But the license goes further and forbids convenient cloud services such as Travis CI or CircleCI:

> LICENSEE agrees not to put the PROGRAM or the DATABASE on a network, server, or other similar technology that may be accessed by any individual other than the LICENSEE.

As with CIBERSORT, users take on restrictions that exceed copyright. Specifically, licensees are forbidden from reimplementing the software to make it more open:

> LICENSEE agrees that … the PROGRAM … shall not be rewritten in another computer language or otherwise adapted to circumvent the need for obtaining a license for use of the PROGRAM or the DATABASE other than as specified by this Agreement.

Continuous analysis strives to automate all downstream consequences of a change. However, the GSEA license imposes onerous and manual reporting requirements:

> LICENSEE agrees to provide … a written evaluation of the PROGRAM … Modifications and BUG FIXES shall be provided to MIT promptly upon their creation.

The GSEA team has [received](http://grantome.com/grant/NIH/R01-CA121941-06A1) millions of dollars in funding from the NIH, including the NCI and NIGMS, to develop their software and database. Join me in declaring it unacceptable for university licensing offices to hijack such major public investments.

## What can you do?

If you're a:

+ **Journal**. Adopt an open source policy that requires all software to be released under an OSI-approved license. See [_Genome Biology_’s policy](https://doi.org/10.1186/s13059-016-1040-y "Rafal Marszalek & Louisa Flintoft (2016) Being open: our policy on source code. Genome Biology") as an example.

+ **Funder**. Mandate the open release of all software. Fund researchers with a track record of producing open source software. The nascent website [Depsy](http://depsy.org/) can [help identify](https://doi.org/10.1038/529115a "Dalmeet Chawla (2016) The unsung heroes of scientific software. Nature") open source contributors. Also check that the researchers are already active on GitHub or other repository hosting services.

+ **University**. Stress the importance of open source to your Licensing Office. Ensure that your Licensing Office receives input from experts on reuse, such as librarians, not just experts on commercialization, liability, and "technology transfer".

+ **Researcher**. In most cases, your University owns the software you produce. Ideally, you can engineer a situation where you don't have to consult your University every time you want to openly license your software. The best method is committing to open licensing in your grant applications, thereby placing legally binding obligations on your University. See this example [resource sharing plan](https://github.com/lab-carpentry/blueprint-resourcesharing/blob/master/examples/NIH-example.md "Lab Carpentry: NIH example for open licensing") from Lab Carpentry, which we developed to prevent situations like CIBERSORT, GSEA, or [Xenome](https://medium.com/@greenescientist/when-software-goes-missing-f6a0dffd68e5 "Casey Greene (2016) When software goes missing. Medium"). 

    However, even if the licensing of your software is up to the discretion of your University, there's still hope. Communicate to your Licensing Office the importance of open source licensing. Remember that should you change institutions or go the entrepreneurial route, your ability to freely use your past code will be contingent upon its open licensing.

# Epilogue

This post focuses on the interplay between continuous analysis and petty software licensing by universities. However, many of the concepts apply more generally. The right to redistribute is the bedrock of reproducibility. While the absence of open licensing has harmed reproducibility in the past -- here's a [bizarre example](http://gu.com/p/4dcx2/stw "Pete Etchells (2015) Replication frustration: what stops experiments being reliably repeated? The Guardian") — the problem is only accelerating as science become more data driven and computational.

New technologies like Docker that integrate hundreds of software products exacerbate licensing issues. As [Michael Herzog](http://www.nexb.com/info/nexb_bio.pdf "CEO of nexB, a company that helps companies comply with open source software licensing") [explains](https://youtu.be/7493AmJdCwM "Heather Meeker & Michael Herzog (2016) Managing open source software in the Docker era. DejaCode on YouTube"), "when you ship or deploy an image you are responsible for compliance for all layers included in that image." Given the impending legal difficulties for reproducible research that solely integrates open software, the last thing science needs is for universities to employ legal tactics to explicitly preclude reproducible research using publicly funded software.
