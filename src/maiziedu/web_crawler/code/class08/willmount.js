var Test = React.createClass({
	getInitialState: function(){
		return {
			count: 0
		}
	},
	//挂载页面之前
	componentWillMount: function(){
		this.setState({count: 1});
		console.log('i will mount');
	},

	componentDidMount: function(){
		console.log('i have mounted');
		setTimeout((function(){
			this.setState({count: 2});
		}).bind(this) ,2000);
	},

	render: function(){
		return(
			<div>the count is {this.state.count}</div>
		);
	}
});

ReactDOM.render(
	<Test />,
	document.getElementById('example')
);