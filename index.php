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
    <label>First Name:</label> <input type = "text" name="Firstname" />
    <label>Last Name:</lable> <input type = "text" name="Lastname" />
   <input type="submit" name="runQ" value="Get User Key">
</form>

<br>
<br>
<br>

<form action="../buttons/AddNewUser.php" method="post">
    <label>First Name:</label> <input type = "text" name="newfirstname" />
    <label>Last Name:</label> <input type = "text" name="newlastname" />
   <input type="submit" name="runQ" value="Add User">
</form>

<br>

<form action="../buttons/DeleteUser.php" method="post">
    <label>First Name:</label> <input type = "text" name="deletefirstname" />
    <label>Last Name:</label> <input type = "text" name="deletelastname" />
   <input type="submit" name="runQ" value="Delete User">
</form>

<br>

<form action="../buttons/AddNewCountry.php" method="post">
    <label>Country:</label> <input type = "text" name="new_country_name" />
    <label>Continent:</label> <input type = "text" name="continent_name" />
   <input type="submit" name="runQ" value="Add Country">
</form>

<br>

<form action="../buttons/AddNewCity.php" method="post">
    <label>Country:</label> <input type = "text" name="country_name" />
    <label>City:</label> <input type = "text" name="new_city_name" />
   <input type="submit" name="runQ" value="Add City">
</form>

<br>

<form action="../buttons/DeleteCountry.php" method="post">
    <label>Country:</label> <input type = "text" name="country_name" />
   <input type="submit" name="runQ" value="Delete Country">
</form>

<br>

<form action="../buttons/DeleteCity.php" method="post">
    <label>City:</label> <input type = "text" name="city_name" />
   <input type="submit" name="runQ" value="Delete City">
</form>

<br>

<form action="../buttons/DeleteCityData.php" method="post">
    <label>City:</label> <input type = "text" name="city_name" />
   <input type="submit" name="runQ" value="Delete City Data">
</form>

<br>

<form action="../buttons/UpdateFile.php" method="post">
    <label>Old Date:</label> <input type = "text" name="old_date" />
    <label>New Date:</label> <input type = "text" name="new_date" />
   <input type="submit" name="runQ" value="Update Date">
</form>

<br>

<form action="../buttons/UpdateAQIforCity.php" method="post">
    <label>User Key Login:</label> <input type = "text" name="login" />
    <label>City:</label> <input type = "text" name="city_name" />
    <label>Date:</label> <input type = "text" name="new_date" />
    <label>New AQ Value:</label> <input type = "text" name="new_AQI_value" />
   <input type="submit" name="runQ" value="Update AQI Entry">
</form>

<br>

<form action="../buttons/AddEntrytoCurrent.php" method="post">
    <label>User Key Login:</label> <input type = "text" name="login" />
    <label>City:</label> <input type = "text" name="city_name" />
    <label>Date:</label> <input type = "text" name="new_date" />
    <label>New AQ Value:</label> <input type = "text" name="new_AQI_value" />
   <input type="submit" name="runQ" value="Add AQI Entry">
</form>

<br>

<form action="../buttons/GetDatafromCurrent.php" method="get">
   <input type="submit" name="runQ" value="Print Current_AQ_Info Table">
</form>

<br>

<form action="../buttons/get_city_table.php" method="get">
   <input type="submit" name="runQ" value="Print Capital_City Table">
</form>

<br>

<form action="../buttons/get_country_table.php" method="get">
   <input type="submit" name="runQ" value="Print Country Table">
</form>

<br>

<form action="../buttons/get_continent_table.php" method="get">
   <input type="submit" name="runQ" value="Print Continent Table">
</form>

<br>

<form action="../buttons/get_history.php" method="get">
   <input type="submit" name="runQ" value="Print History Table">
</form>

<br>

<form action="../buttons/get_history_status.php" method="get">
   <input type="submit" name="runQ" value="Print HistoryStatus Table">
</form>

<br>

<form action="../buttons/get_status.php" method="get">
   <input type="submit" name="runQ" value="Print Status Table">
</form>

<br>

<form action="../buttons/get_user_edits.php" method="get">
   <input type="submit" name="runQ" value="Print UserEdits Table">
</form>

<br>

<form action="../buttons/get_users.php" method="get">
   <input type="submit" name="runQ" value="Print Users Table">
</form>

<br>

<form action="../buttons/AllEditsmadebyUser.php" method="get">
   <input type="submit" name="runQ" value="Count Edits">
</form>

