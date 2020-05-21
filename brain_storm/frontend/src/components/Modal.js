 // frontend/src/components/Modal.js

    import React, { Component } from "react";
    import axios from "axios"
    import {
      Button,
      Modal,
      ModalHeader,
      ModalBody,
      ModalFooter,
      Form,
      FormGroup,
      Input,
      Label
    } from "reactstrap";

    export default class CustomModal extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: this.props.activeItem
        };
      }
      componentWillMount() {
        this.getSnapshots();
      }
      getSnapshots = async () => {
        let url = "http://localhost:5000/users/" + this.state.activeItem.userId + "/" + "snapshots"; 
        let res = await axios.get(url);
        this.setState({ snapshotsList: res.data })
      }
      handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === "checkbox") {
          value = e.target.checked;
        }
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
      };
      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> Todo Item </ModalHeader>
            <ModalBody>
              <div>{this.state.snapshotsList != null ? JSON.stringify(this.state.snapshotsList) : null}</div>
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>Return</Button>
            </ModalFooter>
          </Modal>
        );
      }
    }