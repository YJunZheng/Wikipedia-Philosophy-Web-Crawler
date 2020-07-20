#  Wikipedia Web Crawler
<h3>Introduction</h3>
This python script is a web crawler/scraper that starts on a random wikipedia site (you can select a certain one by changing 
the urlSuffix variable to the desired url suffix) and follows the rules of the <i>"Getting to Philosophy"</i> phenomenon seen below
https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy to reach /wiki/Philosophy using the <b>BeautifulSoup</b> library.

<h3>Rules:</h3>
1. Clicking on the first non-parenthesized, non-italicized link</br>
2. Ignoring external links, links to the current page, or red links (links to non-existent pages)</br>
3. Stopping when reaching "Philosophy", a page with no links or a page that does not exist, or when a loop occurs</br></br>

The bot crawls and prints the title of every site it goes to and stops when it reaches philosophy (statistically likely),
a loop occurs, or when the page is a referral/help/blank page

<h3>Preview</h3>
<img src="https://github.com/JunZheng-dev/Wikipedia-Philosophy-Web-Crawler/blob/master/preview/preview.gif"/>

<b>Idea from:</b> https://github.com/ammar-s847 and https://github.com/AliNaqvi01</br>
