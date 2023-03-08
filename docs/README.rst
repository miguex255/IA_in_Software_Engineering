
# PDF analyzer software

## Description

This is a PDF analyzer software that allows users who use it to obtain relevant data such as:

* Get the keywords.
* Visually see the number of images that the pdf contains.
* The links that the pdf contains

## Requirements

* [Docker](https://docs.docker.com/get-docker/) 

## Installation instructions

* If you are a Linux user, you can use the following command:

```bash
sudo apt-get update
sudo apt-get install docker docker-engine docker.io containerd runc
```

You can check the status of docker using:

```bash
sudo service docker status
```

* If you are a Windows user, you can download [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)

After you set up docker, you have to clone the PDF analyzer repository on your local machine. Use the following command:

```bash
git clone https://github.com/miguex255/IA_in_Software_Engineering.git && cd IA_in_Software_Engineering
```

## Execution instructions

* First, run the following command to get into the app folder

```bash
cd Individual_Assessment_1
```

* Place all your PDF into the PDFs folder.
* After that, depending on the operating system you are using, you need to execute one of the following commands:

  * For windows users, run the following command:

  ```bash
     run.bat
  ```

  * For Linux users, run the following command:

  ```bash
     ./run.sh
  ```
* Then, the process will be completed when the following message appears:

  ```bash
  Serving Flask app 'main'
  Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   Running on http://127.0.0.1:8080
  Press CTRL+C to quit
  ```
* Finally, you will be able to view the results of your analysis in your web browser at the following URL:

  ```bash
  http://localhost:8080
  ```

To close the server press CTRL+C in the terminal.

## Running example

Once the containers have been executed, the following directories should contain the following files:

```bash
    ─Individual_Assessment_1
    ├───PDFs
    ├───Script
    ├── static
    │   ├── figures-0.png
    │   ├── figures-1.png
    │   ├── figures-2.png
    │   ├── figures-3.png
    │   ├── figures-4.png
    │   ├── figures-5.png
    │   ├── figures-6.png
    │   ├── figures-7.png
    │   ├── figures-8.png
    │   ├── figures-9.png
    │   ├── jquery-3.5.1.min.js
    │   ├── style.css
    │   ├── wordcloud-0.png
    │   ├── wordcloud-1.png
    │   ├── wordcloud-2.png
    │   ├── wordcloud-3.png
    │   ├── wordcloud-4.png
    │   ├── wordcloud-5.png
    │   ├── wordcloud-6.png
    │   ├── wordcloud-7.png
    │   ├── wordcloud-8.png
    │   └── wordcloud-9.png
    ├── templates
    │   └── report-2023-03-04.html
    └───test
```

* Elements:
  * figures-i.png: These are the histograms that represent the number of images present in PDF number "i".
  * wordcloud-i.png: These are the graphical representations of the keywords founded in PDF number "i" in word cloud format.
  * report-date.html: This is the final analysis of all processed PDFs. The "-date" field represents the date on which the analysis was done.

## Where to get help

If you have any issue with docker containers, you can find futher information in the following [link](https://docs.docker.com)
