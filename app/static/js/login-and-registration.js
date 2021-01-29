
// if the user presses the spacebar, the input should be ignored
function addWhitespaceListener() {
  $('input:not(input[name="submit"])').on('keypress', function(event) {
    if (event.which == 32) {
      event.preventDefault();
    }
  });
}

// if the input was empty when 'submit' was clicked, and the 'tab'
// key was then clicked while focused on the empty input, it will
// remove the 'invalid' class so the input displays as normal
function addTabKeyListener() {
  $('input:not(input[name="submit"])').on('keydown', function(event) {
    if (event.which == 9) {
      $(this).removeClass('invalid');
    }
  });
}

// 
function addChangeListener() {
  // input 'change' event is when input loses focus
  $('input:not(input[name="submit"])').on('focus focusout change paste keyup', function(event) {
    handleInputChange($(this), event);
  });
}

function handleInputChange(input, event) {
  if (event.type == 'paste') {
    setTimeout(function() {
      input.val(input.val().split(' ').join('')); // wait for val() to be updated
    }, 0);
  }
  else if (event.type == 'keyup') {
    if (input.val() != '') { // prevent validation message spam if input gets updated
      input[0].setCustomValidity('');
      input.removeClass('invalid'); 
    }

    if (input[0].name == 'password' && input.val() == '') {
      $('input[name="confirm_password"]').val('');
      $('input[name="confirm_password"]').prop('disabled', true);
      $('i').each(function() {
        $(this).removeClass('icon-shown');
      });
      $('i').each(function() {
        $(this).addClass('icon-hidden');
      });
    }
    else if (input[0].name == 'password' && input.val() != '') {
      $('input[name="confirm_password"]').prop('disabled', false);
    }

    if (input[0].name == 'confirm_password' && input.val() == '') {
      $('i.fa-check').removeClass('icon-shown');
      $('i.fa-times').removeClass('icon-shown');
      $('i.fa-check').addClass('icon-hidden');
      $('i.fa-times').addClass('icon-hidden');
    }
    else if (input[0].name == 'confirm_password' && input.val() != '' && input.val() != $('input[name="password"]').val()) {
      $('i.fa-times').addClass('icon-shown');
      $('i.fa-times').removeClass('icon-hidden');
      $('i.fa-check').addClass('icon-hidden');
      $('i.fa-check').removeClass('icon-shown');
    }
    else if (input[0].name == 'confirm_password' && input.val() != '' && input.val() == $('input[name="password"]').val()) {
      $('i.fa-check').addClass('icon-shown');
      $('i.fa-check').removeClass('icon-hidden');
      $('i.fa-times').addClass('icon-hidden');
      $('i.fa-times').removeClass('icon-shown');
    }
  }
  else if (event.type == 'focus') {
    if (input[0].name == 'confirm_password' && input.val() != '') {
      if (input.val() != $('input[name="password"]').val()) {
        $('i.fa-times').addClass('icon-shown');
        $('i.fa-times').removeClass('icon-hidden');
        $('i.fa-check').addClass('icon-hidden');
        $('i.fa-check').removeClass('icon-shown');
      }
      else {
        $('i.fa-check').addClass('icon-shown');
        $('i.fa-check').removeClass('icon-hidden');
        $('i.fa-times').addClass('icon-hidden');
        $('i.fa-times').removeClass('icon-shown');
      }
    } 
  }
  else if (event.type == 'focusout') {
    if (input.val() == '' || (input[0].name == 'username' && !isValidUsername(input.val()))) { // remove invalid class if user clicks outside invalid input field
      input.removeClass('invalid'); 
    }

    $('i.fa-check').removeClass('icon-shown');
    $('i.fa-times').removeClass('icon-shown');
    $('i.fa-check').addClass('icon-hidden');
    $('i.fa-times').addClass('icon-hidden');
  }
}

function isValidUsername(usernameInput) {
  return (new RegExp('^[A-Za-z0-9]+$', 'g')).test(usernameInput);
}

$(document).ready(function() {
  $('input').each(function() {
    $(this)[0].setCustomValidity('');
  });

  var usernameInput = $('input[name="username"]');
  var emailInput = $('input[name="email"]');
  var passwordInput = $('input[name="password"]');
  var confirmPasswordInput = $('input[name="confirm_password"]');

  confirmPasswordInput.prop('disabled', true);

  addTabKeyListener();
  addWhitespaceListener();
  addChangeListener();

  $('input[name="submit"]').on('click', function() {
    if (usernameInput.val() == '') {
      usernameInput[0].setCustomValidity('Please enter a username.');
      usernameInput.addClass('invalid');
    } 
    else if (emailInput.val() == '') {
      emailInput[0].setCustomValidity('Please enter an email.');
      emailInput.addClass('invalid');
    }
    else if (passwordInput.val() == '') {
      passwordInput[0].setCustomValidity('Please enter a password.');
      passwordInput.addClass('invalid');
    }
    else if (confirmPasswordInput.val() == '') {
      confirmPasswordInput[0].setCustomValidity('Please confirm password.');
      confirmPasswordInput.addClass('invalid');
    }
    else if (!isValidUsername(usernameInput.val())) {
      usernameInput[0].setCustomValidity('Please use only numbers and letters.');
      usernameInput.addClass('invalid');
    }
    else if (confirmPasswordInput.val() != passwordInput.val()) {
      confirmPasswordInput[0].setCustomValidity('Passwords must match.');
      confirmPasswordInput.addClass('invalid');
    }
  });
});


