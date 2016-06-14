var Form = React.createClass({
	getInitialState: function(){
		return{
			input: '1'
		}
	},

	shouldComponentUpdate: function(){
		debugger
	},

	handleRadioChange: function(evt){
		console.log(evt.target.value);
	},

	render: function(){
		return(
			<div>
          <input type="radio" name="opt" onChange={this.handleRadioChange} value='1' defaultChecked /> Option 1
          <input type="radio" name="opt" onChange={this.handleRadioChange} value='2' /> Option 2
			</div>
		);
	}
});

ReactDOM.render(
	<Form />,
	document.getElementById('example')
)