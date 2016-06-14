var Form = React.createClass({
	getInitialState: function(){
		return{
			input: ['B','C']
		}
	},

	handleSelecChange: function(evt){
		console.log(evt.target.value);
		//evt.target.options[0].value
		//evt.target.options[0].selected
	},
	render: function(){
		return(
			<div>
        <select defaultValue={this.state.input} onChange={this.handleSelecChange} ref='mySelect' multiple={true}>
          <option value="A">Apple</option>
          <option value="B">Banana</option>
          <option value="C">Strawberry</option>
        </select>
			</div>
		);
	}
});

ReactDOM.render(
	<Form />,
	document.getElementById('example')
)