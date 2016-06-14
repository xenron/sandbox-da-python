var Hello = React.createClass({
	
	render: function(){
		return(
			<span className="content" style={{color: 'red',fontSize: 20}>Hello World!</span>
		);
	}
});

ReactDOM.render(
	<Hello class="content"/>,
	document.getElementById('example')
);