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
  
  var address = $("#street1").val();
  var address2 = $("#street2").val();
  var city = $("#city").val();
  var state = $("#state").val();
  var post = $("#post").val();
  var country = $("#country").val();
  
  var params = "user=".concat(user).concat("&guest=").concat(guest).concat("&address=").concat(address).concat("&address2=").concat(address2).concat("&city=").concat(city).concat("&state=").concat(state).concat("&post=").concat(post).concat("&country=").concat(country);

  xhttp.open("POST", "addresshelper.py", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(params);
}

