import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication code is generated in your mail
s.login("arjunvijayece2018@gmail.com", "muuldeubdwdonoxr") 
  
# message to be sent 
message = "Some Strange Person Found In Front Of Door "
  
# sending the mail 
s.sendmail("123pnaveenkumar@gmail.com", "arjunvijayece2018@gmail.com", message) 
  
# terminating the session 
s.quit() 
