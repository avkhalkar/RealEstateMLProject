// Retrieve selected bathroom value from radio buttons
function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(i) + 1; // Return selected bath count (1-indexed)
    }
  }
  return -1; // Return -1 if no valid selection
}

// Retrieve selected BHK value from radio buttons
function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1; // Return selected BHK count (1-indexed)
    }
  }
  return -1; // Return -1 if no valid selection
}

// Called when "Estimate Price" button is clicked
// Collects input values and sends a POST request to Flask backend
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price";

  // Send user inputs to the backend using jQuery's POST method
  $.post(url, {
    total_sqft: parseFloat(sqft.value),
    bhk: bhk,
    bath: bathrooms,
    location: location.value
  }, function(data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>"; // Display prediction
    console.log(status);
  });
}

// Called when page is loaded
// Fetches location names from backend and populates the dropdown
function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_location_names";

  $.get(url, function(data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");

      $('#uiLocations').empty(); // Clear existing options
      $('#uiLocations').append(new Option("Choose a Location", "", true, true)).prop('disabled', false); // Default option

      // Add new options fetched from backend
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $('#uiLocations').append(opt);
      }
    }
  });
}

// Trigger location population on page load
window.onload = onPageLoad;
