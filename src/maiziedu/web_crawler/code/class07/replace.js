var Count = React.createClass({
	getInitialState: function(){
		return {
			count: 0,
			time : new Date().toTimeString()
		};
	},
	clickHandler: function(){
		if(this.state.count == 2){
			this.replaceState({count: 0});
		}else{
			this.setState({count: this.state.count+1, time: new Date().toTimeString()});
		}
	},
	render: function(){
		return (
			<div onClick={this.clickHandler}>
				Clicked {this.state.count} times at {this.state.time}
			</div>
		)
	}
});

ReactDOM.render(
	<Count />,
	document.getElementById('example')
);