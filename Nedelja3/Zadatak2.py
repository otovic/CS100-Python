seconds = int(input("Broj sekundi: "))

days = 0
hours = 0
minutes = 0

if seconds >= 60 and seconds < 3600:
    minutes = int(seconds / 60)
    seconds = seconds - (minutes * 60)
    print(f"{minutes} i {seconds}")
elif seconds >= 3600 and seconds < 86400:
    hours = int(seconds / 3600)
    seconds = seconds - (hours * 3600)
    minutes = int(seconds / 60)
    seconds = seconds - (minutes * 60)
    print(f"Sati: {hours}, Minuta: {minutes}, Sekundi {seconds}")
elif seconds >= 86400:
    days = int(seconds / 86400)
    seconds = seconds - (days * 86400)
    hours = int(seconds / 3600)
    seconds = seconds - (hours * 3600)
    minutes = int(seconds / 60)
    seconds = seconds - (minutes * 60)
    print(f"Dana: {days}, Sati: {hours}, Minuta: {minutes}, Sekunde: {seconds}")
