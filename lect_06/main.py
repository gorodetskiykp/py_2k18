with open('template.html') as html_template:
    htmp_text = html_template.read()
    
fio = "Юрий Гагарин"
birth_date = "1934"

with open('index.html', 'w') as html_page:
    html_page.write(htmp_text.format(fio=fio, b_date=birth_date))

