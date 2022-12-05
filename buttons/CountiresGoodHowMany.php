<?php
    function Continents_withCountry_Good_HowMany($status) {
        $db = new SQLite3('../newdb.sqlite');

        $ret = $db->query("select Threshold_Lower, Threshold_Upper FROM Status WHERE Description = '" . $status . "'");
        $threshold = $ret->fetchArray();

        $sql = "SELECT Continent.Name, COUNT(Country.Name) as cnt FROM Current_AQ_Info " .
        "INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key " .
        "INNER JOIN Country ON Capital_City.Country_Key = Country.Country_Key " .
        "INNER JOIN Continent ON Country.Cont_Key = Continent.Cont_Key " .
        "INNER JOIN (SELECT DISTINCT Capital_City.Name AS good_ones FROM Current_AQ_Info, Status " .
                            "INNER JOIN Capital_City ON Current_AQ_Info.City_Key = Capital_City.City_Key " .
                            "WHERE Current_AQ_Info.AQI_Value >= " . $threshold['Threshold_Lower'] . " " .
                            "AND Current_AQ_Info.AQI_Value <= " . $threshold['Threshold_Upper'] . ")" .
            "AS good_cities ON good_cities.good_ones = Capital_City.Name " .
        "GROUP BY Continent.Name";

        echo "<table>";
                echo "<caption>Continents with " . $status . " Status</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Continent Name</th><th>Count</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["Name"] . "</td>" .
                    "<td>" . $row["cnt"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    Continents_withCountry_Good_HowMany($_GET["status"]);

?>