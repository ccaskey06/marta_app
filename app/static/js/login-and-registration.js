
// Add Dynamic Validation Messages...
// Clear Content and Disable Confirm Input Until Password Input has Text...

$(document).ready(function() {
  $('input[name="password"]').keyup(function() {
    $('input[name="confirm_password"]')[0].setCustomValidity("");
    var pass = $('input[name="password"]').val();
    var confirm = $('input[name="confirm_password"]').val();

    if (confirm.length > 0) {
      if (pass.length < confirm.length) {
        $('input[name="confirm_password"]')[0].setCustomValidity("Confirm Password Too Long For Password");
      } else if (pass.length > confirm.length) {
        $('input[name="confirm_password"]')[0].setCustomValidity("Confirm Password Too Short For Password");
      } else if (pass != confirm) {
        $('input[name="confirm_password"]')[0].setCustomValidity("Confirm Password Must Match Password");
      } else {
        $('input[name="confirm_password"]')[0].setCustomValidity("");
      }
    }
  });

  $('input[name="confirm_password"]').keyup(function() {
    $(this)[0].setCustomValidity("");
    var pass = $('input[name="password"]').val();
    var confirm = $('input[name="confirm_password"]').val();
    
    if (confirm.length > 0) {
      if (pass.length < confirm.length) {
        $(this)[0].setCustomValidity("Confirm Password Too Long For Password");
      } else if (pass.length > confirm.length) {
        $(this)[0].setCustomValidity("Confirm Password Too Short For Password");
      } else if (pass != confirm) {
        $(this)[0].setCustomValidity("Confirm Password Must Match Password");
      } else {
        $(this)[0].setCustomValidity("");
      }
    }
  });
});
