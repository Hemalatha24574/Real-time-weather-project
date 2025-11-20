# Real-Time Weather Information & Data Logger

A Python application that fetches **real-time weather data**, displays it to the user, and securely logs every weather query into a local file.  
The program uses the **OpenWeatherMap API**, demonstrates **Object-Oriented Programming (OOP)** principles, and implements **error handling** to ensure stability and reliability.

---

# 📌 Task Overview

## **Task Title:**  
**Real-Time Weather Information & Data Logger**

## **Task Objective:**  
Build a Python application capable of:
- Fetching real-time weather information from a public weather API.
- Accepting city names as user input.
- Displaying weather data clearly and neatly.
- Logging every response with a timestamp to a CSV or database.
- Handling API failures, invalid user input, and network issues.
- Using OOP design to organize the program.

---

# 🌤️ Features

### ✅ **Live Weather Fetching**
Retrieves the latest weather details for any city using OpenWeatherMap API:
- Temperature (°C)
- Feels-like temperature
- Humidity
- Weather condition (description)
- Wind speed

### ✅ **User Input Support**
The user enters a city name and receives formatted weather output.

### ✅ **Data Logging**
Each successful API response is stored in:
```
weather_data.csv
```
This includes:
- Timestamp  
- City  
- Country  
- Temperature  
- Humidity  
- Feels-like  
- Condition  
- Wind speed  

### ✅ **Error Handling**
The program gracefully handles:
- Invalid city name  
- API key errors  
- API failure or wrong URL  
- No internet / timeout  
- Unexpected server responses  

### ✅ **OOP-Based Structure**
A dedicated `WeatherApp` class wraps the main execution flow.

---

# 🧩 Project Structure

```
project/
│── main.py               # Main program logic and OOP interface
│── weather_data.csv      # Auto-generated weather logs
│── README.md             # Documentation
```

---

# ⚙️ How It Works (Flowchart Explanation)

1. User enters a city name  
2. Request is sent to OpenWeatherMap API  
3. API returns weather data in JSON format  
4. Program extracts key information  
5. Weather details are displayed to user  
6. Data is appended to CSV file with timestamp  
7. Class handles the flow and method calls  

---

# ▶️ How to Run the Application

## **1. Install required Python library**
```bash
pip install requests
```

## **2. (Optional) Set your API Key**
Linux/macOS:
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

Windows (PowerShell):
```powershell
setx OPENWEATHER_API_KEY "your_api_key_here"
```

If not set, the script uses a fallback internal key.

## **3. Run the program**
```bash
python main.py
```

---

# 📄 Sample Console Output

```
Weather in London:
 Temperature: 15°C
 Feels Like: 13°C
 Condition: Clear Sky
 Humidity: 62%
 Wind Speed: 4.1 m/s

 Weather data for London stored in weather_data.csv
```

---

# 📊 CSV Logging Format

The CSV file (`weather_data.csv`) contains:

| Timestamp           | City   | Country | Temp (°C) | Feels Like | Humidity | Condition  | Wind |
|--------------------|--------|---------|-----------|------------|----------|------------|------|
| 2025-02-10 14:22:00 | London | GB      | 15        | 13         | 62       | Clear Sky  | 4.1  |

This helps in analyzing weather trends or maintaining historical logs.

---

# 🧱 OOP Structure Explained

### **WeatherApp Class**
Handles:
- Reading user input  
- Coordinating data fetch  
- Displaying results  
- Triggering CSV logging  

### **Helper Functions**
- `request(city)` → Makes API call  
- `information(city)` → Prints weather details  
- `store(city)` → Logs data  

OOP separation improves:
- Modularity  
- Testing capability  
- Readability  
- Future expansion  

---

# 🔐 Error Handling Explained

The program avoids crashes by catching:
- Connection errors
- Invalid city inputs
- Missing API keys
- API downtime
- Unexpected JSON structures

Example error messages:
```
City not found or API error
Error: Unable to connect to API
```

---

# 🚀 Future Enhancements

Possible improvements:
- Add a SQLite database option  
- Add GUI (Tkinter, PyQt)  
- Voice input for city name  
- 5-day forecast integration  
- Export logs in JSON or Excel format  
- Web dashboard using Flask / FastAPI  

---

# 👨‍💻 Author  
**Pabbu Hemalatha**  
Real-Time Weather Detection Application Developer

📧Email: pabbu.hemalatha24@gmail.com

🪩GitHub:https://github.com/Hemalatha24574

---
