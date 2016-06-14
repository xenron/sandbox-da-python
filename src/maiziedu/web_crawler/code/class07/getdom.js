var Test = React.createClass({
	render: function(){
		return(
			<div>I am just a test...</div>
		)
	}
});

var Note = React.createClass({
	getInitialState: function(){
		return {
			name: 'world'
		}
	},
	inputChange: function(){
		console.log(this.refs.myTest);
		console.log( ReactDOM.findDOMNode(this.refs.myTest));
		this.setState({name: ReactDOM.findDOMNode(this.refs.myInput).value});
	},

	render: function(){
		return (
			<div>
				<input ref="myInput" onChange={this.inputChange} defaultValue={this.state.name}/>
				<br/>
				<span>
					{this.props.content},{this.state.name}
				</span>
				<Test ref='myTest' />
			</div>
		);
	}
});

var msg = 'Hi, there!';

ReactDOM.render(
	<Note content={msg} />,
	document.getElementById('example')
)