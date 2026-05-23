# &#x09;**Netflix Titles Dataset Analysis**

📌 **Project Overview**



This project is part of my college activity for Statistics and Data Analysis practice.

The goal of this project was to collect, clean, organize, and analyze a real-world dataset using Google Sheets.



For this analysis, I used the Netflix Titles Dataset, which contains information about Movies and TV Shows available on Netflix.

The dataset includes details such as title name, type, director, cast, country, release year, ratings, genres, and duration.



**The project helped me understand:**



* Data cleaning techniques
* Spreadsheet operations
* Data organization
* Basic exploratory data analysis (EDA)
* Finding insights from raw data
* Creating charts and summaries



**📂 Project Structure**



Data\_Analysis\_projects/

│

├── College\_Projects/

│   └── Netflix\_Data\_Analysis/

│       ├── README.md

│       ├── netflix\_titles.xlsx

│       ├── charts/

│       └── screenshots/

│

├── Major\_Projects/

│

└── Mini\_Projects/





🎯 **Objective**



The objective of this project was to:



* Work with a real-world dataset
* Understand how streaming platform data is structured
* Perform data cleaning and preprocessing
* Generate meaningful insights using spreadsheet analysis
* Build a beginner-level data analysis portfolio project



🗂 Dataset Information



The dataset contains Netflix Movies and TV Shows data.



**Important Columns**

**| Column Name    | Description                 |**

**| -------------- | --------------------------- |**

**| `show\\\_id`      | Unique ID of each title     |**

**| `type`         | Movie or TV Show            |**

**| `title`        | Name of the content         |**

**| `director`     | Director name               |**

**| `cast`         | Main actors/actresses       |**

**| `country`      | Production country          |**

**| `date\\\_added`   | Date added on Netflix       |**

**| `release\\\_year` | Original release year       |**

**| `rating`       | Audience rating             |**

**| `duration`     | Movie minutes or TV seasons |**

**| `listed\\\_in`    | Genre/category              |**

**| `description`  | Short summary               |**









**🧹 Data Cleaning Process**



The following preprocessing steps were performed:



* Checked and verified column headers
* Enabled filters for easy sorting
* Identified missing/null values
* Converted date columns into proper date format
* Extracted numeric duration values
* Split genres into separate categories
* Removed duplicate entries
* Organized data for analysis and visualization





Google Sheets Functions Used



=COUNTBLANK(range)



=DATEVALUE(cell)



=VALUE(REGEXEXTRACT(duration\_cell,"\\d+"))



=SPLIT(cell,", ")





📊 **Analysis Performed**

Basic Analysis

* Count of Movies vs TV Shows
* Country-wise content distribution
* Content ratings analysis
* Genre analysis
* Duration analysis
* Release year trends



Visualization Ideas



* Pie Chart → Movies vs TV Shows
* Bar Chart → Top Countries by Titles
* Word Cloud → Popular Genres
* Trend Analysis → Content added over years



🔍 **Key Insights \& Observations**



1\. Movies dominate Netflix content



&#x09;	Netflix contains more Movies than TV Shows.



2\. United States has the highest content production



&#x09;Most titles were produced in the United States, followed by India and the United Kingdom.



3\. Growth of TV Shows



&#x09;Recent years show a significant increase in TV Shows on Netflix.



4\. Popular Genres



&#x09;Drama, Comedy, and International TV Shows are among the most common genres.



5\. Mature audience content is common



&#x09;Ratings such as TV-MA and TV-14 appear most frequently.



6\. Strong international presence



&#x09;Netflix includes content from many countries including:



* &#x09;India
* &#x09;Korea
* &#x09;Japan
* &#x09;Spain
* &#x09;Canada

7\. Missing data exists



&#x09;Several records had missing director or cast information, highlighting the importance of data cleaning.



8\. Most TV Shows have fewer seasons



&#x09;Most shows contain only 1–2 seasons.



🛠 Tools \& Technologies Used

* Google Sheets
* Spreadsheet Functions
* Pivot Tables
* Data Cleaning Techniques
* Basic Data Visualization



📚 What I Learned



Through this project, I learned:



* How to clean raw datasets
* How to organize structured data
* How to analyze trends and patterns
* How to use spreadsheet formulas effectively
* Basics of Exploratory Data Analysis (EDA)
* How real-world datasets contain missing and inconsistent values



🚀 Future Improvements



In the future, I plan to:



* Analyze this dataset using Python (Pandas)
* Create dashboards using Power BI/Tableau
* Perform advanced visualizations
* Build recommendation-based analysis
* Use machine learning for content prediction



**📌 Conclusion**



This project was my first college-level data analysis project using a real-world Netflix dataset.

It helped me build foundational skills in:



* Data cleaning
* Spreadsheet analysis
* Visualization
* Insight generation



The project also improved my understanding of how data analysts work with structured datasets to extract meaningful business insights.



👨‍💻 **Author**



**Ayush Rajput**

**Aspiring Data Analyst \& Data Science Learner**

