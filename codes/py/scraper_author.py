# to scrape author info from saved htmls
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

authordic = pd.read_csv("author.csv", encoding = "utf-8-sig").to_dict("list")

files = os.listdir("data/authors/html/")
for i, file in enumerate(files):
    if file.replace(".html","") not in authordic["authorid"]:
        print(i,file)
        with open("data/authors/html/"+file, encoding = "utf-8-sig") as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        f.close()

        # authorid
        authorid = file.replace(".html","")
        # name
        name = soup.find('div', id="gsc_prf_in").text
        # emailsuffix
        emailsuffix = re.findall("[a-zA-Z0-9._-]+", soup.find('div', id="gsc_prf_ivh").text)[0]
        # misc
        misc = soup.find('div',class_="gsc_prf_il").text
        # index
        indexspan = soup.find("table").find_all("td")
        for i,s in enumerate(indexspan):
            if s.text == "引用":
                t2302cite = indexspan[i+1].text
                s18t2302cite = indexspan[i+2].text
            elif s.text == "h 指数":
                t2302hindex = indexspan[i+1].text
                s18t2302hindex = indexspan[i+2].text
            elif s.text == "i10 指数":
                t2302i10index = indexspan[i+1].text
                s18t2302i10index = indexspan[i+2].text

        # citations
        try:
            yeartags = soup.find("div", class_="gsc_md_hist_b").find_all("span", class_= "gsc_g_t")
            years = dict([(str(len(yeartags)-i), "cite"+tag.text) for i, tag in enumerate(yeartags)])
            cites = dict([(tag.get("style").split(":")[-1], tag.text) for tag in soup.find("div", class_="gsc_md_hist_b").find_all("a", class_= "gsc_g_a")])

            yearcitedic = {}
            for idx in years.keys():
                try:
                    yearcitedic[years[idx]] = cites[idx]
                except:
                    yearcitedic[years[idx]] = 0

            for i in range(2024-1980):
                if "cite"+str(1980+i) not in yearcitedic.keys():
                    authordic["cite"+str(1980+i)].append("")
                else:
                    authordic["cite"+str(1980+i)].append(yearcitedic["cite"+str(1980+i)])
        except:
            for i in range(2024-1980):
                authordic["cite"+str(1980+i)].append("")

        # append other info
        authordic["authorid"].append(authorid)
        authordic["authorname"].append(name)
        authordic["misc"].append(misc)
        authordic["emailsuffix"].append(emailsuffix.lower())
        authordic["t2302cite"].append(t2302cite)
        authordic["s18t2302cite"].append(s18t2302cite)
        authordic["t2302hindex"].append(t2302hindex)
        authordic["s18t2302hindex"].append(s18t2302hindex)
        authordic["t2302i10index"].append(t2302i10index)
        authordic["s18t2302i10index"].append(s18t2302i10index)
        authordic["affiliationid"].append("")

df = pd.DataFrame(authordic)
df.to_csv("author.csv", index = False, encoding = "utf-8-sig")
df.to_csv("author_no_header.csv", index = False, header = False, encoding = "utf-8-sig")