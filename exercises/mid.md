# Medium

 

### Problem Statement: Multi-Platform Notification System 🔔

Imagine you're building a software system for a large-scale e-commerce company. The primary function of this system is to handle and send a variety of **notifications** to users based on different events in their order lifecycle (e.g., order placed, order shipped, delivery completed).

This system must handle the following requirements:

- **Diverse Communication Channels:** Notifications need to be sent through multiple channels, including **email**, **SMS**, and **push notifications** to a mobile app. The system should be easily extensible to support new channels (e.g., WhatsApp, in-app messages) in the future without significant code changes.
- **Notification Types:** There are different types of notifications for different events. Examples include:
    - **Order Confirmation:** A simple message with order details.
    - **Shipping Update:** A message with a tracking number and link.
    - **Promotional Offer:** A rich message that might include an image and a link to a product page.
- **Template Management:** Each notification type needs a specific **template** for each channel. For example, an "Order Confirmation" email will have a different template from an "Order Confirmation" SMS. These templates should be manageable and easily updated without deploying new code.
- **User Preferences:** The system must respect user preferences. A user might prefer SMS for shipping updates but email for promotional offers. If a user hasn't opted in for a certain channel for a specific notification type, the system should simply skip sending that notification on that channel.
- **Logging and Auditing:** Every notification sent (or attempted to be sent) must be logged for auditing and debugging purposes. This logging logic should be a cross-cutting concern, applied consistently without cluttering the core business logic.
- **System Reliability:** The system needs to be resilient. If a specific channel's service (e.g., the SMS gateway) is temporarily down, the system should not fail. Instead, it should log the failure and, if possible, retry sending the notification at a later time.

## Solution

- Objects
    - Object level
        - class Notification() ⇒ build notification object (direction, content)
            - methods
                - create_notification(notification_type, channel)
            - note
                - We have `Builder` for each type of notification
                - We use `flyweight` to keep track of instrisic state being a template for a given channel. We still have M*N templates that need to be defined, but only M*N maximum possible templates in memory
        - class NotifierSender() ⇒ sends notification
            - Methods
                - set_strategy(channel)
                - send_notification(notification: Notification)
            - Note
                - We use a `strategy` in order to send notification by any channel
                    - It will ask for the given Template from flywieght given the channel. Then overwrite the values and send it to the proper channel
                - send_notification is the invoker of a `Command` design pattern that has possibility to rollback, and queue operation for later on if there was an error when trying to send the notification on a given channel
                - We are using `Composite` for possible cases where an object may be compromised of multiple channels simultaneously
    - Manager level
        - class NotifierManager
            - methods
                - send_notification(notification: Notification)
                    - `Chain of responsibility` is used to check the returned notification is under size limits, in user preferences, and channel-format-ready
                    - After that it sets strategy in NotifierSender, then call send_notification
            - Note
                - We are using `Facade` with references to Notification class in order to decouple code and respect single responsibility principle
    - Client
        - Defines settings/user preferences
        - create_notification(notification_type, channel) is called returns director object with the Builder that works for the given channel + notification type. It can overwrite template methods by calling the steps directly, otherwise the defaults are integrated when the final output object is requested
        - It then calls send_notification to to the NotifierManger
- General
    - We can use `Wrapper/Decorator` for logging purposes before executing relevant methods
- Discarded patterns
    - Adapter ⇒ theres no old interface
    - Iterator ⇒ theres no clear need for iterating over any the specified objects
    - Observer, Mediator ⇒ theres no need for communication between objects
    - Abstract, simple factories and factory ⇒ we use Builder instead
    - Prototype ⇒ no need to copy object
    - Memento ⇒ revert is well-defined, we use Command instead  (assuming we can cancel notifications/send a new notification cancelling the other one)
    - State ⇒ no major behavior change at different notifiaction stages
    - Singleton ⇒ there may be more than one user at a time (thus a single settings object is erroneous)