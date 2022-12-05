<?php
    function Low_and_High_CountryAQI() {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT best_con.Name as name, MIN(best_aq.AQI_Value) as value " .
        "FROM Current_AQ_Info best_aq " .
        "INNER JOIN Capital_City best_city ON best_aq.City_Key = best_city.City_Key " .
        "INNER JOIN Country best_con ON best_city.Country_Key = best_con.Country_Key " .
        "UNION " .
        "SELECT worst_con.Name as name, MAX(worst_aq.AQI_Value) as value " .
        "FROM Current_AQ_Info worst_aq " .
        "INNER JOIN Capital_City worst_city ON worst_aq.City_Key = worst_city.City_Key " .
        "INNER JOIN Country worst_con ON worst_city.Country_Key = worst_con.Country_Key ";

        echo "<table>";
        echo "<caption>Best and Worst City</caption>";
        echo "<thead>";
        echo "<tr>";
        echo "<th>Category</th><th>City Name</th><th>Air Quality Value</th>";
        echo "</tr>";
        echo "</thead>";
        echo "<tbody>";


        $ret = $db->query($sql);
        $row = $ret->fetchArray();

        echo "<tr>";
        echo "<td>Best</td>" .
            "<td>" . $row["name"] . "</td>" .
            "<td>" . $row["value"] . "</td>";
        echo "</tr>";

        $row = $ret->fetchArray();

        echo "<tr>";
        echo "<td>Worst</td>" .
            "<td>" . $row["name"] . "</td>" .
            "<td>" . $row["value"] . "</td>";
        echo "</tr>";

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    Low_and_High_CountryAQI();

?>