//注意state 更新时间

var Child = React.createClass({
	getInitialState: function(){
		return {time: new Date().toTimeString()}
	},

	componentWillReceiveProps: function(nextProps){
		this.setState({time: new Date().toTimeString()});

		// if(this.props.number == 3 ){
		// 	ReactDOM.unmountComponentAtNode(this.refs.myDiv);
		// 	// this.refs.myDiv.remove();
		// }

	},
	componentWillUnmount: function(){
		console.log('child will be unmounted....');
		debugger
	},

	render: function(){
		return(
			<div ref="myDiv">Child get props: {this.props.number} at {this.state.time}</div>
		)
	}
});

var Parent = React.createClass({
	getInitialState: function(){
		return {
			count: 0
		}
	},

	componentWillMount: function(){
		this.setState({count: 1});
	},

	clickHandler: function(){
		this.setState({count: this.state.count+1})
	},	

	render: function(){
		return(
			<div onClick={this.clickHandler}>
					{ this.state.count == 3?
						'':
						<Child number={this.state.count}></Child>
					}
			</div>
		);
	}
});

ReactDOM.render(
	<Parent />,
	document.getElementById('example')
);