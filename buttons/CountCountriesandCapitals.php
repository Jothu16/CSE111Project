<br>
<br>
<button onclick="countamountofcountriesandcapitals()">count the amount of countries and their capital cities and their entries(city count = country count since country can only have 1 capital)</button>

<script>
function countamountofcountriesandcapitals() 
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