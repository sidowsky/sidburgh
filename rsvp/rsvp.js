function submitRSVP()
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("results").innerHTML = xhttp.responseText;
    }
  };
  var user = $("#user").val();
  var guest = $("#guest").val();
  var rsvp = $("#rsvp").val();
  var attending = $("#attending").val();
  var notes = $("#notes").val();
  
  if (rsvp == "YES") {
    rsvp = 1
  }
  else {
    rsvp = 0
  }

  //notes = notes.replace(/'/g,"\\'");
  //notes = notes.replace(/\"/g,"\\\"");


  var params = "user=".concat(user).concat("&guest=").concat(guest).concat("&attending=").concat(attending).concat("&rsvp=").concat(rsvp).concat("&notes=").concat(notes)
  xhttp.open("POST", "rsvphelper.py", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(params);
}

