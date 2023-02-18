# define function to scrape
def scrape_articles(journalabbr, page_num, output_filename):
    # for pages
    base_url = "https://econpapers.repec.org/article/"+journalabbr+"/default"
    pages = [".htm"]
    for i in range(page_num):
        pages.append(str(i+1)+".htm")

    # set attrs
    attrs = ["journal","title","authors","volume","jel","abstract","url","doi"]
    dict = {}
    for attr in attrs:
        dict[attr] = []

    # prefix for article link
    prefix = "https://econpapers.repec.org/article/"+journalabbr+"/"

    for p, page in enumerate(pages):
        driver.get(base_url+page)
        driver.refresh()
        # load into soup
        soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
        links = [prefix+dttag.a.get("href") for dttag in soup.find_all("dt") if dttag.a != None]
        for i, link in enumerate(links):
            # load page
            driver.get(link)
            driver.refresh()
            # load into soup
            soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
            # get url
            url = link
            # get title
            title = soup.find("h1").text
            if soup.find("h2") != None:
                h = soup.find("h2") 
            else:
                h = soup.find("h1")
            # get authors
            authorstag = h.next_sibling.next_sibling
            authors = [itag.text for itag in authorstag.find_all("i")]
            # get journal and volume
            publishtag = authorstag.next_sibling
            publish_text = publishtag.text.strip().split(", ")
            journal = publish_text[0]
            volume = ", ".join(publish_text[1:])
            # get abstract
            abstracttag = publishtag.next_sibling
            abstract = abstracttag.text.replace("\n"," ").strip()
            # get jel
            jel = [atag.text for atag in abstracttag.next_sibling.find_all("a") if "/scripts/search.pf?jel=" in atag.get("href")]
            # get doi
            doi = abstracttag.next_sibling.next_sibling.a.text.replace("http://hdl.handle.net/","")
            # append to dict
            dict["journal"].append(journal)
            dict["title"].append(title)
            dict["authors"].append(authors)
            dict["volume"].append(volume)
            dict["abstract"].append(abstract)
            dict["jel"].append(jel)
            dict["url"].append(url)
            dict["doi"].append(doi)
            
            print("Finished: Page ", p+1, "-",i+1)

    # save to csv
    df = pd.DataFrame(dict)
    df.to_csv(output_filename, index = False, encoding = "utf-8-sig")