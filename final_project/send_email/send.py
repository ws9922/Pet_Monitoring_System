import smtplib, ssl
import time

def SendEmail(mode, image_id = ""):
    import smtplib,ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import imghdr
    from email.message import EmailMessage
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ethuang17@gmail.com"  # Enter your address
    receiver_email = "shuow6@illinois.edu" #enter receiver address
    password = "Icon103!"
    
    newMessage = EmailMessage()
    newMessage['From'] = sender_email
    newMessage['To'] = receiver_email
    if (mode):
        newMessage['Subject'] = 'Reminder to feed your cat'
        content = """\
        Dear Master,
        
        It is time to feed your little angel K Bao.
        Otherwise, it will turn to a monster.
        
        Best,
        PetBot"""
        newMessage.set_content(content) 
    else:
        content = """\
        Dear Master,
        
        K Bao appears in forbidden areas.
        The alarm has been activated.
        The picture of that little monster is attached below.
        Hope everything going well!
        
        Best,
        PetBot"""
        newMessage['Subject'] = 'Alert'
        newMessage.set_content(content)
        with open(image_id, 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype = 'image', subtype = image_type, filename = image_name)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(newMessage)
