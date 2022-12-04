<?php
    function getProducts($maker, $product) {
        if ($maker == "") {
            echo "<div style='float:left;width:100%; background-color:pink;color:#ffffff;text-align:center;'>No maker provided</div>";
            return;
        }

        try {
            $db = new SQLite3('../data.sqlite');

            if ($product == "All") {
                $sql =
                "select P.model as model, P.type as type, PC.price as price " .
                "from Product P, PC " .
                "where P.model = PC.model AND maker = '" . $maker . "' " .
                "UNION " .
                "select P.model as model, P.type as type, L.price as price " .
                "from Product P, Laptop L " .
                "where P.model = L.model AND maker = '" . $maker . "' " .
                "UNION " .
                "select P.model as model, P.type as type, Pr.price as price " .
                "from Product P, Printer Pr " .
                "where P.model = Pr.model AND maker = '" . $maker  . "' ";

                echo "<table>";
                echo "<caption>product by maker " . $maker . "</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Model</th><th>Type</th><th>Price</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

                $ret = $db->query($sql);
                while ($row = $ret->fetchArray()) {
                    echo "<tr>";
                    echo "<td>" . $row["model"] . "</td>" .
                        "<td>" .$row["type"] . "</td>" .
                        "<td>" .$row["price"] . "</td>";
                    echo "</tr>";
                }

                echo "</tbody>";
                echo "</table>";
            }
            else {
                $sql = "select P.model as model, " . $product . ".price as price "
                    . "from Product P, " . $product
                    . " where P.model = " . $product . ".model AND " . "maker = '" . $maker . "'";

                echo "<table>";
                echo "<caption>" . $product . " by maker " . $maker . "</caption>";
                echo "<thead>";
                echo "<tr>";
                echo "<th>Model</th><th>Price</th>";
                echo "</tr>";
                echo "</thead>";
                echo "<tbody>";

                $ret = $db->query($sql);
                while ($row = $ret->fetchArray()) {
                    echo "<tr>";
                    echo "<td>" . $row["model"] . "</td>" .
                        "<td>" .$row["price"] . "</td>";
                    echo "</tr>";
                }

                echo "</tbody>";
                echo "</table>";
            }

            $db->close();
        }
        catch (Exception $e) {
            echo "<h2 style='width:100%; background-color:ff0000;color:#ffffff;text-align:center;'>Database error!</h2><br/>" . $e;
        }
    }
    
    // Perform action
    getProducts($_GET["maker"], $_GET["product"]);
?>
