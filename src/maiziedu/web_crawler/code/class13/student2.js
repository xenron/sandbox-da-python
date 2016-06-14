var StudentScoreTable,
    GenderFilter,
    NameFilter,
    ScoreTable,
    ScoreItem,
		ModifyScore,
    ScoreItemDeleteEvt = 'scoreitem delete event',
		ScoreItemModifyEvt = 'scoreitem modify event',
		ScoreItemSaveEvt = 'scoreitem save event',
    GenderFilterChangeEvt = 'genderFilter change event',
    NameFilterChangeEvt = 'nameFilter change event';

var url = 'http://localhost:8181/getScoreData';

//学生分数表
StudentScoreTable = React.createClass({
    getInitialState: function () {
        return {
            genderFilter: 0,
            nameFilter: '',
            data: null,
            modifyScore: null,
            className: 'dialog modify'
        }
    },
    componentDidMount: function () {
        // 订阅ScoreItem的删除事件
        PubSub.subscribe(ScoreItemDeleteEvt, this.onDeleteScoreItem);

        // 订阅GenderFilter的改变事件
        PubSub.subscribe(GenderFilterChangeEvt, this.onGenderChange);

        // 订阅NameFilter的改变事件
        PubSub.subscribe(NameFilterChangeEvt, this.onNameChange);

				//订阅保存item信息
				PubSub.subscribe(ScoreItemSaveEvt, this.onItemSave);

        $.get(url, function(res){
           if(res.code != 0){
              alert('获取数据失败~~');
              return;
           }
           this.setState({data: JSON.parse(res.data)});
        }.bind(this));
    },
		onItemSave: function(item){
			var tmpData = this.state.data.map(function(val){
				if(val._id == item._id){
					val = item;
				}
				return val;
			});
			this.setState({data: tmpData});
		},
    onGenderChange: function (gender) {
        this.setState({genderFilter: gender});
    },
    onDeleteScoreItem: function (id) {
        var data = this.state.data.map(function (item) {
            if(item._id === id) {
                item.deleteFlag = true;
            }
            return item;
        });

        this.setState({data:data});
    },
    onNameChange: function (name) {
        this.setState({nameFilter: name});
    },
    render: function () {
        if(!this.state.data){
					return <div>loading...</div>
				}else{
					return (
							<div>
								<GenderFilter genderFilter={this.state.genderFilter}/>
								<NameFilter nameFilter={this.state.nameFilter}/>
								<ModifyScore />
								<ScoreTable
										scoreNotes={this.state.data}
										genderFilter={this.state.genderFilter}
										nameFilter={this.state.nameFilter}
								/>
						</div>
					);
				}
    }
});

//修改分数信息
ModifyScore = React.createClass({
	getInitialState: function () {
		return {
			name: '',
			gender: 1,
			chinese: 0,
			math: 0,
			_id: 0
		};
	},
	componentDidMount: function () {
		PubSub.subscribe(ScoreItemModifyEvt, this.onModifyData);
	},
	shouldComponentUpdate:function(nextProps, nextState){
		for(var i in nextState){
			if(this.state[i]!= nextState[i]){
				return true;
			}
		}
		return false;
	},
	componentWillUpdate: function(nextProps, nextState){
		console.log('....update modify');
	},
	onModifyData: function(data){
		this.replaceState(data);
		this.refs.name.value = data.name;
		this.refs.gender.value = data.gender;
		this.refs.chinese.value = data.chinese;
		this.refs.math.value = data.math;
	},
	saveHandler: function () {
		if (this.state._id == 0) {
			alert('请先选择学生!');
			return;
		}
		PubSub.publish(ScoreItemSaveEvt, {
			name: this.refs.name.value,
			gender: this.refs.gender.value,
			chinese: this.refs.chinese.value,
			math: this.refs.math.value,
			_id: this.state._id
		});
	},
	render: function () {
		return (
			<div>
				<span>姓名</span>
				<input ref='name' defaultValue={this.state.name}/>
				<span>性别</span>
				<select ref='gender' defaultValue={this.state.gender}>
					<option value="男">男生</option>
					<option value="女">女生</option>
				</select>
				<span>语文</span>
				<input ref='chinese' defaultValue={this.state.chinese}/>
				<span>数学</span>
				<input ref='math' defaultValue={this.state.math}/>
				<button onClick={this.saveHandler} >保存</button>
			</div>
		)
	}
});

