var Hello = React.createClass({
	
	render: function(){
		return(
			<span>Hello World!</span>
		);
	}
});

ReactDOM.render(
	<Hello />,
	document.getElementById('example')
);