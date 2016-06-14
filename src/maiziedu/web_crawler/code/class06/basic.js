// 基础props使用
// 不可修改父组件
// 1.getDefaultProps
// 2.对于外界/父组件 传递的属性值，无法直接修改，它是只读的


var Hello = React.createClass({
  // getInitialState: function(){}
  getDefaultProps: function(){
    return {
      name: 'Default'
    }
  },

  render: function() {
    // this.props.name = ' Hello...';
    return (
      <div>
        <span>Hello {this.props.name}!</span>
      </div>
    );
  }
});

ReactDOM.render(
  <Hello />,
  document.getElementById('example')
);