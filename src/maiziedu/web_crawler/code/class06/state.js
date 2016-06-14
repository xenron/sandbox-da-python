// props和state的区别

var Msg = React.createClass({
	render: function(){
		return(
			<div>
				<span style={{color:this.props.color}}>Hello {this.props.master}.It is {this.props.time} now. The color is {this.props.color}</span>
			</div>
		)
	}
});

var Hello = React.createClass({
	getInitialState: function(){
		return{
			time: new Date().toDateString(),
			color: 'black'
		}
	},
	changeColor: function(){
		this.setState({color: 'green'})
	},

	render: function() {
    return (
    	<div>
	    	<span onClick={this.changeColor}>The ownerName is {this.props.name}</span>
	    	<br/>
	      <Msg master={this.props.name} time={this.state.time} color={this.state.color}/>
	    </div>
    );
  }
});

ReactDOM.render(
  <Hello name="World" />,
  document.getElementById('example')
);



// 拥有者组件 ==（增加父组件的属性值）> 子组件