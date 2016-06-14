


//输入信息
var Input = React.createClass({
  changeName: function(e){
    this.props.change(e.target.value);
  },

  render: function(){
    return(
      <div>
        <span>Name: </span><input onChange={this.changeName} defaultValue={this.props.name}/>
      </div>
    );
  }
});

var Show = React.createClass({
  render: function(){
    return(
      <div>
        <span>Hello {this.props.name}</span>
      </div>
    );
  }
});


var Hello = React.createClass({
  getInitialState: function(){
    return {name: 'Mr Right'}
  },

  changeName: function(val){
    this.setState({name: val})
  },

  render: function(){
    return(
      <div>
        <Input change={this.changeName} name={this.state.name}/>
        <Show name={this.state.name} />
      </div>
    );
  }
});


ReactDOM.render(
  <Hello />,
  document.getElementById('example')
);