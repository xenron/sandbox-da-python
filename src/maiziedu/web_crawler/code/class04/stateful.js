var ChildList = React.createClass({
    render: function() {
    var results = this.props.results;
    return (
      <ol>
        {results.map(function(result) {
          return <li key={result.id}>{result.text}</li>;
        })}
      </ol>
    );
  }
});

var data = [{id:1,text: 'one'},{id:2,text: 'two'},{id:3,text: 'three'}];

ReactDOM.render(
  <ChildList results={data} />,
  document.getElementById('example')
);
