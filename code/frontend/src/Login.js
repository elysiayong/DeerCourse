import React, { useState }from 'react';
import { NewAccountForm } from './RegistrationForm'
import {Button} from 'react-bootstrap';
import { Formik, Form, Field, ErrorMessage} from 'formik';
import * as Yup from 'yup';
import axios from "axios";

/* Form Inspired By: https://www.positronx.io/build-react-login-sign-up-ui-template-with-bootstrap-4/ */
export const Login = () => {

    const [show, setShow] = useState(true);
    const handleClose = () => { setShow(false);}
    const handleShow = () => setShow(true);

    return (
        <div className="login-form"> { show ? <LoggingIn show={show} handleClose={handleClose} /> :  <LoggedIn show={show} handleShow={handleShow}/> } </div>
    );
}

const LoggingIn = ({show, handleClose}) => {
    return (
        <>
            <Formik
                initialValues={{
                    username:'',
                    password:'',
                }}
                validationSchema={Yup.object({
                    username: Yup.string()
                        .required("UToronto email is required.")
                        .email('Please enter a UToronto email.')
                        .matches(/@mail\.utoronto\.ca/, "Must be a UToronto email!"),
                    password: Yup.string()
                        .required("Password is required.")
                })}
    
                onSubmit={(values, {setSubmitting, resetForm}) => {

                    var bodyFormData = new FormData();
                    bodyFormData.append('username', values.username);
                    bodyFormData.append('password', values.password);

                    axios
                        .post('/auth', bodyFormData)
                        .then(function (response) {
                            // Response received, check status code
                            if (response && response.status === 200) {
                                setSubmitting(false);
                                resetForm();
                                handleClose();

                            } else { 
                                // Failed
                                setSubmitting(false);
                                console.log("Could not authenticate user.");
                                alert("Could not authenticate user.");
                            }
                        })
                        .catch(function (error) {
                            // Another fail
                            setSubmitting(false);
                            console.log(error);
                            console.log("Could not authenticate user.");
                            alert("Could not authenticate user.");
                        })
                        .finally(function () {
                            // Add to later maybe...
                        });

                }}
            >
    
            {({isSubmitting}) => (
                <Form>
                    <h1 className="login-title">Login</h1> 
                    <Field className="form-group form-control spacing btn-block" placeholder="Enter UToronto Email" type="text" name="username" />
                    <ErrorMessage className="error-message" name="username" component="div" />
                    
                    <Field className="form-group form-control spacing btn-block" placeholder="Enter Password" type="password" name="password" />
                    <ErrorMessage className="error-message" name="password" component="div" />
    
                    <Button disabled={isSubmitting} className="submit-login spacing btn btn-primary btn-block" variant="primary" type="submit">
                        Login
                    </Button>
                    <br></br>
    
                    <p className="forgot text-center">
                        Forgot <a className="forgot-password" href="/error">Password?</a>
                    </p>
    
                    <hr></hr>
                    <React.Fragment>
                        <NewAccountForm />
                    </React.Fragment>
                </Form>
            )}
            </Formik>
        </>); 
}

const LoggedIn = ({show, handleShow}) => {
    return (
        <>
            <Button className="submit-login spacing btn btn-primary btn-block" variant="primary" type="submit" onClick={handleShow}>
                Logout
            </Button>
        </>
    );
}
