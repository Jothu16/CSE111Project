<html>
<body>

<form action="../buttons/CountHistoryentries.php" method="get">
   <input type="submit" name="runQ" value="Count History and Users">
</form>

<form action="../buttons/CountCountriesandCapitals.php" method="get">
   <input type="submit" name="runQ" value="Count Cities and Countries">
</form>

<form action="../buttons/GetCurrentUserKey.php" method="post">
    First Name: <input type = "text" name="Firstname" />
    <br>
    <br>
    Last Name: <input type = "text" name="Lastname" />
   <input type="submit" name="runQ" value="Get User Key">
</form>

<form action="../buttons/AddNewUser.php" method="post">
    First Name: <input type = "text" name="newfirstname" />
    <br>
    <br>
    Last Name: <input type = "text" name="newlastname" />
   <input type="submit" name="runQ" value="Add User">
</form>

<script>
function addnewuser() 
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


<br>
<br>
<button onclick="deleteuser()">delete user</button>
<input type="text">

<script>
function deleteuser() 
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


<br>
<br>
<button onclick="addnewcountry()">add new country</button>
<input type="text">

<script>
function addnewcountry() 
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


<br>
<br>
<button onclick="addnewcity()">add new city</button>
<input type="text">

<script>
function addnewcity() 
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


<br>
<br>
<button onclick="deletecountry()">delete country</button>
<input type="text">

<script>
function deletecountry() 
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


<br>
<br>
<button onclick="deletecity()">delete city</button>
<input type="text">

<script>
function deletecity() 
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


<br>
<br>
<button onclick="deletecitydata()">Delete data relating to a city - copy paste this segment and change some names to make work with other tables</button>
<input type="text">


<script>
function deletecitydata() 
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


<br>
<br>
<button onclick="updateAQIforcity()">update aqi value of a city - records user who did - check valid data later</button>
<input type="text">

<script>
function updateAQIforcity() 
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


<br>
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
</script>


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

<form action="../buttons/AllEditsmadebyUser.php" method="get">
   <input type="submit" name="runQ" value="Count Edits">
</form>

<br>
<br>
<button onclick="myFunction()">print lowest and highest country's AQI Value</button>

<form action="../buttons/CitiesGoodStatus.php" method="get">
   <input type="submit" name="runQ" value="Print Good Cities">
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