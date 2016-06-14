//两层及以上的传递
var Child = React.createClass({
	render: function(){
		return(
			<div>
				<span>Hello {this.props.fullName}.It is {this.props.time} now</span>
			</div>
		)
	}
});

var Parent = React.createClass({
	getInitialState: function(){
		return{
			time: new Date().toDateString()
		}
	},
	addFamilyName: function(name){
		return name + ' Jobs';
	},

  render: function() {
    return (
      <Child fullName={this.addFamilyName(this.props.name)} time={this.state.time} />
    );
  }
});

var StevenData = {
	img: "http://a.hiphotos.baidu.com/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=a5575f5d7c899e516c83324623ceb256/500fd9f9d72a6059b5806dba2f34349b023bbafa.jpg",
	birthDay: "1955年2月24日" 
}

ReactDOM.render(
  <Parent data={StevenData}/>,
  document.getElementById('example')
);