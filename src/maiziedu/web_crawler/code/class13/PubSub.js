

window.PubSub = {
  cbArr: {},
  //发送消息
  publish: function(evt, data, context){
    if(this.cbArr[evt]){
      this.cbArr[evt].map(function(cb){
        cb.call(context, data);
      })
    }
  },

  //订阅消息
  subscribe: function(evt, handler){
    if(!this.cbArr[evt]){
      this.cbArr[evt] = [];
    }
    if(this.cbArr[evt].indexOf(handler) > -1){
      return;
    }
    this.cbArr[evt].push(handler);
  },

  // 取消订阅消息
  unSubscribe: function(evt, handler){
    if(this.cbArr[evt] && this.cbArr[evt].indexOf(handler) > -1){
      this.cbArr[evt].splice(this.cbArr[evt].indexOf(handler), 1);
    }
  }
}
