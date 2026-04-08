# Code-Generation-Refactoring

## Weather App (OpenWeatherMap)

This workspace includes a command-line weather app in [weather_script.py](weather_script.py) that fetches current weather data from the OpenWeatherMap API.

### 1. Install dependency

```powershell
python -m pip install requests
```

### 2. Set your API key

Get your key from OpenWeatherMap, then set this environment variable.

Temporary (current PowerShell session):

```powershell
$env:OPENWEATHER_API_KEY = "your_api_key_here"
```

Persistent (future sessions):

```powershell
setx OPENWEATHER_API_KEY "your_api_key_here"
```

### 3. Run the app

```powershell
python weather_script.py "London"
```

Optional arguments:

```powershell
python weather_script.py "London" --country GB --units metric
python weather_script.py "New York" --country US --units imperial
python weather_script.py "Tokyo" --units standard
```

If no city is passed, the app prompts you interactively.
