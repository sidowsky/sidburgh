function saveGuest(guest_id)
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("results_".concat(guest_id)).innerHTML = xhttp.responseText;
    }
  };

  var first = $("#first_".concat(guest_id)).val();
  var last = $("#last_".concat(guest_id)).val();
  var first2 = $("#first2_".concat(guest_id)).val();
  var last2 = $("#last2_".concat(guest_id)).val();
  var address = $("#address_".concat(guest_id)).val().replace("\n"," ");
  var email = $("#email_".concat(guest_id)).val();
  var max = $("#max_".concat(guest_id)).val();
  var tag = $("#tag_".concat(guest_id)).val();

  var params = "id=".concat(guest_id);
  params = params.concat("&name=").concat(first);
  params = params.concat("&last=").concat(last);
  params = params.concat("&first2=").concat(first2);
  params = params.concat("&last2=").concat(last2);
  params = params.concat("&email=").concat(email);
  params = params.concat("&max=").concat(max);
  params = params.concat("&tag=").concat(tag);
  params = params.concat("&address=").concat(address);

  //document.getElementById("results").innerHTML = params

  xhttp.open("GET", "saveguest.py?".concat(params), true );
  xhttp.send();
  //xhttp.open("POST", "saveguest.py", true );
  //xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  //xhttp.send(params);
}
