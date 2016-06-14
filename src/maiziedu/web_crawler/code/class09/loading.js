var Test = React.createClass({
  getInitialState: function(){
    return {
      isloading: true,
      error: null,
      data: null
    }
  },
  componentDidMount: function(){
    this.serverRequest = $.get('http://localhost:8181/getData', function(res){
      if(res.code != 0){
        this.setState({isloading: false, error: res.msg});
      }else{
        var _data = res.data;
        _data = JSON.parse(_data);
        this.setState({isloading: false, error: null, data:{name: _data.name, age: _data.age}});
      }
    }.bind(this));
  },

  componentWillUnmount: function() {
    this.serverRequest.abort();
  },

  render: function(){
    if(this.state.isloading){
      return <span>loading...</span>;
    }else if(this.state.error){
      return <span>Error: {this.state.error}</span>;
    }else{
      return <span>Hello, I am {this.state.data.name}, I am {this.state.data.age} years old</span>;
    }
  }
});

ReactDOM.render(
  <Test />,
  document.getElementById('example')
);