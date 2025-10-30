import qrcode

# Ask user for input
data = input("Enter a link or text: ").strip()
filename = input("Enter file name to save (without extension): ").strip()

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data and generate the QR code
qr.add_data(data)
qr.make(fit=True)

# Create the image (requires Pillow)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image as a PNG file
img.save(f"{filename}.png")

print(f"QR code saved successfully as {filename}.png")
