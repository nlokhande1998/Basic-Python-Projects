#install plyer module using pip. time module is installed by default in python
from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Reminder",
            message = "Drink 200 ml water after every 1 hour.",
            # app_icon = 'Paste image file location here',   location should be copied using forward slashes '/' along with file name. Preferably use .ico file
            timeout = 2  # time for which notification is diplayed
        )

        time.sleep(10)        # 10 sec delay between 2 notifications


'''    Syntax: notify(title=”, message=”, app_name=”, app_icon=”, timeout=10, ticker=”, toast=False)

    Parameters:

        title (str)  Title of the notification
        message (str)  Message of the notification
        app_name (str)  Name of the app launching this notification
        app_icon (str) Icon to be displayed along with the message
        timeout (int)  time to display the message for, defaults to 10
        ticker (str)  text to display on status bar as the notification arrives
        toast (bool)  simple Android message instead of full notification'''