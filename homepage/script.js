const specifications = [  'Electronics Communication Engineering student',  'Embedded Systems ',  'Software ',  'Artificial Intelligence'];

const specificationElem = document.querySelector('.specification');
let currentSpecificationIndex = 0;

function typeSpecification() {
  const currentSpecification = specifications[currentSpecificationIndex];
  let currentCharIndex = 0;

  const typingInterval = setInterval(() => {
    if (currentCharIndex === currentSpecification.length) {
      clearInterval(typingInterval);
      setTimeout(eraseSpecification, 2000);
    } else {
      specificationElem.textContent = currentSpecification.slice(0, currentCharIndex + 1);
      currentCharIndex++;
    }
  }, 100);
}

function eraseSpecification() {
  let currentCharIndex = specificationElem.textContent.length - 1;

  const erasingInterval = setInterval(() => {
    if (currentCharIndex === -1) {
      clearInterval(erasingInterval);
      currentSpecificationIndex++;

      if (currentSpecificationIndex === specifications.length) {
        currentSpecificationIndex = 0;
      }

      setTimeout(typeSpecification, 1000);
    } else {
      specificationElem.textContent = specificationElem.textContent.slice(0, currentCharIndex);
      currentCharIndex--;
    }
  }, 50);
}

typeSpecification();


document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("contact-form");
  const alert = document.getElementById("alert");

  form.addEventListener("submit", function(event) {
    event.preventDefault();
    sendEmail();
  });

  function sendEmail() {
    const firstName = document.getElementById("first-name").value;
    const lastName = document.getElementById("last-name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    Email.send({
      Host: "smtp.gmail.com",
      Username: "YOUR_GMAIL_ADDRESS",
      Password: "YOUR_GMAIL_PASSWORD",
      To: "mwael1971@gmail.com",
      From: "YOUR_GMAIL_ADDRESS",
      Subject: "New Contact Form Submission",
      Body: `First Name: ${firstName}<br>Last Name: ${lastName}<br>Email: ${email}<br>Message: ${message}`,
    }).then(function() {
      form.reset();
      alert.classList.remove("d-none");
    });
  }
});
