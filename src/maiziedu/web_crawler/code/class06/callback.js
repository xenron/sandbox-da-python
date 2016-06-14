// 子组件向父组件的数据流动

//子组件
var Child = React.createClass({
  clickFunc: function(){
    this.props.add();
  },

  render: function(){
    return(
      <div onClick={this.clickFunc}>
        <span>Hello {this.props.fullName}.</span>
      </div>
    )
  }
});

//父组件
var Parent = React.createClass({
  getInitialState: function(){
    return{
      count: 0
    }
  },
  //增加计数
  addCount: function(){
    this.setState({count: ++this.state.count});
  },
  //增加姓氏
  addFamilyName: function(name){
    return name + ' Jobs';
  },

  render: function() {
    return (
      <div>
        <div>Total Count: {this.state.count}</div>
        <br/>
        <Child fullName={this.addFamilyName(this.props.name)} add={this.addCount}/>
        <br/>
        <Child fullName={this.addFamilyName(this.props.name)} add={this.addCount}/>
      </div>
    );
  }
});

ReactDOM.render(
  <Parent name="Steven"/>,
  document.getElementById('example')
);




// 父组件（回调传递） ==> 子组件（调用回调函数） ==>修改父组件的 state
