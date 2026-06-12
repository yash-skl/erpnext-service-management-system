app_name = "service_app"
app_title = "Service App"
app_publisher = "Yash Shukla"
app_description = "Service Maintanance Management System"
app_email = "yshukla2775@gmail.com"
app_license = "mit"


doc_events = {
    "Service Visit": {
        "on_submit": "service_app.service_app.events.service_visit.on_submit"
    }
}