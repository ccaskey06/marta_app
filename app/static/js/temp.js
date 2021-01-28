function isValidKey(event) {
  return $.isNumeric(String.fromCharCode(event.which)) || event.which == 8;
}

$(document).ready(function() {
  $('input[name="transit_card"]').on('keypress', function(event) {
    // prevent non-numeric characters from being shown in input field

    if (!isValidKey(event)) {
      event.preventDefault();
    }
  });

  $('input[name="transit_card"]').on('keyup', function(event) {
    if ($.isNumeric(String.fromCharCode(event.which))) {
      // place whitespace between every 4 characters

      var formattedCardNum = $(this).val().split(' ').join('');

      if (formattedCardNum.length > 0) {
        formattedCardNum = formattedCardNum.match(new RegExp('.{1,4}', 'g')).join(' ');
      }

      $(this).val(formattedCardNum);
    }
    else if (event.which == 8) {
      // remove trailing whitespace if deleting character led
      // to some multiple of 4 characters remaining

      $(this).val($(this).val().trim());
    }
  });
});

// // Array To Hold First Password Input
// var pass = new Array("");

// // User Selects "Have Breezecard" Option
// // Function Displays Input For Breezecard Number - Makes It Required
// $(document).ready(function(){
//   $("#haveBreezecard").click(function(){
//     if ($(this).is(":checked")) {
//       $("#breezecard").show("fast","linear").prop("required", true);
//     }
//   });
// });

// // User Selects "Need"Breezecard" Option
// // Function Hides Input For Breezecard Number - Makes It Not Required
// $(document).ready(function(){
//   $("#needBreezecard").click(function(){
//     if ($(this).is(":checked")) {
//       $("#breezecard").hide("fast","linear").prop("required", false);
//     }
//   });
// });
