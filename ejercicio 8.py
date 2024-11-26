tiempo=float(input("ingrese los segundos "))
hora=tiempo/3600
minutos=tiempo%3600/60
segundos=tiempo%60
print("Hay ",hora, "horas", minutos, "minutos", segundos,"segundos")
