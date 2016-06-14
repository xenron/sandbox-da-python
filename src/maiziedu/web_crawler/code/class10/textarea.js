var styles = {
	inputText: {
		fontSize: 20,
		color: 'red',
		display: 'block'
	}
};

var Form = React.createClass({
	getInitialState: function(){
		return{
			input: 'this is a default textarea'
		}
	},
	handleTextChange: function(evt){
		this.setState({'input': evt.target.value});
	},
	render: function(){
		return(
			<div>
				<textarea style={styles.inputText} onChange={this.handleTextChange} defaultValue={this.state.input}/>
			</div>
		);
	}
});

ReactDOM.render(
	<Form />,
	document.getElementById('example')
)
