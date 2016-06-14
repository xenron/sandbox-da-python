var Test = React.createClass({
	getInitialState: function(){
		return {
			name: 'White',
			age: 51
		}
	},

	//注意作用域问题
	componentDidMount: function(){
		$.get('http://localhost:8181/getData', function(res){
			if(res.code != 0){
				alert(res.msg);
			}else{
				var _data = res.data;
				_data = JSON.parse(_data);
				this.setState({name: _data.name, age: _data.age});
			}
		}.bind(this));
	},

	render: function(){
		return(
			<div>
				<span>Hello, I am {this.state.name}, I am {this.state.age} years old</span>
			</div>
		)
	}
});

ReactDOM.render(
	<Test />,
	document.getElementById('example')
);