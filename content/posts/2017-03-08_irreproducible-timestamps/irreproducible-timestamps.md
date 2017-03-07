Title: The most interested case of scientific irreproducibility ever?
Slug: irreproducible-timestamps
Date: 2017-03-08
Tags: blockchain, bitcoin, clinical trials, scientific misconduct, proof of existence, timestamps
Status: draft

On February 26, 2016, an was posted to _F1000Research_ titled "How blockchain-timestamped protocols could improve the trustworthiness of medical science [[version 1](https://doi.org/10.12688/f1000research.8114.1)]". The paper had two authors: [Greg Irving](http://www.phpc.cam.ac.uk/people/pcu-group/pcu-senior-research-staff/greg-irving/) of the University of Cambridge and [John Holden](http://www.garswoodsurgery.co.uk/staff1.aspx) of Garswood Surgery. The article describes a method for timestamping clinical trials, so the retrospective existence of the trial can be verified at a later date. The technique uses the Bitcoin blockchain as an immutable timestamped data store.

Despite the paper's reliance on cryptography, both of initial two reviews — by [Amy I Price](https://doi.org/10.5256/f1000research.8730.r12891) and [Luís Pinho-Costa](https://doi.org/10.5256/f1000research.8730.r13757) — lack any interrogation of the method's cryptography and both approve the manuscript. Upon the second approval on May 11, 2016, the paper was deemed "peer reviewed" and subsequently [press released](https://www.eurekalert.org/pub_releases/2016-05/fo1-dub051116.php "Doctors use Bitcoin tech to improve transparency in clinical trial research. EurekaAlert. May 11, 2016."). The study has subsequently been covered by [FierceBiotech](http://www.fiercebiotech.com/cro/doctors-use-bitcoin-tech-to-improve-transparency-trial-research "Doctors use bitcoin tech to improve transparency in trial research. May 19, 2016"), the [Economist](http://www.economist.com/news/science-and-technology/21699099-blockchain-technology-could-improve-reliability-medical-trials-better "Better with bitcoin: Blockchain technology could improve the reliability of medical trials. May 21 2016"), and the [Huffington Post](http://www.huffingtonpost.com/margaret-anderson/top-ten-medical-research_b_13975834.html "Top Ten Medical Research Issues and Trends to Watch in 2017. January 5, 2017").

However, it quickly became apparent that the paper [plagiarized](http://retractionwatch.com/2016/07/14/plagiarism-concerns-raised-over-popular-blockchain-paper-on-catching-misconduct/ "Plagiarism concerns raised over popular blockchain paper on catching misconduct. Retraction Watch. July 14, 2016") a 2014 [blog post](http://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/ "Proof of prespecified endpoints in medical research with the bitcoin blockchain. August 25, 2014") by Benjamin Carlisle titled "Proof of prespecified endpoints in medical research with the bitcoin blockchain." Ironically, Carlisle [is](http://www.bgcarlisle.com/blog/curriculum-vitae/ "Benjamin Gregory Carlisle. Curriculum vitae") a PhD candidate in at McGill University in the Biomedical Ethics Unit.

[Version 2](https://doi.org/10.12688/f1000research.8114.2) of the Irving & Holden study was posted on May 25, 2016, which attributes Carlisle's blog post and claims only to demonstrate the method. As noted by the _F1000Research_ editors, the Committee on Publication Ethics [decided](http://publicationethics.org/case/what-extent-plagiarism-demands-retraction-vs-correction "What extent of plagiarism demands a retraction vs correction? COPE case number 16-11. 2016") a correction rather than retraction was sufficient to rectify the plagiarism. Hence, to this date, Irving & Holden has not been retracted.

This post will demonstrate that Irving & Holden's problems aren't limited to plagiarism. In addition, their implementation of Carlisle's method is insecure and broken. Three aspects make Irving & Holden's study a strong candidate for the most interesting case of scientific irreproducibility ever:

1. Unless the study is 100% reproducible, the proposed implementation for timestamping clinical trials is wholly brankrupt. Unlike most scientific protocols which are not required to operate perfectly 100% of the time, _proof of existence_ assumes complete reproducibility and is worthless without it.

2. Irving & Holden claim a "second researcher" replicated their _address generation_. If so, the second researcher should be able to demonstrate replication. The replication is subject to the laws of mathematics and therefore cannot be forged. Therefore, Irving & Holden are now in a position to cryptographically prove the reproducibility of their analysis, thereby exonerating their study from claims of scientific misconduct.

3. Irving & Holden have left, presumably unwittingly, a 40 millibit bounty (worth approximately $50 US) to reproduce their analysis. This longer this bounty remains unclaimed, the greater the evidence of the study's irreproducibility.

## Proof of existence

Here we'll use the terms _proof of existence_ or _timestamping_ to refer to irrefutable evidence that digital content (e.g. document) existed at a certain point in time. Proof of existence alone does not:

1. prove that content did not exist prior to its timestamp
2. prove who authored a piece of content
3. prove that alternative versions of a piece of content did not exist and were not also timestamped

So proof of existence can attest that a clinical trial description existed at a certain past date. However, it falls short of the application proposed by Irving & Holden to "provide proof of pre-specified endpoints in clinical trial protocols." This is because their approach fails to prove clinical trial authorship and that multiple "pre-specified endpoints" did not exist.

Since the Bitcoin blockchain is the immutable data structure known to humankind, it is the natural choice for publicly storing data. Using bitcoin, you can make your data impervious to tampering, censorship, or deletion. However, you can only directly store very small amounts of data using Bitcoin. Therefore, proof of existence relies on encoding a file's hash into the blockchain rather than the entire file itself. A hash is a compact fixed-length sequence of characters that provides a unique fingerprint for a piece of content. Carlisle and Irving & Holden use SHA-256 hash, which is considered a secure hash and checksum, since it's physically impossible with current technology to generate two pieces of content that produce the same SHA-256 hash.

## Existing Implementations

At the time of Irving & Holden's study there were dozens of existing tools to create Bitcoin-verifiable timestamps. For example, in March 2015 a [Reddit user](https://redd.it/30ndi6) compiled a [table](https://goo.gl/VpFT3e) of 15 timestamping services. There are two primary methods for encoding hashes in the blockchain:

1. Use the input hash to generate a bitcoin address. Send a miniscule amount of bitcoin to the minted address to prove the address (and hence the hash that generated it) existed at a certain point in time.
2. Create a bitcoin transaction that encodes the input hash using [`OP_RETURN`](https://21.co/learn/embedding-data-blockchain-op-return/#embedding-data-in-the-blockchain-with-op_return "Embedding data in the blockchain with OP_RETURN") — a field for attaching arbitrary data to a transaction.

Carlisle's blog post uses the first method of address generation. Personally, I've timestamped scientific outputs using two existing `OP_RETURN` solutions. On August 14, 2015, I used [proofofexistence.com](https://proofofexistence.com) to timestamp a pre-release version of Hetionet ([reference](https://doi.org/10.15363/thinklab.d102), [transaction](https://blockchain.info/tx/092f81abd7bb5c59e52e2d8e794de6cee4a1cd701f7a87d2bc11cfefe97d4923?show_adv=true)). And on March 3, 2017, I [added](https://github.com/greenelab/deep-review/pull/274) [OpenTimestamps](http://opentimestamps.org) integration to the Deep Review, a collaborative review article. Every time the Deep Review manuscript is changed, the manuscript is automatically timestamped. OpenTimestamps, along with other newer methods, combines multiple input hashes before writing to the blockchain. This innovation makes timestamping with bitcoin more economical and scalable.

Irving & Holden seem unaware of these existing implementations and the larger study of cryptocurrency. They fail to cite prior work, such as [digital timestamping](https://doi.org/10.1007/3-540-38424-3_32 "Stuart Haber, W. Scott Stornetta. How to Time-Stamp a Digital Document. Advances in Cryptology. 1990"), Bitcoin's [white paper](https://bitcoin.org/bitcoin.pdf "Satoshi Nakamoto. Bitcoin: A Peer-to-Peer Electronic Cash System. October 31, 2008"), and [OriginStamp](https://arxiv.org/abs/1502.04015 "Bela Gipp, Norman Meuschke, André Gernandt. Decentralized Trusted Timestamping using the Crypto Currency Bitcoin. February 13, 2015"). Most fatally however, they created their own manual implementation of address generation, rather than relying on existing single-step solutions.

## The Carlisle Method

Benjamin Gregory Carlisle's [blog post](http://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/) from August 25, 2014 suggests using the address generation method to timestamp clinical trial documents. This method decomposes into three steps:

1. Generate a SHA-256 hash of a document.
2. Use the hash as a bitcoin private key and generate the corresponding bitcoin address.
3. Send bitcoin to the address. The confirmed transaction proves the documents existence.

The post is thoughtful and presents its limitations fairly. However, a reference implementation is not provided. Hence, the post alone is insufficient to teach non computer scientists how to create their own timestamps.




Irving & Holden created a Microsoft Word document ([supplement](https://doi.org/10.5256/f1000research.8114.d114596), [download](https://f1000researchdata.s3.amazonaws.com/datasets/8114/9c9f9a18-a852-40c6-953e-c75107abc714_Appendix_1_-_unformatted_text_file_.docx)) which they erroneously refer to as an "unformatted text file." Applying Carlisle's method to this document (see this [Jupyter notebook for a Python implementation](https://nbviewer.jupyter.org/gist/dhimmel/1da98d7def1366a6c09e6e69c6224e52)), we get the following SHA-256 hash (private key): 8da3088936035521f9e9b57963679d89e306a06c6aebd1167b4d198e79562326. There are two methods to go from a hex encoded private key to a bitcoin address. Neither Carlisle nor Irving & Holden specify which method they use. If we use an *uncompressed* public key, we get the bitcoin address of [1P6cxmuSsjDqUGCsyaEzgcj7iTEPsMAjhU](https://blockchain.info/address/1P6cxmuSsjDqUGCsyaEzgcj7iTEPsMAjhU). If we instead use a *compressed* public key, we get [17pJjJGJJTzVsJx9JSfbx6vp1sGkPNoDoA](https://blockchain.info/address/17pJjJGJJTzVsJx9JSfbx6vp1sGkPNoDoA). Neither of these addresses have been used, indicating that Irving & Holden did not correctly implement Carlisle's method.

## Irving & Holden's Intended Implementation

Irving & Holden advocate for the following implementation of Carlisle's method (corresponding to the above steps):

1. Use [Xorbin](http://www.xorbin.com/tools/sha256-hash-calculator) to compute the SHA-256 hash of the clinical trial description.
2. Use the [StrongCoin](https://strongcoin.com/) online bitcoin wallet to generate an address using the Xorbin-generated hash as a private key. Irving & Holden specify this address to be [1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH](https://blockchain.info/address/1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH) for their document.
3. Send bitcoin to the the address. Currently, the Irving & Holden address has only a [single incoming transaction](https://blockchain.info/tx/6a6fe5df3fe8ef3ed04582885ad8f50177a446ffe7fc87a8fcc4b8be6f155a8d) that deposited 40 millibits (currently valued at $51.11 US).

Were this approach to implement Carlisle's method, it would be a vulnerable implementation. It relies on Xorbin for computing the hash. Xorbin is an insecure, untrusted, and closed-source website. Therefore, malicious activity by Xorbin or through a man-in-the-middle attack could record the private key and monitor the blockchain to withdraw funds immediately from the corresponding address (i.e. financial loss). Alternatively, malicious activity could produce an incorrect hash, thereby invalidating the proof of existence (i.e. exposing users to accusations of fraud when their proof of existence fails).

However, we know that Irving & Holden did not properly implement Carlisle's method. Therefore, let's not dwell on the insecure nature of their intended implementation. Next we'll investigate why it fails.

## Irving & Holden's Broken Implementation

Irving & Holden's implementation of Carlisle's method appears broken for boths steps 1 & 2.

1.  Xorbin appears to only accept plain text input rather than a file for computing the SHA-256 hash. This indicates that Irving & Holden pasted formatted text from a Word documented, which includes a table, into a plain text field and were unaware of the inherent irreproducibility of this method. Nonetheless, it could be possible under the same software environment to reproduce the pasting behavior that generated the Irving & Holden private key.

2.  Irving & Holden erroneously assume that "account password" in the StrongCoin wallet is the private key. Instead as far as I can tell, each account on StrongCoin is a bitcoin address with a randomly generated private key. The account password is used to client-side encrypt the private key, but is not itself a private key. Therefore, the private key to address conversion of Irving & Holden is entirely broken.

Accordingly the Irving & Holden is irreproducible in two ways. First, the hash computation is unreliable. Unfortunately, Irving & Holden do not disclose the private key they generate. However, the hash computation could be reproduced on the same or similar systems. Second, the address generation is not based on the hash, rendering the Irving & Holden implementation completely irreproducible and ineffective.

## The most interesting scientific misconduct proceedings ever?

My judgment is that it's impossible for a third-party to reproduce the address generation of Irving & Holden. However, Irving & Holden undeniable claim that their address generation was reproduced using their described method:

> To verify the existence of the document a second researcher was sent the originally prepared unformatted document. An SHA256 digest was created as previously described and a corresponding private key, public key and bitcoin address generated. The exact replication of the bitcoin address (1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH) was then used to prove the documents existence in the blockchain using blockchain.info©.

Therefore, unless Irving & Holden can produce a demonstration that replicates their address generation, there is strong evidence that scientific fraud has been committed. While Irving & Holden failed at proof of existence, they succeeded at proof of fraud (absent address generation replication). In other words, Irving & Holden are in the position of having to cryptographically disprove scientific misconduct by verifying their proof of existence.

Since the funds remain in the bitcoin address, there is a bounty for replicating Irving & Holden's address generation. Currently, the bounty is equivalent to $51.11 US. The fact that it has not yet been claimed is evidence of the irreproducibility of Irving & Holden's implementation. The longer the funds stay, the greater the evidence that Irving & Holden's implementation is irreproducible. Note that withdrawing the funds could be performed by Irving & Holden or StrongCoin. Accordingly, withdrawal is not proof of reproducibility.

Together, the ability to cryptographically disprove fraud combined with the bounty will make the following scientific misconduct proceedings highly interesting.

## Conclusion

At a minimum, Irving & Holden acted with extreme negligence by publishing a security-critical technique with their extremely weak understanding of computer science, cryptography, bitcoin, and proof of existence. They expose users of their method to financial loss when private keys leak and accusations of fraud when timestamps don't validate. Furthermore, the assertion of the techniques replicability raises serious concerns of academic misconduct and fraud.




# Summary


Unfortunately, the Carlisle method is a suboptimal method for proof of existence (timestamping) using Bitcoin. Furthermore, the implementation of Carlisle's method by Irving & Holden is broken: there is no way to prove existence of the clinical trial document from publicly available information. Finally, were the Irving & Holden implementation to work as they intended, it would be insecure and subject users to financial loss and accusations of fraud.









reproducibility canary


[https://proofofexistence.com](https://proofofexistence.com) released in 2013

opentimestamps.org

[https://doi.org/10.12688/f1000research.8114.2](https://doi.org/10.12688/f1000research.8114.2)

[https://en.bitcoin.it/wiki/Proof\_of\_Ownership](https://en.bitcoin.it/wiki/Proof_of_Ownership)

https://bitsig.io/

[http://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/](http://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/)

[http://retractionwatch.com/2016/07/14/plagiarism-concerns-raised-over-popular-blockchain-paper-on-catching-misconduct/](http://retractionwatch.com/2016/07/14/plagiarism-concerns-raised-over-popular-blockchain-paper-on-catching-misconduct/)

https://www.eurekalert.org/pub\_releases/2016-05/fo1-dub051116.php

How blockchain-timestamped protocols could improve the trustworthiness
of medical science [\[version 2; referees: 3
approved\]](https://doi.org/b2pt)

Greg Irving, John Holden

F1000Research (2016) DOI:
[10.12688/f1000research.8114.2](https://doi.org/10.12688/f1000research.8114.2)

I'm a data scientist not a cryptographer, but have been followed Bitcoin
since 2013. In 2014, I was an editor for Let's Talk Bitcoin. Since then,

Once a block of data is recorded on a blockchain ledger it is extremely
difficult to change or remove it as doing so would require changing the
record on many thousands computers worldwide.

The process cost was free as the nominal bitcoin transaction could be
retrieved.

Why © symbols after every product name?

Unformated text file as .docx?

[https://www.bitaddress.org](https://www.bitaddress.org)

Strongcoin cannot generate the same address twice from the same private
key

Account password is not a private key.

Cannot go from sha256 hash to the bitcoin address

https://blockchain.info/address/1AHjCz2oEUTH8js4S8vViC8NKph4zCACXH

Any changes made to the original document generated different public and
private keys indicating that protocol had been altered.

\# Get sha256sum of https://doi.org/10.5256/f1000research.8114.d114596

[https://nbviewer.jupyter.org/gist/dhimmel/1da98d7def1366a6c09e6e69c6224e52](https://nbviewer.jupyter.org/gist/dhimmel/1da98d7def1366a6c09e6e69c6224e52)

[https://botbot.me/freenode/bitcoin-wizards/2016-10-05/?msg=74251566&page=3](https://botbot.me/freenode/bitcoin-wizards/2016-10-05/?msg=74251566&page=3)

[http://www.newsbtc.com/proof-of-existence/](http://www.newsbtc.com/proof-of-existence/)

[https://app.originstamp.org/home](https://app.originstamp.org/home)

[https://crypto-copyright.com/](https://crypto-copyright.com/)