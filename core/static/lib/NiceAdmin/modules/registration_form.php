<h5 class="card-title">Registration Form</h5>

<style>
  /* --- CUSTOM DESIGN ENHANCEMENTS (OVERRIDING BOOTSTRAP) --- */

  /* General Form Styling */
  .needs-validation {
    padding: 30px;
    background-color: #f7f9fc; /* Light, modern background color */
    border-radius: 12px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05); /* Soft, prominent shadow */
    border-top: 5px solid #007bff; /* Accent color border at the top */
  }

  /* Form Title Enhancement */
  .card-title {
    text-align: center;
    color: #007bff; /* Primary brand color */
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 30px;
    border-bottom: 2px solid #e9ecef; /* Subtle separator */
    padding-bottom: 10px;
  }

  /* Floating Input Styling */
  .form-control, .form-select {
    border-radius: 8px; /* Slightly more rounded corners */
    min-height: 55px; /* Taller input fields for better touch targets */
    border: 1px solid #ced4da; /* Standard border color */
    transition: all 0.3s ease;
  }

  /* Focus State */
  .form-control:focus, .form-select:focus, .form-floating textarea:focus ~ label {
    border-color: #007bff;
    box-shadow: 0 0 0 0.25rem rgba(0, 123, 255, 0.25); /* Lighter blue focus ring */
    background-color: #ffffff;
  }
  
  /* Textarea Specific Height Adjustment */
  #floatingTextarea {
    min-height: 120px !important; /* Make the address box a bit larger */
  }
  
  /* Select Dropdown Arrow Color (for some browsers) */
  .form-select {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23007bff' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  }

  /* Invalid Feedback (Error Message) Styling */
  .invalid-feedback {
    font-size: 0.85rem;
    color: #dc3545; /* Standard red */
    font-style: italic;
  }

  /* Terms and Conditions Link */
  .form-check-label a {
    color: #007bff;
    font-weight: 600;
    text-decoration: none;
    transition: color 0.3s;
  }
  .form-check-label a:hover {
    color: #0056b3;
    text-decoration: underline;
  }

  /* Submit Button Styling */
  .btn-primary {
    background-color: #007bff; /* Primary blue */
    border-color: #007bff;
    padding: 10px 30px;
    font-weight: 600;
    border-radius: 25px; /* Pill shape for modern look */
    transition: background-color 0.3s, border-color 0.3s, transform 0.1s;
  }
  .btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
    transform: translateY(-1px); /* Slight lift effect */
  }

  /* Reset Button Styling */
  .btn-secondary {
    background-color: #6c757d; /* Standard secondary color */
    border-color: #6c757d;
    padding: 10px 30px;
    font-weight: 600;
    border-radius: 25px; /* Match submit button shape */
    margin-left: 15px;
  }

  /* Center the button group */
  .text-center {
    margin-top: 20px;
    padding-top: 15px;
  }
  
</style>

<form class="row g-3 needs-validation" novalidate>
  <div class="col-md-12">
    <div class="form-floating">
      <input type="text" class="form-control" id="floatingName" placeholder="Your Name" required>
      <label for="floatingName">Your Name</label>
      <div class="invalid-feedback">Please enter your name.</div>
    </div>
  </div>

  <div class="col-md-6">
    <div class="form-floating">
      <input type="email" class="form-control" id="floatingEmail" placeholder="Your Email" required>
      <label for="floatingEmail">Your Email</label>
      <div class="invalid-feedback">Please enter a valid email address.</div>
    </div>
  </div>

  <div class="col-md-6">
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password" required pattern=".{8,}" title="Password must be at least 8 characters long">
      <label for="floatingPassword">Password</label>
      <div class="invalid-feedback">Please enter a valid password (min 8 characters).</div>
    </div>
  </div>

  <div class="col-12">
    <div class="form-floating">
      <textarea class="form-control" placeholder="Address" id="floatingTextarea" style="height: 100px;" required></textarea>
      <label for="floatingTextarea">Address</label>
      <div class="invalid-feedback">Please enter your address.</div>
    </div>
  </div>

  <div class="col-md-6">
    <div class="form-floating">
      <input type="text" class="form-control" id="floatingCity" placeholder="City" required>
      <label for="floatingCity">City</label>
      <div class="invalid-feedback">Please enter your city.</div>
    </div>
  </div>

  <div class="col-md-4">
    <div class="form-floating mb-3">
      <select class="form-select" id="floatingSelect" aria-label="State" required>
        <option selected disabled value="">Choose your state</option>
        <option value="1">New York</option>
        <option value="2">Oregon</option>
        <option value="3">DC</option>
      </select>
      <label for="floatingSelect">State</label>
      <div class="invalid-feedback">Please select your state.</div>
    </div>
  </div>

  <div class="col-md-2">
    <div class="form-floating">
      <input type="text" class="form-control" id="floatingZip" placeholder="Zip" required pattern="\d{5}" title="Zip code should be 5 digits">
      <label for="floatingZip">Zip</label>
      <div class="invalid-feedback">Please enter a valid zip code (5 digits).</div>
    </div>
  </div>

  <div class="col-12">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="termsCheck" required>
      <label class="form-check-label" for="termsCheck">
        I agree to the <a href="#" data-bs-toggle="tooltip" title="Read the terms and conditions">terms and conditions</a>.
      </label>
      <div class="invalid-feedback">You must agree to the terms and conditions to proceed.</div>
    </div>
  </div>

  <div class="text-center">
    <button type="submit" class="btn btn-primary">Submit</button>
    <button type="reset" class="btn btn-secondary">Reset</button>
  </div>
</form><script>
  // Enable tooltips for terms and conditions
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Form Validation
  (function () {
    'use strict'
    var forms = document.querySelectorAll('.needs-validation')
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
          form.classList.add('was-validated')
        }, false)
      })
  })()
</script>