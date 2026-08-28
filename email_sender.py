import smtplib

def send_email(news_data):
    email = "lucmarvens6@gmail.com"
    email2 = "lucmarvens@gmail.com"
    passwords = "sibf lgyf fyhw mwxu"
    
    for i in news_data:
        body_text = f"Subject: Stock Update\n\nHere's an update on {i}: {news_data[i]['title']} - {news_data[i]['description']} ({news_data[i]['url']})"
        body_text = body_text.encode('ascii', 'ignore').decode('ascii')
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=passwords)
            connection.sendmail(from_addr=email, to_addrs=email2, msg=body_text)