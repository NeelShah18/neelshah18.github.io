# SCOPUS journal Data analysis of Indian Research

<p style="text-align: justify;">About: The main aim of this data analysis is to identify the ongoing research in Indian Universities and Indian Industry. It gives a basic answer about research source and trend with top authors and publication. It also shows the participation of Industry and Universities in research.</p>

Created By : 
-------------
**Neel Shah:** [Website](https://neelshah18.github.io/) | [Linkedin](https://www.linkedin.com/in/neel-shah-7b5495104/) | [GitHub](https://github.com/NeelShah18) | Email:**neelknightme@gmail.com**
**Open to hire**

Edited and Guided By:
-----------
1) Malaikannan Sankarasubbu - Know about him more:  [Linkedin](https://www.linkedin.com/in/malaikannan/) | [GitHub](href="https://github.com/malaikannan)

2) Dr. Jacob Minz - Know about him more:  [Linkedin](https://www.linkedin.com/in/jacob-minz-16762a3/) | [GitHub](https://github.com/jrminz)

3) Anirban Santara - Know about him more:  [Linkedin](https://www.linkedin.com/in/anirbansantara/) | [GitHub](https://github.com/Santara)

-------------------------------------------------------------------------------------------------------------------

#### Technical Implementation - Open source license

It is implemented in a Jupyter notebook with a back of Anaconda and Python 3.6+ version. 

Dataset and Jupyter notebook is available under MIT - open source license. If you want to use this code or data feel free to do it, But,  Please cite me.

* Link to the repository : [click here!](https://github.com/NeelShah18/scopus-analysis-for-indian-researcher)
* Link to Code and Dataset(store in SQLite and CSV format) : [click here!](https://github.com/NeelShah18/scopus-analysis-for-indian-researcher)

#### About SCOPUS journal:
<img src="/images/scopus_pic/scopus.png" width="750px" height="250px">

#### Results of data analysis:

<p style="text-align: justify;">The first pie chart shows that 85.58% research done by Industry and 14.42% research done by University. It is a little bit surprising that in India the ratio of Industry and University research is not good compared to other countries.</p> 
<img src="/images/scopus_pic/pic_1.png" width="750px" height="250px">

<p style="text-align: justify;">Second pie chart gives the information about companies research, and It is surprising that almost  70% research done by non-Indian companies headquarters in India. Google and IBM published almost 62% of total industry research publication. While there is only one Indian company who survive in top 10 is TCS with 13% publication.</p> 
<img src="/images/scopus_pic/pic_2.png" width="750px" height="250px">

<p style="text-align: justify;">A country with more 129 Deemed Universities, 67 Institution of National Importance (Public), 700 Total Degree-granting Institutions, 35,539 Affiliated Colleges (Public or Private) below result create a big question on the quality of education. It is a big concern for the Indian government and Indian University. From all university publication almost 42% of research publication done by Top - 15 Universities. It is surprising that almost 7.5% of total research publication done by IIS - Banglore alone.  Even IIT - Kharagpur which knows as research hub of Indian IT sector, ranked 7th in top 15 Universities with 2.86% of publication.</p>
<img src="/images/scopus_pic/pic_3.png" width="750px" height="250px">

<p style="text-align: justify;">Currently, there is a boom of Artificial Intelligence, Machine learning, and deep learning and below bar graph proves the popularity of those research from 2001 to 2016. It also shows that publication in AI field shows zig-zag patterns because of complexity in research and lake of financial support in India.</p>
<img src="/images/scopus_pic/trend.png" width="750px" height="250px">

Below bar graph shows top 20  cited paper of Indian researcher.
<img src="/images/scopus_pic/pic_4.png" width="750px" height="250px">

below graph shows top 20 Indian authors based on the citation number.
<img src="/images/scopus_pic/pic_5.png" width="750px" height="250px">

Below six bar graph shows top research trend in an individual year from 2010 to 2016.
<img src="/images/scopus_pic/2010.png" width="750px" height="250px">
<img src="/images/scopus_pic/2011.png" width="750px" height="250px">
<img src="/images/scopus_pic/2012.png" width="750px" height="250px">
<img src="/images/scopus_pic/2013.png" width="750px" height="250px">
<img src="/images/scopus_pic/2014.png" width="750px" height="250px">
<img src="/images/scopus_pic/2015.png" width="750px" height="250px">
<img src="/images/scopus_pic/2016.png" width="750px" height="250px">

#### About Dataset and processing and cleaning of data:

1) It is a collection of 1387 paper dataset from SCOPUS journal between 2001 to 2016 published by Indian Universities or India based research center of any industry.
2) If a paper has multiple authors from Industry and Indian University, we count that paper as university paper.
3) If a paper published by industry and non-Indian university, we count that paper as Industry paper.
4) During cleaning of data, we consider the different name of Institute as single Institute. For example  IIT-Madras, Indian Institute of Technology and IIT-M count as the same institute.
5) We also consider the different name of same industry as single industry, For example, TCS and tata consultancy service count as the same industry.
