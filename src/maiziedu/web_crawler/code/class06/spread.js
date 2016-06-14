//解构赋值

var Child = React.createClass({
  render: function(){
    return(
      <div>
        <span>I am {this.props.name}! I am {this.props.age} years old. It is {this.props.time} now</span>
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

  render: function() {
    var {age, ...others} = this.props;
    return (
      <Child name={this.props.name} time={this.state.time} />
    );
  }
});

ReactDOM.render(
  <Parent name="Steven" age="20" country="china"/>,
  document.getElementById('example')
);