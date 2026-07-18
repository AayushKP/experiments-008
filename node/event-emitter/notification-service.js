import EventEmitter from "node:stream";

class NotificationCenter extends EventEmitter {
  constructor() {
    super();
    this.notifications = [];
  }

  addNotification(type, message) {
    const notification = {
      id: Date.now(),
      type,
      message,
      timestamp: new Date(),
    };
    this.notifications.push(notification);

    //Emit the Event
    this.emit("notification", notification);
    this.emit(`notification:${type}`, notification);
  }
}

const notificationCenter = new NotificationCenter();

//Subscribe to all notifications
notificationCenter.on("notification", (notification) => {
  console.log(`${notification.type}: ${notification.message}`);
});

//Trigger notifications
notificationCenter.addNotification("success", "User logged in");
notificationCenter.addNotification("error", "Failed to save data");
