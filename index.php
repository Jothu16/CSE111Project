<html>
<body>

<form action="../buttons/CountHistoryentries.php" method="get">
   <input type="submit" name="runQ" value="Count History and Users">
</form>

<br>

<form action="../buttons/CountCountriesandCapitals.php" method="get">
   <input type="submit" name="runQ" value="Count Cities and Countries">
</form>

<br>

<form action="../buttons/GetCurrentUserKey.php" method="post">
    First Name: <input type = "text" name="Firstname" />
    Last Name: <input type = "text" name="Lastname" />
   <input type="submit" name="runQ" value="Get User Key">
</form>

<br>

<form action="../buttons/AddNewUser.php" method="post">
    First Name: <input type = "text" name="newfirstname" />
    Last Name: <input type = "text" name="newlastname" />
   <input type="submit" name="runQ" value="Add User">
</form>

<br>

<form action="../buttons/DeleteUser.php" method="post">
    First Name: <input type = "text" name="deletefirstname" />
    Last Name: <input type = "text" name="deletelastname" />
   <input type="submit" name="runQ" value="Delete User">
</form>

<br>

<form action="../buttons/AddNewCountry.php" method="post">
    Country: <input type = "text" name="new_country_name" />
    Continent: <input type = "text" name="continent_name" />
   <input type="submit" name="runQ" value="Add Country">
</form>

<br>

<form action="../buttons/AddNewCity.php" method="post">
    Country: <input type = "text" name="country_name" />
    City: <input type = "text" name="new_city_name" />
   <input type="submit" name="runQ" value="Add City">
</form>

<br>

<form action="../buttons/DeleteCountry.php" method="post">
    Country: <input type = "text" name="country_name" />
   <input type="submit" name="runQ" value="Delete Country">
</form>

<br>

<form action="../buttons/DeleteCity.php" method="post">
    City: <input type = "text" name="city_name" />
   <input type="submit" name="runQ" value="Delete City">
</form>

<br>

<form action="../buttons/DeleteCityData.php" method="post">
    City: <input type = "text" name="city_name" />
   <input type="submit" name="runQ" value="Delete City Data">
</form>

<br>
<br>
<button onclick="updatefile()">Update file - date = new_date where date = old_date</button>
<input type="text">

<script>
function updatefile() 
{
    var inputId = document.getElementById("HospitalId").value; //we get the user input value and put it in a var

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "C:\Users\kingk\Documents\GitHub\CSE111Project\count_user_history.py" + inputId, true); // we're passing the hId to the server as a parameter
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("SearchBoxPt").value = this.responseText;
        }
    };
    xhttp.send(); 

}
</script>

<form action="../buttons/UpdateAQIforCity.php" method="post">
    User Key Login: <input type = "text" name="login" />
    City: <input type = "text" name="city_name" />
    Date: <input type = "text" name="new_date" />
    New AQ Value: <input type = "text" name="new_AQI_value" />
   <input type="submit" name="runQ" value="Update AQI Entry">
</form>


<!-- <br>
<br>
<button onclick="updatehistorynewentry()">update history with new entry</button>
<input type="text">

<script>
function updatehistorynewentry() 
{
    var inputId = document.getElementById("HospitalId").value; //we get the user input value and put it in a var

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "C:\Users\kingk\Documents\GitHub\CSE111Project\count_user_history.py" + inputId, true); // we're passing the hId to the server as a parameter
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("SearchBoxPt").value = this.responseText;
        }
    };
    xhttp.send(); 

}
</script> -->


<br>
<br>
<button onclick="newentrytoaqdatabase()">add new entry to current aq database</button>
<input type="text">

<script>
function newentrytoaqdatabase() 
{
    var inputId = document.getElementById("HospitalId").value; //we get the user input value and put it in a var

    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "C:\Users\kingk\Documents\GitHub\CSE111Project\count_user_history.py" + inputId, true); // we're passing the hId to the server as a parameter
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("SearchBoxPt").value = this.responseText;
        }
    };
    xhttp.send(); 

}
</script>

<form action="../buttons/GetDatafromCurrent.php" method="get">
   <input type="submit" name="runQ" value="Print Current_AQ_Info Table">
</form>

<br>

<form action="../buttons/AllEditsmadebyUser.php" method="get">
   <input type="submit" name="runQ" value="Count Edits">
</form>

<br>
<button onclick="myFunction()">print lowest and highest country's AQI Value</button>

<br>
<form action="../buttons/CitiesGoodStatus.php" method="post">
    Status: <input type = "text" name="status" />
   <input type="submit" name="runQ" value="Print Cities With Given Status">
</form>

<br>
<br>
<button onclick="myFunction()">print all countries with a "good" status</button>

<br>
<br>
<button onclick="myFunction()">print all continents with a country with "good" status and how many</button>

<br>
<br>
<button onclick="myFunction()">Count the amount of entries for each status description</button>

<br>
<br>
<button onclick="myFunction()">Print the history of a city</button>

<br>
<br>
<button onclick="myFunction()">print average air quality and the average status of each continent</button>

<br>
<br>
<button onclick="myFunction()">count the amount of times each city had a certain status</button>

<br>
<br>
<button onclick="myFunction()">find cities that had both "Good" and "Moderate" Statuses in its history - change variables if needed</button>

<br>
<br>
<button onclick="myFunction()">find all cities except for unhealthy or worse cities</button>

<br>
<br>
<button onclick="myFunction()">print all cities that had changes in statuses and order by date</button>

<br>
<br>
<button onclick="myFunction()">select all countries status</button>

</body>
</html>