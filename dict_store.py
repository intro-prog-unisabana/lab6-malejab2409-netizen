def temp_and_color(data):
  temperatura = data.get("temp")
  color = data.get("color")
  return (temperatura, color)
data = {"temp": 22.5, "color": "blue", "status": "ok"}
print(temp_and_color(data)) 