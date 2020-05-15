import React from "react";
import "./myStyle.css";
import TodoItem from "./TodoItem";

class Mytodolist extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      inputValue: "Test",
      list: ["Python", "JavaScript1"],
    };
  }

  handleInputChange(e) {
    this.setState({
      inputValue: e.target.value,
      // list: ["Python", "JavaScript"],
    });
  }
  handleBtnClick() {
    console.log(this.state.list);

    this.state.list.push(this.state.inputValue);
    console.log(this.state.list);
    this.setState({
      inputValue: "",
      list: this.state.list,
    });
  }
  handItemDel(index) {
    console.log(index);
    const list = this.state.list;
    delete list[index];
    console.log(this.state.list);
    this.setState({
      list: list,
    });
  }
  render() {
    return (
      <div>
        <label htmlFor="insertArea">输入内容</label>
        <input
          className="input"
          id="insertArea"
          type="text"
          value={this.state.inputValue}
          onChange={this.handleInputChange.bind(this)}
        />
        <button onClick={this.handleBtnClick.bind(this)}>提交</button>
        <ul>
          {this.state.list.map((item, index) => {
            return (
              <TodoItem content={item} index={index}/>
              // <li
              //   key={index}
              //   onClick={this.handItemDel.bind(this, index)}
              //   dangerouslySetInnerHTML={{ __html: item }}
              // ></li>
            );
          })}
        </ul>
      </div>
    );
  }
}

export default Mytodolist;
