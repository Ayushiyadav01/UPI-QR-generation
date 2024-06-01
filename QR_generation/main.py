import random
import qrcode


def create_upi_qr(upi_id, amount, transaction_note, filename):
    """
    Return the image file of gemerated QR with provided UPI_id, Amount
    :param upi_id:
    :param amount:
    :param transaction_note:
    :param filename:
    :return:
    """
    upi_link = f"upi://pay?pa={upi_id}&pn=MerchantName&am={amount}&cu=INR&tn={transaction_note}"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_link)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)


if __name__ == "__main__":
    upi_id = "quantumenergy@sbi"
    amount = "2.00"
    transaction_id = str(random.randint(10000, 99999))
    filename = "upi_qr_code_with_tn.png"
    create_upi_qr(upi_id, amount, transaction_id, filename)
    print(f"QR code generated with transaction ID {transaction_id} and saved as {filename}")
