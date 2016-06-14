var countTime = 3;

var Child = React.createClass({
	getInitialState: function(){
		return {time: new Date().toTimeString()}
	},

	componentWillReceiveProps: function(nextProps){
		console.log('componentWillReceiveProps');
		this.setState({time: new Date().toTimeString()});
	},

	shouldComponentUpdate: function(nextProps, nextState){
		//不应该再有任何操作，收到新的state, props确定是否更新
		console.log('shouldComponentUpdate');
		return true;
	},

	componentWillUpdate: function(nextProps, nextState){
		//在接收到新的 props 或者 state 之后，立即更新之前调用
		console.log('componentWillUpdate');
		countTime--;
	},

	componentDidUpdate: function(prevProps, prevState){
		console.log('componentDidUpdate');
		console.log(countTime);
		if(countTime > 0){
			this.state.timer = setTimeout(function(){this.forceUpdate();	}.bind(this), 1000);
		}
	},


	render: function(){
		return(
			<div>Child get props: {this.props.number} at {this.state.time}</div>
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
				<Child number={this.state.count}></Child>
			</div>
		);
	}
});

ReactDOM.render(
	<Parent />,
	document.getElementById('example')
);