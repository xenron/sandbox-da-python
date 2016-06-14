var styles = {
	'title': {
		display: 'block',
		fontSize: 20,
		padding: 5
	}
}

var Form = React.createClass({
	getInitialState: function(){
		return {
			input: ['apple']
		}
	},

	handleCheckboxChange: function(evt){
		var _input = this.state.input,
				_value = evt.target.value;

		if(evt.target.checked){
			if(_input.indexOf(_value) == -1){
				_input.push(_value);
			}
		}else{
			if(_input.indexOf(_value) > -1){
				_input.splice(_input.indexOf(_value),1);
			}
		}
		this.setState({'input': _input});	
	},
	render: function(){
		return(
			<div>
					<span style={styles.title}>水果:</span>
					<div>
						<input type='checkbox' onChange={this.handleCheckboxChange} value='apple' /> <span>苹果</span> <br/>
						<input type='checkbox' onChange={this.handleCheckboxChange} value='banana' checked={this.state.input.indexOf('banana') > -1}/> <span>香蕉</span> <br/>
					</div>
			</div>
		);
	}
});

ReactDOM.render(
	<Form />,
	document.getElementById('example')
)