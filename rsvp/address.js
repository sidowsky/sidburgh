function updateAddress()
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("results").innerHTML = xhttp.responseText;
    }
  };
  var user = $("#user").val();
  var guest = $("#guest").val();
  
  var address = $("#street1").val().concat("\n").concat($("#street2").val()).concat("\n").concat($("#city").val()).concat("\n").concat($("#state").val()).concat("\n").concat($("#post").val()).concat("\n").concat($("#country").val());
  
  var params = "user=".concat(user).concat("&guest=").concat(guest).concat("&address=").concat(address)
  xhttp.open("POST", "addresshelper.py", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(params);
}

