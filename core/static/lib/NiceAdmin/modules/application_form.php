<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Loan Application Form</title>
  <style>
    /* Basic Reset and Body Styling */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f4f7f6; /* Light, calming background */
        color: #333;
        margin: 0;
        padding: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    /* Form Container Styling */
    form {
        background-color: #ffffff; /* White form background */
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
        max-width: 600px;
        width: 100%;
    }

    /* Header Styling */
    h1 {
        text-align: center;
        color: #0056b3; /* Primary color for the title */
        margin-bottom: 30px;
        font-weight: 600;
        font-size: 2em;
        border-bottom: 2px solid #0056b3;
        padding-bottom: 10px;
    }

    /* Label Styling */
    label {
        display: block; /* Make labels take up full width */
        margin-bottom: 8px;
        font-weight: 500;
        color: #555;
        /* The next line ensures checkbox labels appear next to the box */
        line-height: 1.5; 
    }

    /* Input and Textarea Styling */
    input[type="text"],
    input[type="email"],
    input[type="tel"],
    input[type="number"],
    textarea {
        width: 100%;
        padding: 12px;
        margin-bottom: 20px; /* Space after each input/textarea */
        border: 1px solid #ccc;
        border-radius: 8px;
        box-sizing: border-box; /* Include padding/border in element's total width/height */
        transition: border-color 0.3s, box-shadow 0.3s;
    }

    /* Focus State for Inputs */
    input:focus,
    textarea:focus {
        border-color: #007bff; /* Highlight border on focus */
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.2);
        outline: none; /* Remove default focus outline */
    }
    
    /* Textarea specific styling */
    textarea {
        resize: vertical; /* Allow resizing only vertically */
    }

    /* Checkbox Label Group Styling */
    label[for="agree"] {
        display: inline-block; /* Keep the checkbox and text on the same line */
        margin-bottom: 20px;
    }
    
    /* Checkbox Input Styling */
    input[type="checkbox"] {
        width: auto; /* Revert checkbox width */
        margin-right: 10px; /* Space between checkbox and text */
        vertical-align: middle;
    }

    /* Button Styling */
    button[type="submit"] {
        width: 100%;
        background-color: #28a745; /* Green for a positive action */
        color: white;
        padding: 15px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.1em;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }

    /* Button Hover Effect */
    button[type="submit"]:hover {
        background-color: #218838; /* Slightly darker green on hover */
    }

    /* Removing the extra <br> space */
    /* Select all <br> elements that follow a form element and hide them */
    /* This makes the CSS control the spacing instead of the <br> tags */
    .form-group br {
        display: none;
    }

    /* Custom classes for grouping, removing extra <br> tags */
    .form-group {
        margin-bottom: 15px; /* Adds consistent spacing between form elements */
    }
    
 </style>
</head>
<body>

 <h1>Loan Application Form</h1>

 <form action="/submit-loan" method="POST">
    <div class="form-group">
 <label for="fullName">Full Name:</label>
 <input type="text" id="fullName" name="fullName" required>
    </div>

    <div class="form-group">
 <label for="email">Email Address:</label>
 <input type="email" id="email" name="email" required>
    </div>

    <div class="form-group">
 <label for="phone">Phone Number:</label>
 <input type="tel" id="phone" name="phone" required>
    </div>

    <div class="form-group">
<label for="loanAmount">Loan Amount (in USD):</label>
<input type="number" id="loanAmount" name="loanAmount" required>
    </div>

    <div class="form-group">
 <label for="loanTerm">Loan Term (in months):</label>
 <input type="number" id="loanTerm" name="loanTerm" required>
    </div>

    <div class="form-group">
 <label for="income">Monthly Income (in USD):</label>
 <input type="number" id="income" name="income" required>
    </div>

    <div class="form-group">
 <label for="address">Residential Address:</label>
 <textarea id="address" name="address" rows="4" required></textarea>
    </div>

    <div class="form-group">
 <label for="purpose">Purpose of Loan:</label>
  <textarea id="purpose" name="purpose" rows="4" required></textarea>
    </div>

    <div class="form-group">
 <label for="agree">
 <input type="checkbox" id="agree" name="agree" required> I agree to the terms and conditions.
 </label>
    </div>

 <button type="submit">Submit Application</button>
 </form>

</body>
</html>