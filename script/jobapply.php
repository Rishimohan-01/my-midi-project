<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Collect form data
    $name = htmlspecialchars($_POST['name']);
    $address = htmlspecialchars($_POST['address']);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $phone = htmlspecialchars($_POST['phone']);
    $qualification = htmlspecialchars($_POST['qualification']);
    $applyfor = htmlspecialchars($_POST['applyfor']);
    $message = htmlspecialchars($_POST['message']);

    // Resume upload
    $resume = $_FILES['resume']['name'];
    $temp_name = $_FILES['resume']['tmp_name'];
    $upload_folder = "uploads/";

    // Create uploads folder if not exists
    if (!is_dir($upload_folder)) {
        mkdir($upload_folder, 0777, true);
    }

    $file_path = $upload_folder . basename($resume);

    if (move_uploaded_file($temp_name, $file_path)) {

        // Email setup
        $to = "yourmail@gmail.com";  // CHANGE THIS
        $subject = "New Job Application - $applyfor";

        $body = "Name: $name\n";
        $body .= "Address: $address\n";
        $body .= "Email: $email\n";
        $body .= "Phone: $phone\n";
        $body .= "Qualification: $qualification\n";
        $body .= "Applied For: $applyfor\n\n";
        $body .= "Message:\n$message\n\n";
        $body .= "Resume saved at: $file_path";

        $headers = "From: $email";

        if (mail($to, $subject, $body, $headers)) {
            echo "<script>alert('Application submitted successfully!'); window.location.href='index.html';</script>";
        } else {
            echo "Mail sending failed.";
        }

    } else {
        echo "File upload failed.";
    }
}

?>