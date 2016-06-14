var App = React.createClass({
  getInitialState: function() {
    return {userInput: ''};
  },
  handleChange: function(e) {
    this.setState({userInput: e.target.value});
  },
  clearAndFocusInput: function() {
    // Clear the input
    this.setState({userInput: ''}, function() {
      // This code executes after the component is re-rendered
      React.findDOMNode(this.refs.theInput).focus();   // Boom! Focused!
    });
  },
  render: function() {
    return (
      <div>
        <div onClick={this.clearAndFocusInput}>
          Click to Focus and Reset
        </div>
        <input
          ref={ function(component){ ReactDOM.findDOMNode(component).focus();} }
          value={this.state.userInput}
          onChange={this.handleChange}
        />
      </div>
    );
  }
});

ReactDOM.render(
<App />,
document.getElementById('example')
);

