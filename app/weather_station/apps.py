from django.apps import AppConfig


class WeatherStationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather_station'

    def ready(self):
        from apscheduler.schedulers.background import BackgroundScheduler
        
        sched = BackgroundScheduler()

        @sched.scheduled_job('interval', id='fetch_data', minutes=1)
        def job():
            import requests
            from django.conf import settings
            from .models import WeatherData

            response = requests.get(settings.WEATHER_STATION_API_URL)
            if response.status_code == 200:
                data = response.json()
                # WeatherData.objects.create(
                #     temperature=data.get('temperature'),
                #     humidity=data.get('humidity')
                # )

        sched.start()
