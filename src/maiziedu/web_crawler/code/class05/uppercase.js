//也可以使用ref实现，注意this的指向

var Hello = React.createClass({
	getInitialState: function(){
		return{ name: 'world' }
	},

	changeName: function(e){
		this.setState({name: e.target.value});
	},

	render: function(){
		var upperName = this.state.name.toUpperCase();
		
		return(
			<div>
				<input onChange={this.changeName} defaultValue={this.props.name}></input>
				<br/>
				<span>Hello {upperName}</span>
			</div>
		);
	}
});

ReactDOM.render(
	<Hello name="default"/>,
	document.getElementById('example')
);