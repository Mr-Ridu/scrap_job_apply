from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def scrap():
    url = 'https://jobs.bdjobs.com/jobsearch.asp?fcatId=&icatId=11'

    # Send an HTTP GET request to the URL and get the response
    response = requests.get(url)

    # Parse the content of the web page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all job titles and company names
    h3_elements = soup.find_all('div', class_='job-title-text')
    companyname = soup.find_all('div', class_='comp-name-text')
    # Extract the text from job titles and company names


    job_titles = [job.text.strip() for job in h3_elements]
    company_names_list = [c.text.strip() for c in companyname]

    # Zip the job titles and company names together
    jobs_data = list(zip(job_titles, company_names_list))
    # Pass the zipped data to the template
    return render_template('scrap.html', jobs_data=jobs_data)

if __name__ == '__main__':
    app.run(debug=True)
