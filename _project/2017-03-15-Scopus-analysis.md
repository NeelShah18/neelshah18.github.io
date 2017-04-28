---
layout: post
title: Research trends of AI in India
---

#### Introduction:
<p style="text-align: justify;">The goal of this data analysis is to identify trends in ongoing research at Indian universities and companies. It also provides a quick glimpse of top authors and research papers. To put this in perspective, we compare this data to its global equivalent, which reveals some surprising differences in research trends.</p>

**Note: All data is related to computer science field only.**

Created by:

**Neel Shah** | [Website](https://neelshah18.github.io/) | [Linkedin](https://www.linkedin.com/in/neel-shah-7b5495104/) | [GitHub](https://github.com/NeelShah18) | Email: **neelknightme@gmail.com**

**Open to hire!!!**

#### Guided by:

1) **Malaikannan Sankarasubbu** | [Linkedin](https://www.linkedin.com/in/malaikannan/) | [GitHub](href="https://github.com/malaikannan)
2) **Dr. Jacob Minz** | [Linkedin](https://www.linkedin.com/in/jacob-minz-16762a3/) | [GitHub](https://github.com/jrminz)
3) **Anirban Santara** | [Linkedin](https://www.linkedin.com/in/anirbansantara/) | [GitHub](https://github.com/Santara)

#### Technical Implementation - Open Source license

This analysis was implemented in a Jupyter notebook running on the Anaconda distribution of Python 3.6+.
We used the SCOPUS journal dataset to examine papers and research conducted by Indian authors within India. This dataset details 1387 papers published between 2001 and 2016.
We used the arXiv dataset with 24700+ papers for global data.
The Jupyter notebook (code) and arXiv dataset are available for free under the MIT open source license. However, the SCOPUS journal dataset is not available under an open source license.

* View the repository [here](https://github.com/NeelShah18/scopus-analysis-for-indian-researcher).
* Find the arXiv dataset (stored in SQLite and CSV formats)  [here](https://github.com/NeelShah18/Arxiv_Data_analysis).

#### About the SCOPUS journal:
<img src="/images/scopus_pic/scopus.png" width="750px" height="250px">

#### About arXiv
<p style="text-align: justify;">arXiv is an e-print service in the fields of physics, mathematics, computer science, quantitative biology, quantitative finance and statistics. Submissions to arXiv should conform to Cornell University academic standards. arXiv is owned and operated by Cornell University, a private not-for-profit educational institution. arXiv is funded by Cornell University Library, the Simons Foundation, and member institutions.<a href="https://arxiv.org/"> [Ref] </a></p>

#### Results of data analysis:

<p style="text-align: justify;">This first pie-chart shows that 14.42% of research is done by the industry, compared to 85.58% at universities. It is a little bit surprising that in India the ratio of industry and university research is not very good compared to other countries.</p>
<img src="/images/scopus_pic/pic_1.png" width="750px" height="250px">

<p style="text-align: justify;">The following pie-chart examines industrial research. Almost 70% of the research is at non-Indian companies’ headquarters in India. Google and IBM published almost 62% of all industry research publications, while there is only one Indian company in the top 10 – TCS with 13% of all publications.</p>
<img src="/images/scopus_pic/pic_2.png" width="750px" height="250px">

<p style="text-align: justify;">For a country with more than 129 deemed universities, 67 institutions of national importance (public), 700 degree-granting Institutions, 35,539 affiliated colleges (public and private), the chart below raises questions about the quality of education. The top 15 universities contribute to almost 42% of all research publications. A substantial 7.5% of publications are at IISc Banglore alone. Even IIT Kharagpur, known as the research hub of the Indian IT sector, ranks 7th with 2.86% of publications.</p>
<img src="/images/scopus_pic/pic_3.png" width="750px" height="250px">

<p style="text-align: justify;">Currently, there is a boom in Artificial Intelligence, Machine Learning, and Deep Learning and the bar graph below shows the popularity of research in these areas from 2001 to 2016 in India. It also shows that publications in AI shows a “zig-zag” pattern, likely due to complexity of research and lack of financial support in India.</p>
<img src="/images/scopus_pic/trend.png" width="750px" height="250px">

<p style="text-align: justify;">We compare this data to global trends. The disparity in growth rates is very apparent.</p>
<img src="/images/arxiv_pic/trend.png" width="750px" height="250px">

<p style="text-align: justify;">The top words used in the titles of arXiv papers are shown below.</p>
<img src="/images/arxiv_pic/word.png" width="750px" height="250px">

<p style="text-align: justify;">The top 20 Indian authors based on citation number are shown below. (Multiple persons indicate a tie.) </p>
<img src="/images/scopus_pic/pic_5.png" width="750px" height="250px">
<p style="text-align: justify;">Top researchers from around the globe:</p>
<img src="/images/arxiv_pic/author.png" width="750px" height="250px">

The graphs below shows Indian research trends for each year from 2010 to 2016:
<p style="text-align: justify;">2010:</p>
<img src="/images/scopus_pic/2010.png" width="750px" height="250px">
<img src="/images/arxiv_pic/2010.png" width="750px" height="250px">
<p style="text-align: justify;">2011:</p>
<img src="/images/scopus_pic/2011.png" width="750px" height="250px">
<img src="/images/arxiv_pic/2011.png" width="750px" height="250px">
<p style="text-align: justify;">2012:</p>
<img src="/images/scopus_pic/2012.png" width="750px" height="250px">
<img src="/images/arxiv_pic/2012.png" width="750px" height="250px">
<p style="text-align: justify;">2013:</p>
<img src="/images/scopus_pic/2013.png" width="750px" height="250px">
<img src="/images/arxiv_pic/2013.png" width="750px" height="250px">
<p style="text-align: justify;">2014:</p>
<img src="/images/scopus_pic/2014.png" width="750px" height="250px">
<img src="/images/arxiv_pic/2014.png" width="750px" height="250px">
<p style="text-align: justify;">2015:</p>
<img src="/images/scopus_pic/2015.png" width="750px" height="250px">
<img src="/images/arxiv_pic/2015.png" width="750px" height="250px">
<p style="text-align: justify;">2016:</p>
<img src="/images/scopus_pic/2016.png" width="750px" height="250px">
<img src="/images/arxiv_pic/2016.png" width="750px" height="250px">

#### About the datasets

* The SCOPUS dataset is not open source. We are not able to publish it.
* arXiv meta data (limited fields such as author name, title name, summary, citation, category) is open source and a link is available below.
* The arXiv data is already clean and arranged.

**The Jupyter notebook is available under MIT open source license. If you want to use this code, feel free to do so and cite me.**

* View the repository [here](https://github.com/NeelShah18/scopus-analysis-for-indian-researcher).
* Find the arXiv dataset (stored in SQLite and CSV formats)  [here](https://github.com/NeelShah18/Arxiv_Data_analysis).

**References:**
* [The Google Brain team — Looking Back on 2016](https://research.googleblog.com/2017/01/the-google-brain-team-looking-back-on.html)
* [PM Modi addresses Indian Science Congress in Tirupati](http://rstv.nic.in/pm-modi-addresses-indian-science-congress-tirupati.html?sf52381424=1)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/FBogZqSuP8eNzy" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/neelknight1/research-trend-of-ai-in-india-73238255" title="Research trend of AI in India" target="_blank">Research trend of AI in India</a> </strong> from <strong><a target="_blank" href="//www.slideshare.net/neelknight1">Neel Shah</a></strong> </div>
