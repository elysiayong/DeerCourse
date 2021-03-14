import {Button, Modal} from 'react-bootstrap';
import React, { useState } from 'react';
import { Formik, Form, Field, ErrorMessage} from 'formik';
import * as Yup from 'yup';
import axios from "axios";

export const NewAccountForm = () => {

    // toggle show/hide modal

    const [show, setShow] = useState(false);
    const handleClose = () => { setShow(false); hideBackendMesssage(); }
    const handleShow = () => setShow(true);

    const [backendMessage, displayBackendMessage] = useState(false);
    const hideBackendMesssage = () => displayBackendMessage(false);
    const showBackendMessage = () => displayBackendMessage(true);

    return (
        <>
        <Button className="create-new-account btn btn-primary btn-block" variant="primary" onClick={handleShow}>
          Create New Account
        </Button>
        <Modal centered={true} size="lg" aria-labelledby="contained-modal-title-hcenter" className="new-account-form" show={show} onHide={handleClose} animation={false}>
            <Modal.Header className="create-new-account-title" closeButton>
                <Modal.Title>Create New Account</Modal.Title>
            </Modal.Header>

            <Modal.Body>
                <Formik
                    initialValues={{
                        email:'',
                        password:'',
                        confirmPassword:''
                    }}
                    validationSchema={Yup.object({
                        email: Yup.string()
                            .required("UToronto email is required.")
                            .email('Please enter a UToronto email.')
                            .matches(/@mail\.utoronto\.ca/, "Must be a UToronto email!"),
                        password: Yup.string()
                            .required("Password is required."),
                        confirmPassword: Yup.string()
                            .required("Please confirm password.")
                            .oneOf([Yup.ref('password'), null], 'Passwords do not match...')
                    })}

                    onSubmit={(values, {setSubmitting, resetForm}) => {
                        axios
                        .post('/users/', {"email": values.email, "password": values.password})
                        .then(function (response) {
                            // Response received, check status code
                            if ( response && response.status === 200) {
                                setSubmitting(false);
                                resetForm();
                                handleClose();
                                hideBackendMesssage();
                                alert("User successfully created!");

                            } else { 
                                // Failed
                                showBackendMessage();
                                setSubmitting(false);
                                console.log("User already exists in database.");
                            }
                        })
                        .catch(function (error) {
                            // Another fail
                            showBackendMessage();
                            setSubmitting(false);
                            console.log(error);
                            console.log("User already exists in database.");
                        })
                        .finally(function () {
                            // Add to later maybe...
                        });
                    }}
                >

                    {({isSubmitting}) => (
                        <Form>
                            <Field className="form-group form-control spacing btn-block" placeholder="* UToronto Email" type="email" name="email" />
                            <ErrorMessage className="error-message" name="email" component="div" />
                            
                            <Field className="form-group form-control spacing btn-block" placeholder="* Password" type="password" name="password" />
                            <ErrorMessage className="error-message" name="password" component="div" />
                            
                            <Field className="form-group form-control spacing btn-block" placeholder="* Confirm Password"  type="Password" name="confirmPassword" />
                            <ErrorMessage className="error-message" name="confirmPassword" component="div" />
                            <hr></hr>

                            <div> { backendMessage ? <UserExists /> : null } </div>

                            <Button disabled={isSubmitting} className="float-right create-new-account mr-1" variant="primary" type="submit">
                                Register
                            </Button>
                            <Button className="float-right submit-login mr-1 " variant="secondary" onClick={handleClose}> Close </Button>
                        </Form>
                    )}
                </Formik>
            </Modal.Body>
        </Modal>
      </>
    );
  }

  const UserExists = () => (
    <div className="error-message spacing btn-block">
      User already exists.
    </div>
  )