'use strict';

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
    displayName: 'StudentScoreTable',

    getInitialState: function getInitialState() {
        return {
            genderFilter: 0,
            nameFilter: '',
            data: null,
            modifyScore: null,
            className: 'dialog modify'
        };
    },
    componentDidMount: function componentDidMount() {
        // 订阅ScoreItem的删除事件
        PubSub.subscribe(ScoreItemDeleteEvt, this.onDeleteScoreItem);

        // 订阅GenderFilter的改变事件
        PubSub.subscribe(GenderFilterChangeEvt, this.onGenderChange);

        // 订阅NameFilter的改变事件
        PubSub.subscribe(NameFilterChangeEvt, this.onNameChange);

        //订阅保存item信息
        PubSub.subscribe(ScoreItemSaveEvt, this.onItemSave);

        $.get(url, function (res) {
            if (res.code != 0) {
                alert('获取数据失败~~');
                return;
            }
            this.setState({ data: JSON.parse(res.data) });
        }.bind(this));
    },
    onItemSave: function onItemSave(item) {
        var tmpData = this.state.data.map(function (val) {
            if (val._id == item._id) {
                val = item;
            }
            return val;
        });
        this.setState({ data: tmpData });
    },
    onGenderChange: function onGenderChange(gender) {
        this.setState({ genderFilter: gender });
    },
    onDeleteScoreItem: function onDeleteScoreItem(id) {
        var data = this.state.data.map(function (item) {
            if (item._id === id) {
                item.deleteFlag = true;
            }
            return item;
        });

        this.setState({ data: data });
    },
    onNameChange: function onNameChange(name) {
        this.setState({ nameFilter: name });
    },
    render: function render() {
        if (!this.state.data) {
            return React.createElement(
                'div',
                null,
                'loading...'
            );
        } else {
            return React.createElement(
                'div',
                null,
                React.createElement(GenderFilter, { genderFilter: this.state.genderFilter }),
                React.createElement(NameFilter, { nameFilter: this.state.nameFilter }),
                React.createElement(ModifyScore, null),
                React.createElement(ScoreTable, {
                    scoreNotes: this.state.data,
                    genderFilter: this.state.genderFilter,
                    nameFilter: this.state.nameFilter
                })
            );
        }
    }
});