<br>

<form action="../buttons/LowandHighCountryAQI.php" method="get">
   <input type="submit" name="runQ" value="Best and Worst">
</form>

<br>

<form action="../buttons/CitiesGoodStatus.php" method="get">
    <label>Status:</label>
    <select name="status" id="status">
      <option value='Good'>Good</option>
      <option value='Moderate'>Moderate</option>
      <option value='Unhealthy for Sensitive Groups'>Unhealthy for Sensitive Groups</option>
      <option value='Unhealthy'>Unhealthy</option>
      <option value='Very Unhealthy'>Very Unhealthy</option>
      <option value='Maroon'>Maroon</option>
    </select>
   <input type="submit" name="runQ" value="Print Cities With Given Status">
</form>

<br>

<form action="../buttons/CountiresGoodStatus.php" method="get">
    <label>Status:</label>
    <select name="status" id="status">
      <option value='Good'>Good</option>
      <option value='Moderate'>Moderate</option>
      <option value='Unhealthy for Sensitive Groups'>Unhealthy for Sensitive Groups</option>
      <option value='Unhealthy'>Unhealthy</option>
      <option value='Very Unhealthy'>Very Unhealthy</option>
      <option value='Maroon'>Maroon</option>
    </select>
   <input type="submit" name="runQ" value="Print Countries With Given Status">
</form>

<br>

<form action="../buttons/CountiresGoodHowMany.php" method="get">
    <label>Status:</label>
    <select name="status" id="status">
      <option value='Good'>Good</option>
      <option value='Moderate'>Moderate</option>
      <option value='Unhealthy for Sensitive Groups'>Unhealthy for Sensitive Groups</option>
      <option value='Unhealthy'>Unhealthy</option>
      <option value='Very Unhealthy'>Very Unhealthy</option>
      <option value='Maroon'>Maroon</option>
    </select>
   <input type="submit" name="runQ" value="Print Continents With Given Status">
</form>

<br>

<form action="../buttons/EntriesForEachStatus.php" method="get">
   <input type="submit" name="runQ" value="Get Amount of Entries for Each Status">
</form>

<br>

<form action="../buttons/HistoryofCity.php" method="post">
    <label>City:</label> <input type = "text" name="city_name" />
   <input type="submit" name="runQ" value="Get History">
</form>

<br>

<form action="../buttons/AverageAQandStatusContinent.php" method="get">
   <input type="submit" name="runQ" value="Get Average">
</form>

<br>

<form action="../buttons/CountCityCertainStatus.php" method="get">
   <input type="submit" name="runQ" value="Count Amount of Status Each City Had">
</form>

<br>

<form action="../buttons/CitiesGood&Moderate.php" method="get">
    <label>Status 1:</label>
    <select name="status1" id="status1">
      <option value='Good'>Good</option>
      <option value='Moderate'>Moderate</option>
      <option value='Unhealthy for Sensitive Groups'>Unhealthy for Sensitive Groups</option>
      <option value='Unhealthy'>Unhealthy</option>
      <option value='Very Unhealthy'>Very Unhealthy</option>
      <option value='Maroon'>Maroon</option>
    </select>

    <label>Status 2:</label>
    <select name="status2" id="status2">
      <option value='Good'>Good</option>
      <option value='Moderate'>Moderate</option>
      <option value='Unhealthy for Sensitive Groups'>Unhealthy for Sensitive Groups</option>
      <option value='Unhealthy'>Unhealthy</option>
      <option value='Very Unhealthy'>Very Unhealthy</option>
      <option value='Maroon'>Maroon</option>
    </select>
   <input type="submit" name="runQ" value="Print Cities with Two Selected Statuses">
</form>

<br>

<form action="../buttons/ALLCitiesexceptunhealthy.php" method="get">
    <label>Status:</label>
    <select name="status" id="status">
      <option value='Good'>Good</option>
      <option value='Moderate'>Moderate</option>
      <option value='Unhealthy for Sensitive Groups'>Unhealthy for Sensitive Groups</option>
      <option value='Unhealthy'>Unhealthy</option>
      <option value='Very Unhealthy'>Very Unhealthy</option>
      <option value='Maroon'>Maroon</option>
    </select>
   <input type="submit" name="runQ" value="Find all Cities with Status Better than Selected">
</form>

<br>
<br>
<button onclick="myFunction()">print all cities that had changes in statuses and order by date</button>

<br>
<br>
<button onclick="myFunction()">select all countries status</button>

</body>
</html>