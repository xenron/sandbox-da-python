var Time = React.createClass({
  getInitialState: function(){
    return { today: new Date().toDateString()}
  },
  
  render: function(){
    return(
      <span>Today is {this.state.today}</span>
    );
  }
});

var Hello = React.createClass({
  getInitialState: function() {
    return {name: 'Steven'};
  },
  render: function() {
    return (
      <p>
        Hello {this.state.name}. <Time />
      </p>
    );
  }
});

ReactDOM.render(
  <Hello />,
  document.getElementById('example')
);


parent
owner

owner 传递props
parent


