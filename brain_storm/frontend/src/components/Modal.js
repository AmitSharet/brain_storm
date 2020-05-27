 // frontend/src/components/Modal.js

    import React, { Component } from "react";
    import axios from "axios"
    import { Accordion, AccordionItem } from 'react-sanfona';
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
      getSnapshotContent = (snapshot) => {
        let content = ""
        if (snapshot.pose != null) 
        {
          content += 
          "Pose translation\n" +
          "x: " + JSON.stringify(snapshot.pose.translation.x) + "\n" +
          "y: " + JSON.stringify(snapshot.pose.translation.y) + "\n" +
          "z: " + JSON.stringify(snapshot.pose.translation.z) + "\n" +
          "Pose rotation\n" +
          "x: " + JSON.stringify(snapshot.pose.rotation.x) + "\n" +
          "y: " + JSON.stringify(snapshot.pose.rotation.y) + "\n" +
          "z: " + JSON.stringify(snapshot.pose.rotation.z) + "\n" +
          "w: " + JSON.stringify(snapshot.pose.rotation.w) + "\n"
        }
        if (snapshot.colorImage != null)
        {
          content += 
          "Color image\n" +
          "width: " + JSON.stringify(snapshot.colorImage.width) + "\n" +
          "height: " + JSON.stringify(snapshot.colorImage.height) + "\n" +
          "path: " + JSON.stringify(snapshot.colorImage.colorPath) + "\n"
        }
        if (snapshot.depthImage != null)
        {
          content += 
          "Depth image\n" +
          "width: " + JSON.stringify(snapshot.depthImage.width) + "\n" +
          "height: " + JSON.stringify(snapshot.depthImage.height) + "\n" +
          "path: " + JSON.stringify(snapshot.depthImage.depthPath) + "\n"
        }
        if (snapshot.feelings != null)
        {
          content += 
          "Feelings\n" +
          "Hunger: " + JSON.stringify(snapshot.feelings.hunger) + "\n" +
          "Thirst: " + JSON.stringify(snapshot.feelings.thirst) + "\n" +
          "Exhaustion: " + JSON.stringify(snapshot.feelings.exhaustion) + "\n" +
          "Happiness: " + JSON.stringify(snapshot.feelings.happiness) + "\n"
        }
          
        // if (snapshot.feelings != null) content += snapshot.feelings
        // if (snapshot.color_image != null) content += snapshot.color_image.path
        return content }
        // if (snapshot.)  
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
            <ModalHeader toggle={toggle}> {this.state.activeItem.username +"'s snapshots"} </ModalHeader>
            <ModalBody>
            <div>{this.state.snapshotsList != null ?
              <Accordion className="react-sanfona-item-title">
                {this.state.snapshotsList.map(item => {
                  return (
                    <AccordionItem title={'Snapshot ' + item.datetime}>
                      <div className='react-sanfona-item-body'>
                        {this.getSnapshotContent(item)}
                      </div>
                    </AccordionItem>
                  );
                })}
              </Accordion>
            : null}</div>

              {/* {<div>{this.state.snapshotsList != null ? JSON.stringify(this.state.snapshotsList) : null}</div>} */}
              {/* <Accordion>
                {this.state.snapshotsList.map(item => {
                  alert('hi');
                  return (
                    <AccordionItem title={'Item'} expanded={item == 1}>
                      <div>
                        {'Item content'}
                      </div>
                    </AccordionItem>
                  );
                })}
              </Accordion> */}
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>Return</Button>
            </ModalFooter>
          </Modal>
        );
      }
    }