//修改分数信息
ModifyScore = React.createClass({
    displayName: 'ModifyScore',

    getInitialState: function getInitialState() {
        return {
            name: '',
            gender: 1,
            chinese: 0,
            math: 0,
            _id: 0
        };
    },
    componentDidMount: function componentDidMount() {
        PubSub.subscribe(ScoreItemModifyEvt, this.onModifyData);
    },
    shouldComponentUpdate: function shouldComponentUpdate(nextProps, nextState) {
        for (var i in nextState) {
            if (this.state[i] != nextState[i]) {
                return true;
            }
        }
        return false;
    },
    componentWillUpdate: function componentWillUpdate(nextProps, nextState) {
        console.log('....update modify');
    },
    onModifyData: function onModifyData(data) {
        this.replaceState(data);
        this.refs.name.value = data.name;
        this.refs.gender.value = data.gender;
        this.refs.chinese.value = data.chinese;
        this.refs.math.value = data.math;
    },
    saveHandler: function saveHandler() {
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
    render: function render() {
        return React.createElement(
            'div',
            null,
            React.createElement(
                'span',
                null,
                '姓名'
            ),
            React.createElement('input', { ref: 'name', defaultValue: this.state.name }),
            React.createElement(
                'span',
                null,
                '性别'
            ),
            React.createElement(
                'select',
                { ref: 'gender', defaultValue: this.state.gender },
                React.createElement(
                    'option',
                    { value: '男' },
                    '男生'
                ),
                React.createElement(
                    'option',
                    { value: '女' },
                    '女生'
                )
            ),
            React.createElement(
                'span',
                null,
                '语文'
            ),
            React.createElement('input', { ref: 'chinese', defaultValue: this.state.chinese }),
            React.createElement(
                'span',
                null,
                '数学'
            ),
            React.createElement('input', { ref: 'math', defaultValue: this.state.math }),
            React.createElement(
                'button',
                { onClick: this.saveHandler },
                '保存'
            )
        );
    }
});

// 姓名筛选器
GenderFilter = React.createClass({
    displayName: 'GenderFilter',

    genderChangeHandler: function genderChangeHandler() {
        // 发布GenderChange事件
        PubSub.publish(GenderFilterChangeEvt, this.refs.genderFilter.value);
    },
    render: function render() {
        return React.createElement(
            'div',
            { className: 'condition-item' },
            React.createElement(
                'label',
                null,
                React.createElement(
                    'span',
                    null,
                    '按性别筛选'
                ),
                React.createElement(
                    'select',
                    { onChange: this.genderChangeHandler, ref: 'genderFilter' },
                    React.createElement(
                        'option',
                        { value: '0' },
                        'All'
                    ),
                    React.createElement(
                        'option',
                        { value: '1' },
                        '男生'
                    ),
                    React.createElement(
                        'option',
                        { value: '2' },
                        '女生'
                    )
                )
            )
        );
    }
});

// 姓名筛选器
NameFilter = React.createClass({
    displayName: 'NameFilter',

    nameChangeHandler: function nameChangeHandler() {
        PubSub.publish(NameFilterChangeEvt, this.refs.nameFilter.value);
    },
    render: function render() {
        return React.createElement(
            'div',
            { className: 'condition-item' },
            React.createElement(
                'label',
                null,
                React.createElement(
                    'span',
                    null,
                    '按姓名筛选'
                ),
                React.createElement('input', { type: 'text', ref: 'nameFilter', onChange: this.nameChangeHandler, value: this.props.nameFilter })
            )
        );
    }
});

//分数表格
ScoreTable = React.createClass({
    displayName: 'ScoreTable',

    render: function render() {
        var scoreNotes = [];
        var genderFilter = +this.props.genderFilter,
            nameFilter = this.props.nameFilter,
            GENDER = ['', '男', '女'],
            _this = this;

        this.props.scoreNotes.map(function (scoreItem) {
            if (genderFilter !== 0 && nameFilter === '') {
                // 仅genderfilter生效
                if (GENDER[genderFilter] === scoreItem.gender) {
                    !scoreItem.deleteFlag && scoreNotes.push(React.createElement(ScoreItem, { key: scoreItem._id, score: scoreItem }));
                }
                return;
            }

            if (genderFilter === 0 && nameFilter !== '') {
                // 仅nameFilter生效
                if (scoreItem.name.indexOf(nameFilter) > -1) {
                    !scoreItem.deleteFlag && scoreNotes.push(React.createElement(ScoreItem, { key: scoreItem._id, score: scoreItem }));
                }
                return;
            }

            if (genderFilter !== 0 && nameFilter !== '') {
                // 两个filter都生效
                if (GENDER[genderFilter] === scoreItem.gender && scoreItem.name.indexOf(nameFilter) > -1) {
                    !scoreItem.deleteFlag && scoreNotes.push(React.createElement(ScoreItem, { key: scoreItem._id, score: scoreItem }));
                }
                return;
            }

            !scoreItem.deleteFlag && scoreNotes.push(React.createElement(ScoreItem, { key: scoreItem._id, score: scoreItem }));
        });

        return React.createElement(
            'table',
            null,
            React.createElement(
                'thead',
                null,
                React.createElement(
                    'tr',
                    null,
                    React.createElement(
                        'th',
                        null,
                        '姓名'
                    ),
                    React.createElement(
                        'th',
                        null,
                        '性别'
                    ),
                    React.createElement(
                        'th',
                        null,
                        '语文'
                    ),
                    React.createElement(
                        'th',
                        null,
                        '数学'
                    ),
                    React.createElement(
                        'th',
                        null,
                        '操作'
                    )
                )
            ),
            React.createElement(
                'tbody',
                null,
                scoreNotes
            )
        );
    }
});

//分数表项
ScoreItem = React.createClass({
    displayName: 'ScoreItem',

    deleteHandler: function deleteHandler(e, id) {
        PubSub.publish(ScoreItemDeleteEvt, this.props.score._id);
    },
    modifyHandler: function modifyHandler() {
        PubSub.publish(ScoreItemModifyEvt, this.props.score);
    },
    render: function render() {
        var score = this.props.score;

        return React.createElement(
            'tr',
            null,
            React.createElement(
                'td',
                null,
                score.name
            ),
            React.createElement(
                'td',
                null,
                score.gender
            ),
            React.createElement(
                'td',
                null,
                score.chinese
            ),
            React.createElement(
                'td',
                null,
                score.math
            ),
            React.createElement(
                'td',
                null,
                React.createElement(
                    'span',
                    { className: 'trigger', onClick: this.modifyHandler },
                    '修改'
                ),
                React.createElement(
                    'span',
                    { className: 'trigger', onClick: this.deleteHandler },
                    '删除'
                )
            )
        );
    }
});

ReactDOM.render(React.createElement(StudentScoreTable, null), document.querySelector('#example'));
