Title: The most interesting case of scientific irreproducibility?
Slug: irreproducible-timestamps
Date: 2017-03-08
Tags: bitcoin, clinical trials, proof of existence, timestamps, blockchain, timestamping, replication, reproducibility


On February 26, 2016, the [first version](https://doi.org/10.12688/f1000research.8114.1 "Version 1") of an article titled "How blockchain-timestamped protocols could improve the trustworthiness of medical science" was posted to _F1000Research_. The paper had two authors: [Greg Irving](http://www.phpc.cam.ac.uk/people/pcu-group/pcu-senior-research-staff/greg-irving/) of the University of Cambridge and [John Holden](http://www.garswoodsurgery.co.uk/staff1.aspx) of Garswood Surgery. The article describes a method for timestamping clinical trials, so the retrospective existence of a trial can be verified at a later date. The technique uses the Bitcoin blockchain as an immutable and timestamped data store.

Despite the paper's reliance on cryptography, both of the initial two reviews — by [Amy Price](https://doi.org/10.5256/f1000research.8730.r12891) and [Luís Pinho-Costa](https://doi.org/10.5256/f1000research.8730.r13757) — lacked any interrogation of the method's cryptography and approved the manuscript. Upon the second approval on May 11, 2016, the paper was deemed "peer reviewed" and [press released](https://www.eurekalert.org/pub_releases/2016-05/fo1-dub051116.php "Doctors use Bitcoin tech to improve transparency in clinical trial research. EurekaAlert. May 11, 2016."). The study has since been covered by [FierceBiotech](http://www.fiercebiotech.com/cro/doctors-use-bitcoin-tech-to-improve-transparency-trial-research "Doctors use bitcoin tech to improve transparency in trial research. May 19, 2016"), the [Economist](http://www.economist.com/news/science-and-technology/21699099-blockchain-technology-could-improve-reliability-medical-trials-better "Better with bitcoin: Blockchain technology could improve the reliability of medical trials. May 21 2016"), and the [Huffington Post](http://www.huffingtonpost.com/margaret-anderson/top-ten-medical-research_b_13975834.html "Top Ten Medical Research Issues and Trends to Watch in 2017. January 5, 2017").

However, it quickly became apparent that the paper [plagiarized](http://retractionwatch.com/2016/07/14/plagiarism-concerns-raised-over-popular-blockchain-paper-on-catching-misconduct/ "Plagiarism concerns raised over popular blockchain paper on catching misconduct. Retraction Watch. July 14, 2016") a 2014 [blog post](http://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/ "Proof of prespecified endpoints in medical research with the bitcoin blockchain. August 25, 2014") by Benjamin Carlisle titled "Proof of prespecified endpoints in medical research with the bitcoin blockchain." Carlisle [is](http://www.bgcarlisle.com/blog/curriculum-vitae/ "Benjamin Gregory Carlisle. Curriculum vitae") a PhD candidate at McGill University in the Biomedical Ethics Unit.

[Version 2](https://doi.org/10.12688/f1000research.8114.2) of Irving & Holden's study was posted on May 25, 2016, which attributes Carlisle's blog post and claims only to demonstrate the method. As noted by the _F1000Research_ editors, the Committee on Publication Ethics [decided](http://publicationethics.org/case/what-extent-plagiarism-demands-retraction-vs-correction "What extent of plagiarism demands a retraction vs correction? COPE case number 16-11. 2016") a correction was sufficient to rectify the plagiarism. Hence, to this date, Irving & Holden's study has not been retracted.

This post will demonstrate that Irving & Holden's problems aren't limited to plagiarism. In addition, their implementation of Carlisle's method is insecure and broken. Three aspects make Irving & Holden's study a strong candidate for the most interesting case of scientific irreproducibility ever:

1. Unless the study is 100% reproducible, the proposed implementation for timestamping clinical trials is wholly bankrupt. Unlike most scientific protocols which are not required to operate perfectly 100% of the time, timestamping assumes complete reproducibility and is worthless without it.

2. Irving & Holden claim a "second researcher" replicated their _address generation_. If so, the second researcher should be able to demonstrate the replication, which is subject to the laws of mathematics and therefore cannot be forged. Thus, Irving & Holden are now in a position to cryptographically prove the reproducibility of their analysis, thereby exonerating their study from any claim of scientific misconduct.

3. Irving & Holden have left, presumably unwittingly, a 40 millibit bounty (worth approximately $50 US) to reproduce their analysis. The longer this bounty remains unclaimed, the greater the evidence of the study's irreproducibility.

## Proof of existence

Here we'll use the terms _proof of existence_ or _timestamping_ to refer to irrefutable evidence that digital content (e.g. a document) existed at a certain point in time. Proof of existence alone cannot:

1. prove that content did not exist prior to its timestamp.
2. prove who authored content.
3. prove that alternative versions of content did not exist and were not also timestamped.

So proof of existence can attest that a clinical trial protocol existed at a certain past date. However, it falls short of the application proposed by Irving & Holden to "provide proof of pre-specified endpoints in clinical trial protocols." This is because their approach fails to prove clinical trial authorship and that multiple "pre-specified endpoints" did not exist.

Since the Bitcoin blockchain is the most immutable database in existence, it is the natural choice for indefinitely and publicly storing data. Using bitcoin, you can make your data impervious to tampering, censorship, or deletion. However, you can only directly store very small amounts of data using Bitcoin. Therefore, proof of existence relies on encoding a file's hash into the blockchain rather than the entire file itself. A hash is a compact fixed-length sequence of characters that provides a unique fingerprint for a piece of content. Carlisle and Irving & Holden use the SHA-256 hash, which is considered a secure hash and checksum, since it's physically impossible with current technology to generate two pieces of content that produce the same SHA-256 hash.

## Existing Implementations

At the time of Irving & Holden's study there were dozens of existing tools to create Bitcoin-verifiable timestamps. For example, in March 2015 a [Reddit user](https://redd.it/30ndi6) compiled a [table](https://goo.gl/VpFT3e) of 15 timestamping services. There are two primary methods for encoding hashes in the blockchain:

1. Use the hash to generate a bitcoin address. Send a miniscule amount of bitcoin to the minted address to prove the address (and hence the hash that generated it) existed at a certain point in time.
2. Create a bitcoin transaction that encodes the hash using [`OP_RETURN`](https://21.co/learn/embedding-data-blockchain-op-return/#embedding-data-in-the-blockchain-with-op_return "Embedding data in the blockchain with OP_RETURN") — a field for attaching arbitrary data to a bitcoin transaction.

Carlisle's blog post uses the first method, address generation. Personally, I've timestamped scientific outputs using two existing `OP_RETURN` solutions. On August 14, 2015, I used [proofofexistence.com](https://proofofexistence.com) to timestamp a pre-release version of Hetionet ([reference](https://doi.org/10.15363/thinklab.d102), [transaction](https://blockchain.info/tx/092f81abd7bb5c59e52e2d8e794de6cee4a1cd701f7a87d2bc11cfefe97d4923?show_adv=true)). And on March 3, 2017, I [added](https://github.com/greenelab/deep-review/pull/274) [OpenTimestamps](http://opentimestamps.org) integration to the Deep Review, a collaborative review article. Every time the Deep Review [manuscript](https://greenelab.github.io/deep-review/) is changed, it's automatically timestamped. OpenTimestamps, along with other newer methods like [OriginStamp](https://originstamp.org), combines multiple input hashes before writing to the blockchain. This innovation makes timestamping with bitcoin more economical and scalable.

Irving & Holden seem unaware of these existing implementations and the larger study of cryptocurrency. They fail to cite prior work, such as [digital timestamping](https://doi.org/10.1007/3-540-38424-3_32 "Stuart Haber, W. Scott Stornetta. How to Time-Stamp a Digital Document. Advances in Cryptology. 1990"), Bitcoin's [white paper](https://bitcoin.org/bitcoin.pdf "Satoshi Nakamoto. Bitcoin: A Peer-to-Peer Electronic Cash System. October 31, 2008"), and [OriginStamp](https://arxiv.org/abs/1502.04015 "Bela Gipp, Norman Meuschke, André Gernandt. Decentralized Trusted Timestamping using the Crypto Currency Bitcoin. February 13, 2015"). Most fatally however, they created their own manual implementation of address generation, rather than relying on existing single-step solutions.

## The Carlisle Method

Benjamin Gregory Carlisle's [blog post](http://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/) from August 25, 2014 suggests using an address generation method to timestamp clinical trial protocols. This method can be decomposed into three steps:

1. Generate a SHA-256 hash of a document.
2. Use the hash as a bitcoin private key and generate the corresponding bitcoin address.
3. Send bitcoin to the address. The confirmed transaction proves the document's existence.

Carlisle's post is thoughtful and presents its limitations fairly. However, a reference implementation is not provided. At the present time, cryptocurrency is confusing. I encourage everyone to play with it, at their own risk. But I _do not_ encourage novices to implement security critical applications and advertise those applications without extensive review from seasoned computer scientists.

Irving & Holden created a Microsoft Word document ([supplement](https://doi.org/10.5256/f1000research.8114.d114596), [download](https://f1000researchdata.s3.amazonaws.com/datasets/8114/9c9f9a18-a852-40c6-953e-c75107abc714_Appendix_1_-_unformatted_text_file_.docx)) which they [erroneously](https://medium.com/@OmnesRes/medical-students-cant-help-but-plagiarize-apparently-f81074824c17 "Jordan Anaya. Medical students can’t help but plagiarize, apparently. Medium. July 21, 2016") refer to as an "unformatted text file." Applying Carlisle's method to this document (see this [Jupyter notebook for a Python implementation](https://github.com/dhimmel/irreproducible-timestamps/blob/master/addresses.ipynb)), we get the following SHA-256 hash (private key): <small>`8da3088936035521f9e9b57963679d89e306a06c6aebd1167b4d198e79562326`</small>. There are two methods to go from a hex encoded private key to a bitcoin address. Neither Carlisle nor Irving & Holden specify which method they use. If we use an _uncompressed_ public key, we get the bitcoin address of <small>[`1P6cxmuSsjDqUGCsyaEzgcj7iTEPsMAjhU`](https://blockchain.info/address/1P6cxmuSsjDqUGCsyaEzgcj7iTEPsMAjhU)</small>. If we instead use a _compressed_ public key, we get <small>[`17pJjJGJJTzVsJx9JSfbx6vp1sGkPNoDoA`](https://blockchain.info/address/17pJjJGJJTzVsJx9JSfbx6vp1sGkPNoDoA)</small>. Neither of these addresses have been used, indicating that Irving & Holden did not properly timestamp their Word document according to Carlisle's method.

## Irving & Holden's Intended Implementation

Irving & Holden describe their implementation of Carlisle's method as follows:

1. Use the [Xorbin](http://www.xorbin.com/tools/sha256-hash-calculator) website to compute the SHA-256 hash of the clinical trial protocol. Irving & Holden do not disclose this hash.
2. Use the [StrongCoin](https://strongcoin.com/) online bitcoin wallet to generate an address using the Xorbin-generated hash as a private key. Irving & Holden specify this address to be <small>[`1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH`](https://blockchain.info/address/1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH)</small>.
3. Send bitcoin to the the address. Currently, the disclosed address has a single [transaction](https://blockchain.info/tx/6a6fe5df3fe8ef3ed04582885ad8f50177a446ffe7fc87a8fcc4b8be6f155a8d) that deposited 40 millibits on February 11, 2016. At that time, 40 millibits was worth approximately $15 US. These funds were never withdrawn and are now worth close to $50.

Were this approach to properly implement Carlisle's method, it would be riddled with vulnerabilities. It requires trusting Xorbin and an insecure (HTTP) internet connection to Xorbin. It requires trusting StrongCoin. If either service has a bug, it requires confidence that these services will continue to be available in the future without fixing the bug. Neither Xorbin nor StrongCoin are open source projects and are thus difficult to preserve and lack community code review.

There's ample room for malicious attacks. Xorbin or a man-in-the-middle could record private keys and monitor the blockchain for transactions to the corresponding addresses. Funds could then be withdrawn by the attacker before the user got around to transferring them to a secure address. When using address generation for timestamping, users should send only a miniscule amount of bitcoin to the address. So a more devastating attack would produce an incorrect hash, depriving users from subsequently proving their document's existence. In the high-stakes pharmaceutical industry, billions of dollars could ride on whether a timestamp verifies. Furthermore, an attacker could timestamp a modified protocol and, at a later date, frame the original author for unethical changes to the clinical trial.

However, we know that Irving & Holden did not properly execute Carlisle's method. So let's not dwell on the vulnerabilities of their intended implementation.

## Irving & Holden's Broken Implementation

Irving & Holden's implementation of Carlisle's method appears broken for both steps 1 & 2.

**Step 1.** Xorbin only accepts plain text input for computing SHA-256 hashes. Xorbin does not allow users to upload a file indicating that Irving & Holden pasted formatted text from a Word documented into Xorbin's plain text field.

The conversion from formatted to plain text is nondeterministic and depends on the specific system environment and text selection method. Did Irving & Holden select all (`⎈`/`⌘` + `A`) or drag the cursor when copying the text? How did the table get downgraded to plain text? How were newlines represented?

Pasting formatted text into a plain text field is a terrible design decision. Nonetheless, under the same conditions, one could replicate the pasting behavior and hence the hash generation of Irving & Holden.

**Step 2.** Irving & Holden erroneously assume that "account password" in the StrongCoin wallet is equivalent to "private key". Instead as far as I can tell, each account on StrongCoin is a bitcoin address with a randomly generated private key. The account password is used for client-side encryption of the private key, but is not itself a private key. To demonstrate that the account password is not a private key, I generated two accounts that both use the same SHA-256 hash for their password:

![StrongCoin Paper Wallet](https://github.com/dhimmel/irreproducible-timestamps/raw/master/strongcoin/paper-wallet-06-03-2017-191921.png)

As you can see, the two accounts have different addresses. Therefore, the private key → address conversion of Irving & Holden is irreparably broken. Since nothing that must derive from the account password ever gets incorporated into the blockchain, there is no proof that Irving & Holden's protocol ever existed.

In summary, Irving & Holden's timestamp is irreproducible. There is no way to prove the past existence of their clinical trial protocol from publicly available information.

## Conclusion

Despite the evidence herein that their address generation cannot be reproduced, Irving & Holden make the following claim:

> To verify the existence of the document a second researcher was sent the originally prepared unformatted document. An SHA256 digest was created as previously described and a corresponding private key, public key and bitcoin address generated. The exact replication of the bitcoin address (<small>`1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH`</small>) was then used to prove the documents existence in the blockchain using blockchain.info©.

I do not think a second researcher could have reproduced the address generation, since StrongCoin generates a random private key, in lieu of using the protocol hash as the private key.

The beauty of cryptography is that it doesn't matter what I think. If Irving & Holden's statement is true, they or the "second researcher" will be able to provide the exact chain of operations to go from clinical trial protocol to public key. And anyone will be able to independently verify their proof.

Furthermore, there is currently a bounty to reproduce Irving & Holden's address generation. This bounty was publicly disclosed over a year ago with the initial posting of their study and remains unclaimed. Note that Irving/Holden and StrongCoin should both possess enough information to move the funds from <small>`1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH`</small>. Therefore, withdrawal is insufficient to prove the protocol's existence. But the continued lack of withdrawal is evidence that no third party can reproduce their analysis.

Past attempts to reproduce scientific studies have been [notoriously inconclusive](https://doi.org/10.1038/541269a "Monya Baker & Elie Dolgin. Cancer reproducibility project releases first results. Nature News. January 18, 2017"). Irving & Holden's timestamp is notedly different in that its replicability is unambiguous. It will or will not provably replicate. There is no in between. So in a perverse way, this incident gives us a glimpse into a more reproducible future.

***

The analyses for this blog post are posted to GitHub at [`dhimmel/irreproducible-timestamps`](https://github.com/dhimmel/irreproducible-timestamps) and archived [on Zenodo](https://doi.org/10.5281/zenodo.375952 "dhimmel/irreproducible-timestamps v1.0: Initial replication analysis for the Satoshi Village blog post"). For those looking to claim the bounty, you can open the address generation notebook [in Binder](http://mybinder.org/repo/dhimmel/irreproducible-timestamps).

***

## Update on March 30, 2017

Today, Irving & Holden posted [version 3](https://doi.org/10.12688/f1000research.8114.3) of their study to _F1000Research_. The updated study now claims have verified the clinical trial protocol timestamp by:

1. logging into the same StrongCoin account that generated the bitcoin address <small>`1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH`</small>.
2. decrypting the corresponding private key using the protocol's hash as the account password.

So Irving & Holden have conceded that their protocol's hash was used as an account password. Wallet passwords are entirely off-chain; they are never written to the Bitcoin blockchain. In other words, there is no timestamp of Irving & Holden's protocol. Game over.

On the other hand, I'm tempted to ask Irving & Holden for their StrongCoin login (email & password), so I can "verify" that their protocol's hash decrypts their address's private key — also known as claiming my damn bounty!

Thanks Benjamin Carlisle for contributing diffs showing the revisions between versions [2–3](https://github.com/dhimmel/irreproducible-timestamps/blob/37f66dc39bab650671d1d05e510199705c59248b/f1000/v2-3.pdf "PDF of the diff between Irving & Holden v2 and v3") and [1–2](https://github.com/dhimmel/irreproducible-timestamps/blob/37f66dc39bab650671d1d05e510199705c59248b/f1000/v1-2.pdf "PDF of the diff between Irving & Holden v1 and v2"). Note that version 3 also switches to using a text file rather than a Word Document to store the protocol. I [generated](http://nbviewer.jupyter.org/github/dhimmel/irreproducible-timestamps/blob/37f66dc39bab650671d1d05e510199705c59248b/addresses.ipynb#Update-for-protocol-for-manuscript-version-3) addresses using Carlisle's method for the new SHA-256 hash. However, reproducing Irving & Holden's hash is irrelevant (unless you have access to their StrongCoin account).

## Update on May 26, 2017

_F1000Research_ announced on May 24 that the study will be retracted, [as covered](http://retractionwatch.com/2017/05/24/authors-retract-much-debated-blockchain-paper-f1000/ "Authors retract much-debated blockchain paper from F1000. Retraction Watch. By Alison McCook on 2017-05-24") by Retraction Watch. The retraction note states:

> The authors have taken this decision after considering the methodological concerns raised by a peer reviewer during the post-publication open peer review process. As the methodology has been deemed to be unreliable, the article is now retracted.

The retraction came after a fourth reviewer, William Knottenbelt, [reached](https://doi.org/10.5256/f1000research.12186.r22913 "Review by William J. Knottenbelt on 2017-05-22") the same conclusions about the flawed methodology as this blog post.
