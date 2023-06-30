document.addEventListener("DOMContentLoaded", function () {
  const contactForm = document.getElementById("contact-form");
  contactForm.addEventListener("submit", function (event) {
    if (!validateForm()) {
    event.preventDefault();
    }
  });

  function validateForm() {
    const nameInput = document.getElementById("id_name");
    const emailInput = document.getElementById("id_email");
    const titleInput = document.getElementById("id_title");
    const messageInput = document.getElementById("id_message");

    const nameError = document.getElementById("name_error");
    const emailError = document.getElementById("email_error");
    const titleError = document.getElementById("title_error");
    const messageError = document.getElementById("message_error");

    let isValid = true;

    // Validate name (required)
    if (nameInput.value.trim() === "") {
      isValid = false;
      nameInput.classList.add("is-invalid");
      nameError.innerText = "Name field can't be empty";
    } else if (nameInput.value.trim().length < 2) {
      isValid = false;
      nameInput.classList.add("is-invalid");
      nameError.innerText = "Name can't be shorter than 2 characters";
    } else {
      nameInput.classList.remove("is-invalid");
      nameError.innerText = "";
    }

    // Validate email (required and email format)
    if (emailInput.value.trim() === "") {
      isValid = false;
      emailInput.classList.add("is-invalid");
      emailError.innerText = "Email field can't be empty";
    } else if (!isValidEmail(emailInput.value)) {
      isValid = false;
      emailInput.classList.add("is-invalid");
      emailError.innerText = "Please enter a valid email";
    } else {
      emailInput.classList.remove("is-invalid");
      emailError.innerText = "";
    }

    // Validate title (required)
    if (titleInput.value.trim() === "") {
      isValid = false;
      titleInput.classList.add("is-invalid");
      titleError.innerText = "Title field can't be empty";
    } else if (titleInput.value.trim().length < 10) {
      isValid = false;
      titleInput.classList.add("is-invalid");
      titleError.innerText = "Title can't be shorter than 10 characters";
    } else {
      titleInput.classList.remove("is-invalid");
      titleError.innerText = "";
    }

    // Validate message (required)
    if (messageInput.value.trim() === "") {
      isValid = false;
      messageInput.classList.add("is-invalid");
      messageError.innerText = "Message field can't be empty";
    } else if (messageInput.value.trim().length < 50) {
      isValid = false;
      messageInput.classList.add("is-invalid");
      messageError.innerText = `Message can't be shorter than 50 characters (current: ${
        messageInput.value.trim().length
      })`;
    } else {
      messageInput.classList.remove("is-invalid");
      messageError.innerText = "";
    }

    return isValid;
  }

  function isValidEmail(email) {
    // Simple email format validation
    const emailRegex = /^\S+@\S+\.\S+$/;
    return emailRegex.test(email);
  }
});
