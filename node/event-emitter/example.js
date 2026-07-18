import EventEmitter from "node:events";

const myEmitter = new EventEmitter();

function c1() {
  console.log("an event occured!");
}

function c2() {
  console.log("Yet another event occured");
}

myEmitter.on("eventOne", c1);
myEmitter.on("eventOne", c2);

myEmitter.emit("eventOne");

myEmitter.on("data", (msg) => console.log(`Received: ${msg}`));
myEmitter.emit("data", "Hello World");

function greet(name) {
  console.log(`Hi ${name}`);
}

myEmitter.on("greet", greet);
myEmitter.off("greet", greet); //removes from listener
myEmitter.emit("greet", "Bob"); // Nothing happens
