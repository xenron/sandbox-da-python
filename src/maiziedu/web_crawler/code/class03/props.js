var Age = React.createClass({
	render: function(){
		return(
			<span>My age is {this.props.age}.</span> 
		)
	}
});

var Hello = React.createClass({
	
	render: function(){
		return(
			<div>
				<span>Hello {this.props.name}!</span>
				<Age age={this.props.age} style={{fontSize: 14, backgroundColor: 'red'},{fontSize: 20}}/>
			</div>
		);
	}
});

var props = {};
props.name = "steven";
props.age = 17;
var MyHello = <Hello {...props}/>;

ReactDOM.render(
	MyHello,
	document.getElementById('example')
);