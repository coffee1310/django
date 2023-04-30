import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from .models import Order, food
from django.http import request


def send_message(message, subject, recipient):
    sender = 'rassilka0102@gmail.com' #Email отправителя
    password = 'pgwmwvmhywurzulq'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = f"{subject}" #Здесь вводится тема сообщения
        server.sendmail(sender,recipient, msg.as_string())#Отправитель, получатель, сообщение
        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\n Check your login or email"

def order(order_list,last_order,posts,):
    order_price = 0
    post = food.objects.all()
    print(order_list)
    del order_list[0]
    for o in order_list:
        price = o.get('price')
        quantity = o.get('quantity')
        order_price += float(price) * float(quantity)

    order = ''
    for p in post:
        for o in order_list:
            if o.get('product_id') == p.pk:
                order += '\n'
                order += '    '
                order += str(p.cat)
                order += ' '
                order += str(o.get('name'))
                order += " X "
                order += str(o.get('quantity'))

    for p in posts:
        if p == last_order:
            message = f"Спасибо, что оформили заказ!\nВаш номер заказа {p.pk}\nВаш заказ:{order}\nВаш адрес: {p.adress}\nВаш номер телефона: {p.customer_phone}" \
                      f"\nВремя создания заказа {datetime.now().year}.{datetime.now().month}.{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}" \
                      f"\nИтговая сумма: {order_price} рублей"
            send_message(message=f"{message}", subject="Kombo Food", recipient=p.email)
            message = f"Номер заказа {p.pk}\nЗаказ: {order}\nАдресс: {p.adress}\nНомер телефона: {p.customer_phone}"\
                       f"\nВремя создания заказа {datetime.now().year}.{datetime.now().month}.{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}" \
                       f"\nИтговая сумма: {order_price} рублей"
            send_message(message=message, subject="Kombo Food", recipient="rassilka0102@gmail.com")
def main():
    message = input("Type your message:") #Ваше сообщение
    subject = input("Type your Subject:")#Ваша тема
    print(send_message(message=message, subject=subject))

if __name__ == "__main__":
    main()