import requests
import os
import re
import sys
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from datetime import date
import matplotlib.pyplot as plt

def process_pdf(file_path):
    inputFile = open(file_path, 'rb')
    response = requests.post("http://localhost:8070/api/processFulltextDocument", 
                                 files={"input": inputFile})
    return response.content

report_name = 'report-'+str(date.today())
report = open("/app/templates/report-"+str(date.today())+".html","w", encoding='utf-8')
html_content = f'''
<!DOCTYPE html>
<html>
<head>
  <title>{report_name}</title>
  <meta charset="utf-8">
  <meta http-equiv="cache-control" content="max-age=0" />
  <meta http-equiv="cache-control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="expires" content="0" />
  <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
  <meta http-equiv="pragma" content="no-cache" />
  <link rel="stylesheet" type="text/css" href="../static/style.css">        
  <link rel="stylesheet" 
              href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" 
              integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" 
              crossorigin="anonymous">        
        <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">        
  <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">        
  <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
  <script type="text/javascript" src="../static/jquery-3.5.1.min.js"></script>
</head>
<body>
'''

i = 0
print("Processing files. Please wait....")
for filename in os.listdir('/app/PDFs/'):
    h1 = f"<h1 class=\"display-3\">Report for {filename} file</h1>"
    html_content = html_content + h1
    try:
        grobit_file = process_pdf("/app/PDFs/"+ filename)
    except:
        report.close()
        print("Grobit service is unreachable")
        sys.exit(1)
    soup = BeautifulSoup(grobit_file, "xml")
    link_tags = soup.find_all('ref') + soup.find_all('ptr')
    figure_count = len(soup.find_all("figure")) if  len(soup.find_all("figure")) > len(soup.find_all("ref", attrs={"type": "figure"}))\
                    else len(soup.find_all("ref", attrs={"type": "figure"}))
    links = [str(link.get('target')) for link in link_tags\
                if str(link.get('target')) != 'https://github.com/kermitt2/grobid' and \
                not(re.compile("#b*").match(str(link.get('target')))) and str(link.get('target')) != 'None']
    if soup.find('keywords') != None:
        keywords = soup.find('keywords').text 
    else:
        keywords = str(0)
    if keywords != '0': 
        wordcloud = WordCloud(width=800, height=800,
                            background_color="white",
                            min_font_size=10).generate(keywords)
    else: 
        keywords = 'None'

    # Display the generated image
    p = "\n\t<p class=\"h2\">1) Word cloud</p>"
    html_content = html_content + p
    plt.figure(figsize=(8,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.savefig(f'/app/static/wordcloud-{i}.png')
    img = f"\n\t<img src=\"{{{{ url_for('static', filename='wordcloud-{i}.png')}}}}\" width=\"400\" height=\"400\" class=\"img-thumbnail\">"
    html_content = html_content + img
    # Create a bar plot
    p = "\n\t<p class=\"h2\">2) Number of figures founded</p>"
    html_content = html_content + p
    fig, ax = plt.subplots()
    ax.bar("Figures", figure_count)
    ax.set_ylabel("Number of Figures")
    ax.set_title("Figure Count in "+filename)
    fig.savefig(f'/app/static/figures-{i}.png')
    img = f"\n\t<img src=\"{{{{ url_for('static', filename='figures-{i}.png')}}}}\" width=\"400\" height=\"400\" class=\"img-thumbnail\">"
    html_content = html_content + img
    p = f"\n\t<p class=\"h2\">3) Links in {filename}</p>"
    p2 = f"<p class=\"h2\"> "+str(links) if len(links)!= 0 else 'None'+ "</p>"
    html_content = html_content + p + p2 + f"\n\t<h2 class=\"display-3\">End of the report for {filename} file</h2>\n\t"
    i+=1
html_content = html_content +  '''
        \t\t<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    \t\t<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    \t\t<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    
</body>
</html>

'''
report.write(html_content)
report.close()
