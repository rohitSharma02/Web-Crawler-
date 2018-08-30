# Web-Crawler-
A Project Report
On
WEB CRAWLER, WEB SCRAPING WITH BROWSER
AUTOMATION USING PYTHON
submitted for partial fulfillment of the requirements
for the award of the degree of
Bachelor of Technology
in
Computer Science and Engineering
Submitted by
Kuldeep Kumar (1302910074)
Kuldeep Verma (1302910075)
Rohit Sharma (1302910124)
Under supervision of
Prof. Neha Gupta
KIET Group of Institutions, Ghaziabad
Dr. A.P.J. Abdul Kalam Technical University, Lucknow
May, 2017
ii
DECLARATION
We hereby declare that this submission is our own work and that, to the best of our knowledge and belief, it contains no material previously published or written by another person, nor material which to a substantial extent has been accepted for the award of any other degree or diploma of the university or other institute of higher learning, except where due acknowledgment has been made in the text.
Signature
Name:- Kuldeep Kumar
Roll No.:- 1302910074
Date:-
Signature
Name:- Kuldeep Verma
Roll No.:- 1302910075
Date:-
Signature
Name:- Rohit Sharma
Roll No.:- 1302910124
Date:-
iii
CERTIFICATE
This is to certify that Project Report entitled “Web Crawler, Web Scrapping with browser automation using python ” which is submitted by Kuldeep Kumar, Kuldeep Verma and Rohit Sharma in partial fulfillment of the requirement for the award of degree B. Tech. in Department of Computer Science & Engineering of Dr. A.P.J. Abdul Kalam Technical University, Lucknow is a record of the candidates own work carried out by them under my supervision. The matter embodied in this report is original and has not been submitted for the award of any other degree.
.
Date: (Prof. Neha Gupta)
Supervisor
Assistant Professor
Deptt. of C.S.E.
iv
ACKNOWLEDGEMENT
It gives us a great sense of pleasure to present the report of the B. Tech Project undertaken during B. Tech. Final Year. We owe a special debt of gratitude to Professor Neha Gupta, Department of Computer Science & Engineering, KIET, Ghaziabad, for her constant support and guidance throughout the course of our work. Her sincerity, thoroughness and perseverance have been a constant source of inspiration for us. It is only her cognizant efforts that our endeavors have seen the light of the day.
We also take the opportunity to acknowledge the contribution of Dr. Vineet Sharma, Head of the Department of Computer Science & Engineering, KIET, Ghaziabad, for his full support and assistance during the development of the project. We also do not like to miss the opportunity to acknowledge the contribution of all the faculty members of the department for their kind assistance and cooperation during the development of our project.
We also do not like to miss the opportunity to acknowledge the contribution of all faculty members, especially Professor Neha Gupta, of the department for their kind assistance and cooperation during the development of our project. Last but not the least, we acknowledge our friends for their contribution in the completion of the project.
Date :
Signature: Signature :
Name : Kuldeep Kumar Name : Rohit Sharma
Roll No. : 1302910074 Roll No. : 1302910124
Signature:
Name : Kuldeep Verma
Roll No. : 1302910075
v
ABSTRACT
A Web crawler is a computer program that browses the World Wide Web in a methodical, automated manner or in an orderly fashion. Web crawling is an important method for collecting data on, and keeping up with, the rapidly expanding Internet. A vast number of web pages are continually being added every day, and information is constantly changing. This Paper is an overview of various types of Web Crawlers and the policies like selection, revisit, politeness, parallelization involved in it. The behavioral pattern of the Web crawler based on these policies is also taken for the study. The evolution of these web crawler from Basic general purpose web crawler to the latest Adaptive web crawler is studied. Web scraping (web harvesting or web data extraction) is data scraping used for extracting data from websites. Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis.Web scraping a web page involves fetching it and extracting from it. Fetching is the downloading of a page (which a browser does when you view the page). Therefore, web crawling is a main component of web scraping, to fetch pages for later processing. Once fetched, then extraction can take place. The content of a page may be parsed, searched, reformatted, its data copied into a spreadsheet, and so on. Web scrapers typically take something out of a page, to make use of it for another purpose somewhere else. An example would be to find and copy names and phone numbers, or companies and their URLs, to a list (contact scraping).Web scraping is used for contact scraping, and as a component of applications used for web indexing, data mining, online price change monitoring and price comparison, product review scraping (to watch the competition), gathering real estate listings, weather data monitoring, website change detection, research, tracking online presence and reputation, web mashup and, web data integration.
vi
TABLE OF CONTENTS
Page No.
DECLARATION…………………………………………………………………….
ii
CERTIFICATE………………………………………………………………………
iii
ACKNOWLEDGEMENTS………………………………………………………….
iv
ABSTRACT……………………………………………………………………….....
v
LIST OF FIGURES………………………………………………………………….
ix
LIST OF TABLES……………………………………………………………………
xi
LIST OF ABBREVIATIONS……………………………………………………….
xii
CHAPTER 1 (INTRODUCTION)………………………………………………….
1
1.1. Introduction……………………………………………………………………...
1
1.2. Project Description………………………………………………………………
4
CHAPTER 2 (WEB CRAWLER)…………………………………………..............
5
2.1. Web Crawler ……………….................................................................................
5
2.2. Prerequisites of a crawling system........................................................................
6
2.3. Crawling the Web……………………..................................................................
7
2.4. Crawling Strategies................................................................................................
2.4.1 Breadth-First Crawling……………………………………………...........
2.4.2 Repetitive Crawling....................................................................................
2.4.3 Targeted Crawling......................................................................................
2.4.4 Random Walks and Sampling.....................................................................
2.4.5 Deep Web Crawling....................................................................................
2.5 Crawling Policies....................................................................................................
2.5.1 Selection Policy...........................................................................................
2.5.2 Revisit Policy...............................................................................................
2.5.3 Parrarelisation Policy ................................................................................
7
8
9
9
9
10
10
10
13
13
vii
2.6 Crawler Identification............................................................................................
14
CHAPTER 3 (WEB SCRAPING)................................................................................
16
3.1. Web Scraping........................................................................................................
16
3.2. Techniques.............................................................................................................
3.2.1. Human Copy And Paste...............................................................................
3.2.2. Text Pattern Matching..................................................................................
3.2.3. Http Programming........................................................................................
3.2.4. Html Programming.......................................................................................
3.2.5. DOM Parsing................................................................................................
3.2.6. Vertical Aggregration...................................................................................
3.2.7. Semantic Annotation Recognizing...............................................................
3.2.8. Computer Vision Web Page Analysis..........................................................
3.2.9. Methods To Prevent Web Scraping. ............................................................
17
17
17
17
18
18
18
19
19
20
CHAPTER 4 (METHODOLOGY)..............................................................................
21
4.1. Modules.................................................................................................................
27
4.2 Urllib vs Urllib2 vs Request. .................................................................................
28
4.3. Implementing Web Scraping.................................................................................
28
4.4. Browser Automation Using Selenium...................................................................
4.4.1.Selenium Binding in Python.........................................................................
4.4.2. Web Drivers.................................................................................................
29
29
29
CHAPTER 5 (Meta Search Engine)......................................................………...........
30
viii
5.1. Meta Search Engine...............................................................................................
31
5.2. History...................................................................................................................
32
5.3. Advantages............................................................................................................
33
5.4. Disadvantages........................................................................................................
33
5.5. Operation...............................................................................................................
33
5.6. Archtecture............................................................................................................
33
CHAPTER 6 (RESULTS AND DISCUSSION)..........................................................
34
6.1. Web Crawler..........................................................................................................
39
6.2. Meta Search Engine...............................................................................................
41
6.3. Seat Availibility.....................................................................................................
42
6.4. Subtitle Downloader..............................................................................................
43
CHAPTER 7 (CONCLUSIONS AND FUTURE SCOPE)..........................................
44
7.1. Conclusion............................................................................................................
44
7.2. Future Scope.........................................................................................................
45
REFERENCES……………………………………………………………………….
46
ix
LIST OF FIGURES
Figure No.
Description
Page No.
2.1
Architecture of Web Crawler
6
2.2
2.3
3.1
4.1
4.2
5.1
6.1
6.2
6.3
6.4
6.5
6.6
6.7
6.8
6.9
6.10
6.11
6.12
6.13
6.14
Breadth-First Search
Depth First Search
Architecture of Web Scraping
Architecture of Scrapy
Architecture of Urllib
Architecture of Meta Search Engine
Executing Python Script
File Created by Domain Crawler
Crawl.txt
Queue.txt
Executing Meta Search Engine Script
Result Of Query
Result in Web Browser
Executing Train Availaibility Script
Automated Browser Window
Available Trains Query
Train.txt
Train.txt With Result
Copy the File Path of Video File
Subtitle Downloaded
8
9
16
26
29
34
35
36
36
37
37
38
39
39
40
40
41
42
42
43
x
LIST OF ABBREVIATIONS
WWW World Wide Web
HTML Hypertext Markup Language
URL Uiform Resource Locator
HTTP Hypertext Transfer Protocol
XHTML Extensible Hypertext Markup Language
DOM Document Object Model
JSON Javascript Object Notation
CAPCHA Completely Automated Public Turing test
to tell Computers and Humans Apart
1
CHAPTER 1
INTRODUCTION
1.1 INTRODUCTION
The need and importance of extracting data from the web are becoming increasingly loud and clear. Every few weeks, I find myself in a situation where we need to extract data from the web. For example, last week we were thinking of creating an index of hotness and sentiment about various data science courses available on the internet. This would not only require finding out new courses, but also scrape the web for their reviews and then summarizing them in a few metrics! This is one of the problems / products, whose efficacy depends more on web scrapping and information extraction (data collection) than the techniques used to summarize the data.
WWW provides us with great amounts of useful information electronically available as hypertext. This large pool of hypertext is changing dynamically and semantically unstructured, making us finding the related and valuable information difficult. Therefore, a web crawler for automatic discovering of valuable information from the Web, or Web Mining is important for us nowadays. In reality, this web crawler is a program, which automatically traverses the web by downloading documents and following links from page to page. They are mainly used by search engines to gather data for indexing. Other possible applications include page validation, structural analysis and visualization, update notification, mirroring and personal web assistants/ agents etc. Web crawlers are also known as spiders, robots, worms etc.
There are important characteristics of the Web that make crawling very difficult:
• Its large volume
2
• Its fast rate of change
• dynamic page generation
The large volume implies that the crawler can only download a fraction of the Web pages within a given time, so it needs to prioritize its downloads. The high rate of change implies that by the time the crawler is downloading the last pages from a site, it is very likely that new pages have been added to the site, or that pages have already been updated or even deleted.
General-purpose web crawlers collect and process the entire contents of the Web in a centralized location, so that it can be indexed in advance to be able to respond to many user queries. In the early stage when the Web is still not very large, simple or random crawling method was enough to index the whole web. However, after the Web has grown very large, a crawler can have large coverage but rarely refresh its crawls, or a crawler can have good coverage and fast refresh rates but not have good ranking functions or support advanced query capabilities that need more processing power. Therefore, more advance crawling methodologies are needed due to the limited resources like time and network bandwidth. Before a search engine can tell you where a file or document is, it must be found. To find information on the hundreds of millions of Web pages that exist, a search engine employs special software robots, called spiders, to build lists of the words found on Web sites. When a spider is building its lists, the process is called Web crawling. (There are some disadvantages to calling part of the Internet the World Wide Web -- a large set of arachnid-centric names for tools is one of them.) In order to build and maintain a useful list of words, a search engine's spiders have to look at a lot of pages. How does any spider start its travels over the Web? The usual starting points are lists of heavily used servers and very popular pages. The spider will begin with a popular site, indexing the words on its pages and following every link found within the site. In this way, the spidering system quickly begins to travel, spreading out across the most widely used portions of the Web.
3
Google began as an academic search engine. In the paper that describes how the system was built, Sergey Brin and Lawrence Page give an example of how quickly their spiders can work. They built their initial system to use multiple spiders, usually three at one time. Each spider could keep about 300 connections to Web pages open at a time. At its peak performance, using four spiders, their system could crawl over 100 pages per second, generating around 600 kilobytes of data each second. Keeping everything running quickly meant building a system to feed necessary information to the spiders. The early Google system had a server dedicated to providing URLs to the spiders. Rather than depending on an Internet service provider for the domain name server (DNS) that translates a server's name into an address, Google had its own DNS, in order to keep delays to a minimum. When the Google spider looked at an HTML page, it took note of two things: 1.The words within the page 2.Where the words were found Words occurring in the title, subtitles, meta tags and other positions of relative importance were noted for special consideration during a subsequent user search. The Google spider was built to index every significant word on a page, leaving out the articles "a," "an" and "the." Other spiders take different approaches. These different approaches usually attempt to make the spider operate faster, allow users to search more efficiently, or both. For example, some spiders will keep track of the words in the title, sub-headings and links, along with the 100 most frequently used words on the page and each word in the first 20 lines of text. Lycos is said to use this approach to spidering the Web. Other systems, such as AltaVista, go in the other direction, indexing every single word on a page, including "a," "an," "the" and other "insignificant" words. The push to completeness in this approach is matched by other systems in the attention given to the unseen portion of the Web page, the meta tags.
4
1.2 PROJECT DESCRIPTION
Web crawler and web scraper are primarily used for the purpose of crawling and fetching data from internet.It can be used for various purposes. The main objectives of this thesis project are:
(1) Implementing a web crawler which crawls all the urls in a specific domain.
(2) Implementing a meta search engine
(3) Web scraping Indian Railways website for seat availability status
(4) Implementing web scraper to download subtitles for video files
(5) Using selenium web-driver for browser automation
5
CHAPTER 2
WEB CRAWLER
2.1 WEB CRAWLER
A Web crawler starts with a list of URLs to visit, called the seeds. As the crawler visits these URLs, it identifies all the hyperlinks in the page and adds them to the list of URLs to visit, called the crawl frontier. URLs from the frontier are recursively visited according to a set of policies. If the crawler is performing archiving of websites it copies and saves the information as it goes. The archives are usually stored in such a way they can be viewed, read and navigated as they were on the live web, but are preserved as ‘snapshots'.
The archive is known as the repository and is designed to store and manage the collection of web pages. The repository only stores HTML pages and these pages are stored as distinct files. A repository is similar to any other system that stores data, like a modern day database. The only difference is that a repository does not need all the functionality offered by a database system. The repository stores the most recent version of the web page retrieved by the crawler.
The large volume implies the crawler can only download a limited number of the Web pages within a given time, so it needs to prioritize its downloads. The high rate of change can imply the pages might have already been updated or even deleted.
The number of possible URLs crawled being generated by server-side software has also made it difficult for web crawlers to avoid retrieving duplicate content. Endless combinations of HTTP GET (URL-based) parameters exist, of which only a small selection will actually return unique content. For example, a simple online photo gallery may offer three options to users, as specified through HTTP GET parameters in the URL. If there exist four ways to sort images, three choices of thumbnail size, two file formats, and an option to disable user-provided content, then the same set of content can be accessed with 48 different URLs, all of which may
6
be linked on the site. This mathematical combination creates a problem for crawlers, as they must sort through endless combinations of relatively minor scripted changes in order to retrieve unique content.
As Edwards et al. noted, "Given that the bandwidth for conducting crawls is neither infinite nor free, it is becoming essential to crawl the Web in not only a scalable, but efficient way, if some reasonable measure of quality or freshness is to be maintained." A crawler must carefully choose at each step which pages to visit next.
Figure 2.1: Architecture of Web Crawler
2.2 PREREQUISITE OF A CRAWLING SYSTEM
The minimum requirements for any large scale crawling system
are as follows:
1. Flexibility:“Our system should be suitable for various
scenarios”.
7
2. High Performance: “The system should be scalable with a minimum of thousand pages to millions so the quality and disk assurance are crucial for maintaining high performance.”
3. Fault Tolerance: “The first goal is to identifying the problems like invalid HTML,and having good communication protocols. Secondly the system should be persitent(eg:restart after failure)since the crawling process takes about 2 t0 5 days.”
4. Maintainability and Configurability: “There should be a appropriate interface for the monitoring for crawling process including download speed,statistics and the administrator can adjust the speed of crawler.” 2.3 CRAWLING THE WEB A component called the “URL Frontier”for storing the list of URLs to download. Given a set s of “seed” Uniform Resource Locators (URLs), the crawler repeatedly removes one URL from s, downloads the corresponding page, extracts all the URLs contained in it, and adds any previously unknown URLs to s.
2.4 CRAWLING STRATEGIES
There are mainly five types of crawling strategies as below:  Breadth-First Crawling  Repetitive Crawling  Targeted Crawling  Random Walks and Sampling  Deep Web Crawling
8
2.4.1 BREADTH-FIRST SEARCH
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key’) and explores the neighbor nodes first, before moving to the next level neighbors.
Figure 2.2: BREADTH- FIRST SEARCH
2.4.2 DEPTH-FIRST SEARCH
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking
9
Figure 2.3: DEPTH-FIRST SEARCH
2.4.3 REPETITIVE CRAWLING
Repetitive Crawling: once page have been crawled,some systems requrie the process to be repeated periodically so that indexes are kept updated.which may be achieved by launching a second crawl in parallel,to overcome this problem we should constantly update the “Index List.”
2.4.4 TARGETED CRAWLING
Targeted Crawling: Here main objective is to retrieve the greatest number of pages relating to a particular subject by using the “Minimum Bandwidth.”most search engines use crawling process heuristics in order to target certain type of page on specific topic.
2.4.5 RANDOM WALKS AND SAMPLES
Random Walks and Samples: They focus on the effect of random walks on web graphs or modified versions of these graphs via sampling to estimate the size of documents in online.
10
2.4.6 DEEP WEB CRAWLING
Deep Web Crawling: The data that which is present in the data base may only be downloaded through the medium of appropriate request or forms this Deep Web name is give to this category of data.
2.5 CRAWLING POLICIES
The characteristics of web that make crawling difficult:
1. Its Fast Rate of Change
2. Dynamic Page Generation
3. Its Large Volume
2.5.1 SELECTION POLICY
A Selection Policy that states which page to download. Given the current size of the Web, even large search engines cover only a portion of the publicly available part. A 2009 study showed even large-scale search engines index no more than 40-70% of the indexable Web a previous study by Steve Lawrence and Lee Giles showed that no search engine indexed more than 16% of the Web in 1999. As a crawler always downloads just a fraction of the Web pages, it is highly desirable for the downloaded fraction to contain the most relevant pages and not just a random sample of the Web.
This requires a metric of importance for prioritizing Web pages. The importance of a page is a function of its intrinsic quality, its popularity in terms of links or visits, and even of its URL (the latter is the case of vertical search engines restricted to a single top-level domain, or search engines restricted to a fixed Web site). Designing a good selection policy has an added difficulty: it must work with partial information, as the complete set of Web pages is not known during crawling.
11
Cho et al. made the first study on policies for crawling scheduling. Their data set was a 180,000-pages crawl from the stanford.edu domain, in which a crawling simulation was done with different strategies. The ordering metrics tested were breadth-first, backlink count and partial Pagerank calculations. One of the conclusions was that if the crawler wants to download pages with high Pagerank early during the crawling process, then the partial Pagerank strategy is the better, followed by breadth-first and backlink-count. However, these results are for just a single domain. Cho also wrote his Ph.D. dissertation at Stanford on web crawling.
Najork and Wiener performed an actual crawl on 328 million pages, using breadth-first ordering.They found that a breadth-first crawl captures pages with high Pagerank early in the crawl (but they did not compare this strategy against other strategies). The explanation given by the authors for this result is that "the most important pages have many links to them from numerous hosts, and those links will be found early, regardless of on which host or page the crawl originates."
Abiteboul designed a crawling strategy based on an algorithm called OPIC (On-line Page Importance Computation). In OPIC, each page is given an initial sum of "cash" that is distributed equally among the pages it points to. It is similar to a Pagerank computation, but it is faster and is only done in one step. An OPIC-driven crawler downloads first the pages in the crawling frontier with higher amounts of "cash". Experiments were carried in a 100,000-pages synthetic graph with a power-law distribution of in-links. However, there was no comparison with other strategies nor experiments in the real Web.
Boldi et al. used simulation on subsets of the Web of 40 million pages from the .it domain and 100 million pages from the WebBase crawl, testing breadth-first against depth-first, random ordering and an omniscient strategy. The comparison was based on how well PageRank computed on a partial crawl approximates the true PageRank value. Surprisingly, some visits that accumulate PageRank very quickly (most notably, breadth-first and the omniscient visit) provide very poor progressive approximations.
12
Baeza-Yates et al. used simulation on two subsets of the Web of 3 million pages from the .gr and .cl domain, testing several crawling strategies. They showed that both the OPIC strategy and a strategy that uses the length of the per-site queues are better than breadth-first crawling, and that it is also very effective to use a previous crawl, when it is available, to guide the current one.
Daneshpajouh et al. designed a community based algorithm for discovering good seeds.Their method crawls web pages with high PageRank from different communities in less iteration in comparison with crawl starting from random seeds. One can extract good seed from a previously-crawled-Web graph using this new method. Using these seeds a new crawl can be very effective.
2.5.1.1 RESTRICTING FOLLOWED LINKS
A crawler may only want to seek out HTML pages and avoid all other MIME types. In order to request only HTML resources, a crawler may make an HTTP HEAD request to determine a Web resource's MIME type before requesting the entire resource with a GET request. To avoid making numerous HEAD requests, a crawler may examine the URL and only request a resource if the URL ends with certain characters such as .html, .htm, .asp, .aspx, .php, .jsp, .jspx or a slash. This strategy may cause numerous HTML Web resources to be unintentionally skipped.
Some crawlers may also avoid requesting any resources that have a in them (are dynamically produced) in order to avoid spider traps that may cause the crawler to download an infinite number of URLs from a Web site. This strategy is unreliable if the site uses URL rewriting to simplify its URLs.
2.5.1.2 PATH-ASCENDING CRAWLING
Some crawlers intend to download as many resources as possible from a particular web site. So path-ascending crawler was introduced that would ascend to every path in each URL that it
13
intends to crawl.For example, when given a seed URL of http://llama.org/hamster/monkey/page.html, it will attempt to crawl /hamster/monkey/, /hamster/, and /. Cothey found that a path-ascending crawler was very effective in finding isolated resources, or resources for which no inbound link would have been found in regular crawling.
2.5.1.3 FOCUSED CRAWLING
The importance of a page for a crawler can also be expressed as a function of the similarity of a page to a given query. Web crawlers that attempt to download pages that are similar to each other are called focused crawler or topical crawlers. The concepts of topical and focused crawling were first introduced by Filippo Menczer and by Soumen Chakrabarti et al.
The main problem in focused crawling is that in the context of a Web crawler, we would like to be able to predict the similarity of the text of a given page to the query before actually downloading the page. A possible predictor is the anchor text of links; this was the approach taken by Pinkerton in the first web crawler of the early days of the Web. Diligenti et al. propose using the complete content of the pages already visited to infer the similarity between the driving query and the pages that have not been visited yet. The performance of a focused crawling depends mostly on the richness of links in the specific topic being searched, and a focused crawling usually relies on a general Web search engine for providing starting points.
2.5.2 RE-VISIT POLICY
The Web has a very dynamic nature, and crawling a fraction of the Web can take weeks or months. By the time a Web crawler has finished its crawl, many events could have happened, including creations, updates, and deletions.From the search engine's point of view, there is a cost associated with not detecting an event, and thus having an outdated copy of a resource. The most-used cost functions are freshness and age.
14
2.5.3 PARALLELIZATION POLICY
A parallel crawler is a crawler that runs multiple processes in parallel. The goal is to maximize the download rate while minimizing the overhead from parallelization and to avoid repeated downloads of the same page. To avoid downloading the same page more than once, the crawling system requires a policy for assigning the new URLs discovered during the crawling process, as the same URL can be found by two different crawling processes. 2.6 CRAWLER IDENTIFICATION
Web crawlers typically identify themselves to a Web server by using the user-agent field of an HTTP request. Web site administrators typically examine their Web servers' log and use the user agent field to determine which crawlers have visited the web server and how often. The user agent field may include a URL where the Web site administrator may find out more information about the crawler. Examining Web server log is tedious task, and therefore some administrators use tools to identify, track and verify Web crawlers. Spambots and other malicious Web crawlers are unlikely to place identifying information in the user agent field, or they may mask their identity as a browser or other well-known crawler.
It is important for Web crawlers to identify themselves so that Web site administrators can contact the owner if needed. In some cases, crawlers may be accidentally trapped in a crawler trap or they may be overloading a Web server with requests, and the owner needs to stop the crawler. Identification is also useful for administrators that are interested in knowing when they may expect their Web pages to be indexed by a particular search engine.
15
CHAPTER 3
WEB SCRAPING
3.1 WEB SCRAPING
Web scraping (web harvesting or web data extraction) is data scraping used for extracting data from websites. Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis.
Web scraping a web page involves fetching it and extracting from it. Fetching is the downloading of a page (which a browser does when you view the page). Therefore, web crawling is a main component of web scraping, to fetch pages for later processing. Once fetched, then extraction can take place. The content of a page may be parsed, searched, reformatted, its data copied into a spreadsheet, and so on. Web scrapers typically take something out of a page, to make use of it for another purpose somewhere else. An example would be to find and copy names and phone numbers, or companies and their URLs, to a list (contact scraping).
Web scraping is used for contact scraping, and as a component of applications used for web indexing, data mining, online price change monitoring and price comparison, product review scraping (to watch the competition), gathering real estate listings, weather data monitoring, website change detection, research, tracking online presence and reputation, web mashup and, web data integration.
Web pages are built using text-based mark-up languages (HTML and XHTML), and frequently contain a wealth of useful data in text form. However, most web pages are designed for human end-users and not for ease of automated use. Because of this, tool kits that scrape
16
web content were created. A web scraper is an API to extract data from a web site. Companies like Amazon AWS and Google provide web scraping tools, services and public data available free of cost to end users.
Newer forms of web scraping involve listening to data feeds from web servers. For example, JSON is commonly used as a transport storage mechanism between the client and the web server.
There are methods that some websites use to prevent web scraping, such as detecting and disallowing bots from crawling (viewing) their pages. In response, there are web scraping systems that rely on using techniques in DOM parsing, computer vision and natural language processing to simulate human browsing to enable gathering web page content for offline parsing.
Figure 3.1: Architecture of Web Scrap
17
3.2 TECHNIQUES
Web scraping is the process of automatically mining data or collecting information from the World Wide Web. It is a field with active developments sharing a common goal with the semantic web vision, an ambitious initiative that still requires breakthroughs in text processing, semantic understanding, artificial intelligence and human-computer interactions. Current web scraping solutions range from the ad-hoc, requiring human effort, to fully automated systems that are able to convert entire web sites into structured information, with limitations.
3.2.1 HUMAN COPY-AND-PASTE
Sometimes even the best web-scraping technology cannot replace a human’s manual examination and copy-and-paste, and sometimes this may be the only workable solution when the websites for scraping explicitly set up barriers to prevent machine automation.
3.2.2 TEXT PATTERN MATCHING
A simple yet powerful approach to extract information from web pages can be based on the UNIX grep command or regular expression-matching facilities of programming languages (for instance Perl or Python).
3.2.3 HTTP PROGRAMMING
Static and dynamic web pages can be retrieved by posting HTTP requests to the remote web server using socket programming.
3.2.4 HTML PARSING
Many websites have large collections of pages generated dynamically from an underlying structured source like a database. Data of the same category are typically encoded into similar pages by a common script or template. In data mining, a program that detects such templates in a particular information source, extracts its content and translates it into a relational form, is
18
called a wrapper. Wrapper generation algorithms assume that input pages of a wrapper induction system conform to a common template and that they can be easily identified in terms of a URL common scheme. Moreover, some semi-structured data query languages, such as XQuery and the HTQL, can be used to parse HTML pages and to retrieve and transform page content.
3.2.5 DOM PARSING
By embedding a full-fledged web browser, such as the Internet Explorer or the Mozilla browser control, programs can retrieve the dynamic content generated by client-side scripts. These browser controls also parse web pages into a DOM tree, based on which programs can retrieve parts of the pages.
3.2.6 VERTICAL AGGREGATION
There are several companies that have developed vertical specific harvesting platforms. These platforms create and monitor a multitude of “bots” for specific verticals with no "man in the loop" (no direct human involvement), and no work related to a specific target site. The preparation involves establishing the knowledge base for the entire vertical and then the platform creates the bots automatically. The platform's robustness is measured by the quality of the information it retrieves (usually number of fields) and its scalability (how quick it can scale up to hundreds or thousands of sites). This scalability is mostly used to target the Long Tail of sites that common aggregators find complicated or too labor-intensive to harvest content from.
3.2.7 SEMANTIC ANNOTATION RECOGNIZING
The pages being scraped may embrace metadata or semantic markups and annotations, which can be used to locate specific data snippets. If the annotations are embedded in the pages, as Microformat does, this technique can be viewed as a special case of DOM parsing. In another case, the annotations, organized into a semantic layer, are stored and managed separately from
19
the web pages, so the scrapers can retrieve data schema and instructions from this layer before scraping the pages.
3.2.8 COMPUTER VISION WEB- PAGE ANALYSIS
There are efforts using machine learning and computer vision that attempt to identify and extract information from web pages by interpreting pages visually as a human being might.
3.2.8 METHODS TO PREVENT WEB SCRAPING
The administrator of a website can use various measures to stop or slow a bot. Some techniques include:
1. Blocking an IP address either manually or based on criteria such as geolocation and DNSRBL. This will also block all browsing from that address.
2. Disabling any web API that the website's system might expose.
3. Bots sometimes declare who they are and can be blocked on that basis using robots.txt; googlebot is an example. Other bots make no distinction between themselves and a human using a browser.
4. Bots can be blocked by monitoring excess traffic
5. Bots can sometimes be blocked with tools to verify that it is a real person accessing the site, like a CAPTCHA. Bots are sometimes coded to explicitly break specific CAPTCHA patterns or may employ third-party services that utilize human labor to read and respond in real-time to CAPTCHA challenges.
6. Commercial anti-bot services: Companies offer anti-bot and anti-scraping services for websites. A few web application firewalls have limited bot detection capabilities as well.
7. Locating bots with a honeypot or other method to identify the IP addresses of automated crawlers.
8. Obfuscation using CSS sprites to display such data as phone numbers or email addresses, at the cost of accessibility to screen reader users.
20
9. Because bots rely on consistency in the front-end code of a target website, adding small variations to the HTML/CSS surrounding important data and navigation elements would require more human involvement in the initial set up of a bot and if done effectively may render the target website too difficult to scrape due to the diminished ability to automate the scraping process.
21
CHAPTER 4
METHODOLOGY
4.1 MODULES
Web service applications will involve us in a new kind of programming called client-server programming; the programs we will look at will be client programs making requests from service on the Internet. Although the underlying foundation of a web-scraping program is also a client-server interaction, we will use some tools that hide the details of those interactions, and allow us to fetch web page content directly. We will then look at how to extract patterned information from a web page.
4.2 LIBRARIES
Web scraping is a common and effective way of collecting data for projects and for work. In this guide, we’ll be touring the essential stack of Python web scraping libraries.
4.2.1 REQUEST LIBRARY
The first thing we’ll need to do to scrape a web page is to download the page. We can download pages using the Python requests library. The requests library will make a GET request to a web server, which will download the HTML contents of a given web page for us. There are several different types of requests we can make using requests , of which GET is just one.
22
4.2.2 BEAUTIFUL SOUP
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. The BeautifulSoup object itself represents the document as a whole. For most purposes, you can treat it as a Tag object. This means it supports most of the methods described in Navigating the tree and Searching the tree. Since the Beautiful object doesn’t correspond to an actual HTML or XML tag, it has no name and no attributes. But sometimes it’s useful to look at its .name, so it’s been given the special .name “[document]”. Beautiful Soup defines classes for anything else that might show up in an XML document: CDATA,Processing Instruction,Declaratio, and Doctype. Just like Comment, these classes are subclasses of NavigableString that add something extra to the string. Beautiful Soup (BS4) is a parsing library that can use different parsers. A parser is simply a program that can extract data from HTML and XML documents. Beautiful Soup's default parser comes from Python's standard library. It's flexible and forgiving, but a little slow. The good news is that you can swap out its parser with a faster one if you need the speed. One advantage of BS4 is its ability to automatically detect encodings. This allows it to gracefully handle HTML documents with special characters. In addition, BS4 can help you navigate a parsed document and find what you need. This makes it quick and painless to build common applications.
23
4.2.3 LXML
Lxml is a high-performance, production-quality HTML and XML parsing library. The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and libxslt. It is unique in that it combines the speed and XML feature completeness of these libraries with the simplicity of a native Python API, mostly compatible but superior to the well-known ElementTree API. The latest release works with all CPython versions from 2.6 to 3.6.
There is a separate module lxml.objectify that implements a data-binding API on top of lxml.etree.
In addition to the ElementTree API, lxml also features a sophisticated API for custom XML element classes. This is a simple way to write arbitrary XML driven APIs on top of lxml. lxml.etree also has a C-level API that can be used to efficiently extend lxml.etree in external C modules, including fast custom element class support.
4.2.4 LXML VS BEAUTIFUL
BeautifulSoup uses a different parsing approach. It is not a real HTML parser but uses regular expressions to dive through tag soup. It is therefore more forgiving in some cases and less good in others. It is not uncommon that lxml/libxml2 parses and fixes broken HTML better, but BeautifulSoup has superiour support for encoding detection. It very much depends on the input which parser works better. The downside of using this parser is that it is much slower than the HTML parser of lxml. So if performance matters, you might want to consider using soupparser only as a fallback for certain cases.
4.2.5 SELENIUM
Selenium is a portable software-testing framework for web applications. Selenium provides a record/playback tool for authoring tests without the need to learn a test scripting language(Selenium IDE). It also provides a test domain-specific language (Selenese) to write
24
tests in a number of popular programming languages, including C#, Groovy, Java, Perl, PHP, Python, Ruby and Scala. The tests can then run against most modern web browsers. Selenium deploys on Windows, Linux, and OS X platforms. It is open-source software, released under the Apache 2.0 license: web developers can download and use it without charge.
Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.
Selenium Python bindings provide a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote etc.
Selenium was originally developed by Jason Huggins in 2004 as an internal tool at ThoughtWorks. Huggins was later joined by other programmers and testers at ThoughtWorks, before Paul Hammant joined the team and steered the development of the second mode of operation that would later become "Selenium Remote Control" (RC). The tool was open sourced that year.
In 2005 Dan Fabulich and Nelson Sproul (with help from Pat Lightbody) made an offer to accept a series of patches that would transform Selenium-RC into what it became best known for. In the same meeting, the steering of Selenium as a project would continue as a committee, with Huggins and Hammant being the ThoughtWorks representatives.
In 2007, Huggins joined Google. Together with others like Jennifer Bevan, he continued with the development and stabilization of Selenium RC. At the same time, Simon Stewart at ThoughtWorks developed a superior browser automation tool called WebDriver. In 2009, after a meeting between the developers at the Google Test Automation Conference, it was decided to merge the two projects, and call the new project Selenium WebDriver, or Selenium 2.0.[1]
In 2008, Philippe Hanrigou (then at ThoughtWorks) made "Selenium Grid", which provides a hub allowing the running of multiple Selenium tests concurrently on any number of local or remote systems, thus minimizing test execution time. Grid offered, as open source, a similar
25
capability to the internal/private Google cloud for Selenium RC. Pat Lightbody had already made a private cloud for "HostedQA" which he went on to sell to Gomez, Inc.
The name Selenium comes from a joke made by Huggins in an email, mocking a competitor named Mercury, saying that you can cure mercury poisoning by taking selenium supplements. The others that received the email took the name and ran with it.
4.2.5 SELENIUM WEBDRIVER
Selenium WebDriver is the successor to Selenium RC. Selenium WebDriver accepts commands (sent in Selenese, or via a Client API) and sends them to a browser. This is implemented through a browser-specific browser driver, which sends commands to a browser, and retrieves results. Most browser drivers actually launch and access a browser application (such as Firefox, Chrome or Internet Explorer); there is also an HtmlUnit browser driver, which simulates a browser using HtmlUnit.
Unlike in Selenium 1, where the Selenium server was necessary to run tests, Selenium WebDriver does not need a special server to execute tests. Instead, the WebDriver directly starts a browser instance and controls it. However, Selenium Grid can be used with WebDriver to execute tests on remote systems (see below). Where possible, WebDriver uses native operating system level functionality rather than browser-based JavaScript commands to drive the browser. This bypasses problems with subtle differences between native and JavaScript commands, including security restrictions.
In practice, this means that the Selenium 2.0 API has significantly fewer calls than does the Selenium 1.0 API. Where Selenium 1.0 attempted to provide a rich interface for many different browser operations, Selenium 2.0 aims to provide a basic set of building blocks from which developers can create their own Domain Specific Language. One such DSL already exists: the Watir project in the Ruby language has a rich history of good design. Watir-webdriver implements the Watir API as a wrapper for Selenium-Webdriver in Ruby. Watir-webdriver is created entirely automatically, based on the WebDriver specification and the HTML specification.
26
As of early 2012, Simon Stewart (inventor of WebDriver), who was then with Google and now with Facebook, and David Burns of Mozilla were negotiating with the W3C to make WebDriver an internet standard. In July 2012, the working draft was released. Selenium-Webdriver (Selenium 2.0) is fully implemented and supported in Python, Ruby, Java, and C#.
4.2.6 SCRAPY
Figure 4.1: Architecture of SCRAPY
Scrapy is a free and open source framework, written in Python. Originally designed for web scraping, it can also be used to extract data using APIs or as a general purpose web crawler.It is currently maintained by Scrapinghub Ltd., a web scraping development and services company.
Scrapy project architecture is built around ‘spiders’, which are self-contained crawlers which are given a set of instructions. Following the spirit of other don’t repeat yourself frameworks, such as Django, it makes it easier to build and scale large crawling projects by allowing developers to re-use their code. Scrapy also provides a web crawling shell which can be used by developers to test their assumptions on a site’s behavior.
27
Scrapy was born at London-based web aggregation and e-commerce company Mydeco, where it was developed and maintained by employees of Mydeco and Insophia (a web consulting company based in Montevideo, Uruguay). The first public release was in August 2008 under the BSD license, with a milestone 1.0 release happening in June 2015. In 2011, Scrapinghub became the new official maintainer.
4.3 URLLIB VS URLLIB2 VS REQUEST
Urllib and Urllib2 are both Python modules that do URL request related stuff but offer different functionalities.
1) urllib2 can accept a Request object to set the headers for a URL request, urllib accepts only a URL.
2) urllib provides the urlencode method which is used for the generation of GET query strings, urllib2 doesn't have such a function. This is one of the reasons why urllib is often used along with urllib2.
Requests’ is a simple, easy-to-use HTTP library written in Python.
1) Python Requests encodes the parameters automatically so you just pass them as simple arguments, unlike in the case of urllib, where you need to use the method urllib.encode() to encode the parameters before passing them.
2) It automatically decoded the response into Unicode.
3) Requests also has far more convenient error handling.If your authentication failed, urllib2 would raise a urllib2.URLError, while Requests would return a normal response object, as expected. All you have to see if the request was successful by boolean response.ok.
28
4.4 IMPLEMENTING WEB SCRAPING
There are mainly two ways to extract data from a website:
1. Use the API of the website (if it exists). For example, Facebook has the Facebook Graph API which allows retrieval of data posted on Facebook.
2. Access the HTML of the webpage and extract useful information/data from it. This technique is called web scraping or web harvesting or web data extraction.
Steps involved in web scraping:
1. Send a HTTP request to the URL of the webpage you want to access. The server responds to the request by returning the HTML content of the webpage. For this task, we will use a third-party HTTP library for python requests.
2. Once we have accessed the HTML content, we are left with the task of parsing the data. Since most of the HTML data is nested, we cannot extract data simply through string processing. One needs a parser which can create a nested/tree structure of the HTML data. There are many HTML parser libraries available but the most advanced one is html5lib.
3. Now, all we need to do is navigating and searching the parse tree that we created, i.e. tree traversal. For this task, we will be using another third-party python library, Beautiful Soup. It is a Python library for pulling data out of HTML and XML files.
4.4 BROWSER AUTOMATION USING SELENIUM
Selenium is a powerful tool for controlling web browser through program. It is functional for all browsers, works on all major OS and its scripts are written in various languages i.e Python, Java, C# etc, we will be working with Python.
Mastering Selenium will help you automate your day to day tasks like controlling your tweets, Whatsapp texting and even just googling without actually opening a browser in just 15-30 lines of python code. The limits of automation is endless with selenium.
29
4.4.1 SELENIUM BINDING IN PYTHON
Selenium Python bindings provide a convenient API to access Selenium Web Driver like Firefox,Chrome,etc.
4.4.2 WEB DRIVERS
Selenium requires a web driver to interface with the chosen browser.Web drivers is a package to interact with web browser. It interacts with the web browser or a remote web server through a wire protocol which is common to all. You can check out and install the web drivers of your browser choice.
Figure 4.2: Architecture of URLLIB
30
CHAPTER 5
META SEARCH ENGINE
5.1 META SEARCH-ENGINE
A metasearch engine (or aggregator) is a search tool that uses another search engine's data to produce their own results from the Internet. Metasearch engines take input from a user and simultaneously send out queries to third party search engines for results. Sufficient data is gathered, formatted by their ranks and presented to the users.
However, Metasearch also has issues. Scores of websites stored on search engines are all different: this can draw in irrelevant documents. Other problems such as spamming also significantly reduce the accuracy of the search. The process of fusion aims to tackle this issue and improve the engineering of a metasearch engine.
There are many types of metasearch engines available to allow users to access specialised information in a particular field. These include Savvysearch engine and Metaseek engine.
5.2 HISTORY
"Why search the web with one search engine when you can search them all - or at least several?" This was the question tackled by researchers following a search engine review that found different search engines to be producing different results because of the different algorithms on which each was based.
The first person to incorporate the idea of meta searching was Colorado State University's Daniel Dreilinger. He revealed SearchSavvy, which let users search up to 20 different search engines and directories at once. Although fast, the search engine was restricted to simple searches and thus wasn't too reliable. University of Washington student Eric Selberg released a more "updated" version called MetaCrawler. This search engine improved on SearchSavvy's accuracy by adding its own search syntax behind the scenes, and matching the syntax to that of the search engines it was probing. Metacrawler reduced the amount of search engines queried
31
to 6, but although it produced more accurate results, it still wasn't considered as accurate as searching a query in an individual engine.
Another metasearch engine was created in May 20, 1996. HotBot, owned by Wired at the time, was a search engine with search results coming from the Inktomi and Direct Hit database. It was known at the time for its fast results and funky name, and as a search engine with the ability to search within search results. Upon being bought by Lycos in 1998, development for the search engine staggered and its market share fell drastically. After going through a few alterations, HotBot was redesigned into a simplified search interface, with its features being incorporated into Lycos' website redesign.
Ixquick is a search engine more recently known for its privacy policy statement. Developed and launched in 1998 by David Bodnick, it is currently owned by Surfboard Holding BV as of year 2000. On June 2006, Ixquick began to delete private details of its users following the same process with Scroogle. Ixquick's privacy policy includes no recording of users' IP addresses, no identifying cookies, no collection of personal data, and no sharing of personal data with third parties. It also uses a unique ranking system where a result is ranked by stars. The more stars in a result, the more search engines agreed on the result.
In April 2005, Dogpile (owned and operated by InfoSpace, Inc. at the time) collaborated with researchers from University of Pittsburgh and Pennsylvania State University to measure the overlap and ranking differences of leading Web search engines in order to gauge the benefits of using a metasearch engine to search the web. Results found that from 10,316 random user-defined queries from Google, Yahoo!, and Ask Jeeves, only 3.2 percent of first page search results were the same across those search engines for a given query. Another study later that year using 12,570 random user-defined queries from Google, Yahoo!, MSN Search, and Ask Jeeves found that only 1.1 percent of first page search results were the same across those search engines for a given query.
32
5.3 ADVANTAGES
By sending multiple queries to several other search engines this extends the search coverage of the topic and allows more information to be found. They use the indexes built by other search engines, aggregating and often post-processing results in unique ways. A metasearch engine has an advantage over a single search engine because more results can be retrieved with the same amount of exertion.[2] It also reduces the work of users from having to individually type in searches from different engines to look for resources.
Metasearching is also a useful approach if the purpose of the user’s search is to get an overview of the topic or to get quick answers. Instead of having to go through multiple search engines like Yahoo! or Google and comparing results, metasearch engines are able to quickly compile and combine results. They can do it either by listing results from each engine queried with no additional post-processing (Dogpile) or by analyzing the results and ranking them by their own rules (IxQuick, Metacrawler, and Vivismo).
5.4 DISADVANTAGES
Metasearch engines are not capable of decoding query forms or able to fully translate query syntax. The number of links generated by metasearch engines are limited, and therefore do not provide the user with the complete results of a query. The majority of metasearch engines do not provide over ten linked files from a single search engine, and generally do not interact with larger search engines for results. Sponsored webpages are prioritised and are normally displayed first.
Metasearching also gives the illusion that there is more coverage of the topic queried, particularly if the user is searching for popular or commonplace information. It's common to end with multiple identical results from the queried engines. It is also harder for users to search with advanced search syntax to be sent with the query, so results may not be as precise as when a user is using an advanced search interface at a specific engine. This results in many metasearch engines using simple searching.
33
5.5 OPERATION
A metasearch engine accepts a single search request from the user. This search request is then passed on to another search engine’s database. A metasearch engine does not create a database of webpages but generates a virtual database to integrate data from multiple sources.
Since every search engine is unique and has different algorithms for generating ranked data, duplicates will therefore also be generated. To remove duplicates,a metasearch engine processes this data and applies its own algorithm. A revised list is produced as an output for the user. When a metasearch engine contacts other search engines, these search engines will respond in three ways:
1. They will both cooperate and provide complete access to interface for the metasearch engine, including private access to the index database, and will inform the metasearch engine of any changes made upon the index database;
2. Search engines can behave in a non-cooperative manner whereby they will not deny or provide any access to interfaces;
3. The search engine can be completely hostile and refuse the metasearch engine total access to their database and in serious circumstances, by seeking legal methods.
5.6 ARCHITECTURE
Webpages that are highly ranked on many search engines are likely to be more relevant in providing useful information. However, all search engines have different ranking scores for each website and most of the time these scores are not the same. This is because search engines prioritise different criteria and methods for scoring, hence a website might appear highly ranked on one search engine and lowly ranked on another. This is a problem because Metasearch engines rely heavily on the consistency of this data to generate reliable accounts.
34
Figure 5.1: Architecture of META SEARCH ENGINE
35
CHAPTER 6
RESULTS AND DISCUSSION
6.1 WEB CRAWLER
When we run the program from command prompt, it will ask for project name and starting url.
Figure 6.1: Executing python script for domain crawler
Then it will create the directory with name you had entered,and two files in that directory name crawled.txt and queued.txt.
36
Figure 6.2: Files createdby domain crawler
Crawled.txt file contains the link which has been crawled and queue.txt contain which has to crawled.
Figure 6.3: Crawl.txt file
37
Fig 6.4 Queue.txt file
Web crawler go to url you have provided initially and download the page, then it parse the html page by using html parser to extract the link from the page. Then insert those link into queue.txt file. After then it takes first link from queue.txt and repeat the process until links are exhaust or certain depth has been reached. The main point is here for removing the same link or avoiding the link which has been crawled or in queue.txt we use the set data structure.
6.2 META SEARCH ENGINE
Our meta search engine takes the query from user and pass it to three different search engine google , yahoo and bing and take the result back from these search engine and process this result with its algorithm and present the processed result to user.
When you run the program it will ask Enter your query , you can ask any query to search engine. Then it pass this query to above mentioned search engine and gather first page link from them and present to user.
38
Figure 6.5: Executing meta search engine script
Then it will ask that whether you want to open the link or not, if you want to open the link the enter y otherwise n. then it will ask for link no. you want to open. Enter the link number ,it will open the link on web browser.
Figure 6.6: Result of query on meta search engine
39
Figure 6.7: Result opened in a web browser
6.2 SEAT AVAILAIBILTY IN TRAIN
Our application give you the information of availability of seats in train. When you run the program ,you have to provide the source station code ,destination code ,day and month.
Figure 6.8: Executing train availability script
40
Then it will open the irctc website for you and fill the details you have provided. It will automatically full the form using python script .
Figure 6.9: Automated Browser window
After filling the form it will present the list of train between those station.
Figure 6.10: Available trains for the query
Then it will go to each individual train and store all the information in text file named train.txt.
41
Figure 6.11: Train.txt file with the result
6.3 SUBTITLE DOWNLOADER
Then the subtitle downloader is used for downloading and saving the English subtitles for a video file in the same directory as the video file. This saves the user the hassel of searching for subtitles online and then downloading and saving the subtitles in the proper directory after renaming the subtitle file.
Firstly the user has to copy the file path of the video file then the user has to feed this file path into the subtitle-downloader.py script.
42
Figure 6.12: copy the file path of video file
Figure 6.13: Input the file path into script
43
Subtitle file is downloaded into the directory containing the video file
Figure 6.14: Subtitles downloaded into target directory
44
CHAPTER 7
FUTURE SCOPE
7.1 CONCLUSION
Web Crawler forms the back-bone of applications that facilitate Web information Retrieval. In this report I have presented the architecture and implementation details of my crawling system which can be deployed on the client machine to browse the web concurrently and autonomously. It combines the simplicity of asynchronous downloader and the advantage of using multiple threads. It reduces the consumption of resources as it is not implemented on the mainframe servers as other crawlers also reducing server management. The proposed architecture uses the available resources efficiently to make up the task done by high cost mainframe servers.
A major open issue for future work is a detailed study of how the system could become even more distributed, retaining though quality of the content of the crawled pages. Due to dynamic nature of the Web, the average freshness or quality of the page downloaded need to be checked, the crawler can be enhanced to check this and also detect links written in JAVA scripts or VB scripts and also provision to support file formats like XML, RTF, PDF, Microsoft word and Microsoft PPT can be done.
7.2 FUTURE SCOPE
With rise in data, redundancies in web scraping are rising. No more is web scraping a domain of the coders; in fact, companies now offer customized scraping tools to clients which they can use to get the data they want. The outcome of everyone equipped to crawl, scrape, and extract, is unnecessary waste of precious man-power. Collaborative scraping could well heal this hurt. Here, where one web crawler does a broad scraping, the others scrape data off an API. An extension of the problem is that text retrieval attracts more attention than multimedia; and with websites becoming more complex, this enforces limited scraping capacity.
45
Easily, the biggest challenge to web scraping technology is Privacy concerns. With data freely available (most of it voluntary, much of it involuntary), the call for stricter legislation rings loudest. Unintended users can easily target a company and take advantage of the business using web scraping. The disdain with which “do not scrape” policies are treated and terms of usage violated, tells us that even legal restrictions are not enough. The flipside to this argument is that if technological barriers replace legal clauses, then web scraping will see a steady, and sure, decline. This is a distinct possibility since the only way scraping activity thrives is on the grid, and if the very means are taken away and programs no longer have access to website information, then web scraping by itself will be wiped out. On the same thought is the growing trend of accepting “open data”. The open data policy, while long mused hasn’t been used at the scale it should be. The old way was to believe that closed data is the edge over competitors. But that mindset is changing. Increasingly, websites are beginning to offer APIs and embracing open data. Yet, beyond these obvious challenges, there’s a glimmer of hope for web scraping. And this is based on a singular factor: the growing need for data! With Internet & web technology spreading, massive amounts of data will be accessible on the web. Particularly with increased adoption of mobile internet. According to one report, by 2020, the number of mobile internet users will hit 3.8 billion, or around half of the world’s population! Since ‘big data’ can be both, structured & unstructured; web scraping tools will only get sharper and incisive. There is fierce competition between those who provide web scraping solutions. With the rise of open source languages like Python, R & Ruby, Customized scraping tools will only flourish bringing in a new wave of data collection and aggregation methods.
46
REFERENCES
[1] Spetka, Scott. "The TkWWW Robot: Beyond Browsing". NCSA. Archived from the original on 3 September 2004. Retrieved 21 November 2010.
[2] Kobayashi, M. & Takeda, K. (2000). "Information retrieval on the web". ACM Computing Surveys. ACM Press. 32 (2): 144–173. doi:10.1145/358923.358934.
[3] See definition of scutter on FOAF Project's wiki
[4] Masanès, Julien (February 15, 2007). Web Archiving. Springer. p. 1. ISBN 978-3-54046332-0. Retrieved April 24, 2014.
[5] Patil, Yugandhara; Patil, Sonal (2016). "Review of Web Crawlers with Specification and Working" (PDF). International Journal of Advanced Research Computer and Communication Engineering. 5 (1): 4.
[6] b Edwards, J., McCurley, K. S., and Tomlin, J. A. (2001). "An adaptive model for optimizing performance of an incremental web crawler". In Proceedings of the Tenth Conference on World Wide Web. Hong Kong: Elsevier Science: 106–113. doi:10.1145/371920.371960. ISBN 1581133480.
[7] Castillo, Carlos (2004). Effective Web Crawling (Ph.D. thesis). University of Chile. Retrieved 2010-08-03.
[8]A. Gulli; A. Signorini (2005). "The indexable web is more than 11.5 billion pages". Special interest tracks and posters of the 14th international conference on World Wide Web. ACM Press. pp. 902–903. doi:10.1145/1062745.1062789.
[9] Steve Lawrence; C. Lee Giles (1999-07-08). "Accessibility of information on the web". Nature. 400 (6740): 107–9. Bibcode:1999Natur.400..107L. doi:10.1038/21987. PMID 10428673.
47
[10] Cho, J.; Garcia-Molina, H.; Page, L. (April 1998). "Efficient Crawling Through URL Ordering". Seventh International World-Wide Web Conference. Brisbane, Australia. Retrieved 2009-03-23.
