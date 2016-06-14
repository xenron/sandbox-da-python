// 大部分组件的工作应该是从 props 里取数据并渲染出来。但是，有时需要对用户输入、服务器请求或者时间变化等作出响应，这时才需要使用 State。


var Count = React.createClass({
  getInitialState: function(){
    return {
      count: 0
    }
  },

  handleClick: function(){
    this.setState({count: this.state.count + 1});
  },

  render: function() {
    return (
      <div>
        <a onClick={this.handleClick}>You have clicked {this.state.count} times!</a>
      </div>
    );
  }
});

ReactDOM.render(
  <Count />,
  document.getElementById('example')
);
  
