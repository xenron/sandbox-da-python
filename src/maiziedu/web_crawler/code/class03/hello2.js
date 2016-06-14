var Hello = React.createClass({
	displayName: "Hello",
	
	render: function render() {
		return React.createElement(
			"span",
			null,
			"Hello World!"
		);
	}
});

ReactDOM.render(
	React.createElement(Hello, null), document.getElementById('example')
);