// 姓名筛选器
GenderFilter = React.createClass({
    genderChangeHandler: function () {
        // 发布GenderChange事件
        PubSub.publish(GenderFilterChangeEvt, this.refs.genderFilter.value);
    },
    render: function () {
        return (
            <div className="condition-item">
                <label>
                    <span>按性别筛选</span>
                    <select onChange={this.genderChangeHandler} ref="genderFilter">
                        <option value="0">All</option>
                        <option value="1">男生</option>
                        <option value="2">女生</option>
                    </select>
                </label>
            </div>
            );
    }
});

// 姓名筛选器
NameFilter = React.createClass({
    nameChangeHandler: function () {
        PubSub.publish(NameFilterChangeEvt, this.refs.nameFilter.value);
    },
    render: function () {
        return (
            <div className="condition-item">
                <label>
                    <span>按姓名筛选</span>
                    <input type="text" ref="nameFilter" onChange={this.nameChangeHandler} value={this.props.nameFilter}/>
                </label>
            </div>
            );
    }
});


//分数表格
ScoreTable = React.createClass({
    render: function () {
        var scoreNotes = [];
        var genderFilter = +this.props.genderFilter,
            nameFilter = this.props.nameFilter,
            GENDER = ['', '男', '女'],
            _this = this;

        this.props.scoreNotes.map(function (scoreItem) {
            if (genderFilter !== 0 && nameFilter === '') {
                // 仅genderfilter生效
                if (GENDER[genderFilter] === scoreItem.gender) {
                    !scoreItem.deleteFlag && scoreNotes.push(<ScoreItem key={scoreItem._id} score={scoreItem} />);
                }
                return;
            }

            if (genderFilter === 0 && nameFilter !== '') {
                // 仅nameFilter生效
                if (scoreItem.name.indexOf(nameFilter) > -1) {
                    !scoreItem.deleteFlag && scoreNotes.push(<ScoreItem key={scoreItem._id} score={scoreItem} />);
                }
                return;
            }

            if (genderFilter !== 0 && nameFilter !== '') {
                // 两个filter都生效
                if (GENDER[genderFilter] === scoreItem.gender && scoreItem.name.indexOf(nameFilter) > -1) {
                    !scoreItem.deleteFlag && scoreNotes.push(<ScoreItem key={scoreItem._id} score={scoreItem} />);
                }
                return;
            }

            !scoreItem.deleteFlag && scoreNotes.push(<ScoreItem key={scoreItem._id} score={scoreItem} />);
        });

        return (
            <table>
                <thead>
                    <tr>
                        <th>姓名</th>
                        <th>性别</th>
                        <th>语文</th>
                        <th>数学</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {scoreNotes}
                </tbody>
            </table>
            );
    }
});

//分数表项
ScoreItem = React.createClass({
    deleteHandler: function (e, id) {
        PubSub.publish(ScoreItemDeleteEvt, this.props.score._id);
    },
		modifyHandler: function(){
			PubSub.publish(ScoreItemModifyEvt, this.props.score);
		},
    render: function () {
        var score = this.props.score;

        return (
            <tr>
                <td>{score.name}</td>
                <td>{score.gender}</td>
                <td>{score.chinese}</td>
                <td>{score.math}</td>
                <td><span className="trigger" onClick={this.modifyHandler}>修改</span><span className="trigger" onClick={this.deleteHandler}>删除</span></td>
            </tr>
            );
    }
});

ReactDOM.render(
  <StudentScoreTable />,
  document.querySelector('#example')
);
