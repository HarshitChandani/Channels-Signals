from asgiref.sync import async_to_sync
import channels.layers


def send_notification(sender, instance, **kwargs):
    message = "Your book {0} which was published on {1} is successfully added in our records. Thank you for using our system .".format(
        instance.title, instance.published_date
    )

    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification-room",
        {
            "type": "notification.send",
            "text": {
                "message": message,
                "title": instance.title,
                "description": instance.description,
                "published_date": instance.published_date,
            },
        },
    )
