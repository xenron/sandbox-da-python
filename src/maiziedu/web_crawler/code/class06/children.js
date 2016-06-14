//this.props.children


var Note = React.createClass({
  render: function(){
    return (
      <li>{this.props.text}</li>
    );
  }
});

var NotesList = React.createClass({
  render: function() {
    return (
      <ol>
        {
          // this.props.children.map(function (child, index) {
          React.Children.map(this.props.children, function (child, index) {
            return <li text={child}>{child}</li>
          })
        }
      </ol>
    );
  }
});

ReactDOM.render(
  <NotesList>
    <span>Hello</span>
    <span>World</span>
  </NotesList>,
  document.getElementById('example')
);