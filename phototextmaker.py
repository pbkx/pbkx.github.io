text = input("text: ")
year = input("year: ")
link = input("href: ")


print("<img src=" + '''"''' + link + '''"''')
print("alt=" + '''"''' + text + "; " + year + '''" ''' + '''width="500" height="500"><p>''' + text + "</p><br>")
print("<br>")