import React from "react";

class TodoItem extends React.Component {
    constructor(props){
        super(props)
        this.handleDelete=this.handleDelete.bind(this)
    }
  handleDelete() {
    console.log("11");
  }

  render() {
    console.log("->this props", this.props);
    return (
      <div onClick={this.handleDelete}>{this.props.content}</div>
    );
  }
}

export default TodoItem;
