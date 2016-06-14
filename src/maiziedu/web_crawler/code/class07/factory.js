window.Note = React.createClass({
	render: function(){
		return (
			<div>I am a Note</div>
		);
	}
});

ReactDOM.render(
	React.createFactory(Note)(),
	document.getElementById('example')
)

// React.createFactory 返回的不是实例！！只是生产实例的工厂方法