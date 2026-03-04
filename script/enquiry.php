<?php

if($_SERVER["REQUEST_METHOD"] == "POST"){

    $name = htmlspecialchars($_POST['name']);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $phone = htmlspecialchars($_POST['phone']);
    $message = htmlspecialchars($_POST['message']);

    $to = "yourmail@gmail.com"; // change this
    $subject = "New Enquiry";

    $body = "Name: $name\n";
    $body .= "Email: $email\n";
    $body .= "Phone: $phone\n\n";
    $body .= "Message:\n$message";

    $headers = "From: $email";

    if(mail($to, $subject, $body, $headers)){
        echo "<script>alert('Enquiry sent successfully!'); window.location.href='index.html';</script>";
    } else {
        echo "Something went wrong.";
    }
}
?>