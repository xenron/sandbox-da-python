var styles = {
	inputText: {
		width: 100,
		height: 20,
		display: 'block'
	}
};

var Form = React.createClass({
	getInitialState: function(){
		return{
			input: 'default'
		}
	},
	handleTextChange: function(evt){
		this.setState({'input': evt.target.value});
	},
	render: function(){
		return(
			<div>
				<input type='text' style={styles.inputText} value='123' onChange={this.handleTextChange} defaultValue={this.state.input}/>
			</div>
		);
	}
});

ReactDOM.render(
	<Form />,
	document.getElementById('example')
)
