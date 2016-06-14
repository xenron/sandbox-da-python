var Note = React.createClass({
	render: function(){
		return (
			<div>{this.props.content}</div>
		);
	}
});

var msg = 'Hi, there!';

ReactDOM.render(
	<Note content={msg} />,
	document.getElementById('example')
)
