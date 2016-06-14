//也可以使用ref实现，注意this的指向

var Hello = React.createClass({
	getInitialState: function(){
		return{ name: 'world'}
	},

	changeName: function(e){
		this.setState({name: e.target.value});
	},

	render: function(){
		return(
			<div>
				<input onChange={this.changeName} defaultValue={this.state.name}></input>
				<span>Hello {this.state.name}</span>
			</div>
		);
	}
});

ReactDOM.render(
	<Hello />,
	document.getElementById('example')
);