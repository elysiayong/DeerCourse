import React from 'react'

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

            <button type="submit" className="create-new-account btn btn-primary btn-block">Create New Account</button>
            <br></br>
        </form>
    </div>
)