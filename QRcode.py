import qrcode

upi_id = (input(" Enter your UPI ID : "))
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
fampay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
#create qr
phonepe_qr = qrcode.make(phonepe_url)
googlepay_qr = qrcode.make(googlepay_url)
fampay_qr = qrcode.make(fampay_url)
# save qr
phonepe_qr.save('phonepe_qr.png')
googlepay_qr.save('googlepay_qr.png')
fampay_qr.save('fampay_qr.png')
#Dispay qr code
phonepe_qr.show()
googlepay_qr.show()
fampay_qr.show()


