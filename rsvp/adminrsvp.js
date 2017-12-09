function getStats()
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("results").innerHTML = xhttp.responseText;
      $("#stats").trigger("update");
    }
  };
  var event = $('input[name="radio-event"]:checked').val();
  var category = $('input[name="radio-tag"]:checked').val();
  var params = "event=".concat(event).concat("&category=").concat(category);
  xhttp.open("POST", "adminhelper.py", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(params);
}
function showPlayerStats(url, element)
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("dialog").innerHTML = xhttp.responseText;
      $("#dialog").dialog( { position: {  my : 'center top+15%', at : 'center top', of : element } } );
      $("#dialog").dialog("open");
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}

