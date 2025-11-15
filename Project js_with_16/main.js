let person = {
    name: "Saif",
    greet() {
        console.log("Hello! My name is " + this.name);
    }
};

person.greet(); // Hello! My name is Saif