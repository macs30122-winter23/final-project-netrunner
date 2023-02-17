CREATE TABLE author
  (authorid char(12),
   name varchar(30),
   misc varchar(100),
   emailsuffix varchar(50),
   t2302cite integer,
   s18t2302cite integer,
   t2302hindex integer,
   s18t2302hindex integer,
   t2302i10index integer,
   s18t2302i10index integer,
	cite1980 integer,
	cite1981 integer,
	cite1982 integer,
	cite1983 integer,
	cite1984 integer,
	cite1985 integer,
	cite1986 integer,
	cite1987 integer,
	cite1988 integer,
	cite1989 integer,
	cite1990 integer,
	cite1991 integer,
	cite1992 integer,
	cite1993 integer,
	cite1994 integer,
	cite1995 integer,
	cite1996 integer,
	cite1997 integer,
	cite1998 integer,
	cite1999 integer,
	cite2000 integer,
	cite2001 integer,
	cite2002 integer,
	cite2003 integer,
	cite2004 integer,
	cite2005 integer,
	cite2006 integer,
	cite2007 integer,
	cite2008 integer,
	cite2009 integer,
	cite2010 integer,
	cite2011 integer,
	cite2012 integer,
	cite2013 integer,
	cite2014 integer,
	cite2015 integer,
	cite2016 integer,
	cite2017 integer,
	cite2018 integer,
	cite2019 integer,
	cite2020 integer,
	cite2021 integer,
	cite2022 integer,
	cite2023 integer,
	affiliationid varchar(50)
   );

.separator ","
.import author_no_header.csv author

CREATE TABLE article
  (doi varchar(100),
	journal varchar(50),
	volume varchar(50),
	date char(10),
	title varchar(100),
	abstract varchar(1000),
	url varchar(100)
   );

.separator ","
.import article_no_header.csv article

CREATE TABLE author_article
	(authorid char(12),
	 doi varchar(100)
	);

.separator ","
.import author_article_no_header.csv author_article

CREATE TABLE affiliation
	(affiliationid varchar(50),
	 name varchar(100),
	 email varchar(50)
	);

.separator ","
.import affiliation_no_header.csv affiliation