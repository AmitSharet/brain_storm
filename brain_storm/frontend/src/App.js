// frontend/src/App.js

  import React, { Component } from "react";
  import axios from "axios";
  import Modal from "./components/Modal"
  class App extends Component {
    constructor(props) {
      super(props);
      this.state = {
        usersList: [],
        snapshotsList: [],
        modal: false,
        activeItem: {
          userId: "",
          username: "",
          birthday: false
        },
      };
    }
    componentDidMount() {
      this.refreshList();
    }
    refreshList = async () => {
      await axios
        .get("http://localhost:5000/users")
        .then(res => this.setState({ usersList: res.data }))
        .catch(err => console.log(err))
    };
    refreshSnapshots = async () => {
      let url = "http://localhost:5000/users/" + this.state.activeItem.userId + "/" + "snapshots"; 
      await axios
        .get(url)
        .then(res => this.setState({ snapshotsList: res.data }))
        .catch(err => console.log(err))
    };
    displayCompleted = status => {
      if (status) {
        return this.setState({ viewCompleted: true });
      }
      return this.setState({ viewCompleted: false });
    };
    editItem = async item => {
      await this.setState({ activeItem: item });
      this.setState({ modal: !this.state.modal })
      // alert(this.state.snapshotsList)

      // await axios
      //   .get(url)
      //   .then(async res=> await this.setState({ snapshotsList: res.data }))
      //   .then(this.setState({ modal: !this.state.modal }))
      //   .catch(err => console.log(err))
      
      // await this.refreshSnapshots();
      // alert(this.state.snapshotsList)
      // this.setState({ modal: !this.state.modal })
    };
    handleSubmit = item => {
      this.setState({ activeItem: item, modal: !this.state.modal });
      // this.toggle();
      // if (item.id) {
      //   axios
      //     .put(`http://localhost:8000/api/todos/${item.id}/`, item)
      //     .then(res => this.refreshList());
      //   return;
      // }
      // axios
      //   .post("http://localhost:8000/api/todos/", item)
      //   .then(res => this.refreshList());
    };
    renderTabList = () => {
      // return (
      //   <div className="my-5 tab-list">
      //     <span
      //       onClick={() => this.displayCompleted(true)}
      //       className={this.state.viewCompleted ? "active" : ""}
      //     >
      //       Users
      //     </span>
      //     <span
      //       onClick={() => this.displayCompleted(false)}
      //       className={this.state.viewCompleted ? "" : "active"}
      //     >
      //       Snapshots
      //     </span>
      //   </div>
      // );
    };
    renderItems = () => {
      if (this.state.usersList == null) return null;
      let res = []

      for (var i = 0; i < this.state.usersList.length; i++) {
        let item = this.state.usersList[i]
        res.push(
        <div key={"user " + item.userId} className={i == this.state.usersList.length - 1 ? '' : 'divider'}>
          <div className="my-5 tab-list divided"> 
          <span className='datatype'>{"ID:"}</span><span className="active">{item.userId}</span>
          <span className='datatype'>{"Username:"}</span><span className="active">{item.username}</span>
          <span className='datatype'>{"Birthday:"}</span><span className="active">{item.birthday}</span>
          <span className="snapshot"><button onClick={() => this.editItem(item)} className="btn btn-info">Snapshots</button></span>
          </div>
        </div> )
      }
      return res 
    };
    render() {
      return (
        <main className="content">
          <h1 className="text-white text-uppercase text-center my-4">BRAIN STORM</h1>
          <div className="row ">
            <div className="col-md-6 col-sm-10 mx-auto p-0">
              <div className="card p-3">
                {this.renderTabList()}
                <ul className="list-group list-group-flush">
                  {this.renderItems()}
                </ul>
              </div>
            </div>
          </div>
          {this.state.modal ? (
            <Modal
              activeItem={this.state.activeItem}
              activeSnapshots={this.state.activeSnapshots}
              toggle={this.toggle}
              onSave={this.handleSubmit}
            />
          ) : null}
        </main>
      );
    }
  }
  export default App;