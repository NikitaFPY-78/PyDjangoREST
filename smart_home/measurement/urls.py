from django.urls import path

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', DeviceView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),

]
