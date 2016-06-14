var InnerComponent = React.createClass({
  shouldComponentUpdate: function(nextProps, nextState){
    return nextProps == this.props;
  },

  render: function(){
    return(
      <div>{this.props.value.foo}</div>
    )
  }
});

var Test = React.createClass({
  getInitialState: function() {
    return { value: { foo: 'bar' } };
  },
  onClick: function() {
    var value = this.state.value;
    value.foo += 'bar'; 
    this.setState({ value: value });
  },
  render: function() {
    return (
      <div>
        <InnerComponent value={this.state.value} />
        <a onClick={this.onClick}>Click me</a>
      </div>
    );
  }
});

ReactDOM.render(
<Test />,
document.getElementById('example')
);