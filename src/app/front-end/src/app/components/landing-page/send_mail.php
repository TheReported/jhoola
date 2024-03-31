<?php
if(isset($_SERVER['REQUEST_METHOD']) == "POST") {
    $nombre = $_POST["name"];
    $email = $_POST["Email"]; 
    $asunto = $_POST["subject"];
    $mensaje = $_POST["message"];
    
    $destinatario = "jhoolateam@gmail.com"; 
    
    $contenido = "Nombre: $nombre\n";
    $contenido .= "Email: $email\n\n";
    $contenido .= "Mensaje:\n$mensaje";
    
    if (mail($destinatario, $asunto, $contenido)) {
        echo "<p>El formulario ha sido enviado correctamente.</p>";
    } else {
        echo "<p>Hubo un error al enviar el formulario.</p>";
    }
}
?>