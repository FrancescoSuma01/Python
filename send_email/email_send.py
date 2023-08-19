import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

my_email = "francescosuma05@gmail.com"
password = "grsyhyuhklnfmrhr"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

subject = "Oggetto della Mail"
message = "Questa mail è stata inviata con uno script python e questo è il codice: "

msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = my_email
msg["To"] = "nicola.menga.1993@gmail.com"

# Aggiungi il testo del messaggio
msg.attach(MIMEText(message, "plain"))

# Aggiungi l'allegato del documento di testo
with open("C:\\Users\\franc\\Documents\\Coding\\Python\\send_email\\documento.txt", "rb") as f:
    part = MIMEApplication(f.read(), Name="documento.txt")
part["Content-Disposition"] = f"attachment; filename=documento.txt"
msg.attach(part)

connection.sendmail(from_addr=my_email, to_addrs=msg["To"], msg=msg.as_string())

connection.quit()
