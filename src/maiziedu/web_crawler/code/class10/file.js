var Form = React.createClass({
	handleFileChange: function(evt){
		this.setState({'input': evt.target.value});
	},
	render: function(){
		return(
			<div>
				<input type='file' onChange={this.handleFileChange}/>
			</div>
		);
	}
});

ReactDOM.render(
	<Form />,
	document.getElementById('example')
)