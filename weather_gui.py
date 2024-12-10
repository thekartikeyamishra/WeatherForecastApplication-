import tkinter as tk
from tkinter import messagebox
from utils.weather_api import fetch_weather
from utils.export_csv import export_to_csv

class WeatherApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Forecast")


        tk.Label(self.root, text="Enter Location:", font=("Helvetica",12)).pack(pady=10)
        self.location_entry = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.location_entry.pack(pady=5)

        self.fetch_button = tk.Button(self.root, text="Fetch Weather", command=self.fetch_weather)
        self.fetch_button.pack(pady=10)

        self.result_text = tk.Text(self.root, height = 15, width=60, wrap=tk.WORD)
        self.fetch_button.pack(pady=10)

        self.export_button = tk.Button(self.root, text="Export to CSV", command=self.export_data, state=tk.DISABLED)
        self.export_button.pack(pady=10)

        self.weather_data = None


    def fetch_weather(self):
        location = self.location_entry.get()
        if not location:
            messagebox.showerror("Error", "Please enter a location.")
            return
        self.weather_data = fetch_weather(location)
        if self.weather_data:
            self.result_text.delete(1.0, tk.END)
            for key, value in self.weather_data.items():
                self.result_text.insert(tk.END, f"{key}:{value}\n")
            self.export_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Failed to fetch weather data. Please check the location.")

    def export_data(self):
        if self.weather_data:
            export_to_csv(self.weather_data)
            messagebox.showinfo("Success", "Weather data exported to CSV.")

    def run(self):
        self.root.mainloop()