import smtplib

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.set_debuglevel(1)  # Enable debug output
    server.starttls()
    server.login("mothalindokuhle168@gmail.com", "ebjmkthbnjphixwk")
    print("Connected successfully!")
    server.quit()
except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication Error:", e)
except Exception as e:
    print("Error:", e)
