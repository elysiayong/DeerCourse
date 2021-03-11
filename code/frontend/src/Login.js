import {Button, Modal, Form} from 'react-bootstrap';
import React, {useState, props} from 'react';

/* Form Inspired By: https://www.positronx.io/build-react-login-sign-up-ui-template-with-bootstrap-4/ */

export const Login = () => (
    <div className="login-form">
        <br></br> 
        <form>
            <h1 className="login-title">Login</h1>  <br></br>
            
            <div className="form-group">
                <input type="email" className="form-control" placeholder="Enter Email" />
            </div>

            <div className="form-group">
                <input type="password" className="form-control" placeholder="Enter Password" />
            </div>

            <button type="submit" className="submit-login btn btn-primary btn-block">Login</button> <br></br>
            
            <p className="forgot text-center">
                Forgot <a className="forgot-password" href="/error">Password?</a>
            </p>

            <hr></hr>

            <React.Fragment>
                <NewAccountForm />
            </React.Fragment>
            
            <br></br>
        </form>
    </div>
)

function NewAccountForm() {
    const [show, setShow] = useState(false);
  
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
  
    return (
        <>
        <Button className="create-new-account btn btn-primary btn-block" variant="primary" onClick={handleShow}>
          Create New Account
        </Button>
  
        <Modal {...props} centered={true} size="lg" aria-labelledby="contained-modal-title-hcenter" className="new-account-form" show={show} onHide={handleClose} animation={true}>
            <Modal.Header className="create-new-account-title" closeButton>
                <Modal.Title>Create New Account</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <br></br>
                <Form>
                    <Form.Group controlId="formBasicEmail">
                        <Form.Control type="email" placeholder="* Enter Email" />
                        <Form.Text className="text-muted">
                        Please make sure this is a U Toronto Email.
                        </Form.Text>
                    </Form.Group>

                    <Form.Group controlId="formBasicPassword">
                        <Form.Control type="password" placeholder="* Password" />
                    </Form.Group>
                    <Form.Group controlId="formBasicPassword">
                        <Form.Control type="password" placeholder="* Confirm Password" />
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
                Close
            </Button>
            <Button className="submit-login" variant="primary" onClick={handleClose}>
                Sign-Up
            </Button>
            </Modal.Footer>
        </Modal>
      </>
    );
  }
