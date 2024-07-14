# LA-Times-Robot
<h2>Parameters</h2>
All the parameters needed are received through a GUI which accepts: <br>
1. Search phrase<br>
2. Number of months (example on how this should work: 0 or 1 - only the current month, 2 - current and previous month, 3 - current and two previous months and so on...)<br>
<h2>How does the robot work?</h2>
1. The robot will acces the site by following the link 'https://www.latimes.com/'<br>
2. It will enter a phrase in the search field<br>
3. On the results page it will sort the articles by the newest published<br>
4. For each result it will get the following values: title, date, description, will download the picture and get the filename<br>
5. All the data is stored in and output folder (/output) that will contain all the pictures downloaded and an Excel file<br>
5.1 The excel file will have the following columns:<br>
        - title<br>
        - date<br>
        - description (if available)<br>
        - picture filename (if available)<br>
        - count of search phrases in the title and description<br>
        - True or False, depending on whether the title or description contains any amount of money<br><br>

For further information please refer to the GIF below.<br>
![](https://github.com/Mircea9311/LA-Times-Robot/blob/main/LA%20Times%20Robot.gif)
<h2>How can you run it?</h2>
You have 2 options to run the robot:
<h3>By running the executable file taken from releases.</h3>
Just download the file and run it. 
Please note the file is not digitally signed and windows will notify you about the risks.
<h3>By downloading the source code.</h3>
You will need Python 3.1x+ installed <br>
pip install -r requirements.txt <br>
python3 main.py <br>
