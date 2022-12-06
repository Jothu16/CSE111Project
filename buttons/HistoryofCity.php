<br>
<br>
<button onclick="HistoryofCity()">Print the history of a city</button>

<?php
    function HistoryofCity($city) {
        $db = new SQLite3('../newdb.sqlite');

        $sql = "SELECT * FROM History WHERE History.City_key = (SELECT Capital_City.City_Key FROM Capital_City " .
        "WHERE Capital_City.Name = '" . $city . "')";

        echo "<table>";
                echo "<caption>Histoy of " . $city . "</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>History_Key</th><th>Date</th><th>AQI_Value</th><th>City_Key</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";


        $ret = $db->query($sql);
        while ($row = $ret->fetchArray()) {
            echo "<tr>";
            echo "<td>" . $row["History_Key"] . "</td>" .
                "<td>" . $row["Date"] . "</td>" .
                "<td>" . $row["AQI_Value"] . "</td>" .
                "<td>" . $row["City_Key"] . "</td>";
            echo "</tr>";
        }

        echo "</tbody>";
        echo "</table>";

        $db->close();
    }
    HistoryofCity($_POST["city_name"]);

?>