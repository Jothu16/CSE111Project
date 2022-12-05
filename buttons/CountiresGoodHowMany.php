<br>
<br>
<button onclick="Continents_withCountry_Good_HowMany()">print all continents with a country with "good" status and how many</button>

<?php
    function Continents_withCountry_Good_HowMany() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT Continent.Name, COUNT(Country.Name) FROM Current_AQ_Info
        INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
        INNER JOIN Country ON Capital_City.Country_Key = Country.Country_Key
        INNER JOIN Continent ON Country.Cont_Key = Continent.Cont_Key
        INNER JOIN (SELECT DISTINCT Capital_City.Name AS good_ones FROM Current_AQ_Info, Status
                            INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key
                            WHERE Current_AQ_Info.AQI_Value >= 0
                            AND Current_AQ_Info.AQI_Value <= 50)
             AS good_cities ON good_cities.good_ones = Capital_City.Name
        GROUP BY Continent.Name";

        echo "<table>";
        echo "<caption>Totals</caption>";
        echo "<tbody>";

        $ret = $db->query($sql);
        $row = $ret->fetchArray();
            
        echo "<tr>";
        echo "<td>User Count: " . $row['total'] . "</td>";
        echo "</tr>";

        $row = $ret->fetchArray();
            
        echo "<tr>";
        echo "<td>History Count: " . $row['total'] . "</td>";
        echo "</tr>";

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    Continents_withCountry_Good_HowMany();

?>