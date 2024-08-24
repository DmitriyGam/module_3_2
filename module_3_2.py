def send_email(message, recipint, *, sender='university.help@gmail.com'):
    if sender == recipint:
        print("Нельзя отпривить письмо самому себе")
    elif ("@" and (".com" or ".ru" or ".net")) not in recipint and ("@" and (".com" or ".ru" or ".net")) not in sender:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipint)
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipint)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipint)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

