class People {
    constructor(name) { //构造函数
          this.name = name;
    }
    sayName() {
          console.log('Hello, my name is ' + this.name);
    }
}

var p = new People('Steven');
p.sayName();


class Chinese extends People {
	constructor(name) {
		super(name);
	}
	sayName() {
		// super.sayName();
		console.log('i am Chinese');
	}

	sayCountry() {
		console.log('I come from China.');
	}
}

var c = new Chinese('Jay');
c.sayName();
c.sayCountry();